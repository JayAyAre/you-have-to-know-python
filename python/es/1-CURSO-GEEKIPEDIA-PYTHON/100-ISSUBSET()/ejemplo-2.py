conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {5, 4, 3, 2, 1}

print(f"Conjunto A: {conjunto_a}\nConjunto B: {conjunto_b}\n")
print("¿B es subconjunto de A? \n")

es_subconjunto = conjunto_b.issubset(conjunto_a)
print("Utilizando el método issubset():", es_subconjunto)

es_subconjunto = conjunto_b <= conjunto_a
print("Utilizando el operador <=:", es_subconjunto)

es_subconjunto = conjunto_b < conjunto_a
print("Utilizando el operador <:", es_subconjunto)
