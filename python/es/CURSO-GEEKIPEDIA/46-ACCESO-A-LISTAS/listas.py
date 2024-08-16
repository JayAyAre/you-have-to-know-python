"""
https://www.youtube.com/watch?v=jxA2ZUXjXpQ

En python es posible que tengamos que acceder a una lista
ya sea para leer o modificar su contenido.

Para ello nos apoyamos de los indices los cuales nos indican
su posicion dentro de la lista.
"""

lista_lenguajes = ["Python", "Java", "C++", "JavaScript", "PHP"]

print("Nuestra lista de lenguajes es: ")
print(lista_lenguajes)

print("\nLa longitud de la lista es: ", len(lista_lenguajes))
print("El indice 0 es: ", lista_lenguajes[0])
print("El indice -1 es: ", lista_lenguajes[-1])
print("Los indices 1:3 son: ", lista_lenguajes[0:3])
print("Los indices :2 son: ", lista_lenguajes[:2])
print("Los indices : son: ", lista_lenguajes[:])
print("Los indices ::-1 son: ", lista_lenguajes[::-1])
print("Error si intento acceder al indice len(lista_lenguajes): ", lista_lenguajes[len(lista_lenguajes)])