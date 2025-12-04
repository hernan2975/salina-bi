import polars as pl
import pytest
from pathlib import Path
import tempfile
from salinabi.cli.main import update_daily
from click.testing import CliRunner

def test_etl_pipeline_completo():
    """Debe ejecutar pipeline ETL completo sin errores."""
    runner = CliRunner()
    
    # Crear datos de prueba
    with tempfile.TemporaryDirectory() as tmpdir:
        raw_dir = Path(tmpdir) / "data" / "raw"
        raw_dir.mkdir(parents=True)
        
        # CSV de prueba
        csv_content = """fecha,pileta_id,toneladas,calidad,operario,turno,area_pileta,consumo_kwh,lote_senasa
2025-06-01,P-101,120.0,refinada,Juan,madrugada,5000,300,SAL-LP-2025060101
2025-06-01,P-102,80.0,lavada,María,mañana,5000,180,"""
        
        csv_file = raw_dir / "produccion_test.csv"
        csv_file.write_text(csv_content)
        
        # Ejecutar CLI
        result = runner.invoke(update_daily, [
            "--source", str(csv_file),
            "--output", f"{tmpdir}/produccion.parquet"
        ])
        
        # Verificar
        assert result.exit_code == 0
        assert "✅ Datos actualizados" in result.output
        
        # Verificar salida
        output_file = Path(tmpdir) / "produccion.parquet"
        assert output_file.exists()
        
        df = pl.read_parquet(output_file)
        assert df.shape[0] == 2
        assert "rendimiento_tn_ha" in df.columns
        assert df["rendimiento_tn_ha"][0] == 24.0  # 120 tn / 5 ha
