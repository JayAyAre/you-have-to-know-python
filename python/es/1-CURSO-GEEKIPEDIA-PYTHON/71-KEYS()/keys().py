"""
https://www.youtube.com/watch?v=qAWQRanTD3Y

El metodo keys() devuelve una dict_key que contiene las claves del diccionario.

la sintaxis es:
    diccionario.keys()
ejemplo:
    diccionario = {
        "a": 1,
        "b": 2
        "c": 3
    }
    print(diccionario.keys())
    Esto imprimira dict_keys(['a', 'b', 'c'])
"""

diccionario = {"a": 1, "b": 2}
print(diccionario)
print(f"\nLas claves son:\n{diccionario.keys()}")

lista = list(diccionario.keys())
print("Convirtiendo las claves a lista usando el constructor list()")
print(lista)
print(f"Posición 0 de la lista keys: {lista[0]}")
print(f"Posición 1 de la lista keys: {lista[1]}")
