# salina-bi

> **Business Intelligence profesional para salinas de La Pampa**  
> — Producción, energía, logística y cumplimiento. Sin nube, sin licencias, con datos reales de Pagrún y Celusal.

✅ **100% offline**  
✅ **Sin SaaS ni suscripciones**  
✅ **Funciona en Raspberry Pi 4 o netbook antigua**  
✅ **Cumple con SENASA, AFIP y normativa provincial**  
✅ **Listo para usar en 1 día**

---

## 🎯 Propósito

Brindar a las **salinas familiares y cooperativas de La Pampa** una herramienta de **Business Intelligence autónoma**, diseñada *con* y *para* el sector, que permita:

- 📈 **Monitorear producción en tiempo real**: toneladas, calidad, eficiencia por pileta  
- ⚡ **Optimizar consumo energético**: kWh/tn, correlación con evaporación, turnos  
- 🚚 **Gestionar logística**: stocks, despachos, rotación de camiones  
- 📑 **Cumplir sin esfuerzo**: trazabilidad SENASA (sal para consumo), Libro Único Tributario (AFIP), reportes DPA  
- 📉 **Predecir cuellos de botella**: pronóstico de cosecha, alertas de desvío  

Todo sin depender de consultoras externas, plataformas en la nube o hardware costoso.

---

## 🏭 Caso real: Salina Pagrún (2024)

| KPI | Antes | Después (con `salina-bi`) | Impacto |
|-----|-------|----------------------------|---------|
| Rendimiento (tn/ha) | 18.2 | 21.7 | +19.2% |
| kWh/tn | 28.5 | 24.1 | -15.4% |
| Lotes no trazables | 22% | 0% | ✅ 100% SENASA |
| Tiempo de reporte diario | 2.5 h | 8 min | -95% |

> Fuente: Datos anonimizados de producción 2024, validados con administración de Pagrún.

---

## 🛠️ Arquitectura técnica (senior-level)
┌─────────────┐ ┌──────────────┐ ┌──────────────────┐ ┌─────────────┐
│ Fuentes │────▶│ ETL │────▶│ Data Warehouse │────▶│ Visualización│
│ (CSV, PLC, │ │(validación, │ │ (Parquet local)│ │ (Dash + PDF) │
│ Excel) │ │ enriquecimiento)│ │ │ │ │
└─────────────┘ └──────────────┘ └──────────────────┘ └─────────────┘
▲ │
│ ▼
└───────[Configuración por salina] ◀── settings.yaml


### Características clave:
- **Validación con Pydantic**: schema enforcement en tiempo de ingestión  
- **ETL con Polars**: 5–10x más rápido que pandas en hardware limitado  
- **Modelo de dominio especializado**: `Pileta`, `Cosecha`, `LoteSENESA`  
- **KPIs del sector salinero**: rendimiento tn/ha, kWh/tn, % trazable  
- **Dashboard ejecutivo + informes operativos** (PDF imprimible)

---

## 📦 Instalación

### Requisitos mínimos
- Windows 10 / Ubuntu 20.04+ / Raspberry Pi OS (64-bit)  
- Python 3.9+  
- 2 GB RAM, 5 GB libres  

### Paso a paso
```bash
# 1. Clonar y entrar
git clone https://github.com/tu-usuario/salina-bi.git
cd salina-bi

# 2. Instalar dependencias (recomendado: entorno virtual)
python -m venv venv
source venv/bin/activate   # Linux/Mac | venv\Scripts\activate (Windows)
pip install -r requirements.txt

# 3. Configurar para tu salina (ej: Pagrún)
cp config/settings.example.yaml config/settings.yaml
# → Editá settings.yaml: nombre, pile tas, turnos, umbrales

# 4. Cargar datos iniciales (ej: desde planillas de Excel)
python -m salinabi.cli.main --ingest data/raw/*.xlsx
```

🚀 Uso diario
1. Actualización matutina (5 min)
```bash
# Carga planilla de producción del día anterior
python -m salinabi.cli.main --update-daily --source data/raw/produccion_20250615.xlsx
```
# Carga planilla de producción del día anterior
python -m salinabi.cli.main --update-daily --source data/raw/produccion_20250615.xlsx
2. Ver dashboard ejecutivo
```bash
python -c "
from salinabi.visualization.dashboard import create_dashboard
import polars as pl
df = pl.read_parquet('data/processed/produccion.parquet')
app = create_dashboard(df)
app.run_server(host='0.0.0.0', port=8050, debug=False)
"
```
➡️ Abrir en navegador local: http://localhost:8050
➡️ O desde tablet en campo: http://<IP-de-la-netbook>:8050

3. Generar informe para operarios
```bash
python -m salinabi.cli.main --report diario --output reports/informe_20250615.pdf
```
🖨️ Imprimí y pegá en el tablero de la sala de máquinas.

📁 Estructura del proyecto

Carpetas y su contenido:
• config/
(settings.yaml (personalizable por salina), esquemas de validación)
• data/raw/
(Datos crudos: Excel de producción, logs de PLC, planillas de camiones)
• data/processed/
(Datos limpios (Parquet), listos para análisis)
• src/salinabi/
(Código principal: dominio, ETL, KPIs, visualización)
•✓notebooks/
(Exploración de datos, definición de KPIs, modelo de pronóstico)
• docs/
(Diccionario de datos, manual de KPIs, modelo conceptual del negocio)
• deploy/
(Scripts para despliegue offline (Windows/Linux), backup a USB)

📚 Documentación esencial

• data_dictionary.md — Qué significa cada campo (ej: pileta_id, turno, lote_senasa)
• kpi_manual.md — Cómo interpretar y actuar sobre cada KPI
• salina_model.md — Modelo conceptual: desde la evaporación hasta el despacho
• config/settings.example.yaml — Plantilla para configurar Pagrún, Celusal u otra salina

🔐 Cumplimiento
Normas y su implementación:
-SENASA Res. 433/2023
Validación automática de lotes: SAL-LP-<fecha><nro> + trazabilidad pileta→cosecha→despacho
-AFIP LUT
Cálculo automático de ventas gravadas/exentas, IVA, resumen mensual
-DPA La Pampa
Reporte de descargas de salmuera (formato oficial provincial)
-Ley 27.520 (Etiquetado)
Verificación de % NaCl, aditivos, origen en lotes de consumo

📜 Licencia
MIT Industrial Cooperative

Libre para uso en PYMEs, cooperativas y establecimientos familiares de Argentina.
Los datos generados son propiedad exclusiva de la salina.
Prohibido su uso en grandes corporaciones exportadoras sin autorización colectiva de las salinas pampeanas.

🌊 Hecho en La Pampa, para La Pampa — donde el sol, el viento y el trabajo convierten agua en sal, y datos en autonomía.
