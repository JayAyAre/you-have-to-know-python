"""
https://www.youtube.com/watch?v=hwyszwX3Wnk

Podemos acceder de forma rapida a un valor en un diccionario usando [clave].

sin embargo, si no conocemos las claves, podemos acceder con el metodo items()

items se utiliza para obtener una lista de tuplas que contienen
la clave y el valor de cada elemento del diccionario.

sintaxis:
    diccionario.items()

ejemplo:
    diccionario = {
        "a": 1,
        "b": 2
        "c": 3
    }
    print(diccionario.items())
    Esto imprimira dict_items([('a', 1), ('b', 2), ('c', 3)])
"""

diccionario = {"a": 1, "b": 2}
print(diccionario.items())

lista = list(diccionario.items())
print(lista)
print(lista[0])
print(lista[1])
