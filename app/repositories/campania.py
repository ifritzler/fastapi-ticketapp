"""Campaign repository"""
from typing import List
from fastapi import HTTPException
from sqlmodel import Session, select

from app.db.db import engine
from app.models.campania import Campania


class ExistInDbError(HTTPException):
    """Este error ocurre cuando no se puede insertar un dato por existir en la misma previamente"""


def get_all() -> List[Campania]:
    """Get all campaigns in db"""
    with Session(bind=engine) as session:
        selected_campanias = select(Campania)
        response = session.exec(selected_campanias).all()
        return response


def create(campania: Campania) -> Campania:
    """Creamos una campaña a partir de su modelo y un id autoincremental en base de datos."""
    with Session(bind=engine) as session:
        # _campania = select(Campania).where(Campania.value == campania.value)
        # result = session.exec(_campania).first()
        # if result:
        #    raise ExistInDbError("La campania ya existe en la base de datos.")

        try:
            new_campania = Campania(value=campania.value)
            session.add(new_campania)
            session.commit()

            session.refresh(new_campania)
        except Exception as err:
            raise ExistInDbError(
                status_code=202,
                detail={
                    "msg": "Campaña ya existente",
                    "err": err.args[0],
                },
            )

        return new_campania
