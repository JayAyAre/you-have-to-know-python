"""
https://www.youtube.com/watch?v=Mej4-fWOxds

El metodo popitem se utiliza para obtener eliminar
y obtener el ultimo elemento clave-valor agregado de un diccionario.

lo devolvera como una tupla con la clave y el valor.
el primero sera la clave y el segundo será el valor.

sintaxis:
    ultimo_elemento = diccionario.popitem()
"""

dict_name = {"uno": 1, "dos": 2, "tres": 3}

last_item = dict_name.popitem()
print(last_item)
