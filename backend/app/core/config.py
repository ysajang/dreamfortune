# backend/app/core/config.py
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # App
    APP_NAME: str = "dreamfortune"
    DEBUG: bool = False
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # DB
    DATABASE_URL: str

    # AI
    OPENAI_API_KEY: str
    GEMINI_API_KEY: str
    AI_PROVIDER: str = "gemini"  # "openai" or "gemini"
    AI_MODEL: str = "gemini-2.0-flash"

    # 토스페이먼츠
    TOSS_CLIENT_KEY: str
    TOSS_SECRET_KEY: str
    TOSS_WEBHOOK_SECRET: str = ""

    # 카카오
    KAKAO_REST_API_KEY: str
    KAKAO_REDIRECT_URI: str

    # Firebase (FCM 푸시)
    FIREBASE_CREDENTIALS_PATH: str = "firebase-credentials.json"

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "https://dreamfortune.kr"]

    # CDN
    CDN_BASE_URL: str = "https://cdn.dreamfortune.kr"
    CARD_IMAGE_DIR: str = "app/static/cards"

    class Config:
        env_file = ".env"


settings = Settings()
