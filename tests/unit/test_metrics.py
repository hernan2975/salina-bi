import polars as pl
from salinabi.core.metrics import calculate_daily_kpis

def test_calculate_daily_kpis():
    """Debe calcular KPIs correctamente con datos de ejemplo."""
    # Datos de prueba
    df = pl.DataFrame({
        "fecha": ["2025-06-01", "2025-06-01", "2025-06-02"],
        "toneladas": [100.0, 50.0, 80.0],
        "calidad": ["refinada", "lavada", "refinada"],
        "lote_senasa": ["SAL-LP-2025060101", None, "SAL-LP-2025060201"],
        "consumo_kwh": [25.0, 12.0, 20.0],
        "area_pileta": [5000, 3000, 5000]
    }).with_columns(pl.col("fecha").str.to_date())
    
    # Ejecutar
    kpis = calculate_daily_kpis(df)
    
    # Verificar
    assert kpis["produccion_total_tn"] == 230.0
    assert round(kpis["calidad_refinada_pct"], 1) == 78.3  # (100+80)/230
    assert round(kpis["senasa_trazable_pct"], 1) == 78.3  # 2 de 3 registros
    assert kpis["ultima_fecha"] == "2025-06-02"
