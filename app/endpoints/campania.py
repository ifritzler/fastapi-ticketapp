""" Campania api router"""
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException
from app.models.campania import CampaniaIn, CampaniaOut
from app.repositories import campania as campaign_repository


class ExistInDbError(HTTPException):
    """Este error ocurre cuando no se puede insertar un dato por existir en la misma previamente"""

    def __init__(self, err_msg):

        self.status_code = HTTPStatus.ACCEPTED
        self.detail = {
            "msg": "Campaña ya existente",
            "err": err_msg,
        }


router = APIRouter(
    prefix="/campania",
    tags=["Campañas"],
    responses={HTTPStatus.NOT_FOUND: {"description": "Not found"}},
)


@router.get("/", response_model=List[CampaniaOut], status_code=HTTPStatus.OK)
def get_all_campaigns():
    """Este endpoint nos permite traernos todas las campañas de la db"""
    campanias = campaign_repository.get_all()
    return campanias


@router.get("/{_id}", response_model=CampaniaOut, status_code=HTTPStatus.OK)
def get_campaign_by_id(_id: int):
    """Obtenemos una campaña por su id"""
    campania = campaign_repository.get_by_id(_id)
    return campania


@router.post("/", response_model=CampaniaOut, status_code=HTTPStatus.CREATED)
def create_new_campaign(campania_in: CampaniaIn):
    """Con este endpoint podemos crear una nueva campaña"""
    try:
        new_campania = campaign_repository.create(campania_in)
    except Exception as err:
        raise ExistInDbError(err.args[0])
    return new_campania


@router.delete("/{_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_campaign_by_id(_id: int):
    """Utiliza el repositorio de campania para eliminar mediante el id de la misma."""
    campaign_repository.delete_by_id(_id)
    return {}
