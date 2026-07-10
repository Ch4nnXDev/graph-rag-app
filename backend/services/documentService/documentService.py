from backend.services.dependancyService import DependancyContainer

class DocumentService:
    def __init__(self):
        self.dependancy = DependancyContainer()
        
    def upload_docs(self, doc):
        docs = self.dependancy.injestionService().load_document(doc)
        clean_docs = self.dependancy.injestionService.clean_documents(docs)
        chunked = self.dependancy.injestionService.chunk_documents(clean_docs)
        self.dependancy.vector_store.add_documents(chunked)
        return "Successfully Uploaded"
    
    