"""
https://www.youtube.com/watch?v=k5ZTg6eLzQA

En python es posible modificar o agregar elementos a un diccionario.

Sintaxis:
    diccionario[clave] = valor
"""

diccionario = {"a": 1, "b": 2, "c": 3}

print("Mi diccionario inicial:\n", diccionario)
print("Agrego la clave 'd' con el valor 4\n")

diccionario["d"] = 4
print("Mi diccionario despues de agregar la clave 'd' con el valor 4:\n", diccionario)

diccionario["a"] = "uno"
print(
    "Mi diccionario despues de cambiar el valor de la clave 'a' a 'uno':\n", diccionario
)
