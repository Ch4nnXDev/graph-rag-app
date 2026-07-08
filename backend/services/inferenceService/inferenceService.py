from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from ..prompt_template import prompt, teacher_prompt
from langchain.chains import RetrievalQA



class InferenceService:
    
    def __init__(self, llm):
        self.llm = llm
    
    def create_qa_chain(self, retriever):
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": teacher_prompt}
            
        )
        return qa_chain
        
    
    
        

    