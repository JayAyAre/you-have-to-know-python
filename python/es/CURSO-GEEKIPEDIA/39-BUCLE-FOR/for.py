"""
https://www.youtube.com/watch?v=C2JE-6tNONw

El ciclo o bucle for nos permite realizar una accion o repetir
un bloque de codigo un numero determinado de veces.

sintax:
    for variable in objeto_iterativo:
        codigo

    for variable in objeto_iterativo:
        codigo
        otro_codigo

    for variable in objeto_iterativo:
        if condicion:
            codigo
            break
        else:
            codigo

Un objeto iterativo es aquel que permite recorrer sus elementos de uno a uno
como por ejemplo una cadena de caracteres, una lista, un diccionario, etc.

"""
string = "Hola"

for char in string:
    print(char)

print("Fin del programa\n")