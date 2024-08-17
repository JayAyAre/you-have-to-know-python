"""
https://www.youtube.com/watch?v=jJXro0bDgj4

Se nos solicita un programa en python que dada la siguiente lista

lista_original = [1, 2, 3, 4, 5]

elimine el primer y ultimo elemento de la lista.
teniendo en cuenta que desconocemos los elementos que pueden estar en la lista.

posteriormente, el programa debera mostrar por pantalla las dos listas.

La segunda contendra los elementos que fueron eliminados.
"""

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