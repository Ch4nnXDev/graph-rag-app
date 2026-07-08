from services.InjestionService import DocumentProcessor
from services.embeddingService import HFEmbeddingModel
from services.inferenceService import InferenceService
from services.modelService import modelService
from services.vectorDBService import VectorService
from sentence_transformers import SentenceTransformer
from langchain_unstructured import UnstructuredLoader
from langchain.chains import RetrievalQA

from langchain_text_splitters import RecursiveCharacterTextSplitter

class DependencyContainer:
    def __init__(self):
        self.injestionService = DocumentProcessor(UnstructuredLoader, RecursiveCharacterTextSplitter())
        self.embeddingService = HFEmbeddingModel(SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2'))
        self.inferenceService = InferenceService().create_qa_chain(RetrievalQA, self.embeddingService)
        self.modelService = modelService()
        self.vectorService = VectorService()
        