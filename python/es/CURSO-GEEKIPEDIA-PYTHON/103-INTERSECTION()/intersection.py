"""
https://www.youtube.com/watch?v=z44g9piaNwE

La interseccion de dos conjuntos consiste en encontrar los elementos
en comun en ambos conjuntos.

en python podemos hacer la interseccion de dos conjuntos usando el operador &
o el metodo intersection()

sintaxis:
    conjunto_a & conjunto_b
    conjunto_a.intersection(conjunto_b)
"""

conjunto_a = {1, 2, 3, 4, 5, 6}
conjunto_b = {2, 6, 7, 8, 9}

print(f"El conjunto A: {conjunto_a}\nEl conjunto B: {conjunto_b}")
interseccion = conjunto_a.intersection(conjunto_b)
print(f"El conjunto C: {interseccion}")

interseccion = conjunto_a & conjunto_b
print(f"El conjunto C: {interseccion}")
