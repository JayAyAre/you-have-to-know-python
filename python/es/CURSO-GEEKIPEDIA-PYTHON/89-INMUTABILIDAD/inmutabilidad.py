"""
https://www.youtube.com/watch?v=7wfCq9552bE

Las tuplas son inmutables, es decir, no se pueden cambiar su valor.

es util para garantizar que ciertos datos no cambian, sean constantes.
pero cabe destacar que si contiene elementos mutables, dichos elementos se
pueden cambiar.


"""

vocales = ("a", "e", "i", "o", "u")

print(f"Vocales: {vocales}")
print("La tupla {vocales} es inmutable")

info_tupla = ([1, 2, 3], [4, 5, 6], {"a": 1, "b": 2, "c": 3}, (1, 2, 3))
print(f"info_tupla: {info_tupla}")

info_tupla[0][0] = "a"
print(f"info_tupla: {info_tupla}")

info_tupla[1][0] = "a"
print(f"info_tupla: {info_tupla}")

info_tupla[2]["a"] = "a"
print(f"info_tupla: {info_tupla}")
