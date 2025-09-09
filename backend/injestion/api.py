from loader import load_documents
from splitter import text_splitter
from embeddings import embedding
from vector_store import create_vector_store
from retrieverQA import create_qa_chain
from remove import remove_metadata
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

app = FastAPI(title="AI agent api")
origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for all origins (dev only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

print("Starting the AI agent API...")
raw_docs = load_documents("../data")
split_docs = text_splitter.split_documents(raw_docs)
clean_docs = remove_metadata(split_docs)
vector_store, retriever = create_vector_store(clean_docs, embedding)
qa_chain = create_qa_chain(retriever)


@app.get("/answer")
def get_answer(query: str):
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required")
    try:
        response = qa_chain.invoke({"query": query})
        return {"answer": response["result"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload")
def upload_files(files):
    if not files:
        raise HTTPException(status_code=400, detail="No files provided for upload")
    try:
        for file in files:
            s3.upload_fileobj(
                file.file,
                BUCKET_NAME,
                file.filename
                
            )
        return {"message": "Files uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    