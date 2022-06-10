""" Modelos para la base de datos de usuario """
from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel


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

    id: Optional[int] = Field(primary_key=True)
    nombre: str = Field(max_length=25)
    legajo: int = Field(nullable=False, primary_key=True)
    password: str = Field(nullable=False, min_length=4, max_length=8)
    campania: Campania
