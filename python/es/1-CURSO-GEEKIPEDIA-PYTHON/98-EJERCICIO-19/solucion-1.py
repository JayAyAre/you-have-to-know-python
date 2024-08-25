print("".center(80, "="))
print("ORDENADOR DE TUPLAS".center(80, "="))
print("".center(80, "="))

personas = (("Eduardo", 26), ("Maria", 30), ("Gerardo", 20), ("Valentina", 25))

print("La tupla original es:\t", personas)

min_persona = personas[0]
max_persona = personas[0]
for name, age in personas:
    if age < min_persona[1]:
        min_persona = (name, age)
    if age > max_persona[1]:
        max_persona = (name, age)
print("La persona de menor edad es:\t", min_persona)
print("La persona de mayor edad es:\t", max_persona)

# Si queremos ordenar la tupla de manera ascendente

lista_personas = list(personas)

for i in range(len(lista_personas)):
    for j in range(i + 1, len(lista_personas)):
        if lista_personas[j][1] <= lista_personas[i][1]:
            lista_personas[i], lista_personas[j] = lista_personas[j], lista_personas[i]
print("La tupla ordenada de manera ascendente es:\t", lista_personas)
