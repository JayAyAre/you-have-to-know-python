"""
https://www.youtube.com/watch?v=7t-gB2XszM8

El metodo endswith nos permite saber si una cadena termina por una subcadena
en particular, ademas de que se puede indicar un rango de busqueda.

sintax:
    cadena_variable.endswith(subcadena, int, int)
"""

string = "Diana se peina sola"
empieza_con = string.endswith("D")

print(f"\nNuestra cadena: {string}")
print(f"\nTermina con 'a': {empieza_con}") # Empieza desde la posicion -1

empieza_con = string.endswith("Diana")
print(f"\nTermina con 'sola': {empieza_con}")


empieza_con = string.endswith("se", 6)
print(f"\nTermina con 'se' en el índice 6 (se peina sola): {empieza_con}")

empieza_con = string.endswith("se", 9, 14)
print(f"\nTermina con 'se' en el índice 6 hasta el índice 7 (s): {empieza_con}")

empieza_con = string.endswith("se", -4, -1)
print(f"\nTermina con 'se' en el índice -4 hasta el índice -1 (sol): {empieza_con}")