"""
https://www.youtube.com/watch?v=7t-gB2XszM8

El metodo startswith nos permite saber si una cadena empieza por una subcadena
en particular, ademas de que se puede indicar un rango de busqueda.

sintax:
    cadena_variable.startswith(subcadena, int, int)
"""

string = "Diana se peina sola"
empieza_con = string.startswith("D")

print(f"\nNuestra cadena: {string}")
print(f"\nEmpieza con 'D': {empieza_con}")

empieza_con = string.startswith("Diana")
print(f"\nEmpieza con 'Diana': {empieza_con}")


empieza_con = string.startswith("se", 6)
print(f"\nEmpieza con 'se' en el índice 6 (se peina sola): {empieza_con}") # Ver imagen

empieza_con = string.startswith("se", 6, 7)
print(f"\nEmpieza con 'se' en el índice 6 hasta el índice 7 (s): {empieza_con}")

empieza_con = string.startswith("se", -4, -1)
print(f"\nEmpieza con 'se' en el índice -4 hasta el índice -1 (sol): {empieza_con}")