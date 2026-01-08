import jwt
from fastapi import Depends, Header, HTTPException, Request
from app.core.config import settings

def auth_guard(authorization: str = Header(None), request: Request = None):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = authorization.split(" ", 1)[1]
    try:
        jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        return True
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
