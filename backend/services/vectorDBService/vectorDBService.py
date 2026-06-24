from langchain.vectorstores import Chroma
from chromadb import HttpClient

class VectorStore:
    def __init__(self):
        self.chroma_client = HttpClient(host="localhost", port="8001")
        
        
    def create_vector_store(self, embedding):
        vector_store = Chroma(
            embedding_function=embedding,
            client=self.chroma_client,
            collection_name="ai_agent_collection",
            presist_directory="./chroma_db"
        )
        
        return vector_store
    
    def create_vector_retriever(self, vector_store):
        retriever = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k":3}
        )
        
        return retriever