"""
https://www.youtube.com/watch?v=GZnkdWQTOes

El metodo values() devuelve una dict_values que contiene los valores del diccionario.

la sintaxis es:
    diccionario.values()
ejemplo:
    diccionario = {
        "a": 1,
        "b": 2
        "c": 3
    }
    print(diccionario.values())
    Esto imprimira dict_values([1, 2, 3])
"""

diccionario = {"a": 1, "b": 2}
print(diccionario)
print(f"\nLos valores son:\n{diccionario.values()}")

lista = list(diccionario.values())
print("Convirtiendo los valores a lista usando el constructor list()")
print(lista)
print(f"Posición 0 de la lista values: {lista[0]}")
print(f"Posición 1 de la lista values: {lista[1]}")
