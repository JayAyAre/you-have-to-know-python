conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {1, 2, 3, 4, 5}

print(f"Mi conjunto A es: {conjunto_a}")
print(f"Mi conjunto B es: {conjunto_b}")
print("B es un subconjunto de A?\n")
print(conjunto_b.issubset(conjunto_a))

conjunto_b = {1, 2, "a"}
print(f"Mi conjunto B es: {conjunto_b}")
print("B es un subconjunto de A?\n")
print(conjunto_b.issubset(conjunto_a))

conjunto_b = {1, 2, 3, 4, 5}
print(f"Mi conjunto B es: {conjunto_b}")
print("B es un subconjunto de A?\n")
print(conjunto_b.issubset(conjunto_a))
print("A es un subconjunto de B?\n")
print(conjunto_a.issubset(conjunto_b))
