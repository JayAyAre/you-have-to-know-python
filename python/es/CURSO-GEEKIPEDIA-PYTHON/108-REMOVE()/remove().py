"""
https://www.youtube.com/watch?v=U0q-oZaMMhA

En python para eliminar elementos especificos
de un conjunto, utilizamos el metodo remove() o el metodo discard()

El metodo remove permite eliminar un elemento especifico del conjunto.
si no existe el elemento, saltara un error de tipo KeyError.

sintaxis:
    nombre_conjunto.remove(elemento)

el metodo discard permite eliminar un elemento especifico del conjunto.
si el elemento no existe, no hace nada.

sintaxis:
    nombre_conjunto.discard(elemento)

de por general, es mejor utilizar el metodo discard() que el metodo remove()
"""

# Metodo remove()
frutas = {"manzana", "pera", "uva"}

print(f"Lista original de frutas: {frutas}")
frutas.remove("uva")
print(f"Lista con 'uva' eliminada: {frutas}")

# Metodo discard()
frutas = {"manzana", "pera", "uva"}

print(f"Lista original de frutas: {frutas}")
frutas.discard("uva")
print(f"Lista con 'uva' eliminada: {frutas}")

# Cuando no existe el elemento
frutas = {"manzana", "pera", "uva"}

print(f"Lista original de frutas: {frutas}")
frutas.remove("naranja")  # KeyError
print(f"Lista con 'naranja' eliminada: {frutas}")
