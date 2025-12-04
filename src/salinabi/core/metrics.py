import polars as pl
from typing import Dict

def calculate_daily_kpis(df: pl.DataFrame) -> Dict:
    """Calcula KPIs diarios para dashboard ejecutivo."""
    daily = df.group_by("fecha").agg([
        pl.sum("toneladas").alias("produccion_total_tn"),
        pl.mean("rendimiento_tn_ha").alias("rendimiento_promedio_tn_ha"),
        pl.sum("consumo_kwh").alias("kwh_total"),
        (pl.sum("consumo_kwh") / pl.sum("toneladas")).alias("kwh_por_tn"),
        (pl.sum("toneladas").filter(pl.col("calidad") == "refinada") / pl.sum("toneladas") * 100).alias("calidad_refinada_pct"),
        (pl.sum("toneladas").filter(pl.col("lote_senasa").is_not_null()) / pl.sum("toneladas") * 100).alias("senasa_trazable_pct")
    ]).sort("fecha")
    
    return {
        "ultima_fecha": daily["fecha"].max(),
        "produccion_total_tn": daily["produccion_total_tn"].sum(),
        "rendimiento_promedio": daily["rendimiento_promedio_tn_ha"].mean(),
        "kwh_por_tn": daily["kwh_por_tn"].mean(),
        "calidad_refinada_pct": daily["calidad_refinada_pct"].mean(),
        "senasa_trazable_pct": daily["senasa_trazable_pct"].mean(),
        "alertas": _generate_alerts(daily)
    }

def _generate_alerts(df: pl.DataFrame) -> List[str]:
    """Genera alertas basadas en umbrales configurables."""
    alerts = []
    config = load_config()
    
    if df["rendimiento_promedio_tn_ha"].mean() < config["alertas"]["rendimiento_min_tn_ha"]:
        alerts.append("⚠️ Rendimiento bajo: revisar evaporación")
    
    if df["kwh_por_tn"].mean() > config["alertas"]["kwh_max_por_tn"]:
        alerts.append("⚠️ Consumo energético alto: verificar bombas")
    
    return alerts
