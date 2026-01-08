from fastapi import APIRouter, Depends
from pydantic import BaseModel
from .deps import auth_guard
from .openai_proxy import openai_send_message, openai_create_thread

router = APIRouter(prefix="/agents", tags=["agents"])

class MessageIn(BaseModel):
    thread_id: str
    content: str
    files: list[str] | None = None

class ThreadOut(BaseModel):
    thread_id: str

class MessageOut(BaseModel):
    ok: bool
    answer: str | None = None

@router.post("/threads", response_model=ThreadOut)
def create_thread(_: bool = Depends(auth_guard)):
    t = openai_create_thread()
    return {"thread_id": t["id"]}

@router.post("/messages", response_model=MessageOut)
def send_message(b: MessageIn, _: bool = Depends(auth_guard)):
    _ = openai_send_message(b.thread_id, b.content)
    # MVP: não aguarda run/streaming. Retorna ack simples.
    return {"ok": True, "answer": "Mensagem enviada para processamento."}
