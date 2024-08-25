"""
https://www.youtube.com/watch?v=62UvizLLcNU

Lsa tuplas son estructuras de datos simlilares a las listas, se utiizan para
almacenar colecciones de datos de forma ordenada. y a su vez, los datos pueden estar o no
relacionados entre si.

una tupla puede ser homogenea o heterogena.
    - una tupla homogenea es una tupla que contiene solo datos de un tipo. estan relacionados
    entre si.
    - una tupla heterogena es una tupla que contiene datos de diferentes tipos. no estan
    relacionados entre si.

Son inmutables, es decir, no se pueden modificar una tupla.

sintaxis:
    tupla = ()

si queremos asignar elementos a una tupla, debemos usar la sintaxis:
    tupla = (elemento1, elemento2, ...)
    no podemos crear una tupla con un solo elemento.
    para ello, debemos usar la sintaxis:
    tupla = (elemento,)

ademas, podemos crear una tupla asi:
    tupla = elemento1, elemento2, ...

"""

tupla_vacia = ()

print(f"Una tupla vacia es:\n\t{tupla_vacia}")
print("El tipo de la tupla es: ", type(tupla_vacia))
tupla_sin_parentesis = 3, 2
print(f"Una tupla sin parentesis es:\n\t{tupla_sin_parentesis}")

tupla_heterogena = 3, "Hola", 2.5, True
print(f"Una tupla heterogena es:\n\t{tupla_heterogena}")

tupla_homogenea = (3, 3, 4, 5)
print(f"Una tupla homogenea es:\n\t{tupla_homogenea}")

tupla_con_lista = 3, [1, 2, 3, 4, 5]
print(f"Una tupla con lista es:\n\t{tupla_con_lista}")

"""
Recordemos que python no me deja cambiar una tupla, sin embargo
python me permite cambiar el contenido de dicha estructura dentro de la tupla.

es decir, si tengo una lista en una tupla asi
    tupla = ([1, 2, 3, 4, 5], 6)

    Podemos cambiar los valores de la lista en la tupla, pero
    no podemos cambiar la lista, por un diccionario, o un boleano.

"""
tupla_vacia = ()
print(f"Tupla vacia: {tupla_vacia}")
print(f"El tipo de dato de esta tupla es: {type(tupla_vacia)} \n")

tupla_homogenea = (3, 2)
print(f"Tupla homogénea: {tupla_homogenea}")
print(f"El tipo de dato de esta tupla es: {type(tupla_homogenea)} \n")

tupla_heterogenea = (3, True, "Hola", 2.5)
print(f"Tupla heterogénea: {tupla_heterogenea}")
print(f"El tipo de dato de esta tupla es: {type(tupla_heterogenea)} \n")

tupla_heterogenea2 = ([1, 2, 3], {"uno": 1, "dos": 2}, (3, 2))
print(f"Tupla heterogénea: {tupla_heterogenea2}")
print(f"El tipo de dato de esta tupla es: {type(tupla_heterogenea2)} \n")

tupla_de_un_elemento = (3,)
print(f"Tupla de un elemento: {tupla_de_un_elemento}")
print(f"El tipo de dato de esta tupla es: {type(tupla_de_un_elemento)} \n")

tupla_sin_parentesis = 3, True, "Hola", 2.5
print(f"Tupla sin paréntesis: {tupla_sin_parentesis}")
print(f"El tipo de dato de esta tupla es: {type(tupla_sin_parentesis)} \n")
