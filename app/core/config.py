import os

class Settings:
    APP_NAME: str = "Orkio API"
    ENV: str = os.getenv("ENV", "production")
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change-me")
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "*")
    PORT: int = int(os.getenv("PORT", "8080"))

settings = Settings()
