from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from app.schemas.user import UserCreate, UserOut
# from app.models.user import User
from app.db.database import SessionLocal
# from app.utils.hashing import hash_password

from app.models.member_id import MemberID
from datetime import datetime, timedelta
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.utils.hashing import hash_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Check if user already exists
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user
    db_user = User(
        email=user.email,
        display_name=user.display_name,
        hashed_password=hash_password(user.password),
        role="member",
        is_active=True,
        is_email_verified=False,
        is_admin=False
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def generate_member_id(user_id: int):
    year = datetime.utcnow().year
    return f"BW-{year}-{str(user_id).zfill(4)}"
