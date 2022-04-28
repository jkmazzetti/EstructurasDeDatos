import pickle

from Clases.Cliente import Cliente
from Clases.CuentaMultipersona import CuentaMultipersona
from Clases.CuentaSueldo import CuentaSueldo
from Clases.CuentaSueldoPlus import CuentaSueldoPlus

class PersistenciaPickle():
    def __init__(self,lista_clientes, lista_cuentas,nombre):
        self._lista_clientes=lista_clientes
        self._lista_cuentas=lista_cuentas
        self._nombre=nombre
        self.persistir()
    def persistir(self):
        archivo_de_datos = open(self._nombre, "wb")
        contenedor=[]
        contenedor.append(self._lista_clientes)
        contenedor.append(lista_cuentas)
        pickle.dump(contenedor, archivo_de_datos)
        archivo_de_datos.close()
    def recuperar(self):
        try:
            abir_archivo = open(self._nombre, "rb")
            contenedor_recuperado = pickle.load(abir_archivo)
            clientes_recuperados = contenedor_recuperado[0]
            cuentas_recuperadas = contenedor_recuperado[1]
            return (clientes_recuperados,cuentas_recuperadas)
        except FileNotFoundError as e:
            print("El archivo no existe o fue modificado.")

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
clientes_recuperados, cuentas_recuperadas=PersistenciaPickle(lista_clientes, lista_cuentas, "persistir_instancias_pickle").recuperar()
for cliente in clientes_recuperados:
    print(cliente)
for cuenta in cuentas_recuperadas:
    print(cuenta,cuenta.get_titular())

