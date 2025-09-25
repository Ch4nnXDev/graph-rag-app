from transformers import AutoTokenizer
from langchain.text_splitter import TokenTextSplitter

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text_splitter = TokenTextSplitter(
    encoding_name="gpt2",
    chunk_size=130,
    chunk_overlap=50
)
