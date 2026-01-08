from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.routes.auth import router as auth_router
from app.api.v1.routes.agents import router as agents_router
from app.api.v1.routes.openai_proxy import router as openai_router

app = FastAPI(title=settings.APP_NAME)

# CORS
origins = ["*"] if settings.ALLOWED_ORIGINS == "*" else [o.strip() for o in settings.ALLOWED_ORIGINS.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"ok": True, "service": settings.APP_NAME}

@app.get("/api/v1/health")
def health():
    return {"ok": True}

app.include_router(auth_router, prefix="/api/v1")
app.include_router(agents_router, prefix="/api/v1")
app.include_router(openai_router, prefix="/api/v1")
