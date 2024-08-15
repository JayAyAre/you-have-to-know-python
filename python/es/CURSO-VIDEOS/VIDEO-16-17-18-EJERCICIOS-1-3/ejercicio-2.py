"""

https://www.youtube.com/watch?v=Z3ZQN4mO7sI

El programa debe solicitar un numero e indicar si es par o impar

Requisitos:
    1. Debe mostrar una frase indicando si el numero es par o impar junto al numero

Recordemos que:
    1. Un numero par es aquel que es divisible entre 2, siendo su resto 0
    2. Un numero impar es aquel que al dividir entre 2, su resto no es 0, es 1

"""
print("===================================")
print("Programa de comprobacion de paridad")
print("===================================\n")

input_number = int(input("Introduce un numero: "))

if input_number % 2 == 0:
    print(f"El numero {input_number} es par")
else:
    print(f"El numero {input_number} es impar")
