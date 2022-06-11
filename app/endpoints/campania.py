""" Campania api router"""
from http import HTTPStatus
from typing import List
from fastapi import APIRouter, HTTPException
from app.models.campania import Campania

from app.repositories import campania as campaign_repository


class ExistInDbError(HTTPException):
    """Este error ocurre cuando no se puede insertar un dato por existir en la misma previamente"""


router = APIRouter(
    prefix="/campanias",
    tags=["Campañas"],
    responses={HTTPStatus.NOT_FOUND: {"description": "Not found"}},
)


@router.get("/", response_model=List[Campania], status_code=HTTPStatus.OK)
def get_all_campaigns():
    """Campaign endpoint to obtain all"""
    campanias = campaign_repository.get_all()
    return campanias


@router.post("/", status_code=HTTPStatus.CREATED)
def create_new_campaign(campania_in: Campania):
    """Con este endpoint podemos crear una nueva campaña"""
    try:
        new_campania = campaign_repository.create(campania_in)
    except Exception as err:
        raise ExistInDbError(
            status_code=HTTPStatus.ACCEPTED,
            detail={
                "msg": "Campaña ya existente",
                "err": err.args[0],
            },
        )
    return new_campania


@router.delete("/{id}", status_code=HTTPStatus.NO_CONTENT)
def get_campaign_by_id(_id: int):
    """Utiliza el repositorio de campania para eliminar mediante el id de la misma."""
    campaign_repository.delete_by_id(_id)
    return {}
