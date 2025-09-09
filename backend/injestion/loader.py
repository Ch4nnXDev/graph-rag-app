import os
from langchain_unstructured import UnstructuredLoader




def load_documents(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            loader = UnstructuredLoader(filepath)
            
            docs.extend(loader.load())
    return docs
