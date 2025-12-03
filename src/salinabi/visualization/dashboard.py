from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import polars as pl

def create_dashboard(df: pl.DataFrame):
    app = Dash(__name__, external_stylesheets=["https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"])
    
    app.layout = html.Div([
        html.H1("📊 BI Salina — Pagrún", className="text-center my-4"),
        
        html.Div([
            dcc.Graph(id="produccion-mensual"),
            dcc.Graph(id="calidad-por-turno")
        ], className="row"),
        
        html.Div([
            html.Div(id="kpi-cards", className="row")
        ])
    ])
    
    @app.callback(
        Output("produccion-mensual", "figure"),
        Input("url", "pathname")
    )
    def update_produccion(_):
        fig = px.bar(
            df.group_by("mes").agg(pl.sum("toneladas")).sort("mes"),
            x="mes", y="toneladas",
            title="Producción Mensual (tn)"
        )
        return fig

    return app
