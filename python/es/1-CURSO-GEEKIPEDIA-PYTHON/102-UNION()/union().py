"""
https://www.youtube.com/watch?v=sWQZJ-Lgx5k

Union entre conjuntos consiste en unir dos conjuntos en un solo conjunto.
manteniendo los elementos unicos de ambos conjuntos.

sintaxis:
    conjunto_a.union(conjunto_b)

Ademas, podemos usar tambien el operador | para hacer union de conjuntos.

    conjunto_a | conjunto_b
"""

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {2, 6, 7}

print(f"El conjunto A: {conjunto_a}\nEl conjunto B: {conjunto_b}")
conjunto_c = conjunto_a.union(conjunto_b)
print(f"El conjunto C: {conjunto_c}")

conjunto_a = {"a", "b", "c", "d", "e"}
conjunto_b = {"b", "f", "g", "h", "i"}

print(f"El conjunto A: {conjunto_a}\nEl conjunto B: {conjunto_b}")
conjunto_c = conjunto_a | conjunto_b
print(f"El conjunto C: {conjunto_c}")
