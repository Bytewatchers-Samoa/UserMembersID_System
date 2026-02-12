from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class MemberID(Base):
    __tablename__ = "member_ids"

    id = Column(Integer, primary_key=True, index=True)
    member_number = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    issue_date = Column(Date, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User")
