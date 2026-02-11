from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class MemberID(Base):
    __tablename__ = "member_ids"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    member_id = Column(String, unique=True, index=True)

    issue_date = Column(DateTime, default=datetime.utcnow)
    expiry_date = Column(DateTime)
    status = Column(String, default="active")

    user = relationship("User")
