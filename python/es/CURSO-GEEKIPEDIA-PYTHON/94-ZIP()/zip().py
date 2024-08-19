"""
https://www.youtube.com/watch?v=-MgjgEKle4M

zip() es una funcion que permite combinar elementos de varias secuencias en una tupla.

crea un iterador que produce tuplas donde el primer elemento
en cada una de las secuencias dadas se empareja, luego el segundo elemento
en cada una de las secuencias dadas se empareja, y así sucesivamente.

Si tienen longitudes diferentes, el zip() devuelve una tupla de longitud más corta.

zip devuelve un iterador, se debera transformar a una estructura de datos

sintaxis:
    zip(iterable_1, iterable_2, ...)
    El unico requisito es que deben ser iterables.
"""

names = ["John", "Mary", "Peter", "Paul", "George", "Ringo", "hola"]
ages = [25, 27, 29, 31, 33, 35]

combination = list(
    zip(names, ages)
)  # Solo estara hasta Ringo, ya que el zip coje el iterador mas corto
print(combination)

for name, age in combination:
    print(f"Name: {name}, Age: {age}")

for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")
