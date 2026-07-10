from fastapi import FastAPI
from chatService import ChatService
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome"
    }


@app.post("/chat")
def chat(query):
    