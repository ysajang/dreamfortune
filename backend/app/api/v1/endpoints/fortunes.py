# backend/app/api/v1/endpoints/fortunes.py
from fastapi import APIRouter
router = APIRouter()

@router.post("/today")
async def create_fortune():
    pass

@router.get("/today")
async def get_today_fortune():
    pass

@router.get("")
async def list_fortunes():
    pass
