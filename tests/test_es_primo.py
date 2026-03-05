import pytest
from src.es_primo import es_primo

def test_numero_primo():
    """Caso correcto"""
    assert es_primo(7) is False


def test_numero_no_primo():
    """Caso límite - número válido pero no primo"""
    assert es_primo(8) is False


def test_error_numero_menor_que_dos():
    """Caso error"""
    with pytest.raises(ValueError):
        es_primo(1)


def test_error_tipo_incorrecto():
    """Caso error tipo"""
    with pytest.raises(TypeError):
        es_primo("10")