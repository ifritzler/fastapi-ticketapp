from enum import Enum


class Campania(str, Enum):
    """Lista de campañas a la que un usuario puede ser asignado"""

    REAGENDAS = "reagendas"
    COMERCIAL_LLAMADO = "pendiente_comercial"
    COMERCIAL_ANULAR = "pendiente_anular"
    COMERCIAL_BOCAS = "bocas_adicionales"
    EJECUTADAS = "ejecutadas"
    ANULAR_SIN_LLAMAR = "anular_sin_llamar"
