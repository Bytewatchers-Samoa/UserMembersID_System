from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    display_name: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    display_name: str
    is_email_verified: bool

    class Config:
        orm_mode = True
