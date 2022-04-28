import pytest
from Clases.Cliente import Cliente, ClienteException

class TestCliente():

    def test_instancia_Cliente_valida(self):
        nuevo_cliente = Cliente("Juan Perez", "1542215487")
        assert "1542215487" == nuevo_cliente.get_dni()
        assert "Juan Perez" == nuevo_cliente.get_nombre()

    def test_instancia_Cliente_con_nombre_vacio(self):
        with pytest.raises(ClienteException) as e:
            nuevo_cliente=Cliente("","1121212")
        assert str(e.value)=="El nombre no puede estar vacío."

    def test_instancia_Cliente_con_dni_vacio(self):
        with pytest.raises(ClienteException) as e:
            nuevo_cliente=Cliente("Juan Perez","")
        assert str(e.value)=="El dni no puede estar vacío."

    def test_instancia_Cliente_dato_nombre_invalido(self):
        with pytest.raises(ClienteException) as e:
            nuevo_cliente=Cliente(True,"15164684")
        assert str(e.value)=="El nombre debe ser un string."

    def test_instancia_Cliente_dato_dni_invalido(self):
        with pytest.raises(ClienteException) as e:
            nuevo_cliente=Cliente("Juan Perez",15164684)
        assert str(e.value)=="El dni debe ser ingresado como string."
