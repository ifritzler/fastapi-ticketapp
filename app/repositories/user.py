from typing import List
from sqlmodel import Session, select

from app.db.db import engine
from app.models.user import User


def get_all_users() -> List[User]:
    """Get all users in db"""
    with Session(bind=engine) as session:
        selected_users = select(User)
        response = session.exec(selected_users).all()
        return response
