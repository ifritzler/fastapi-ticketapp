from enum import Enum
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint


class CampaniaEnum(str, Enum):
    """Lista de campañas a la que un usuario puede ser asignado"""

    REAGENDAS = "reagendas"
    COMERCIAL_LLAMADO = "pendiente_comercial"
    COMERCIAL_ANULAR = "pendiente_anular"
    COMERCIAL_BOCAS = "bocas_adicionales"
    EJECUTADAS = "ejecutadas"
    ANULAR_SIN_LLAMAR = "anular_sin_llamar"


class Campania(SQLModel, table=True):
    """Modelo de campaña en base de datos"""

    __table_args__ = (UniqueConstraint("value"),)

    id: Optional[int] = Field(primary_key=True)
    value: CampaniaEnum = Field(max_length=25)
    users: List["User"] = Relationship(back_populates="campania")
