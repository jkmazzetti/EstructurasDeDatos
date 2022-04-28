import json
from Clases.Cliente import Cliente
from Clases.CuentaMultipersona import CuentaMultipersona
from Clases.CuentaSueldo import CuentaSueldo
from Clases.CuentaSueldoPlus import CuentaSueldoPlus


class PersistenciaJson():
    def __init__(self, lista_clientes,lista_cuentas,nombre_archivo):
        self._lista_clientes=lista_clientes
        self._lista_cuentas=lista_cuentas
        self._nombre_archivo=nombre_archivo
        self.persistir()
    def persistir(self):
        try:
            with open(self._nombre_archivo+".json", "w") as contenedor:
                dni_nombre = {}
                dni_cotitulares = {}
                dni_saldo = {}
                dni_disponible = {}
                dni_extracciones_realizadas = {}
                tipo_cuentas = {}

                for cliente in self._lista_clientes:
                    if cliente.get_dni() not in dni_nombre:
                        dni=cliente.get_dni()
                        nombre=cliente.get_nombre()
                        dni_nombre[dni] = nombre

                for cuenta in self._lista_cuentas:

                    tipo = cuenta.__str__()
                    numero_de_cuenta = cuenta.get_numero()
                    dni_titular = cuenta.get_titular().get_dni()
                    saldo = cuenta.get_saldo()
                    if tipo not in tipo_cuentas.keys():
                        tipo_cuentas[tipo] = []
                    if tipo == "MULTIPERSONA":
                        lista_cotitulares=[]
                        disponible = cuenta.get_disponible()
                        decubierto = cuenta.get_descubierto()
                        datos_cuenta = [numero_de_cuenta, dni_titular, decubierto]
                        for cotitular in cuenta.get_cotitulares():
                            lista_cotitulares.append(cotitular.get_dni())
                        tipo_cuentas["MULTIPERSONA"].append(datos_cuenta)
                        dni_disponible[dni_titular] = disponible
                        dni_cotitulares[dni_titular]=lista_cotitulares
                    else:
                        extracciones_permitidas = cuenta.get_extracciones_permitidas()
                        extracciones_realizadas = cuenta.get_extracciones_realizadas()
                        empleador = cuenta.get_empleador()
                        cuil_empleador = cuenta.get_cuit_empleador()
                        if tipo == "SUELDO":
                            datos_cuenta = [numero_de_cuenta, dni_titular, extracciones_permitidas, empleador,
                                            cuil_empleador]
                            tipo_cuentas["SUELDO"].append(datos_cuenta)
                        else:
                            disponible = cuenta.get_disponible()
                            decubierto = cuenta.get_descubierto()
                            datos_cuenta = [numero_de_cuenta, dni_titular, extracciones_permitidas, empleador,
                                            cuil_empleador, decubierto]
                            tipo_cuentas["PLUS"].append(datos_cuenta)
                            dni_disponible[dni_titular] = disponible
                        dni_extracciones_realizadas[dni_titular] = extracciones_realizadas
                    dni_saldo[dni_titular] = saldo
                contenedor_json = []
                contenedor_json.append(dni_nombre)
                contenedor_json.append(tipo_cuentas)
                contenedor_json.append(dni_extracciones_realizadas)
                contenedor_json.append(dni_disponible)
                contenedor_json.append(dni_cotitulares)
                contenedor_json.append(dni_saldo)
                json.dump(contenedor_json, contenedor)
        except Exception as e:
            print(e)
            raise Exception(e)

    def recuperar(self):
        try:
            clientes_recuperados = []
            cuentas_recuperadas = []
            with open(self._nombre_archivo+".json", "r") as contenedor:
                lista_diccionarios = json.load(contenedor)
                diccionario_clientes = lista_diccionarios[0]
                lista_dni = diccionario_clientes.keys()
                for dni in lista_dni:
                    dni_cliente = dni
                    nombre_cliente = diccionario_clientes[dni]
                    clientes_recuperados.append(Cliente(nombre_cliente, dni_cliente))
                diccionario_cuentas = lista_diccionarios[1]
                tipos_cuenta = diccionario_cuentas.keys()
                for tipo in tipos_cuenta:
                    if tipo == "MULTIPERSONA":
                        cuentas_multipersona=diccionario_cuentas.get(tipo)
                        for cuenta in cuentas_multipersona:
                                    numero_cuenta = cuenta[0]
                                    dni_cliente = cuenta[1]
                                    cliente = Cliente(diccionario_clientes.get(dni_cliente), dni_cliente)
                                    descubierto = cuenta[2]
                                    cuentas_recuperadas.append(CuentaMultipersona(numero_cuenta, cliente, descubierto))
                    elif tipo == "SUELDO":
                        cuentas_sueldo=diccionario_cuentas.get(tipo)
                        for cuenta in cuentas_sueldo:
                            numero_cuenta = cuenta[0]
                            dni_cliente = cuenta[1]
                            cliente = Cliente(diccionario_clientes.get(dni_cliente), dni_cliente)
                            extracciones_permitidas = cuenta[2]
                            empleador = cuenta[3]
                            cuit_empleador = cuenta[4]
                            cuentas_recuperadas.append(CuentaSueldo(numero_cuenta, cliente, extracciones_permitidas, empleador,cuit_empleador))
                    else:
                        cuentas_sueldo_plus=diccionario_cuentas.get(tipo)
                        for cuenta in cuentas_sueldo_plus:
                            numero_cuenta = cuenta[0]
                            dni_cliente = cuenta[1]
                            extracciones_permitidas=cuenta[2]
                            empleador = cuenta[3]
                            cuit_empleador = cuenta[4]
                            descubierto = cuenta[5]
                            cliente = Cliente(diccionario_clientes.get(dni_cliente), dni_cliente)
                            cuentas_recuperadas.append(CuentaSueldoPlus(numero_cuenta, cliente, extracciones_permitidas, empleador,cuit_empleador, descubierto))

                diccionario_extracciones = lista_diccionarios[2]
                lista_dni = diccionario_extracciones.keys()
                for dni in lista_dni:
                    for cuenta in cuentas_recuperadas:
                        dni_titular=cuenta.get_titular().get_dni()
                        if dni_titular == dni:
                            cuenta.set_extracciones_realizadas(diccionario_extracciones.get(dni))
                diccionario_disponible = lista_diccionarios[3]
                lista_dni = diccionario_disponible.keys()
                for dni in lista_dni:
                    for cuenta in cuentas_recuperadas:
                        dni_titular=cuenta.get_titular().get_dni()
                        if dni_titular == dni:
                            cuenta.set_disponible(diccionario_disponible.get(dni))
                diccionario_cotitulares = lista_diccionarios[4]
                lista_dni_titulares = diccionario_cotitulares.keys()
                for dni_titular in lista_dni_titulares:
                    lista_dni_cotitulares=diccionario_cotitulares.get(dni_titular)
                    for dni_cotitular in lista_dni_cotitulares:
                        nombre_cotitular=diccionario_clientes.get(dni_cotitular)
                        cotitular=Cliente(nombre_cotitular,dni_cotitular)
                        for cuenta in cuentas_recuperadas:
                            if dni_titular==cuenta.get_titular().get_dni():
                                cuenta.agregar_cotitular(cotitular)
                diccionario_saldos = lista_diccionarios[5]
                lista_dni_titulares = diccionario_saldos.keys()
                for dni in lista_dni_titulares:
                    for cuenta in cuentas_recuperadas:
                            if cuenta.get_titular().get_dni() == dni:
                                for i in range(len(clientes_recuperados)-1):
                                    cuenta.set_saldo(diccionario_saldos.get(dni))

            return(clientes_recuperados,cuentas_recuperadas)

        except FileNotFoundError as e:
            print("No se encuentra el archivo.")


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
clientes_recuperados=[]
cuentas_recuperadas=[]
clientes_recuperados, cuentas_recuperadas=PersistenciaJson(lista_clientes, lista_cuentas, "persistir_instancias_json").recuperar()
for cliente in clientes_recuperados:
    print(cliente)
for cuenta in cuentas_recuperadas:
    print(cuenta,cuenta.get_titular())
