from langchain.prompts import PromptTemplate


template = """
You are a friendly AI tutor. Explain the following question in detail to a beginner,
with examples and step-by-step reasoning. Include relevant sources if possible.

Question: {question}
"""

prompt = PromptTemplate(input_variables=["question"], template=template)

