from fastapi import APIRouter


router = APIRouter()

router.post("/chat")
def chat(query):
    return query

