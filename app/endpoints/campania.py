""" Campania api router"""
from typing import List
from fastapi import APIRouter
from app.models.campania import Campania

from app.repositories import campania

router = APIRouter(
    prefix="/campanias",
    tags=["Campañas"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Campania])
def get_all_campaigns():
    """Campaign endpoint to obtain all"""
    campanias = campania.get_all()
    return campanias
