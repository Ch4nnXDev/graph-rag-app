from services.InjestionService.injestionService import DocumentProcessor
from services.embeddingService.embeddingService import HFEmbeddingModel
from services.inferenceService.inferenceService import InferenceService
from services.modelService.modelService import modelService
from services.vectorDBService.vectorDBService import VectorStore
from sentence_transformers import SentenceTransformer
from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DependencyContainer:
    def __init__(self):
        self.injestionService = DocumentProcessor(UnstructuredLoader, RecursiveCharacterTextSplitter())
        self.embeddingService = HFEmbeddingModel(SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2'))
        self.modelService = modelService('google/gemma-2-2b-it')
        self.inferenceService = InferenceService(self.modelService.load_model())
        self.vectorService = VectorStore()
        self.vector_store = self.dependancy.vectorService().create_vector_store(
            self.dependacy.embeddingService()
        )
        