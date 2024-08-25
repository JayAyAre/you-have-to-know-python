"""
https://www.youtube.com/watch?v=3xM9Dk_Ro6g


Setdefault es un metodo de los diccionarios, se utiliza para asignar
un valor a una clave en un diccionario, si la clave no existe ya en el diccionario.

si la clave ya existe en el diccionario, el metodo de vuelve el valor correspondiente
a esa clave.

sintaxis:
    diccionario.setdefault(clave)
    diccionario.setdefault(clave, valor) # Lo ideal es trabajar con ambos argumentos
"""

dict_name = {"a": 1, "b": 2, "c": 3}
print(f"Mi diccionario: {dict_name}")

valor = dict_name.setdefault("a", 4)
print(f"El valor en 'a' es: {valor}")

valor = dict_name.setdefault("d", 4)
print(f"El valor en 'd' es: {valor}")

valor = dict_name.setdefault("e")
print(f"El valor en 'e' es: {valor}")
print(f"El diccionario: {dict_name}")
