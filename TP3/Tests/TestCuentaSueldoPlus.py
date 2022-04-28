import pytest
from Clases.Cliente import Cliente
from Clases.CuentaSueldoPlus import CuentaSueldoPlus, CuentaSueldoPlusException

class TestCuentaSueldoPlus():

    def crearCliente(self):
        return Cliente("Juan Perez", "1542215487")

    def crearCuentaSueldoPlus(self):
        return CuentaSueldoPlus("24514577", self.crearCliente(), 10, "JM", "215478-9", 5000)

    def test_instancia_valida_CuentaSueldoPlus(self):
        nueva_cuenta_sueldo_plus = self.crearCuentaSueldoPlus()
        5000 == nueva_cuenta_sueldo_plus.get_disponible() == nueva_cuenta_sueldo_plus.get_descubierto()
        0 == nueva_cuenta_sueldo_plus.get_extracciones_realizadas()
        nueva_cuenta_sueldo_plus.extraer(1000)
        assert -1000 == nueva_cuenta_sueldo_plus.get_saldo()
        assert 4000 == nueva_cuenta_sueldo_plus.get_disponible()
        assert 1 == nueva_cuenta_sueldo_plus.get_extracciones_realizadas()
        nueva_cuenta_sueldo_plus.depositar(2500)
        assert 1500 == nueva_cuenta_sueldo_plus.get_saldo()
        assert 5000 == nueva_cuenta_sueldo_plus.get_disponible()

    def test_CuentaSueldoPlus_intanta_extraer_mas_del_disponible_debe_cancelar_la_operacion(self):
        nueva_cuenta_sueldo_plus=self.crearCuentaSueldoPlus()
        5000==nueva_cuenta_sueldo_plus.get_disponible()
        nueva_cuenta_sueldo_plus.extraer(6000)
        5000==nueva_cuenta_sueldo_plus.get_disponible()

    def test_set_descubierto_sin_cubrir_no_debe_efectuarse_hasta_cubrir_a_menos_que_sea_por_mayor_limite(self):
        nueva_cuenta_sueldo_plus = self.crearCuentaSueldoPlus()
        nueva_cuenta_sueldo_plus.extraer(5000)
        0==nueva_cuenta_sueldo_plus.get_disponible()
        False==nueva_cuenta_sueldo_plus.set_descubierto(3000)
        True==nueva_cuenta_sueldo_plus.set_descubierto(8000)
        3000==nueva_cuenta_sueldo_plus.get_disponible()

    def test_instancia_invalida_CuentaSueldoPlus_numero_de_cuenta_entero(self):
        with pytest.raises(CuentaSueldoPlusException) as e:
            nueva_cuenta_sueldo_plus=CuentaSueldoPlus(151515,self.crearCliente(), 10, "JM", "215478-9", 5000)
        assert str(e.value)=="El número de cuenta debe ser un string."

    def test_instancia_invalida_CuentaSueldoPlus_decubierto_negativo(self):
        with pytest.raises(CuentaSueldoPlusException) as e:
            nueva_cuenta_sueldo_plus=CuentaSueldoPlus("151515",self.crearCliente(), 10, "JM", "215478-9", -5000)
        assert str(e.value)=='El descubierto debe ser un numero positivo.'
