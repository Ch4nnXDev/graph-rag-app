from fastapi import APIRouter
from services.chatService.chatService import ChatService
from dto.chat_schema import ChatDTO

chat = ChatService()

router = APIRouter()

@router.post("/ask")
def ask(query: ChatDTO):
    return chat.answer(query)

