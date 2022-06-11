""" User api router"""
from typing import List
from fastapi import APIRouter
from app.models.user import ResponseUser

from app.repositories import user

router = APIRouter(
    prefix="/users",
    tags=["Usuarios"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[ResponseUser])
def root():
    """Root Endpoint"""
    return user.get_all()
