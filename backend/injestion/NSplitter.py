import re

class NSplitter:
    def __init__(self, chunk_size=500, chunk_overlap=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_paragraphs(self, text):
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        return paragraphs

    def split_sentences(self, paragraph):
        sentences = re.split(r'(?<=[.!?]) +', paragraph)
        sentences = [s.strip() for s in sentences if s.strip()]
        return sentences

    def create_chunks(self, sentences, doc_id=0):
        chunks = []
        current_chunk = []
        current_length = 0
        sentence_start_idx = 0

        for idx, sentence in enumerate(sentences):
            sentence_length = len(sentence.split())
            if current_length + sentence_length <= self.chunk_size:
                current_chunk.append(sentence)
                current_length += sentence_length
            else:
                if current_chunk:
                    chunks.append({
                        "doc_id": doc_id,
                        "chunk_index": len(chunks),
                        "start_sentence_idx": sentence_start_idx,
                        "end_sentence_idx": idx - 1,
                        "text": " ".join(current_chunk)
                    })
                # Sliding window overlap
                overlap_sentences = current_chunk[-self.chunk_overlap:] if self.chunk_overlap > 0 else []
                current_chunk = overlap_sentences.copy()
                sentence_start_idx = idx - len(overlap_sentences) if self.chunk_overlap > 0 else idx
                current_chunk.append(sentence)
                current_length = sum(len(s.split()) for s in current_chunk)

        if current_chunk:
            chunks.append({
                "doc_id": doc_id,
                "chunk_index": len(chunks),
                "start_sentence_idx": sentence_start_idx,
                "end_sentence_idx": len(sentences) - 1,
                "text": " ".join(current_chunk)
            })

        return chunks

    def split_documents(self, documents):
        all_chunks = []
        for doc_id, doc in enumerate(documents):
            text = doc.page_content
            paragraphs = self.split_paragraphs(text)
            for paragraph in paragraphs:
                sentences = self.split_sentences(paragraph)
                chunks = self.create_chunks(sentences, doc_id=doc_id)
                all_chunks.extend(chunks)
        return all_chunks
