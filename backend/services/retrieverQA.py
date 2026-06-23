from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from .prompt_template import prompt, teacher_prompt
from langchain.chains import RetrievalQA

def create_qa_chain(retriever):
    hf_pipeline = pipeline(
        model="google/flan-t5-base",
        task="text2text-generation",
        model_kwargs={"temperature": 0.6, "max_length": 512, "do_sample": True, "top_p": 0.9, "repetition_penalty": 1.5},
        device_map="auto"
    )

    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": teacher_prompt}
    )

    return qa_chain



class InferenceService:
    def __init__(self, model):
        self.model = model
        
    def load_model(self):
        huggingFace_pipeline = pipeline(
            model=self.model,
            task='text2text-generation',
            model_kwargs={"temperature": 0.6, "max_length": 512, "do_sample": True, "top_p": 0.7, "repetition_penalty": 0.8},
            device_map='cuda'
            
        )
        llm = HuggingFacePipeline(pipeline=huggingFace_pipeline)
        return llm
    
    def create_qa_chain(self, llm, retriever):
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": teacher_prompt}
            
        )
        return qa_chain
        
    
    
        

    