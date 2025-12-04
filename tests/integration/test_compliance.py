import pytest
from salinabi.services.compliance import SENASACompliance, AFIPCompliance

def test_senasa_compliance_valido():
    """Lote SENASA válido debe pasar validación."""
    resultado = SENASACompliance.check_lote(
        lote_id="SAL-LP-2025060101",
        fecha_cosecha="2025-06-01",
        pileta_id="P-101"
    )
    
    assert resultado["lote_valido"] is True
    assert resultado["registro_completo"] is True
    assert resultado["plazo_vigencia"] is True

def test_senasa_compliance_invalido():
    """Lote con formato incorrecto debe fallar."""
    resultado = SENASACompliance.check_lote(
        lote_id="SAL-XX-123",  # prefijo inválido
        fecha_cosecha="2025-06-01",
        pileta_id="P-101"
    )
    
    assert resultado["lote_valido"] is False

def test_afip_compliance_resumen():
    """Debe calcular resumen AFIP correctamente."""
    # Datos de prueba
    import polars as pl
    df = pl.DataFrame({
        "monto": [1000.0, 2000.0, 1500.0],
        "tipo": ["gravada", "exenta", "gravada"],
        "iva": [210.0, 0.0, 315.0]
    })
    
    resumen = AFIPCompliance.generar_resumen_mensual(df, "2025-06")
    
    assert resumen["ventas_gravadas"] == 2500.0
    assert resumen["ventas_exentas"] == 2000.0
    assert resumen["iva_liquidado"] == 525.0
