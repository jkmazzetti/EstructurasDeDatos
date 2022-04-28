from numbers import Number
from Clases.Cuenta import Cuenta
class CuentaSueldoException(Exception):
    pass


class CuentaSueldo(Cuenta):

    def __init__(self, numero_de_cuenta, cliente, extracciones_permitidas, empleador, cuit_empleador):
        try:
            Cuenta.__init__(self, numero_de_cuenta, cliente)
            if not isinstance(extracciones_permitidas, int) or extracciones_permitidas < 0:
                raise CuentaSueldoException("El dato extracciones permitidas debe ser un entero mayor o igual a cero.")
            if not isinstance(empleador, str):
                raise CuentaSueldoException("El dato empleador debe ser un string.")
            if len(empleador) == 0:
                raise CuentaSueldoException("El dato emplador puede estar vacío.")
            if not isinstance(cuit_empleador, str):
                raise CuentaSueldoException("El dato cuit_empleador debe ser un string.")
            if len(cuit_empleador) == 0:
                raise CuentaSueldoException("El dato cuit_empleador puede estar vacío.")
            self._empleador = empleador
            self._cuit_empleador = cuit_empleador
            self._extracciones_realizadas = 0
            self._extracciones_permitidas = extracciones_permitidas
        except Exception as e:
            raise CuentaSueldoException(e)

    def __incremetar_extracciones_realizadas__(self):
        self._extracciones_realizadas += 1

    def reset_extracciones_realizadas(self):
        self._extracciones_realizadas = 0

    def extraer(self, dinero):
        if isinstance(dinero, Number) and not isinstance(dinero, complex):
            if self._saldo - dinero > 0 and self._extracciones_permitidas>self._extracciones_realizadas:
                self._saldo -= dinero
                self.__incremetar_extracciones_realizadas__()
            elif self._saldo - dinero < 0:
                print("No dispone de fondos.")
            else:
                print("Accedió el limite de extracciones diarias.")
        else:
            print("Dato inválido, intente nuevamente.")

    def set_cantidad_de_extracciones(self, nueva_cantidad):
        self._extracciones_permitidas = nueva_cantidad

    def get_empleador(self):
        return self._empleador

    def get_cuit_empleador(self):
        return self._cuit_empleador

    def get_extracciones_permitidas(self):
        return self._extracciones_permitidas

    def get_extracciones_realizadas(self):
        return self._extracciones_realizadas
    def set_extracciones_realizadas(self,extracciones):
        self._extracciones_realizadas=extracciones
    def get_extracciones_restantes(self):
        return self._extracciones_permitidas-self._extracciones_realizadas

    def __str__(self):
        return "SUELDO"
