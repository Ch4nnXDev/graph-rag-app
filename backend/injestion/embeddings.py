from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings

class HFEmbeddingModel(Embeddings):
    def __init__(self, model):
        self.model = model

    def embed_documents(self, texts):
        return self.model.encode(texts, show_progress_bar=True).tolist()

    def embed_query(self, text):
        return self.model.encode([text], show_progress_bar=False)[0].tolist()

embedding_model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L3-v2')
embedding = HFEmbeddingModel(embedding_model)
