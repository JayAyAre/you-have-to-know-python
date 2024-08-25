"""
https://www.youtube.com/watch?v=ItxvxYZRcDs

Diferencia de conjuntos consiste en encontrar los elementos estan en
A pero no estan en B.

python nos devolvera los elementos que estan en A pero no estan en B.

podemos usar difference() para hacer la diferencia de dos conjuntos o '-'

sintaxis:
    conjunto_a - conjunto_b
    conjunto_a.difference(conjunto_b)
"""

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

print(f"El conjunto A: {conjunto_a}\nEl conjunto B: {conjunto_b}")

diferencia = conjunto_a.difference(conjunto_b)  # diferencia es {1, 2, 3}

# La diferencia es basicamente los numeros del A que no estan en el B.
print(f"A es diferente de B: {diferencia}")

diferencia_b = conjunto_b - conjunto_a  # diferencia_b es {6, 7, 8}
print(f"B es diferente de A: {diferencia_b}")
