"""
https://youtu.be/I5lDyVVhNG8?si=gxDe5O3gf3ZYM20k

En python es posible eliminar elementos de una lista indicandole el elemento a eliminar
a diferencia de indicar la posicion como en pop.

Para ello usaremos el metodo remove.

Sintaxis:
    lista.remove(elemento)

"""

vocales = ["a", "e", "i", "o", "u"]
print("Mi lista de vocales es:", vocales, end="\n\n")

# Hay que tener en cuenta que el metodo dara error en caso de que no exista el elemento en la lista

# Recordemos que recorre uno a uno la lista hasta que encuentre coincidencia con el elemento a eliminar
print("Eliminando la 'a' de la lista...")
vocales.remove("a")
print("La lista es:", vocales, end="\n\n")

# Ademas, elimina la primera ocurrencia de un elemento, no todas las ocurrencias
# Tambien distingue entre mayusculas y minusculas
vocales = ["a", "e", "i", "o", "i"]
print("Mi lista de vocales es:", vocales, end="\n\n")
print("Eliminando la 'i' de la lista...")
vocales.remove("i")
print("La lista es:", vocales, end="\n\n")

vocales = ["a", "e", "i", "o", "i"]
print("Mi lista de vocales es:", vocales, end="\n\n")
print("Eliminando la 'y' de la lista...")
vocales.remove("y")
print("La lista es:", vocales, end="\n\n")