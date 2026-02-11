from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.auth import get_current_admin
from app.db.database import get_db
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    return db.query(User).all()

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}

@router.patch("/users/{user_id}/role")
def update_user_role(
    user_id: int,
    role: str,
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    user = db.query(User).filter(User.id == user_id).first()
    user.role = role
    db.commit()
    return {"message": "Role updated"}
