from numbers import Number

from Clases.Cliente import Cliente
from Clases.Cuenta import Cuenta
from Clases.Descubierto import Descubierto

class CuentaMultipersonaException(Exception):
    pass

class CuentaMultipersona(Cuenta,Descubierto):
    def __init__(self,numero_de_cuenta,cliente,descubierto):
        try:
            Cuenta.__init__(self,numero_de_cuenta,cliente)
            Descubierto.__init__(self,descubierto)
            self._cotitulares=[]
        except Exception as e:
            raise CuentaMultipersonaException(e)

    def get_cotitulares(self):
        return self._cotitulares

    def agregar_cotitular(self,nuevo_cotitular):
        if isinstance(nuevo_cotitular,Cliente):
            existe=False
            for cotitutlar in self._cotitulares:
                if nuevo_cotitular.get_dni()==cotitutlar.get_dni():
                    existe=True
                    print("Ya es cotitular.")
                    break
            if existe==False:
                self._cotitulares.append(nuevo_cotitular)
        else:
            print("Dato inválido, intente nuevamente.")

    def extraer(self, dinero):
        if isinstance(dinero,Number) and not isinstance(dinero,complex):
            if self.get_disponible()+self.get_saldo()-dinero>=0:
                    self._saldo-=dinero
                    if self._saldo<0:
                        self.restar_descubierto(self._saldo)
            else:
                print("No dispone de fondos.")
        else:
            print("Dato inválido, intente nuevamente.")

    def __str__(self):
        lista=[]
        for cotitular in self._cotitulares:
            lista.append(cotitular.get_dni())
        return "MULTIPERSONA"
