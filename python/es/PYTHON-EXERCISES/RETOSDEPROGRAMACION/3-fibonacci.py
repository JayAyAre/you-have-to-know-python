"""
DIFICIL

Escribe una funcion que imprima los primeros 50
numeros de la sucesion de fibonacci. Empezando con el 0.
    - La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...

"""

def first_50_fibonacci():
    number_1, number_2 = 0, 1
    for _ in range(50):
        print(number_1)
        number_1, number_2 = number_2, number_1 + number_2

first_50_fibonacci()