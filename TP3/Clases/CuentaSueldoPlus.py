from numbers import Number
from Clases.CuentaSueldo import CuentaSueldo
from Clases.Descubierto import Descubierto

class CuentaSueldoPlusException(Exception):
    pass

class CuentaSueldoPlus(CuentaSueldo, Descubierto):
    def __init__(self,numero_de_cuenta,cliente,extracciones_permitidas,empleador,cuit_empleador,descubierto):
        try:
            CuentaSueldo.__init__(self, numero_de_cuenta, cliente, extracciones_permitidas, empleador, cuit_empleador)
            Descubierto.__init__(self,descubierto)
        except Exception as e:
            raise CuentaSueldoPlusException(e)

    def extraer(self, dinero):
        if isinstance(dinero,Number) and not isinstance(dinero,complex):
            if self.get_disponible()+self.get_saldo()-dinero>=0 and self.get_extracciones_permitidas()>self.get_extracciones_realizadas():
                    self._saldo-=dinero
                    if self._saldo<0:
                        self.restar_descubierto(self._saldo)
                    self.__incremetar_extracciones_realizadas__()
            elif self.get_disponible()+self.get_saldo()-dinero>=0:
                print("No dispone de fondos.")
            else:
                print("Accedió el limite de extracciones diarias.")
        else:
            print("Dato inválido, intente nuevamente.")

    def depositar(self, dinero):
        if self.get_disponible()+dinero<=self.get_descubierto():
            self.cubrir(dinero)
            self._saldo+=dinero
        elif self.get_disponible()<self.get_descubierto() and self.get_disponible()+dinero>self.get_descubierto():
            diferencia=self.get_disponible()+dinero-self.get_descubierto()
            self._saldo+=(dinero)
            self.cubrir(dinero-diferencia)
        else:
            self._saldo+=dinero
    def get_extracciones_restantes(self):
        return self._extracciones_permitidas-self._extracciones_realizadas
    def __str__(self):
        return "PLUS"
