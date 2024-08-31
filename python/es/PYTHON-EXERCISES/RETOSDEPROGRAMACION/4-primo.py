"""
FACIL

Escribe un numero que se encargue de comprobar si un número es primo
o no, y que imprima los números primos entre 0 y 100.
"""

def is_primo(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

for number in range(0, 101):
    if is_primo(number):
        print(number)