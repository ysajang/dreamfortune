# backend/app/api/v1/endpoints/subscriptions.py
from fastapi import APIRouter
router = APIRouter()

@router.post("/billing-key")
async def create_billing_key():
    pass

@router.post("/start-trial")
async def start_trial():
    pass

@router.get("/me")
async def my_subscription():
    pass

@router.post("/cancel")
async def cancel_subscription():
    pass

@router.post("/change-plan")
async def change_plan():
    pass
