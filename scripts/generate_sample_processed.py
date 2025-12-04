#!/usr/bin/env python3
"""
Genera archivos Parquet de ejemplo para data/processed/
Útil para desarrollo y pruebas (no para producción).
"""
import polars as pl
from datetime import date, timedelta
from pathlib import Path

def generate_produccion():
    # Datos de ejemplo: 30 días de producción
    fechas = [date(2025, 6, 1) + timedelta(days=i) for i in range(30)]
    data = []
    
    for i, fecha in enumerate(fechas):
        # Rotación de piletas y calidades
        piletas = ["P-101", "P-102", "P-201", "P-301"]
        calidades = ["refinada", "lavada", "cruda"]
        operarios = ["Juan", "María", "Carlos", "Elena"]
        turnos = ["madrugada", "mañana", "tarde"]
        
        for j in range(3):  # 3 registros por día
            pileta = piletas[(i + j) % len(piletas)]
            calidad = calidades[(i + j) % len(calidades)]
            ton = 80 + (i % 20) + (j * 15)
            area = 5000 if pileta in ["P-101", "P-102"] else 3000 if pileta == "P-201" else 2000
            kwh = ton * (0.25 if calidad == "refinada" else 0.22 if calidad == "lavada" else 0.18)
            lote = f"SAL-LP-{fecha.strftime('%Y%m%d')}{j+1:02d}" if calidad == "refinada" else None
            
            data.append({
                "fecha": fecha,
                "pileta_id": pileta,
                "toneladas": float(ton),
                "calidad": calidad,
                "operario": operarios[(i + j) % len(operarios)],
                "turno": turnos[(i + j) % len(turnos)],
                "area_pileta": float(area),
                "consumo_kwh": float(kwh),
                "lote_senasa": lote,
                "rendimiento_tn_ha": round(ton / (area / 10000), 2),
                "kwh_por_tn": round(kwh / ton, 2),
                "es_dia_habil": fecha.weekday() < 5,
                "semana_anio": fecha.isocalendar().week
            })
    
    df = pl.DataFrame(data).with_columns([
        pl.col("fecha").cast(pl.Date),
        pl.col("calidad").cast(pl.Categorical),
        pl.col("turno").cast(pl.Categorical)
    ])
    
    Path("data/processed").mkdir(exist_ok=True)
    df.write_parquet("data/processed/produccion.parquet")
    print("✅ data/processed/produccion.parquet generado")

def generate_kpi_diario():
    # Leer producción y calcular KPIs
    df_prod = pl.read_parquet("data/processed/produccion.parquet")
    
    kpi = df_prod.group_by("fecha").agg([
        pl.sum("toneladas").alias("produccion_total_tn"),
        (pl.sum("toneladas") / (pl.sum("area_pileta") / 10000)).alias("rendimiento_promedio_tn_ha"),
        pl.sum("consumo_kwh").alias("kwh_total"),
        (pl.sum("consumo_kwh") / pl.sum("toneladas")).alias("kwh_por_tn"),
        (pl.sum("toneladas").filter(pl.col("calidad") == "refinada") / pl.sum("toneladas") * 100).alias("calidad_refinada_pct"),
        pl.sum("toneladas").alias("stock_final_tn"),  # simplificado
        pl.lit(30.0).alias("stock_dias"),  # simplificado
        (pl.sum("toneladas").filter(pl.col("lote_senasa").is_not_null()) / pl.sum("toneladas") * 100).alias("senasa_trazable_pct"),
        pl.lit([""]).alias("alertas")
    ]).sort("fecha")
    
    kpi.write_parquet("data/processed/kpi_diario.parquet")
    print("✅ data/processed/kpi_diario.parquet generado")

if __name__ == "__main__":
    generate_produccion()
    generate_kpi_diario()
