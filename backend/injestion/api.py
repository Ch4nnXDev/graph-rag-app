from fastapi import FastAPI, HTTPException, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from langchain.schema import Document
from typing import List
from pydantic import BaseModel
import boto3
import os
from io import BytesIO
from dotenv import load_dotenv


from .Filemodel import FileMetadata

from .mongodb import files_collection
from .embeddings import embedding
from .vector_store import create_vector_store
from .retrieverQA import create_qa_chain
from .splitter import text_splitter
from .Extract import extract_text

load_dotenv()

app = FastAPI(title="AI Agent API")

# --- CORS ---
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ChatRequest(BaseModel):
    question: str
    
    
# --- AWS S3 ---
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")


vector_store, retriever = create_vector_store(embedding)
qa_chain = create_qa_chain(retriever) if retriever else None

@app.get("/")
def root():
    return {"message": "API is running"}


@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    global qa_chain
    uploaded = []
    all_new_documents = []
    for file in files:
        
        file_content = file.file.read()
        full_text = extract_text(BytesIO(file_content), file.filename)
        
        s3_path = f"uploads/{file.filename}"
        s3.upload_fileobj(BytesIO(file_content), BUCKET_NAME, s3_path)
        
        file_metadata = FileMetadata(
            filename=file.filename,
            content_type=file.content_type,
            s3_path=s3_path,
        )
        await files_collection.insert_one(file_metadata.dict(by_alias=True))
        uploaded.append(file_metadata)
       
        chunks = text_splitter.split_text(full_text)
        documents = [
            Document(
                page_content=chunk,
                metadata={"filename": file.filename, "s3_path": s3_path},
            )
            for chunk in chunks
        ]
        all_new_documents.extend(documents)
       
    if all_new_documents:
        vector_store.add_documents(all_new_documents)
        vector_store.persist()
        qa_chain = create_qa_chain(vector_store.as_retriever())
        
    return {"uploaded_files": uploaded}
    


@app.post("/answer")
def get_answer(req: ChatRequest):
    if not qa_chain:
        raise HTTPException(status_code=500, detail="QA chain not initialized")
    result = qa_chain.invoke({"query": req.question})
    answer_text = result.get("result") if isinstance(result, dict) else str(result)
    return {"answer": answer_text}
    
@app.get("/files")
def list_files():
    files = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix="uploads/")
    file_urls = {}

    if "Contents" in files:
        for file in files["Contents"]:
            key = file["Key"]  # e.g. "uploads/mydoc.pdf"
            filename = key.split("/")[-1]  # mydoc.pdf
            extension = filename.split(".")[-1].lower()  # pdf

            file_urls[key] = {
                "url": s3.generate_presigned_url(
                    'get_object',
                    Params={'Bucket': BUCKET_NAME, 'Key': key},
                    ExpiresIn=3600  # URL valid for 1 hour
                ),
                "type": extension
            }

    return {"file_urls": file_urls}


@app.delete("/delete-all-files")
async def delete_all_files():
    try:
        # List all objects under 'uploads/'
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix="uploads/")
        if "Contents" not in response:
            return {"message": "No files to delete"}

        objects_to_delete = [{"Key": obj["Key"]} for obj in response["Contents"]]

        # Delete all files
        s3.delete_objects(Bucket=BUCKET_NAME, Delete={"Objects": objects_to_delete})

        # Optional: remove all metadata from MongoDB
        await files_collection.delete_many({"s3_path": {"$regex": "^uploads/"}})

        return {"message": f"Deleted {len(objects_to_delete)} files from S3 and MongoDB"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/test-retriever")
def test_retriever(keyword: str):
    if not vector_store:
        raise HTTPException(status_code=500, detail="Vector store not initialized")
    retriever = vector_store.as_retriever()
    docs = retriever.get_relevant_documents(keyword)
    # Return the first 100 characters of each document for inspection
    return {"results": [d.page_content[:100] for d in docs]}

@app.get("/list-vector-store-docs")
def list_vector_docs():
    if not vector_store:
        raise HTTPException(status_code=500, detail="Vector store not initialized")
    docs = vector_store.as_retriever().get_relevant_documents(" ")  # empty keyword to fetch all
    return {"documents": [d.metadata for d in docs]}
