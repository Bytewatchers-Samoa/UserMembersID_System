from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.db.database import SessionLocal
from app.utils.hashing import hash_password

from app.models.member_id import MemberID
from datetime import datetime, timedelta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):

    # check if email exists
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password),
        display_name=user.display_name,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    member = MemberID(
        user_id=user.id,
        member_id=generate_member_id(user.id),
        expiry_date=datetime.utcnow() + timedelta(days=365)
    )

    db.add(member)
    db.commit()

    return new_user

def generate_member_id(user_id: int):
    year = datetime.utcnow().year
    return f"BW-{year}-{str(user_id).zfill(4)}"
