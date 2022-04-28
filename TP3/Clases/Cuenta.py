from abc import ABC, abstractmethod
from numbers import Number

from Clases.Cliente import Cliente


class CuentaException(Exception):
    pass


class Cuenta(ABC):
    def __init__(self, numero_de_cuenta, cliente):
        try:
            self._saldo = 0
            self._titular = cliente
            if not isinstance(numero_de_cuenta, str):
                raise CuentaException("El número de cuenta debe ser un string.")
            elif len(numero_de_cuenta) == 0:
                raise CuentaException("El número de cuenta no puede estar vacío.")
            elif not isinstance(cliente, Cliente):
                raise CuentaException("El dato cliente debe ser una instancia de Cliente.")
            else:
                str(int(numero_de_cuenta))
                self._numero = numero_de_cuenta
                self._cliente = cliente
        except Exception as e:
            raise CuentaException(e)

    def depositar(self, dinero):
        if not isinstance(dinero, Number) or isinstance(dinero, complex):
            print("Dato inválido, intente nuevamente.")
        elif dinero > 0:
            self._saldo += dinero

    @abstractmethod
    def extraer(self, dinero):
        pass

    def get_saldo(self):
        return self._saldo

    def get_numero(self):
        return self._numero

    def get_titular(self):
        return self._titular
    def set_saldo(self,saldo):
        self._saldo=saldo


