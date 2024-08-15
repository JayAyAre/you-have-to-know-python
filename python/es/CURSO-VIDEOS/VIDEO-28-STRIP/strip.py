"""
https://www.youtube.com/watch?v=8tuyYql2duA

En python, al trabajar con cadenas de caracteres, es comun que se necesiten
eliminar espacios en blanco, o bien, caracteres especiales.

Para ello, se utilizan las siguientes sentencias:
    - strip()
    - lstrip()
    - rstrip()

strip():
    Elimina todos los espacios en blanco al inicio y al final de la cadena.
    Si no se le especifica uno o mas caracteres, se eliminnaran los espacios en blanco y
    los saltos de linea.

    Es equivalente a:
        string.strip()

    Solo puede eliminar espacios en blanco al inicio y al final de la cadena.
    un ejemplo seria:
        string = " hola mundo "
        print(string.strip())
        # imprime "hola mundo"
"""

cadena = "...hola mundo..."
print(cadena.strip(".")) # imprime "hola mundo"
cadena = "HHhola mundo"
print(cadena.strip("H")) # imprime "hola mundo"
cadena = "Hola ernesto"

"""
Si le pasamos un string, se eliminan los caracteres especificados.

Y para hacerlo, elimina en orden, los caracteres especificados, en caso de que lo encuentre, vuelve al
inicio y los borra hasta que no encuentre ninguno.
"""
print(cadena.strip("se tHo"))
