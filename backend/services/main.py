from fastapi import FastAPI
from chatService import ChatService
from api.routes.chat_routes import router as chat_router
app = FastAPI()

app.include_router(chat_router)
