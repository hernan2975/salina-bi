import polars as pl

def calcular_kpis(df: pl.DataFrame) -> dict:
    """KPIs clave para salinas de La Pampa."""
    hoy = pl.datetime(2025, 6, 15)  # dinámico en producción
    
    return {
        # Productividad
        "rendimiento_tn_ha": df["toneladas"].sum() / df["area_pileta"].sum(),
        
        # Eficiencia energética
        "kwh_por_tn": df["consumo_kwh"].sum() / df["toneladas"].sum(),
        
        # Calidad
        "calidad_refinada_pct": (
            df.filter(pl.col("calidad") == "refinada")["toneladas"].sum() 
            / df["toneladas"].sum() * 100
        ),
        
        # Logística
        "stock_dias": df["stock_tn"].sum() / df["venta_promedio_tn_dia"],
        
        # Cumplimiento
        "senasa_trazable_pct": (
            df.filter(pl.col("lote_senasa").is_not_null())["toneladas"].sum()
            / df["toneladas"].sum() * 100
        )
    }
