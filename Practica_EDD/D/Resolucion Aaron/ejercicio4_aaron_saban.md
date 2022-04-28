## Consigna

Escribir las siguientes expresiones regulares. 

1) Que acepte palíndromos(palabras que se leen igual desde adelante hacia atrás y desde atrás hacia adelante) de longitud menor o igual a 5. 
Ejemplo debe aceptar: rotor, ala, solos, 
y rechazar neuquen, el le (porque son dos palabras) 

2) Números enteros y en punto flotante, incluyendo notación científica. Debería aceptar, por ejemplo, "1", "-1", "+15", "1.55", ".5", "5.", "1.3e2", "1E-4", "1e+12" y rechazar "1a", "+-1", "1.2.3", "1+1", "1e4.5", ".5.", 1f5, "."


## Solucion

1:
```/([a-zA-Z])(?:([a-zA-Z])(?:([a-zA-Z])\2|\2?))?\1/```

2:
```[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? ```