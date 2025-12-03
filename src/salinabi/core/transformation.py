import polars as pl
from pydantic import ValidationError
from ..domain.production import Cosecha

def clean_production_data(df: pl.DataFrame) -> pl.DataFrame:
    # Validación con Pydantic (nivel senior)
    records = []
    for row in df.rows(named=True):
        try:
            cosecha = Cosecha(**row)
            records.append(cosecha.model_dump())
        except ValidationError as e:
            print(f"⚠️  Registro inválido omitido: {row.get('pileta_id', 'N/D')} → {e}")
    
    return pl.DataFrame(records)
