from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.api.users.me import router as me_router

router = APIRouter()
router.include_router(me_router)

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
