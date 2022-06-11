""" Modelos para la base de datos de usuario """
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, UniqueConstraint


class Campania(str, Enum):
    """Lista de campañas a la que un usuario puede ser asignado"""

    REAGENDAS = "reagendas"
    COMERCIAL_LLAMADO = "pendiente_comercial"
    COMERCIAL_ANULAR = "pendiente_anular"
    COMERCIAL_BOCAS = "bocas_adicionales"
    EJECUTADAS = "ejecutadas"
    ANULAR_SIN_LLAMAR = "anular_sin_llamar"


class User(SQLModel, table=True):
    """Tabla de usuario"""

    __table_args__ = (UniqueConstraint("legajo"),)

    id: Optional[int] = Field(primary_key=True)
    nombre: str = Field(max_length=25)
    apellido: str = Field(max_length=25)
    legajo: int = Field(nullable=False)
    password: str = Field(nullable=False, min_length=4, max_length=8)
    campania: Campania = Field(nullable=False)


class ResponseUser(BaseModel):
    """This model is a User pwdless model for http responses"""

    id: Optional[int] = Field(primary_key=True)
    nombre: str = Field(max_length=25)
    apellido: str = Field(max_length=25)
    legajo: int = Field(nullable=False)
    campania: Campania = Field(nullable=False)
