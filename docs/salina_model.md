# Modelo Conceptual del Negocio Salinero

## 🌊 Proceso Productivo (ciclo típico: 30–45 días)

```mermaid
graph LR
A[Agua salmuera] --> B[Piletas primarias]
B -->|Evaporación natural| C[Piletas secundarias]
C -->|Cosecha| D[Sal cruda]
D --> E[Lavado]
E --> F[Sal lavada]
F --> G[Secado y tamizado]
G --> H[Sal refinada]
H --> I[Almacenamiento]
I --> J[Despacho]
```
• Fases críticas

     Fase       Duración típica          Factores clave                      Métricas
Evaporación.      20–30 días       Radiación solar, viento, humedad      mm evaporados/día
Cosecha            2–4 días        Humedad de sal, compactación          tn/día, calidad inicial
Lavado              1 día          Calidad del agua de lavado            % NaCl final
Secado             3–7 días        Temperatura, humedad relativa         humedad final (%)

⚡ Modelo Energético
Consumo por etapa

    Etapa             Equipamiento               Consumo típico           Optimización
Bombeo         Electrobombas centrífugas        0.2–0.35 kWh/m³        Ajuste de presión, horarios nocturnos
Cosecha        Retroexcavadoras                 3–5 L/hora             Rutas optimizadas
Secado         Trituradoras + ventiladores      15–25 kWh/tn           Mantenimiento de filtros

Correlaciones clave

• ↑ Viento → ↓ Tiempo de secado → ↓ Consumo energético
• ↑ Radiación solar → ↑ Evaporación → ↑ Rendimiento
• ↑ Humedad relativa → ↑ Tiempo de secado → ↑ Costo

🚚 Modelo Logístico
Flujos de material

Sal cruda → Lavado → Sal lavada → Secado → Sal refinada → Depósito → Camión → Cliente
          ↗                               ↗
    Recirculación de agua           Devolución de granza

    Capacidades típicas 

    Recurso             Capacidad               Observaciones       
Piletas primarias         10 ha             2 unidades de 5 ha c/u
Piletas secundarias        6 ha             2 unidades de 3 ha c/u
Depósito cubierto         500 tn            Almacenamiento de refinada
Camiones propios          3 unidades        25 tn/camión

📑 Cumplimiento Normativo

**SENASA (Res. 433/2023)**
• Trazabilidad: lote único desde pileta → despacho
• Etiquetado: % NaCl, aditivos, origen, RNPA
• Plazos: vigencia 2 años desde cosecha
**AFIP (LUT)**
• Códigos: 2101.10.00 (sal refinada), 2501.00.11 (sal cruda)
• Alicuotas: 10.5% (cruda), 21% (refinada)
**DPA La Pampa**
• Descargas: registro mensual de salmuera residual
• Agua: consumo declarado por pileta

💡 Palancas de mejora identificadas

1. **Aumentar rendimiento:**
• Optimizar secuencia de llenado (piletas más soleadas primero)
• Reducir tiempos muertos en cosecha
2. **Reducir kWh/tn:**
• Programar bombeo en horarios valle (tarifa diferencial)
• Mantenimiento preventivo de bombas
3. **Mejorar calidad:**
• Control de agua de lavado (dureza < 50 ppm)
• Tiempos estandarizados por calidad objetivo
