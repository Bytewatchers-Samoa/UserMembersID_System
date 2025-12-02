from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, TokenResponse
from app.db.database import SessionLocal
from app.models.user import User
from app.utils.hashing import verify_password
from app.utils.jwt_handler import create_access_token


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == credentials.email).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    #create token payload
    access_token = create_access_token({"sub": str(user.id)})

    return TokenResponse(access_token=access_token)
