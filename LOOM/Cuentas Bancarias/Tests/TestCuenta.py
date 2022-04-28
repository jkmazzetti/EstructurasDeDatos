import pytest
from Clases.Cliente import Cliente, ClienteException
from Clases.Cuenta import Cuenta, CuentaException

class TestCuenta():
    def test_se_espera_error_al_intentar_instanciar_Cuenta_ya_que_es_abstracta(self):
        with pytest.raises(Exception) as e:
            Cuenta("161661631",Cliente("Juan Perez", "1542215487"))
        assert str(e.value)=="Can't instantiate abstract class Cuenta with abstract methods extraer"

