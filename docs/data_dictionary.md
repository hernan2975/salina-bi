# Diccionario de Datos — Salina BI

## 📁 `data/raw/`

### `produccion.csv`
| Campo | Tipo | Descripción | Ejemplo | Validación |
|-------|------|-------------|---------|------------|
| `fecha` | date | Fecha de cosecha | `2025-06-01` | `YYYY-MM-DD` |
| `pileta_id` | string | Identificador de pileta | `P-101` | `P-[0-9]{3}` |
| `toneladas` | float | Toneladas cosechadas | `125.3` | > 0 |
| `calidad` | string | Calidad del producto | `refinada` | `cruda`, `lavada`, `refinada` |
| `operario` | string | Nombre del operario | `Juan` | ≥ 2 caracteres |
| `turno` | string | Turno de trabajo | `madrugada` | `madrugada`, `mañana`, `tarde` |
| `area_pileta` | float | Área en m² | `5000` | 1000–10000 |
| `consumo_kwh` | float | Energía consumida | `310` | ≥ 0 |
| `lote_senasa` | string | Lote para SENASA | `SAL-LP-2025060101` | `SAL-LP-[0-9]{10}` o vacío |

### `logistica.csv`
| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `tipo` | string | `entrada` o `salida` | `salida` |
| `cliente_proveedor` | string | Nombre del cliente/proveedor | `Panificadoras Pampeanas` |
| `transporte` | string | Medio de transporte | `Camión PAT-123` |
| `numero_factura` | string | Número de factura AFIP | `A0001-00001234` |

---

## 📁 `data/processed/`

### `produccion.parquet`
| Campo | Tipo | Descripción | Cálculo |
|-------|------|-------------|---------|
| `rendimiento_tn_ha` | float | Toneladas por hectárea | `toneladas / (area_pileta / 10000)` |
| `kwh_por_tn` | float | kWh por tonelada | `consumo_kwh / toneladas` |
| `es_dia_habil` | bool | Lunes a viernes | `fecha.weekday() < 5` |
| `semana_anio` | int | Semana ISO | `fecha.isocalendar().week` |

### `kpi_diario.parquet`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `produccion_total_tn` | float | Suma diaria de toneladas |
| `rendimiento_promedio_tn_ha` | float | Promedio ponderado por área |
| `calidad_refinada_pct` | float | % de toneladas refinadas |
| `senasa_trazable_pct` | float | % con lote SENASA válido |
| `alertas` | list[string] | Alertas activas para el día |

---

## 📁 `data/reference/`

### `piletas.csv`
| Campo | Descripción | Valores típicos |
|-------|-------------|-----------------|
| `tipo` | Función en el proceso | `primaria`, `secundaria`, `lavado` |
| `fase_actual` | Estado operativo | `llenado`, `evaporacion`, `cosecha`, `limpieza` |

### `calidades.csv`
| Calidad | Uso permitido | NaCl mínimo | Precio relativo |
|---------|---------------|-------------|-----------------|
| `cruda` | Industria química | 85% | 1.0x |
| `lavada` | Industria alimenticia | 92% | 1.8x |
| `refinada` | Consumo humano | 98.5% | 3.2x |
