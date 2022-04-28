import pytest
from Clases.Cliente import Cliente
from Clases.CuentaSueldo import CuentaSueldo, CuentaSueldoException

class TestCuentaSueldo():

    def crearCliente(self):
        return Cliente("Juan Perez", "1542215487")
    def crearCuentaSueldo(self):
        return CuentaSueldo("24514577",self.crearCliente(),10,"Jm","215478-9")

    def test_instancia_CuentaSueldo_valida(self):
        nueva_cuenta_sueldo = self.crearCuentaSueldo()
        assert "Jm" == nueva_cuenta_sueldo.get_empleador()
        assert "215478-9" == nueva_cuenta_sueldo.get_cuit_empleador()
        assert 10 == nueva_cuenta_sueldo.get_extracciones_permitidas()
        assert 0 == nueva_cuenta_sueldo.get_extracciones_realizadas()
        assert 0 == nueva_cuenta_sueldo.get_saldo()

    def test_deposito_extraccion_reinicio_de_extracciones_CuentaSueldo_valida(self):
        nueva_cuenta_sueldo = self.crearCuentaSueldo()
        nueva_cuenta_sueldo.depositar(4500)
        nueva_cuenta_sueldo.extraer(500.0)
        nueva_cuenta_sueldo.set_cantidad_de_extracciones(0)
        assert 4000 == nueva_cuenta_sueldo.get_saldo()

    def test_CuentaSueldo_sin_extracciones_no_debe_poder_extraer(self):
        nueva_cuenta_sueldo = self.crearCuentaSueldo()
        nueva_cuenta_sueldo.set_cantidad_de_extracciones(0)
        assert 0==nueva_cuenta_sueldo.get_extracciones_permitidas()
        nueva_cuenta_sueldo.depositar(100)
        nueva_cuenta_sueldo.extraer(100)
        assert 100==nueva_cuenta_sueldo.get_saldo()
        assert 0==nueva_cuenta_sueldo.get_extracciones_realizadas()

    def test_instancia_CuentaSueldo_invalida_extracciones_invalidas(self):
        with pytest.raises(CuentaSueldoException) as e:
            nueva_cuenta_sueldo=CuentaSueldo("24514577",self.crearCliente(),-10,"Jm","215478-9")
        assert str(e.value)=="El dato extracciones permitidas debe ser un entero mayor o igual a cero."

    def test_instancia_CuentaSueldo_invalida_el_numero_debe_ser_string(self):
       with pytest.raises(CuentaSueldoException) as e:
            nueva_cuenta_sueldo=CuentaSueldo(24514577,self.crearCliente(),-10,"Jm","215478-9")
       assert str(e.value)=="El número de cuenta debe ser un string."

    def test_instancia_CuentaSueldo_invalida_empleador_invalido(self):
        with pytest.raises(CuentaSueldoException) as e:
            nueva_cuenta_sueldo=CuentaSueldo("24514577",self.crearCliente(),10,5+4j,"215478-9")
        assert str(e.value)=="El dato empleador debe ser un string."

    def test_instancia_CuentaSueldo_invalida_cuil_invalido(self):
        with pytest.raises(CuentaSueldoException) as e:
            nueva_cuenta_sueldo=CuentaSueldo("24514577",self.crearCliente(),10,"Jm",(10,2,5,4))
        assert str(e.value)=="El dato cuit_empleador debe ser un string."
