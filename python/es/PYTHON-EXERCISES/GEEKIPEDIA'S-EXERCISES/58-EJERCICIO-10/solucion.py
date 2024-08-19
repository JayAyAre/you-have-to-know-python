print("".center(100, "="))
print("SUMAR VALORES DE UNA LISTA".center(100))
print("".center(100, "="), end="\n\n")

len_lista = int(input("Ingrese la longitud de la lista: "))
lista = []

for i in range(0, len_lista, 1):
    lista.append(int(input("Ingrese el numero de la posicion " + str(i) + ": ")))

suma = sum(lista)
print("La lista es: ", lista)
print("La suma de todos los elementos es: ", suma)
