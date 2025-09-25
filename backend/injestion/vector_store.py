from langchain.vectorstores import Chroma
from chromadb import HttpClient

chroma_client = HttpClient(host="localhost", port="8001")

def create_vector_store(embedding):
    vector_store = Chroma(
        embedding_function=embedding,
        client=chroma_client,
        collection_name="ai_agent_collection",
        persist_directory="./chroma_db"
    )
    
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )
    print(vector_store.get())

    return vector_store, retriever

