"""
https://www.youtube.com/watch?v=4-u1wnO46iQ

Constructor list()

en python, podemos ver la necesidad de convertir un elemento iterable en una lista.
para ello, podemos hacer un ciclo e insertarlos uno a uno en una lista.

pero para simplificarlo, podemos usar el constructor list()

Sintaxis:
    lista = list(iterable)


"""

print(range(0, 101, 10))
range = list(range(0, 101,10))
print(range)

print("\n", list("Hola mundo"))
