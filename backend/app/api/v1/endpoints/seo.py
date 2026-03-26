# backend/app/api/v1/endpoints/seo.py
from fastapi import APIRouter
router = APIRouter()

@router.get("/{slug}")
async def get_seo_page():
    pass

@router.get("/sitemap")
async def get_sitemap():
    pass
