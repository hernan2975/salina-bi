from pydantic import BaseModel, validator
from typing import Optional

class Bomba(BaseModel):
    id: str
    estado: str  # "encendida", "apagada", "falla"
    presion_bar: float
    caudal_m3h: float
    energia_kwh: float
    timestamp: str

    @validator("estado")
    def check_estado(cls, v):
        if v not in ["encendida", "apagada", "falla"]:
            raise ValueError("Estado debe ser: encendida, apagada o falla")
        return v

class ConsumoEnergetico(BaseModel):
    fecha: str
    bomba_id: str
    horas_operacion: float
    kwh_consumidos: float
    eficiencia_kwh_tn: Optional[float] = None
