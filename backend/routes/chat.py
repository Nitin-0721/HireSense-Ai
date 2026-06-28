from fastapi import APIRouter
from pydantic import BaseModel

from rag import chat_with_resume

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(data: ChatRequest):

    answer = chat_with_resume(data.question)

    return {
        "answer": answer
    }