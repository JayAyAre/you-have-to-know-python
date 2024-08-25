conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

print(conjunto_A)
print(conjunto_B, "\n")

# Utilizando el método difference()
diferencia_conjuntosAB = conjunto_A.difference(conjunto_B)
diferencia_conjuntosBA = conjunto_B.difference(conjunto_A)

print("conjunto_A.difference(conjunto_B):", diferencia_conjuntosAB)
print("conjunto_B.difference(conjunto_A):", diferencia_conjuntosBA)
print()

# Utilizando el operador -
diferencia_conjuntosAB = conjunto_A - conjunto_B
diferencia_conjuntosBA = conjunto_B - conjunto_A

print("conjunto_A - conjunto_B:", diferencia_conjuntosAB)
print("conjunto_B - conjunto_A:", diferencia_conjuntosBA)
