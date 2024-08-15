"""

https://www.youtube.com/watch?v=QgJkSpwVP5Q

El programa debe solicitar 3 numeros por pantalla e indicar
cual de los 3 es mayor.

Requisitos:
    1. Debe mostrar una frase indicando cual de los 3 numeros es mayor
"""
print("===================================")
print("Programa de comparacion de numeros")
print("===================================\n")

num_1 = int(input("Introduce el primer numero: "))
num_2 = int(input("Introduce el segundo numero: "))
num_3 = int(input("Introduce el tercer numero: "))

if num_1 > num_2:
    if num_1 > num_3:
        print(f"El numero {num_1} es mayor de todos los numeros")
    else:
        print(f"El numero {num_3} es mayor de todos los numeros")
else:
    if num_2 > num_3:
        print(f"El numero {num_2} es mayor de todos los numeros")
    else:
        print(f"El numero {num_3} es mayor de todos los numeros")

"""

Otra forma de hacer:

if num_1 > num_2 and num_1 > num_3:
    print(f"El numero {num_1} es mayor de todos los numeros")
else:
    if num_2 > num_3:
        print(f"El numero {num_2} es mayor de todos los numeros")
    else:
        print(f"El numero {num_3} es mayor de todos los numeros")

"""