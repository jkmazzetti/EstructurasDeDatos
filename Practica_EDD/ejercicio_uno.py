import csv
import json
#Solo pude calcular el promedio anual... me abataté...
if __name__ == '__main__':
    with open("datos-tipo-cambio-usd-futuro-dolar-frecuencia-diaria.csv", "r") as datos_csv:
        reader = csv.DictReader(datos_csv)
        dict_anio = {}
        for fila in reader:
            anio = fila["fecha"].split("-")[0]
            tipo_cambio = fila["tipo_cambio_bna_vendedor"]
            if str(anio) not in dict_anio.keys() and tipo_cambio!=False:
                promedio={"promedio": round(float(tipo_cambio),2)}
                dict_anio[anio]=promedio
            elif tipo_cambio!=False:
                promedio_nuevo=round((dict_anio.get(anio).get("promedio")+float(tipo_cambio))/2,2)
                print(promedio_nuevo)
                dict_anio.get(anio)["promedio"] = promedio_nuevo
    with open("salida.json","w") as contenedor:
        json.dump(dict_anio,contenedor)
