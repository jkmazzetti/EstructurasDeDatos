class ClienteException(Exception):
    pass
class Cliente(Exception):

    def __init__(self,nombre,dni):
        try:
            if not isinstance(nombre,str):
                raise ClienteException("El nombre debe ser un string.")
            if len(nombre)==0:
                raise ClienteException("El nombre no puede estar vacío.")
            if not isinstance(dni,str):
                raise ClienteException("El dni debe ser ingresado como string.")
            if len(dni)==0:
                raise ClienteException("El dni no puede estar vacío.")
            self._nombre=nombre
            self._dni=dni
        except Exception as e:
            raise ClienteException(e)

    def enviar_mensaje(self, mensaje):
        try:
            print("Bienvenido "+self._nombre+"!\n"+mensaje)
        except Exception as e:
            print("No se puede leer el archivo")
            print(e)
    def get_nombre(self):
        return self._nombre
    def get_dni(self):
        return self._dni
    def __str__(self):
        return self.get_nombre()+","+self.get_dni()
