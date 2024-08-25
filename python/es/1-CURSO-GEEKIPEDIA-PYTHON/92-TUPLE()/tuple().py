"""
https://www.youtube.com/watch?v=A6czS1VlRt4

Permite crear una tupla a partir de una estructura de datos.

sintaxis:
    tuple(iterable) Admite unicamente un argumento iterable.
"""

lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
print(f"Lista: {lista}")
print(f"Tupla: {tupla}")

diccionario = {"a": 1, "b": 2, "c": 3}
tupla = tuple(diccionario)
print(f"Diccionario: {diccionario}")
print(f"Tupla: {tupla}")

tupla = tuple(diccionario.items())
print(f"Diccionario: {diccionario}")
print(f"Tupla: {tupla}")
