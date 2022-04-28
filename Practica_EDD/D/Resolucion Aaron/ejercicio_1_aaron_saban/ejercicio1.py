import csv
import json
import re
from pprint import pprint as pp


class CalculadoraDeTemperaturas:

    # Con esta expresion puedo matchear la fecha y de esa manera obtengop el mes
    __regex_month = r"(\d{1,2})\/(\d{1,2})\/(\d{2})"

    def __init__(self, archivo, output="salida.json"):
        self.archivo = archivo
        self.output = output
        self.informacion_procesada = {
            "anio": {"tmin_promedio": 0, "tmax_promedio": 0, "cantidad": 0}}
        self.listado_de_meses = ["ene", "feb", "mar", "abr",
                                 "may", "jun", "jul", "aug", "sep", "oct", "nov", "dic"]

    def __obtener_mes(self, fecha):
        """  
        Metodo para obtener el mes de una fecha con el formato DD/MM/YY
        Retorna el nombre del mes equivalente al numero de mes de la fecha ingresada
        """
        numero_mes = re.match(self.__regex_month, fecha).group(2)
        nombre_mes = self.listado_de_meses[int(numero_mes) - 1]
        return nombre_mes

    def __borrar_estructura_intermedia(self):
        """ Para calcular el promedio use una key adicional de la cantidad, para que no aparezca en el JSON, la elimino en este paso """

        for key in self.informacion_procesada.keys():
            del self.informacion_procesada[key]["cantidad"]

    def procesar_informacion(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    nombre_mes = self.__obtener_mes(row["FECHA"])

                    tmin = row["TMIN"]
                    tmax = row["TMAX"]

                    self.__procesar_promedio_temperaturas(
                        nombre_mes, tmin, tmax)
                    self.__procesar_promedio_temperatura_anual(tmin, tmax)

                self.__borrar_estructura_intermedia()
        except FileNotFoundError as e:
            print(e)

    def __procesar_promedio_temperaturas(self, nombre_mes, tmin, tmax):
        self.informacion_procesada.setdefault(
            nombre_mes, {"tmax_promedio": 0, "tmin_promedio": 0, "cantidad": 0})
        nuevo_promedio = self.__calcular_promedio(
            tmin, tmax, self.informacion_procesada[nombre_mes])
        self.informacion_procesada[nombre_mes] = nuevo_promedio

    def __calcular_promedio(self, tmin, tmax, valores_actuales):
        if not tmin:
            tmin = 0

        if not tmax:
            tmax = 0

        cantidad = valores_actuales['cantidad']
        tmin_promedio = valores_actuales["tmin_promedio"]
        tmax_promedio = valores_actuales["tmax_promedio"]

        nueva_cantidad = cantidad + 1

        nuevo_promedio_tmin = tmin_promedio + \
            ((float(tmin) - tmin_promedio) / nueva_cantidad)
        nuevo_promedio_tmax = tmax_promedio + \
            ((float(tmax) - tmax_promedio) / nueva_cantidad)
        return {"tmin_promedio": nuevo_promedio_tmin, "tmax_promedio": nuevo_promedio_tmax, "cantidad": cantidad}

    def __procesar_promedio_temperatura_anual(self, tmin, tmax):
        nuevo_promedio = self.__calcular_promedio(
            tmin, tmax, self.informacion_procesada["anio"])
        self.informacion_procesada["anio"] = nuevo_promedio

    def guadar_en_disco(self):
        try:
            with open(self.output, "w") as w:
                json.dump(self.informacion_procesada, w)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    calculadora = CalculadoraDeTemperaturas("temperatura.csv")
    calculadora.procesar_informacion()
    calculadora.guadar_en_disco()
    print("Informacion almacenada en disco: ")
    pp(calculadora.informacion_procesada)
