"""Campaign repository"""
from typing import List

from sqlmodel import Session, select
from app.db.db import engine
from app.models.campania import Campania, CampaniaIn, CampaniaOut


def get_all() -> List[CampaniaOut]:
    """Listar todas las campañas en la base de datos"""
    with Session(bind=engine) as session:
        selected_campanias = select(Campania)
        response = session.exec(selected_campanias).all()
        return response


def get_by_id(_id: int) -> CampaniaOut | None:
    """Traer una campaña de la db por su id"""
    with Session(bind=engine) as session:
        query = select(Campania).where(_id == Campania.id)
        result = session.exec(query).first()
        return result


def create(campania: CampaniaIn) -> CampaniaOut:
    """Creamos una campaña a partir de su modelo y un id autoincremental en base de datos."""
    with Session(bind=engine) as session:
        # _campania = select(Campania).where(Campania.value == campania.value)
        # result = session.exec(_campania).first()
        # if result:
        #    raise ExistInDbError("La campania ya existe en la base de datos.")

        new_campania = Campania(value=campania.value)
        session.add(new_campania)
        session.commit()

        session.refresh(new_campania)

        return new_campania


def delete_by_id(_id: int) -> None:
    """Funcion que elimina una campaña por su numero de id"""
    with Session(bind=engine) as session:
        selected = select(Campania).where(Campania.id == _id)
        campaign = session.exec(selected).one_or_none()
        if campaign:
            session.delete(campaign)
            session.commit()
