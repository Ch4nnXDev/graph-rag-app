from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

from langchain.chains import RetrievalQA

def create_qa_chain(retriever):
    hf_pipeline = pipeline(
        model="google/flan-t5-base",
        task="text2text-generation",
        model_kwargs={"temperature": 0.1, "max_length": 512}
    )

    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
