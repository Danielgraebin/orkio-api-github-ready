from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, SecretStr
import time, jwt
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginIn(BaseModel):
    email: EmailStr
    password: SecretStr
    code: str | None = None

class TokenOut(BaseModel):
    access_token: str

@router.post("/login", response_model=TokenOut)
def login(b: LoginIn):
    # TODO: substituir por validação real (DB). MVP aceita qualquer user/senha não vazios.
    if not b.email or not b.password.get_secret_value():
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    payload = {"sub": str(b.email), "iat": int(time.time())}
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    return {"access_token": token}
