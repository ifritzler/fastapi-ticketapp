"""User repository"""
from typing import List

from sqlmodel import Session, select
from app.db.db import engine
from app.models.user import User, UserOut


def get_all() -> List[UserOut]:
    """Get all users in db"""
    with Session(bind=engine) as session:
        query = select(User)
        response = session.exec(query).all()
        return response
