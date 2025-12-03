import polars as pl
from pathlib import Path
from .transformation import clean_production_data

def ingest_from_excel(path: Path) -> pl.DataFrame:
    """Carga planilla de producción diaria (formato Celusal/Pagrún)."""
    try:
        df = pl.read_excel(
            path,
            sheet_name="Producción",
            read_options={"infer_schema_length": 1000}
        )
        return clean_production_data(df)
    except Exception as e:
        raise ValueError(f"Error al cargar {path}: {e}")
