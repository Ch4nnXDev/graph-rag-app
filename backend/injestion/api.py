from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from langchain.schema import Document
from typing import List
import boto3
import os
from dotenv import load_dotenv


from models.Filemodel import FileMetadata
import neo4j_client
import mongodb
from embeddings import embedding
from vector_store import create_vector_store
from retrieverQA import create_qa_chain
from splitter import text_splitter
from Extract import extract_text

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

# --- AWS S3 ---
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")


vector_store, retriever = create_vector_store([], embedding)
qa_chain = None

if retriever:
    qa_chain = create_qa_chain(retriever)

@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    uploaded = []
    for file in files:
        s3_path = f"uploads/{file.filename}"
        s3.upload_fileobj(file.file, BUCKET_NAME, s3_path)
        file_metadata = FileMetadata(
            filename=file.filename,
            content_type=file.content_type,
            s3_path=s3_path,
        )
        full_text = extract_text(file)
        chunks = text_splitter.split_text(full_text)
        document = [
            Document(
                page_content=chunk,
                metadata={"filename": file.filename, "s3_path": s3_path},
            )
            for chunk in chunks
        ]
        vector_store.add_documents(document)
        vector_store.persist()
        qa_chain = create_qa_chain(vector_store.as_retriever())
        
        
        
        await mongodb.files_collection.insert_one(file_metadata.dict(by_alias=True))
        uploaded.append(file_metadata)
        
        
    return {"uploaded_files": uploaded}
    
@app.get("/answer")
def get_answer(question: str):
    try:  
        answer = qa_chain.run(question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
    