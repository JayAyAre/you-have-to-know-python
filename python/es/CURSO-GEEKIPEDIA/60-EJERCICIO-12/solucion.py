print("".center(100, "="))
print("ELIMINAR VALORES DE UNA LISTA Y GUARDARLOS".center(100))
print("".center(100, "="), end="\n\n")

lista_original = [1, 2, 3, 4, 5]

lista_modificada = lista_original[:]
lista_eliminados = []

lista_eliminados.append(lista_modificada.pop(0))
lista_eliminados.append(lista_modificada.pop())

print("La lista original es: ", lista_original)
print("La lista modificada es: ", lista_modificada)
print("La lista eliminados es: ", lista_eliminados)
