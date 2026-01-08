from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, SecretStr
import time, jwt
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginIn(BaseModel):
    # Removido EmailStr para não depender do email-validator
    email: str
    password: SecretStr
    code: str | None = None

class TokenOut(BaseModel):
    access_token: str

@router.post("/login", response_model=TokenOut)
def login(b: LoginIn):
    # TODO: validar usuário real (DB). MVP aceita user/senha não vazios.
    if not b.email or not b.password.get_secret_value():
        raise HTTPException(status_code=400, detail="Credenciais inválidas")

    payload = {"sub": str(b.email), "iat": int(time.time())}
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    return {"access_token": token}
