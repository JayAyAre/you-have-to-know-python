"""
https://www.youtube.com/watch?v=oFYeyghNBJw

Se refiere a la operacion que devuelve un conjunto que contiene
los elementos de A que no estan en B y los elementos de B que no
estan en A. es decir, los elementos exclusivos de A y los elementos
exclusivos de B.

Para ello se puede usar el operador ^ o el método symmetric_difference()

sintaxis:
    conjunto_a ^ conjunto_b
    conjunto_a.symmetric_difference(conjunto_b)
"""

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

print(f"El conjunto A: {conjunto_a}\nEl conjunto B: {conjunto_b}")

diferencia = conjunto_a.symmetric_difference(conjunto_b)

print(f"La diferencia entre A y B es: {diferencia}")

diferencia = conjunto_a ^ conjunto_b

print(f"La diferencia entre A y B es: {diferencia}")
