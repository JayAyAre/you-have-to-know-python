"""
https://youtu.be/xptKv7yhfSA?si=JkCn6hEpAFh6m2PT

Los comentarios es una construccion de Python que nos permita incrustar notas o anotaciones en el codigo
de tal manera que se puedan leer por humanos, sin necesidad de que lo ejecute un interprete o compilador.

Sus principales usos son:
- Hacer el codigo mas facil de entender
- Facilitar el uso y el mantenimiento del codigo
- Evitar que se ejecute el codigo

Se pueden añadir de varias formas:
- Linea:
    # Esto es un comentario
    " Esto es un comentario "
- Bloque:
    Con 3 dobles comillas en vez de 1
    con 3 comisas simples en vez de 1

Las comillas no son comentarios, son Strings, que al no ser asignados a una variable
se interpretan como un valor nulo, por ello el interprete de Python no las toma en cuenta

"""
# Este es un comentario en linea

# Esto escribe "Hola" en la consola
print("Hola")

"Otro comentario en linea"

"""
Hola
es
un
comentario
multilinea
"""

'''
Este
Tambien
es
un
comentario
multilinea

'''


