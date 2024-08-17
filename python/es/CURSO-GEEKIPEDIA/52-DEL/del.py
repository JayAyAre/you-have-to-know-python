"""
https://www.youtube.com/watch?v=ByFYD6vsTR0&list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz&index=53

En python es posible eliminar uno o varios elementos de una lista indicandole el elemento a eliminar
o el indice de la posicion donde se encuentra el elemento a eliminar.

Pero tambien podemos eliminar toda una lista, o eliminar una lista completa.

ademas, de que 'del' nos permite eliminar un elemento en particular, o varios.

sintaxis:
    del lista => Elimina toda la lista
    del lista[index] => Elimina un unico elemento de la lista, posicionado en el index
    del lista[inicio:fin] => Elimina un rango de elementos de la lista, inicio y fin indican el rango
"""

vocales = ["a", "e", "i", "o", "i"]
print("\nMi lista de vocales es:\n", vocales, end="\n\n")

print("Usamos del para eliminar el elemento [0]")
del vocales[0]
print("La lista es:\n", vocales, end="\n\n")

vocales = ["a", "e", "i", "o", "i"]
print("\nMi lista de vocales es:\n", vocales, end="\n\n")

print("Usamos del para eliminar el elemento [0:2]")
del vocales[0:2]
print("La lista es:\n", vocales, end="\n\n")

vocales = ["a", "e", "i", "o", "i"]
print("\nMi lista de vocales es:\n", vocales, end="\n\n")

print("Usamos del para eliminar todos sus elementos [:]")
del vocales[:]
print("La lista es:\n", vocales, end="\n\n")

vocales = ["a", "e", "i", "o", "i"]
print("\nMi lista de vocales es:\n", vocales, end="\n\n")

print("Usamos del para eliminar toda la lista...")
del vocales
print("La lista es:", vocales, end="\n\n") # Salta error porque no existe la lista
