from langchain_unstructured import UnstructuredLoader
from typing import List
from langchain.schema import Document
def extract_text(file):
    file.file.seek(0)
    loader = UnstructuredLoader(file.file)
    docs: List[Document] = loader.load()
    full_text = " ".join([doc.page_content for doc in docs])
    return full_text
