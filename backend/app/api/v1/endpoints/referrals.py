# backend/app/api/v1/endpoints/referrals.py
from fastapi import APIRouter
router = APIRouter()

@router.get("/me")
async def my_referrals():
    pass

@router.post("/claim")
async def claim_reward():
    pass
