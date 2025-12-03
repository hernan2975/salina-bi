from enum import Enum
from typing import List
from pydantic import BaseModel, field_validator

class SalinityLevel(str, Enum):
    cruda = "cruda"
    lavada = "lavada"
    refinada = "refinada"

class Pileta(BaseModel):
    id: str
    area_m2: float
    profundidad_cm: float
    fase: str  # "llenado", "evaporacion", "cosecha"
    salinidad_actual_ppt: float
    ultima_cosecha: str | None

class Cosecha(BaseModel):
    pileta_id: str
    fecha: str
    toneladas: float
    calidad: SalinityLevel
    operario: str
    turno: str  # "mañana", "tarde", "noche"

    @field_validator("toneladas")
    @classmethod
    def check_positive(cls, v):
        if v <= 0:
            raise ValueError("Toneladas debe ser > 0")
        return v
