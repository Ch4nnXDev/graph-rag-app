from langchain.vectorstores import Chroma
from chromadb import HttpClient

chroma_client = HttpClient(host="localhost", port="8000")
def create_vector_store(documents, embedding):
    vector_store = Chroma(
        embedding_function=embedding,
        client=chroma_client,
        collection_name="ai_agent_collection" 
    )
    if documents:
        vector_store.add_documents(documents)

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    return vector_store, retriever
