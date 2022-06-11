""" Campania api router"""
from typing import List
from fastapi import APIRouter, HTTPException
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


@router.post("/", status_code=201)
def create_new_campaign(campania_in: Campania):
    """Con este endpoint podemos crear una nueva campaña"""
    return campania.create(campania_in)
