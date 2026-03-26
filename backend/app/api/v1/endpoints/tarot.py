# backend/app/api/v1/endpoints/tarot.py
from fastapi import APIRouter
router = APIRouter()

@router.post("/draw")
async def draw_tarot():
    pass

@router.get("/history")
async def tarot_history():
    pass

@router.get("/cards")
async def list_cards():
    pass

@router.get("/{tarot_id}")
async def get_tarot():
    pass
