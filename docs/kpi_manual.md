# Manual de KPIs — Salina BI

## 📊 KPIs Ejecutivos (para gerencia)

| KPI | Fórmula | Verde | Amarillo | Rojo | Acción |
|-----|---------|-------|----------|------|--------|
| **Rendimiento (tn/ha)** | Σ toneladas / Σ ha | ≥ 18.0 | 15.0–17.9 | < 15.0 | Revisar evaporación, limpieza de piletas |
| **Eficiencia energética** | kWh total / tn total | ≤ 25.0 | 25.1–28.0 | > 28.0 | Verificar bombas, ajustar presión |
| **Calidad premium** | % tn refinadas | ≥ 65% | 60–64.9% | < 60% | Ajustar tiempos de lavado/secado |
| **Trazabilidad SENASA** | % tn con lote válido | 100% | 95–99% | < 95% | Detener despachos, registrar lotes |

## 🛠️ KPIs Operativos (para supervisores)

| KPI | Fórmula | Meta diaria | Alerta |
|-----|---------|-------------|--------|
| **Productividad por turno** | tn / horas turno | Madrugada: ≥ 15 tn/h<br>Mañana: ≥ 12 tn/h<br>Tarde: ≥ 8 tn/h | < 80% de meta |
| **Stock de seguridad** | tn en depósito / venta diaria | ≥ 15 días | < 10 días |
| **Rotación de camiones** | tn / camión | ≥ 25 tn/camión | < 20 tn/camión |

## 📈 Interpretación de tendencias

- **Rendimiento ↓ + kWh/tn ↑**: Problema en sistema de bombeo o evaporación  
- **Calidad refinada ↓ + stock ↑**: Ajustar parámetros de lavado/secado  
- **Trazabilidad ↓ + despachos ↑**: Urgente: capacitar en registro de lotes  

## 🖨️ Cómo usar los informes

1. **Informe diario (PDF)**:  
   - Pegar en tablero de sala de máquinas  
   - Revisar en reunión de turno  
   - Completar espacio de notas con acciones  

2. **Dashboard ejecutivo**:  
   - Analizar tendencias semanales  
   - Identificar correlaciones (ej: clima vs. rendimiento)  
   - Simular escenarios con controles interactivos  

> ℹ️ **Nota**: Todos los KPIs se calculan automáticamente al ejecutar `salina-bi-update`.
