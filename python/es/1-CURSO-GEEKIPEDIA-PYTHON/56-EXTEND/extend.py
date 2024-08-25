"""
https://www.youtube.com/watch?v=LNJCBp3bbz4

Al trabajar con listas, es posible que queramos concatenar dos listas
para obtener una nueva lista. Para ello usaremos el metodo extend.

este metodo permite concatenar dos o mas listas ademas de añadir un elemento a una lista

sintaxis:
    lista.extend(lista2)
"""

invitados = ["Carolina", "juan", "maria", "pedro"]
amigos = ["Luis", "Ana"]

print(f"\nLista de invitados: {invitados}")
print(f"Lista de amigos: {amigos}")

invitados.extend(amigos) # Añado los elementos de amigos, al final de invitados
print(f"Lista de invitados con los amigos: {invitados}")

decenas_hasta_100 = [10,20]
print(f"Añadimos el resto de decenas a la lista: {decenas_hasta_100}")
decenas_hasta_100.extend(range(30, 110, 10))
print("La lista queda asi: ", decenas_hasta_100)

amigos1 = ["Luis", "Ana"]
amigos2 = ["Maria", "Pedro"]
amigos3 = ["Juan", "Carolina"]
amigos4 = ["Maria", "Pedro"]

print("Ahora juntaremos todas las listas")
del amigos1[:]

amigos.extend(amigos1)
amigos.extend(amigos2)
amigos.extend(amigos3)
amigos.extend(amigos4)

print(f"Lista de amigos: {amigos}")