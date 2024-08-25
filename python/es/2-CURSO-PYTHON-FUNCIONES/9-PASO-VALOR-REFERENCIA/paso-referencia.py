def modificar_lista(lista):
    lista.append(10)
    print("Dentro de la funcion: lista = ", lista)


# Los objetos personalizados se pasan por referencia
# listas, diccionarios, clases, objetos, etc.
lista = [1, 2, 3] # Con la lista, se pasa por referencia
modificar_lista(lista) # Modificara la lista original dentro de la funcion
print("Fuera de la funcion: lista = ", lista)