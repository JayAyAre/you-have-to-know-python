"""
https://www.youtube.com/watch?v=e6ha5NKSeK0

Update sirve para actualizar o agregar elementos a un diccionario.
este metodo acepta como argumento un diccionario, y luego agrega o actualiza
los elementos en el diccionario original.

Al usar update para agregar elementos a un diccionario, se debe tener en cuenta precauciones:
ya que se pueden sobreescribir valores existentes y por consecuencia perder información.

sintaxis:
    dict_name.update(dictionary)

recordemos que este metodo no retorna nada.
"""

dict_name = {"a": 1, "b": 2, "c": 3}
print(f"Mi diccionario: {dict_name}")

# Intentamos agregar una clave que ya existe en el diccionario
dict_name.update({"a": 4})
print(f"El diccionario actualizado es: {dict_name} \n")

dict_name = {"a": 1, "b": 2, "c": 3}
print(f"Mi diccionario: {dict_name}")

# Intentamos agregar una clave que no existe en el diccionario sin valor
dict_name.update({"d": 4})
print(f"El diccionario actualizado es: {dict_name} \n")

dict_name = {"a": 1, "b": 2, "c": 3}
print(f"Mi diccionario: {dict_name}")
