"""
https://www.youtube.com/watch?v=1zpcE7W2AdQ

El metodo copy() crea una copia del diccionario, lista, tupla, etc.
Es muy util ya que podemos modificar la copia y no afectar al original.

la sintaxis es:
    diccionario.copy()

ejemplo:
    diccionario = {
        "a": 1,
        "b": 2
        "c": 3
    }
    diccionario_copy = diccionario.copy()
"""

vocales_diccionario = {"a": 1, "b": 2, "c": 3}
vocales_diccionario_copy = vocales_diccionario.copy()

print("Mi diccionario inicial:", vocales_diccionario)
print("Mi diccionario copy:", vocales_diccionario_copy)
vocales_diccionario_copy["a"] = 4
print("Mi diccionario copy despues de modificar:", vocales_diccionario_copy)
print("Mi diccionario original:", vocales_diccionario)
