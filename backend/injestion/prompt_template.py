from langchain.prompts import PromptTemplate

template = """
You are a friendly AI tutor. Explain the answer clearly and step-by-step,
using simple language.

Context:
{context}

Question:
{question}

Answer:
"""

prompt = PromptTemplate(
    input_variables=["question", "context"],
    template=template
)


from langchain.prompts import PromptTemplate

TEACHER_PROMPT = """
You are a helpful tutor. Explain step-by-step.
If the question is unanswerable, say "I don't know".
If the question is "give me questions", create 3 based on context.

Context:
{context}

Question: {question}

Answer:
"""
teacher_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=TEACHER_PROMPT
)
