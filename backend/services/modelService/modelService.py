from langchain.chain import RetrieverQA
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
class modelService:
    def __init__(self, model_name):
        self.model = model_name
        self.pipeline = None
        self.llm = None
        
    def load_model(self):
        huggingface_pipeline = pipeline(
            model=self.model_name,
            task="text2text-generation",
            model_kwargs={"temperature": 0.6, "max_length": 512, "do_sample": True, "top_p": 0.9, "repetition_penalty": 1.5},
            device_map="auto"
        )
        
        llm = HuggingFacePipeline(pipeline=huggingface_pipeline)
        return llm
        
        