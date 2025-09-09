from langchain.vectorstores import Chroma

def create_vector_store(documents, embedding):
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding,
        persist_directory="../chroma_db"
    )
    

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    return vector_store, retriever
