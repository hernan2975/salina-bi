import polars as pl
import pytest
from pathlib import Path
from salinabi.core.ingestion import ingest_csv

def test_ingest_csv_valido(tmp_path):
    """Debe cargar CSV válido y devolver DataFrame."""
    # Crear CSV de prueba
    csv_content = """fecha,pileta_id,toneladas,calidad,operario,turno,area_pileta,consumo_kwh
2025-06-01,P-101,125.3,refinada,Juan,madrugada,5000,310
2025-06-01,P-102,98.7,lavada,María,mañana,5000,220"""
    
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)
    
    # Ejecutar
    df = ingest_csv(csv_file)
    
    # Verificar
    assert isinstance(df, pl.DataFrame)
    assert df.shape == (2, 8)
    assert df["toneladas"].sum() == 224.0

def test_ingest_csv_faltante():
    """Debe fallar con archivo inexistente."""
    with pytest.raises(ValueError, match="Error al cargar"):
        ingest_csv("archivo_inexistente.csv")
