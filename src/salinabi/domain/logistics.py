from enum import Enum
from pydantic import BaseModel
from typing import Optional

class MovimientoTipo(str, Enum):
    entrada = "entrada"
    salida = "salida"

class MovimientoStock(BaseModel):
    fecha: str
    tipo: MovimientoTipo
    toneladas: float
    cliente_proveedor: str
    transporte: str
    destino_origen: str
    numero_factura: Optional[str] = None

    @validator("toneladas")
    def check_positive(cls, v):
        if v <= 0:
            raise ValueError("Toneladas debe ser > 0")
        return v

class Stock(BaseModel):
    producto: str  # "sal_cruda", "sal_lavada", "sal_refinada"
    toneladas: float
    ubicacion: str  # "pileta", "secadero", "deposito"
    lote_senasa: Optional[str] = None
