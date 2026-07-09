from backend.services.dependancyService.dependancyService import DependencyContainer


class ChatService:
    def __init__(self):
        self.dependancy = DependencyContainer()
        
        
        
        self.vector_store = self.dependancy.vectorService().create_vector_store(
            self.dependacy.embeddingService()
        )
        
        self.retriever = self.dependancy.vectorService().create_vector_retriever(
            self.vector_store
        )
        
        self.qa_chain = self.dependancy.inferenceService().create_qa_chain(
            self.retriever
        )
        
    def answer(self, query):
        return self.qa_chain.invoke({"query": query})
            
            
    
        
        