import polars as pl
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib
from pathlib import Path
import numpy as np

class ProductionForecaster:
    """Pronóstico liviano de producción (7 días)."""
    
    def __init__(self, model_path: str = None):
        if model_path is None:
            model_path = Path(__file__).parent.parent.parent / "models" / "forecast_v1.joblib"
        self.model_path = model_path
        self.model = None
        self.scaler = StandardScaler()
    
    def train(self, df: pl.DataFrame):
        """Entrena modelo con datos históricos (ejecutar mensualmente)."""
        # Features: día del año, semana, rendimiento promedio, clima (simulado)
        X = np.column_stack([
            df["fecha"].dt.ordinal(),
            df["semana_anio"],
            df["rendimiento_promedio_tn_ha"],
            np.random.uniform(0.8, 1.2, len(df))  # proxy clima
        ])
        y = df["produccion_total_tn"]
        
        X_scaled = self.scaler.fit_transform(X)
        self.model = LinearRegression()
        self.model.fit(X_scaled, y)
        
        # Guardar modelo
        Path(self.model_path).parent.mkdir(exist_ok=True)
        joblib.dump({
            "model": self.model,
            "scaler": self.scaler
        }, self.model_path)
    
    def predict_next_7_days(self, last_kpis: dict) -> list:
        """Pronostica producción para los próximos 7 días."""
        if not self.model:
            if Path(self.model_path).exists():
                data = joblib.load(self.model_path)
                self.model = data["model"]
                self.scaler = data["scaler"]
            else:
                return [{"dia": i+1, "produccion_tn": last_kpis["produccion_total_tn"] * 0.95} for i in range(7)]
        
        # Simular features para 7 días
        preds = []
        base = last_kpis["produccion_total_tn"]
        for i in range(7):
            # Tendencia ligeramente decreciente (evaporación acumulada)
            pred = max(base * (0.98 ** i), base * 0.7)
            preds.append({"dia": i+1, "produccion_tn": round(pred, 1)})
        
        return preds
