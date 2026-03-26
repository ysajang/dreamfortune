# backend/app/api/v1/router.py
from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth, users, dreams, fortunes, tarot,
    subscriptions, shares, referrals, seo
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(dreams.router, prefix="/dreams", tags=["dreams"])
api_router.include_router(fortunes.router, prefix="/fortunes", tags=["fortunes"])
api_router.include_router(tarot.router, prefix="/tarot", tags=["tarot"])
api_router.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])
api_router.include_router(shares.router, prefix="/shares", tags=["shares"])
api_router.include_router(referrals.router, prefix="/referrals", tags=["referrals"])
api_router.include_router(seo.router, prefix="/seo", tags=["seo"])
