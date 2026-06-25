from services.InjestionService import DocumentProcessor
from services.embeddingService import HFEmbeddingModel
from services.inferenceService import InferenceService
from services.modelService import modelService
from services.vectorDBService import VectorService

class DependencyContainer:
    def __init__(self):
        self.injestionService = DocumentProcessor().load_Document
        self.embeddingService = HFEmbeddingModel()
        self.inferenceService = InferenceService()
        self.modelService = modelService()
        self.vectorService = VectorService()
        