"""
    Los metodos mas comunes de listas son:

        - append()
        - extend()
        - insert()
        - pop()
        - remove()
        - reverse()
        - sort()
        - index()
        - count()
        - copy()
        - clear()

    Ademas, recordemos que las listas son estructuras de datos ordenadas (Lo que significa que pueden
        ser indexadas con [] y pueden ser sliced con [:], y que los objetos estan colocados de tal forma
        que el ultimo agregado es el ultimo elemento, teniendo en cuenta excepciones.) y que son mutables
        (Lo que significa que pueden ser modificados, añadir elementos, o borrar elementos).
"""

# Como crear listas

lista = []
lista = [1, 2, 3]
# Usamos la funcion built-in list, que crea una lista en funcion de un iterable
lista = list(range(10))

# Acceder a listas
print()
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[0:3])
print(lista[-1::-1])
print()

# Como modificar listas

lista = [1, 2, 3]
lista[0] = 5
lista[1] = 6
lista[2] = 7
print(lista)
print()

# Metodos de listas

# append(), consiste en agregar un elemento al final de la lista

lista = [1, 2, 3]
print(f"Lista original antes de usar el metodo append(4): \n\t {lista}")
lista.append(4)
print("\t", lista)

# extend(), consiste en agregar un iterable al final de la lista

lista = [1, 2, 3]
print(
    f"Lista original antes de usar el metodo extend([4, 5, 6]): \n\t {lista}")
lista.extend([4, 5, 6])
print("\t", lista)

# insert(), consiste en insertar un elemento en una posicion determinada
# El indice es el primer argumento, y el elemento es el segundo argumento

lista = [1, 2, 3]
print(f"Lista original antes de usar el metodo insert(1, 4): \n\t {lista}")
lista.insert(1, 4)
# Cuando se inserta un elemento en una posicion, los elementos incluyendo el de esa posicion, se mueven a la derecha
print("\t", lista)
# Pero si se agrega en la ultima posicion sin incluirsa, es decir, mayore que la lista, no se mueve nada

lista = [1, 2, 3]
print(f"Lista original antes de usar el metodo insert(30, 4): \n\t {lista}")
lista.insert(30, 4)
print("\t", lista)

# El metodo pop() elimina el ultimo elemento de la lista y lo devuelve

lista = [1, 2, 3]
print(f"Lista original antes de usar el metodo pop(): \n\t {lista}")
elemento = lista.pop()
print("\t", lista)
print("\t", elemento)

lista = [1, 2, 3]
print(f"Lista original antes de usar el metodo pop(0): \n\t {lista}")
elemento = lista.pop(0)
print("\t", lista)
print("\t", elemento)

# El metodo remove() elimina el primer elemento que coincida con el parametro

lista = [1, 2, 3, 4, 5, 6]
print(f"Lista original antes de usar el metodo remove(3): \n\t {lista}")
elemento = lista.remove(3)
print("\t", lista)
# Pero debemos tener en cuenta que el metodo remove salta error si no existe el elemento

lista = [1, 2, 3, 4, 5, 6]
print(f"Lista original antes de usar el metodo remove(70): \n\t {lista}")
try:
    lista.remove(70)
except ValueError:
    print("\t No existe el elemento")
print("\t", lista)

# El metodo reverse() invierte la lista

lista = [1, 2, 3, 4, 5, 6]
print(f"Lista original antes de usar el metodo reverse(): \n\t {lista}")
lista.reverse()
print("\t", lista)

# El metodo sort() ordena la lista

lista = [4, 3, 5, 1, 6, 2]
print(f"Lista original antes de usar el metodo sort(): \n\t {lista}")
lista.sort()
print("\t", lista)
lista.sort(reverse=True)
print(f"Lista con sort(reverse=True): \n\t {lista}")

# El metodo index() devuelve el indice del primer elemento que coincida con el parametro
# Lo devuelve. Es decir, si hay mas de un elemento que coincida, devuelve el indice del primer elemento

lista = [1, 2, 3, 4, 5, 6, 3]
print(f"Lista original antes de usar el metodo index(): \n\t {lista}")
print("\t", lista.index(3))
print("\t", lista.index(6))
# Si no lo encuentra, salta error
try:
    print(f"\t", lista.index(70))
except ValueError:
    print("\t No existe el elemento")
# Tambien podemos indicar desde donde buscar el elemento
print("\t", lista.index(3, 1))
print("\t", lista.index(3, 3))

# El metodo count() devuelve el numero de veces que aparece el elemento

lista = [1, 2, 3, 4, 5, 6, 3]
print(f"Lista original antes de usar el metodo count(): \n\t {lista}")
print("\t", lista.count(3))
print("\t", lista.count(6))
print("\t", lista.count(70))

# El metodo copy() devuelve una copia de la lista

lista = [1, 2, 3, 4, 5, 6, 3]
print(f"Lista original antes de usar el metodo copy(): \n\t {lista}")
lista_copy = lista.copy()
print("\t", lista_copy)
print("\t", lista_copy == lista)

# El metodo clear() borra toda la lista

lista = [1, 2, 3, 4, 5, 6, 3]
print(f"Lista original antes de usar el metodo clear(): \n\t {lista}")
lista.clear()
print("\t", lista)


# Por otro lado, ademas podemos hacer otras operaciones con listas

# Borrar con del

lista = list(range(10))
print(f"Lista original antes de usar del: \n\t {lista}")
del lista[0]
print("\t", lista)
del lista[0:3]
print("\t", lista)

# Realizar multiples asignaciones

lista = list(range(3))
print(f"Lista original antes de usar multiples asignaciones: \n\t {lista}")
x, y, z = lista
print("\t", x)
print("\t", y)
print("\t", z)

# Intercambiar posiciones

lista = list(range(3))
print(f"Lista original antes de intercambiar posiciones: \n\t {lista}")
lista[0], lista[2] = lista[2], lista[0]
print("\t", lista)

# Iterar sobre una lista

# forma 1

lista = list(range(3))
print(f"Lista original antes de iterar sobre una lista: \n\t {lista}")
for elemento in lista:
    print("\t", elemento)

# forma 2

lista = list(range(3))
print(f"Lista original antes de iterar sobre una lista: \n\t {lista}")
for index, l in enumerate(lista):
    print("\t", index, l)

# forma 3
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
print(f"Lista original antes de iterar sobre una lista: \n\t {lista_1}")
print(f"\t {lista_2}")
for lst1, lst2 in zip(lista_1, lista_2):
    print("\t", lst1, lst2)
