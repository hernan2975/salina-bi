import polars as pl
from pathlib import Path

def enrich_production_data(df: pl.DataFrame, config: dict) -> pl.DataFrame:
    """Enriquece datos con información de referencia."""
    # Cargar tablas de referencia
    piletas = pl.read_csv("data/reference/piletas.csv")
    turnos = pl.read_csv("data/reference/turnos.csv")
    
    # Enriquecer con datos de piletas
    df = df.join(piletas.select(["pileta_id", "area_m2"]), on="pileta_id", how="left")
    
    # Calcular métricas derivadas
    df = df.with_columns([
        (pl.col("toneladas") / (pl.col("area_m2") / 10000)).alias("rendimiento_tn_ha"),
        (pl.col("consumo_kwh") / pl.col("toneladas")).alias("kwh_por_tn"),
        pl.col("fecha").dt.week().alias("semana_anio"),
        pl.col("fecha").dt.weekday().lt(6).alias("es_dia_habil")  # Lun-Vie
    ])
    
    return df

def validate_against_schema(df: pl.DataFrame, schema_path: str = "config/etl_schema.json") -> pl.DataFrame:
    """Validación adicional contra esquema JSON (opcional)."""
    return df  # Implementación real usaría jsonschema
