# backend/app/api/v1/endpoints/auth.py
from fastapi import APIRouter
router = APIRouter()

@router.post("/kakao")
async def kakao_login():
    pass

@router.post("/google")
async def google_login():
    pass

@router.post("/refresh")
async def refresh_token():
    pass

@router.delete("/withdraw")
async def withdraw():
    pass
