"""
https://www.youtube.com/watch?v=CaY3YcyIO5c

Recordemos que las tuplas son inmutables, es decir, no se pueden cambiar su valor.
pero con la concatenacion de tuplas, podemos unir dos o mas tuplas en una unica tupla nueva.

Formas de concatenar:
    "+" concatena dos tuplas.

"""

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(f"Tupla1: {tupla1}")
print(f"Tupla2: {tupla2}")

tupla3 = tupla1 + tupla2

print(f"Tupla3: {tupla3}")

tupla1 += (
    tupla2  # tuple1 = tupla1 + tupla2, recordemos que esto es reemplazar, no modificar
)
print(f"Tupla1: {tupla1}")

tupla1 = (1, 2, 3)
lista = [1, 2, 3, 4, 5]
tupla4 = tupla1 + tuple(lista)
print(f"Tupla4: {tupla4}")
