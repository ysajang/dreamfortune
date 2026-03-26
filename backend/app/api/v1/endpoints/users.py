# backend/app/api/v1/endpoints/users.py
from fastapi import APIRouter
router = APIRouter()

@router.get("/me")
async def get_me():
    pass

@router.patch("/me")
async def update_me():
    pass

@router.patch("/me/push")
async def update_push():
    pass

@router.get("/me/usage")
async def get_usage():
    pass
