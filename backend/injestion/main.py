from loader import load_documents
from splitter import text_splitter
from embeddings import embedding
from vector_store import create_vector_store
from retrieverQA import create_qa_chain
from remove import remove_metadata
from dotenv import load_dotenv




def main():
    # Load and chunk documents
    raw_docs = load_documents("backend/data")
    split_docs = text_splitter.split_documents(raw_docs)
    clean_docs = remove_metadata(split_docs)

    # Build vector store and retriever
    vector_store, retriever = create_vector_store(clean_docs, embedding)

    # QA Chain
    qa_chain = create_qa_chain(retriever)

    # Run a query
    question = "Summarize the content of the documents"
    response = qa_chain.invoke({"query": question})

    print("\n📄 Answer:")
    print(response["result"])

if __name__ == "__main__":
    main()
