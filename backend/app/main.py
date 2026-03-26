# backend/app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.v1.router import api_router
from app.core.config import settings
from app.db.database import engine
from app.models import user, subscription, dream, fortune, tarot, share
from app.services.scheduler import start_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작 시
    start_scheduler()
    yield
    # 종료 시


app = FastAPI(
    title="꿈해몽+운세 API",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일 (카드 이미지)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# API 라우터
app.include_router(api_router, prefix="/v1")


@app.get("/health")
async def health():
    return {"status": "ok"}
