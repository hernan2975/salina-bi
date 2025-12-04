from weasyprint import HTML
from jinja2 import Template
from pathlib import Path
import polars as pl
from datetime import datetime

def generate_daily_report(kpis: dict, output_path: str):
    """Genera informe diario en PDF para operativos."""
    template = Template("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Informe Diario - Salina BI</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 2cm; }
            .header { text-align: center; border-bottom: 3px solid #2c6e49; padding-bottom: 10px; }
            .kpi { background: #f8f9fa; padding: 10px; margin: 5px 0; border-left: 4px solid #2c6e49; }
            .alert { background: #fff3cd; border-left: 4px solid #ffc107; }
            .footer { margin-top: 30px; font-size: 0.9em; color: #6c757d; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Informe Diario de Producción</h1>
            <h2>{{ fecha }}</h2>
        </div>
        
        <div class="kpi">
            <strong>Producción total:</strong> {{ kpis.produccion_total_tn }} tn
        </div>
        <div class="kpi">
            <strong>Rendimiento promedio:</strong> {{ kpis.rendimiento_promedio|round(2) }} tn/ha
        </div>
        <div class="kpi">
            <strong>Consumo energético:</strong> {{ kpis.kwh_por_tn|round(2) }} kWh/tn
        </div>
        <div class="kpi">
            <strong>Calidad refinada:</strong> {{ kpis.calidad_refinada_pct|round(1) }}%
        </div>
        <div class="kpi">
            <strong>Trazabilidad SENASA:</strong> {{ kpis.senasa_trazable_pct|round(1) }}%
        </div>
        
        {% if kpis.alertas %}
        <div class="alert">
            <strong>⚠️ Alertas:</strong>
            <ul>
            {% for alerta in kpis.alertas %}
                <li>{{ alerta }}</li>
            {% endfor %}
            </ul>
        </div>
        {% endif %}
        
        <div class="footer">
            <p>Generado con salina-bi — {{ fecha_generacion }}</p>
            <p>Espacio para notas del operario:</p>
            <div style="border: 1px dashed #ccc; min-height: 60px;"></div>
        </div>
    </body>
    </html>
    """)
    
    html_str = template.render(
        kpis=kpis,
        fecha=kpis["ultima_fecha"],
        fecha_generacion=datetime.now().strftime("%d/%m/%Y %H:%M")
    )
    
    Path(output_path).parent.mkdir(exist_ok=True)
    HTML(string=html_str).write_pdf(output_path)
