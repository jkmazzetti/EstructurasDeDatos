### Solucion

A):

La tecnica de BlockStorage nos sirve para comprimir la lista de terminos, es una tecnica donde agrupamos las palabras del diccionario en bloques, solo se hace la referencia a la primera palabra del bloque.
Luego cada palabra almacena la longitud del termino para poder recuperarlo.

10conjeturar11conjugación8conjugar10conjunción10conjuntado13conjuntamente  
*
9conjuntar10conjuntero13conjuntivitis10conjuntivo8conjunto7conjura 
*
9conjurado8conjurar7conjuro9conllevar13conmemoración10conmemorar
*
13conmemorativo8conmigo

```*``` = Puntero

Aca hago un salto de linea para que se vea mas claro los bloques, pero esto en realidad esta todo en una linea, para que ocupe menos espacio en disco.

B):

Vamos a aplicar la tecnica de compresion de apariciones con codificación de longitud variable. mostrando los números absolutos, los saltos y la codificación en binario



| docsId   | 1000566 | 1000601 | 1000690 | 1000720 |
 -- | -- | -- | --  | -- |
|gaps | |35 |89 |30|



| __1000566__ | __1000601__ | __1000690__ | __1000720__ 
 -- | -- | -- | --  | -- |
|00111101 00001000 11110110 | 10100011 | 11011001 | 10011110

Utilice aca un separador ("|") para que se vea mas claro el pase de binario de cada uno de los docsId, pero en realidad no existe dentro de la compresion.

