from langchain_unstructured import UnstructuredLoader
from typing import List
from langchain.schema import Document
from io import BytesIO

def extract_text(file_content: BytesIO, filename: str) -> str:
    loader = UnstructuredLoader(file=file_content, metadata_filename=filename)
    docs: List[Document] = loader.load()
    full_text = " ".join([doc.page_content for doc in docs])
    return full_text
