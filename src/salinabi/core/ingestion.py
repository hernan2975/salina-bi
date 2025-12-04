import polars as pl
from pathlib import Path
from typing import Union, List
import yaml
from ..domain.production import validate_production_data

def ingest_csv(file_path: Union[str, Path]) -> pl.DataFrame:
    """Carga y valida datos desde CSV."""
    df = pl.read_csv(file_path, infer_schema_length=10000)
    return validate_production_data(df)

def ingest_excel(file_path: Union[str, Path], sheet_name: str = "Producción") -> pl.DataFrame:
    """Carga datos desde Excel (formato típico de salinas)."""
    df = pl.read_excel(file_path, sheet_name=sheet_name)
    return validate_production_data(df)

def ingest_plc_logs(file_path: Union[str, Path]) -> pl.DataFrame:
    """Carga logs de PLC (bombas, sensores)."""
    return pl.read_csv(file_path)

def load_config(config_path: Union[str, Path] = "config/settings.yaml") -> dict:
    """Carga configuración de la salina."""
    with open(config_path) as f:
        return yaml.safe_load(f)
