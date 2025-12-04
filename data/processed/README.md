# Datos procesados

Esta carpeta contiene datos limpios y listos para análisis.  
**No se commitean al repositorio** (ver `.gitignore`).  
Se generan automáticamente al ejecutar:

```bash
salina-bi-update --source data/raw/example_*.csv
```
Archivos generados

      Archivo                               Descripción                       Formato
-produccion.parquet/            Producción diaria validada y enriquecida/     Parquet
-logistica.parquet/             Movimientos de stock validados/               Parquet
-kpi_diario.parquet/            KPIs calculados por día/                      Parquet
-cumplimiento_senasa.parquet/   Lotes trazables vs. no trazables/             Parque
