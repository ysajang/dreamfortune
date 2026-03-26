# backend/app/api/v1/endpoints/dreams.py
from fastapi import APIRouter
router = APIRouter()

@router.post("")
async def create_dream():
    pass

@router.get("")
async def list_dreams():
    pass

@router.get("/{dream_id}")
async def get_dream():
    pass

@router.delete("/{dream_id}")
async def delete_dream():
    pass

@router.get("/report")
async def get_dream_report():
    pass
