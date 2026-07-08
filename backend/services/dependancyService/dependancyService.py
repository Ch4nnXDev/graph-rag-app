from services.InjestionService import DocumentProcessor
from services.embeddingService import HFEmbeddingModel
from services.inferenceService import InferenceService
from services.modelService import modelService
from services.vectorDBService import VectorService
from sentence_transformers import SentenceTransformer
from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DependencyContainer:
    def __init__(self):
        self.injestionService = DocumentProcessor(UnstructuredLoader, RecursiveCharacterTextSplitter())
        self.embeddingService = HFEmbeddingModel(SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2'))
        self.modelService = modelService('google/flan-t5-large')
        self.inferenceService = InferenceService(self.modelService.load_model())
        self.vectorService = VectorService()
        