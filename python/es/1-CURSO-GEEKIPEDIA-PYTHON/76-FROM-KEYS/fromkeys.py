"""
https://www.youtube.com/watch?v=srRiqR3UfPY

El metodo fromkeys es una funcion de python para crear
un nuevo diccionario con claves de una secuencia dada y valores
previamente establecidos.

fromkeys se encarga de tomar una secuencia de claves y un valor predeterminado
para generar un diccionario con esas claves y el mismo valor predeterminado
en cada una de ellas.

la sintaxis es:
    diccionario = dict.fromkeys(sequence, value)
    sequence: es la secuencia de claves
    value: es el valor predeterminado

    Tambien podemos usar:
    diccionario = {}.fromkeys(sequence, value)
"""

sequence = [1, 2, 3]
diccionario = dict.fromkeys(sequence)
print(diccionario)

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
diccionario = dict.fromkeys(sequence, 0)
print(diccionario)

value = "HOLAMUNDO"
diccionario = dict.fromkeys(sequence, value)
print(diccionario)

sequence = list(range(1, 11))
value = "hello"
diccionario = dict.fromkeys(sequence, value)
print(diccionario)

sequence = "hola mundo"
value = "hello"
diccionario = {}.fromkeys(sequence, value)
print(diccionario)
