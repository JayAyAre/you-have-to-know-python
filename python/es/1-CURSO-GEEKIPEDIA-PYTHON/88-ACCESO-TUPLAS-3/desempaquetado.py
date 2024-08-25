"""
https://www.youtube.com/watch?v=iM41Jxlwjc8

En esta leccion, vamos a enfocarnos en el tercer metodo, el desempaquetador de tuplas.

esta alternativa nos permite asignar cada elemento de una tupla a una variable.

para asignar varias variables en una linea:
    var_1, var_2, var_3 = "hola", "como", "estas"
sintaxis:
    var_1, var_2 = tupla

"""

vocales = ("a", "e", "i", "o", "u")

var_1, var_2, var_3 = vocales[
    :3
]  # Si no asignamos exacamente 3 variables para 3 indices, saltara error

print(f"Mis vocales son: {vocales}")
print(f"Desempaquetamos: {vocales[:3]}")
print(f"Mi primer vocal es: {var_1}")
print(f"Mi segundo vocal es: {var_2}")
print(f"Mi tercer vocal es: {var_3}")
