from langchain.schema import Document
import re


class DocumentProcessor:
    
    def __init__(self, loader, splitter):
           self.loader = loader
           self.splitter = splitter

    def load_document(self, document):
      loader = self.loader(file_path=document, strategy="hi_res", languages=["eng"])
      documents = loader.load()
      return documents
    
    def clean_documents(self, documents):
        clean_docs = [] #Langchain Document Objects are Gonna be Stored Here
        for doc in documents:
            metadata = doc.metadata
            text = doc.page_content
            text = re.sub(r'Page\s+\d+', ' ', text)
            clean_docs.append(
                Document(
                    page_content=text,
                    metadata=metadata
                )
            )
        
        return clean_docs
    
    def chunk_documents(self, clean_docs):
        chunked_docs = self.splitter.split_documents(clean_docs)
        return chunked_docs
            
         







#def extract_text(file_content: BytesIO, filename: str) -> str:
    #loader = UnstructuredLoader(file=file_content, metadata_filename=filename)
    #docs: List[Document] = loader.load()
    #full_text = " ".join([doc.page_content for doc in docs])
    #return full_text