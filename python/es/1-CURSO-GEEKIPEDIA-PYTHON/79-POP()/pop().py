"""
https://www.youtube.com/watch?v=rwg_9ApN00E

Como hemos visto en la leccion 50, el metodo pop sirve para eliminar
un elemento de una lista, tupla, diccionario, etc. y devuelve el valor del elemento eliminado.

Si lo usamos en un diccionario, su comportamiento varia en funcvion de los argumentos que le pasemos.

pop elimina el elemento de la clave proporcionado y devuelve el valor asociado a esa clave.
Si no existe la clave, devuelve KeyError o un valor por defecto que se le pase como segundo argumento.

sintaxis:
    ultimo_elemento = diccionario.pop(clave, valor_por_defecto)
"""

dict_name = {"a": 1, "b": 2, "c": 3}
print(f"Mi diccionario: {dict_name}")

last_value = dict_name.pop("a")
print(f"El ultimo valor es: {last_value}")

last_value = dict_name.pop("d", "No se ha encontrado la clave indicada")
print(f"El ultimo valor es: {last_value}")

last_value = dict_name.pop("d")
print(f"El ultimo valor es: {last_value}")
