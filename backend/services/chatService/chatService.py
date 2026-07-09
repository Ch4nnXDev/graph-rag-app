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
    
    def create_vector_store(self, embedding):
        vector_store = self.dependancy.vectorDBService.create_vector_store(embedding)
        return vector_store
    
    def create_vector_retriever(self, vector_store):
        retriever = self.dependancy.vectorDBService.create_vector_retriever(vector_store)
        return retriever

    
        
        