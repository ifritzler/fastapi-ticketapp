"""Campaign repository"""
from typing import List
from sqlmodel import Session, select

from app.db.db import engine
from app.models.campania import Campania


def get_all() -> List[Campania]:
    """Get all campaigns in db"""
    with Session(bind=engine) as session:
        selected_campanias = select(Campania)
        response = session.exec(selected_campanias).all()
        return response
