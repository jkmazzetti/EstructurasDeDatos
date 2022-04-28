from numbers import Number
from abc import ABC

class DescubiertoException(Exception):
    pass

class Descubierto(ABC):
    def __init__(self,descubierto):
        try:
            if(isinstance(descubierto,Number) and not isinstance(descubierto,complex) and descubierto>0):
                self._descubierto=descubierto
                self._disponible=descubierto
            else:
                raise DescubiertoException("El descubierto debe ser un numero positivo.")
        except DescubiertoException as e:
            print(e)
            raise DescubiertoException(e)
    def set_descubierto(self, descubierto):
        confirmacion=False
        if descubierto>self._descubierto or self._disponible==self._descubierto:
            if self._disponible==self._descubierto:
                self._descubierto=descubierto
                self._disponible=descubierto
            else:
                self._disponible=descubierto-(self._descubierto-self._disponible)
                self._descubierto=descubierto
            confirmacion=True
        return confirmacion
    def aviso_descubierto(self):
        print(self._descubierto)
    def get_disponible(self):
        return self._disponible
    def restar_descubierto(self,adeuda):
        self._disponible+=adeuda
    def get_descubierto(self):
        return self._descubierto
    def cubrir(self,dinero):
        self._disponible+=dinero
    def set_disponible(self,dinero):
        self._disponible=dinero


