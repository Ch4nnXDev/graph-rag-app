from fastapi import APIRouter
from ...services.chatService import chatService

chat = chatService()

router = APIRouter()

router.post("/chat")
def chat(query):
    return query

