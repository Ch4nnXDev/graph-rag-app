from services.injestionService import DocumentProcessor
from services.embeddingService import HFEmbeddingModel
from services.inferenceService import InferenceService
from services.modelService import modelService
from services.vectorDBService import VectorService

class DependacyContainer:
    def __init__(self):
        self.injestionService = DocumentProcessor()
        self.embeddingService = HFEmbeddingModel()
        self.inferenceService = InferenceService()
        self.modelService = modelService()
        self.vectorService = VectorService()
        