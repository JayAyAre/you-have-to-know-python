"""
https://www.youtube.com/watch?v=0xzoID_sbC

Es una alternativa a la concatenacion, que es la operacion de unir dos cadenas de caracteres.
Permiten agregar contenidos en una cadena de caracteres, y tambien se pueden unir
con otros numeros.

Se añadieron a python 3.6.

Es importante su sintaxis:
    f"{variable}" o f"{objeto}"
"""

# Forma 1

nombre , edad = "Jordi", 21
print(f"Hola {nombre} tienes {edad} años")

# Podemos añadir expresiones dentro de la cadena de caracteres
print(f"El siguiente año tendras {edad + 1} años")