from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.models.user import User
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.member_id import MemberID

router = APIRouter()

# @router.get("/me")
# def read_current_user(current_user: User = Depends(get_current_user)):
#     return {"id": current_user.id, "email": current_user.email, "display_name": current_user.display_name, "is_email_verified": current_user.is_email_verified,}
@router.get("/me/id")
def get_my_member_id(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    member = db.query(MemberID).filter(
        MemberID.owner_id == current_user.id
    ).first()

    return member
