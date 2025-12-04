import pytest
import polars as pl
from pathlib import Path

@pytest.fixture
def sample_production_data():
    """Datos de producción de ejemplo para tests."""
    return pl.DataFrame({
        "fecha": ["2025-06-01", "2025-06-01"],
        "pileta_id": ["P-101", "P-102"],
        "toneladas": [120.0, 80.0],
        "calidad": ["refinada", "lavada"],
        "operario": ["Juan", "María"],
        "turno": ["madrugada", "mañana"],
        "area_pileta": [5000, 5000],
        "consumo_kwh": [300, 180],
        "lote_senasa": ["SAL-LP-2025060101", None]
    }).with_columns(pl.col("fecha").str.to_date())
