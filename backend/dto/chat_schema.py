from pydantic import BaseModel

class ChatDTO(BaseModel):
    query: str
    