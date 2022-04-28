import _pytest
from Clases.Cliente import Cliente
from Clases.CuentaMultipersona import CuentaMultipersona
from Clases.CuentaSueldo import CuentaSueldo
from Clases.CuentaSueldoPlus import CuentaSueldoPlus
from Clases.PersistenciaJson import PersistenciaJson


class TestPersistenciaJson():

    def test_recuperacion_de_datos(self):
        mingo = Cliente("Mingo Pizzafrolla", "25458881")
        catita = Cliente("Catita Langanuzzo", "54588752")
        porota = Cliente("Porota Donatuzo De Cacopardo", "2154787")
        lista_clientes = []
        lista_cuentas = []
        mingo_cuentaMultipersona = CuentaMultipersona("48744259", mingo, 11000)
        mingo_cuentaMultipersona.agregar_cotitular(porota)
        mingo_cuentaMultipersona.agregar_cotitular(catita)
        mingo_cuentaMultipersona.extraer(10000)
        catita_cuentaPlus = CuentaSueldoPlus("152487789", catita, 10, "Radio el Mundo", "45787885-8", 10000)
        catita_cuentaPlus.depositar(4500)
        catita_cuentaPlus.extraer(500)
        porota_cuentaSueldo = CuentaSueldo("15445787", porota, 5, "La tota y la porota", "154512-02")
        porota_cuentaSueldo.depositar(500)
        porota_cuentaSueldo.extraer(100)
        lista_clientes.append(mingo)
        lista_clientes.append(catita)
        lista_clientes.append(porota)
        lista_cuentas.append(mingo_cuentaMultipersona)
        lista_cuentas.append(catita_cuentaPlus)
        lista_cuentas.append(porota_cuentaSueldo)
        clientes_recuperados, cuentas_recuperadas = PersistenciaJson(lista_clientes, lista_cuentas,
                                                                     "persistir_instancias_json").recuperar()
        for i in range(len(lista_clientes) - 1):
            assert lista_clientes[i].get_dni() == clientes_recuperados[i].get_dni()
            assert lista_clientes[i].get_nombre() == clientes_recuperados[i].get_nombre()
        for i in range(len(lista_cuentas) - 1):
            tipo = lista_cuentas[i].__str__()
            assert lista_cuentas[i].get_titular().get_nombre() == cuentas_recuperadas[i].get_titular().get_nombre()
            assert lista_cuentas[i].get_titular().get_dni() == cuentas_recuperadas[i].get_titular().get_dni()
            assert lista_cuentas[i].get_saldo() == cuentas_recuperadas[i].get_saldo()
            assert lista_cuentas[i].get_numero() == cuentas_recuperadas[i].get_numero()
            if tipo == "MULTIPERSONA":
                for j in range(len(lista_cuentas[i].get_cotitulares()) - 1):
                    assert lista_cuentas[i].get_cotitulares()[j].get_nombre() == \
                           cuentas_recuperadas[i].get_cotitulares()[j].get_nombre()
                    assert lista_cuentas[i].get_cotitulares()[j].get_dni() == cuentas_recuperadas[i].get_cotitulares()[
                        j].get_dni()
            if tipo == "PLUS":
                assert lista_cuentas[i].get_extracciones_permitidas() == cuentas_recuperadas[
                    i].get_extracciones_permitidas()
                assert lista_cuentas[i].get_extracciones_realizadas() == cuentas_recuperadas[
                    i].get_extracciones_realizadas()
                assert lista_cuentas[i].get_extracciones_restantes() == cuentas_recuperadas[
                    i].get_extracciones_restantes()
                assert lista_cuentas[i].get_empleador()==cuentas_recuperadas[i].get_empleador()
                assert lista_cuentas[i].get_cuit_empleador()==cuentas_recuperadas[i].get_cuit_empleador()
            if tipo == "SUELDO":
                assert lista_cuentas[i].get_extracciones_permitidas() == cuentas_recuperadas[
                    i].get_extracciones_permitidas()
                assert lista_cuentas[i].get_extracciones_realizadas() == cuentas_recuperadas[
                    i].get_extracciones_realizadas()
                assert lista_cuentas[i].get_extracciones_restantes() == cuentas_recuperadas[
                    i].get_extracciones_restantes()
                assert lista_cuentas[i].get_empleador()==cuentas_recuperadas[i].get_empleador()
                assert lista_cuentas[i].get_cuit_empleador()==cuentas_recuperadas[i].get_cuit_empleador()
