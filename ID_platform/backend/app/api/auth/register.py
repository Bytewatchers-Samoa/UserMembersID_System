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


# @router.post("/register", response_model=UserOut)
# def register(user: UserCreate, db: Session = Depends(get_db)):

#     # Check if user already exists
#     existing = db.query(User).filter(User.email == user.email).first()
#     if existing:
#         raise HTTPException(status_code=400, detail="Email already registered")

#     # Create new user
#     db_user = User(
#         email=user.email,
#         display_name=user.display_name,
#         hashed_password=hash_password(user.password),
#         role="member",
#         is_active=True,
#         is_email_verified=False,
#         is_admin=False
#     )

#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)

#     return db_user

# def generate_member_code(user_id: int):
#     year = datetime.utcnow().year
#     return f"BW-{year}-{str(user_id).zfill(4)}"
@router.post("/register")
def register(user_data: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    #Create user
    new_user = User(
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        display_name=user_data.display_name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    #Create MemberID automatically
    member_code = generate_member_code(new_user.id)

    new_member_id = MemberID(
        member_number=member_code,
        full_name=new_user.display_name,
        date_of_birth=user_data.date_of_birth,
        issue_date=datetime.utcnow().date(),
        owner_id=new_user.id
    )


    db.add(new_member_id)
    db.commit()

    return new_user

def generate_member_code(user_id: int):
    year = datetime.utcnow().year
    return f"BW-{year}-{str(user_id).zfill(4)}"
