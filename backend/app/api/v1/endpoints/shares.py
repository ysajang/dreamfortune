# backend/app/api/v1/endpoints/shares.py
from fastapi import APIRouter
router = APIRouter()

@router.post("")
async def log_share():
    pass

@router.get("/card-image/{content_type}/{content_id}")
async def get_card_image():
    pass
