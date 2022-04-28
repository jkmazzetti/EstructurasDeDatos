import shelve
from Clases.Cliente import Cliente
from Clases.CuentaMultipersona import CuentaMultipersona
from Clases.CuentaSueldo import CuentaSueldo
from Clases.CuentaSueldoPlus import CuentaSueldoPlus


class PersistenciaShelve():
    def __init__(self,lista_clientes,lista_cuentas,nombre):
        self._nombre=nombre
        self._lista_clientes=lista_clientes
        self._lista_cuentas=lista_cuentas
        self.persistir()
    def persistir(self):
        try:
            base = shelve.open(self._nombre)
            base["clientes"]=self._lista_clientes
            base["cuentas"]=self._lista_cuentas
        except Exception as e:
            print(e)
        finally:
            base.close()
    def recuperar(self):
        base=shelve.open(self._nombre)
        clientes_recuperados=base["clientes"]
        cuentas_recuperadas=base["cuentas"]
        return (clientes_recuperados,cuentas_recuperadas)
mingo = Cliente("Mingo Pizzafrolla", "25458881")
catita = Cliente("Catita Langanuzzo", "54588752")
porota = Cliente("Porota Donatuzo De Cacopardo", "2154787")
lista_clientes=[]
lista_cuentas=[]
mingo_cuentaMultipersona = CuentaMultipersona("48744259", mingo, 11000)
mingo_cuentaMultipersona.agregar_cotitular(porota)
mingo_cuentaMultipersona.agregar_cotitular(catita)
mingo_cuentaMultipersona.extraer(10000)
catita_cuentaPlus = CuentaSueldoPlus("152487789", catita,10,"Radio el Mundo","45787885-8",10000)
catita_cuentaPlus.depositar(4500)
catita_cuentaPlus.extraer(500)
porota_cuentaSueldo = CuentaSueldo("15445787", porota, 5, "La tota y la porota", "154512-02")
lista_clientes.append(mingo)
lista_clientes.append(catita)
lista_clientes.append(porota)
lista_cuentas.append(mingo_cuentaMultipersona)
lista_cuentas.append(catita_cuentaPlus)
lista_cuentas.append(porota_cuentaSueldo)
clientes_recuperados, cuentas_recuperadas=PersistenciaShelve(lista_clientes, lista_cuentas, "persistir_instancias_shelve").recuperar()
for cliente in clientes_recuperados:
    print(cliente)
for cuenta in cuentas_recuperadas:
    print(cuenta,cuenta.get_titular())

