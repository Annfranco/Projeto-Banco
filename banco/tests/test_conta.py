import pytest
from banco.models.conta import Conta

# @pytest.fixture
# def conta_valida():
#     conta = Conta(333, 444)
#     return conta

@pytest.fixture
def conta_valida():
    return Conta(333, 444)

def test_validando_atributo_numero_conta(conta_valida):
    assert conta_valida.numero_conta == 333
    