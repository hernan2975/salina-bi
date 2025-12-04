import click
from pathlib import Path
from ..core.ingestion import ingest_csv, ingest_excel, load_config
from ..core.transformation import enrich_production_data
from ..core.metrics import calculate_daily_kpis
from ..visualization.reports import generate_daily_report

@click.group()
def cli():
    """salina-bi: Business Intelligence para salinas pampeanas."""
    pass

@cli.command()
@click.option("--source", type=click.Path(exists=True), required=True, help="Archivo fuente (CSV/Excel)")
@click.option("--output", default="data/processed/produccion.parquet", help="Salida Parquet")
def update_daily(source, output):
    """Actualiza datos diarios de producción."""
    config = load_config()
    
    # Ingestión
    if source.endswith(".csv"):
        df = ingest_csv(source)
    else:
        df = ingest_excel(source)
    
    # Transformación
    df = enrich_production_data(df, config)
    
    # Guardar
    Path(output).parent.mkdir(exist_ok=True)
    df.write_parquet(output)
    click.echo(f"✅ Datos actualizados: {output}")

@cli.command()
@click.argument("tipo", type=click.Choice(["diario", "semanal"]))
@click.option("--output", default="reports/informe.pdf", help="Archivo PDF de salida")
def report(tipo, output):
    """Genera informe operativo."""
    df = pl.read_parquet("data/processed/produccion.parquet")
    kpis = calculate_daily_kpis(df)
    generate_daily_report(kpis, output)
    click.echo(f"📄 Informe generado: {output}")

if __name__ == "__main__":
    cli()
