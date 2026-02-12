from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.db.database import get_db
from app.models.member_id import MemberID
from app.dependencies.admin import get_current_admin

router = APIRouter(prefix="/member-ids", tags=["Member IDs"])

@router.post("/")
def create_member_id(
    member_number: str,
    full_name: str,
    date_of_birth: date,
    owner_id: int,
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    new_id = MemberID(
        member_number=member_number,
        full_name=full_name,
        date_of_birth=date_of_birth,
        issue_date=date.today(),
        owner_id=owner_id
    )

    db.add(new_id)
    db.commit()
    db.refresh(new_id)

    return new_id
