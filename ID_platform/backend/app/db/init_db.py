from app.db.database import Base, engine
from app.models.user import User
from app.models.user import User
from app.models.member_id import MemberID


def init_db():
    Base.metadata.create_all(bind=engine)
