import pytest
from salinabi.domain.production import Cosecha, SalinityLevel

def test_cosecha_valida():
    """Cosecha válida debe instanciarse correctamente."""
    cosecha = Cosecha(
        pileta_id="P-101",
        fecha="2025-06-01",
        toneladas=125.5,
        calidad=SalinityLevel.refinada,
        operario="Juan",
        turno="madrugada"
    )
    
    assert cosecha.pileta_id == "P-101"
    assert cosecha.toneladas == 125.5
    assert cosecha.calidad == SalinityLevel.refinada

def test_cosecha_toneladas_invalida():
    """Toneladas debe ser > 0."""
    with pytest.raises(ValueError, match="Toneladas debe ser > 0"):
        Cosecha(
            pileta_id="P-101",
            fecha="2025-06-01",
            toneladas=-5.0,  # inválido
            calidad=SalinityLevel.cruda,
            operario="Juan",
            turno="mañana"
        )

def test_cosecha_pileta_id_invalida():
    """pileta_id debe seguir formato P-XXX."""
    with pytest.raises(ValueError):
        Cosecha(
            pileta_id="101",  # sin prefijo
            fecha="2025-06-01",
            toneladas=100.0,
            calidad=SalinityLevel.lavada,
            operario="María",
            turno="tarde"
        )
