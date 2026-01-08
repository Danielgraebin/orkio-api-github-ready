import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.config import settings

router = APIRouter(prefix="/openai", tags=["openai"])

class Msg(BaseModel):
    thread_id: str
    content: str

def _headers():
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not configured")
    return {
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        "OpenAI-Beta": "assistants=v2"
    }

def openai_create_thread():
    with httpx.Client(timeout=30) as c:
        r = c.post("https://api.openai.com/v1/threads", headers=_headers())
        r.raise_for_status()
        return r.json()

def openai_send_message(thread_id: str, text: str):
    with httpx.Client(timeout=60) as c:
        r = c.post(
            f"https://api.openai.com/v1/threads/{thread_id}/messages",
            headers=_headers(),
            json={"role":"user","content":[{"type":"text","text": text}]}
        )
        r.raise_for_status()
        return {"status": "queued"}
