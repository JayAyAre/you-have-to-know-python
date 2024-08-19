print("".center(80, "="))
print("MODIFICADOR DE TUPLAS".center(80, "="))
print("".center(80, "="))

tupla = (5, 8, 3, 3, 1, 6, 2)

print("\nLa tupla original es:{}".format(tupla))

exist_number = int(input("Ingrese un numero existente en la tupla: "))
lista = list(tupla)

for i in range(len(tupla)):
    if lista[i] == exist_number:
        lista[i] = 0
        print(f"El numero {exist_number} en la posicion {i} se ha reemplazado por 0")
    if exist_number not in lista:
        break

tupla_modificada = tuple(lista)
print("\nLa tupla original es:{}".format(tupla))
print("\nLa tupla modificada es:{}".format(tupla_modificada))
