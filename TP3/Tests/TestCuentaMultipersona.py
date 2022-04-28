import pytest
from Clases.CuentaMultipersona import CuentaMultipersona, CuentaMultipersonaException
from Clases.Cliente import Cliente


class TestCuentaMultipersona():

    def crearCliente(self):
        return Cliente("Juan Perez", "1542215487")

    def crearCuentaMultipersona(self):
        return CuentaMultipersona("24514577", self.crearCliente(), 5000)

    def test_instancia_CuentaMultipersona_valida(self):
        nueva_cuenta_multipersona=self.crearCuentaMultipersona()
        cotitular=Cliente("Ana Maria", "12457856")
        otro_cotitular=Cliente("Ana Maria", "12457856")
        nueva_cuenta_multipersona.agregar_cotitular(cotitular)
        nueva_cuenta_multipersona.agregar_cotitular(otro_cotitular)
        assert [cotitular]==nueva_cuenta_multipersona.get_cotitulares()

    def test_instancia_CuentaMultipersona_invalida_cliente_string(self):
        with pytest.raises(CuentaMultipersonaException) as e:
            nueva_cuenta_multipersona=CuentaMultipersona("24514577", "Juan Parez", 5000)
        assert str(e.value)=="El dato cliente debe ser una instancia de Cliente."

    def test_instancia_CuentaMultipersona_invalida_descubierto_boolean(self):
        with pytest.raises(CuentaMultipersonaException) as e:
            nueva_cuenta_multipersona=CuentaMultipersona("24514577", self.crearCliente(), False)
        assert str(e.value)=="El descubierto debe ser un numero positivo."
