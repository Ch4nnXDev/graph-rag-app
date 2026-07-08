from backend.services.dependancyService.dependancyService import DependencyContainer


class ChatService:
    def __init__(self):
        self.dependancy = DependencyContainer()
        
        
    def query_embedding(self, query):
        embedding = self.dependancy.embeddingService.embed_query(query)
        return embedding
    
    def query_document(self, doc):
        embedding = self.dependancy.embeddingService.embed_documents(doc)
        return embedding
    
    
        
        