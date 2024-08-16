"""

https://youtu.be/35kWoAtgzic?si=LLujjJlUF78_fvZy

Cuando necesitamos comparar mas de dos condiciones logicas dentro de una misma condicion
nos vemos con la necesidad de utilizar operadores lógicos.

estos operadores nos permiten principalmente revisar mas de 2 condiciones en una expresion

los operadores lógicos son:
    Conjuncion => and
    Disyuncion => or
    Negacion => not

"""

num_uno = 7
num_dos = 5

# Ambas condiciones deben ser verdaderas para que se ejecute el bloque de codigo
if num_uno == 5 and num_dos >= 5:
    print("Ambas condiciones son verdaderas")
else:
    print("Alguna condicion o ninguna es verdadera")

# Alguna condicion se debe cumplir
if num_uno == 5 or num_dos >= 5:
    print("Una o ambas condiciones son verdaderas")
else:
    print("Ninguna condicion es verdadera")

# Alguna condicion no se debe cumplir
if not num_dos > 5:
    print("La condicion se cumple cuando es menor o igual a 5")
else:
    print("La condicion se cumple")


# Ejercicio:

# Conjuncion (and)
print("\nConjuncion (and):\n")

num_uno = int(input("Escribe un numero mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("El numero ", num_uno, " cumple con la condicion")
else:
    print("El numero ", num_uno, " NO cumple con la condicion")

# Disyuncion (or)
print("Disyuncion (or):\n")

palabra = input("Escribe la palabra 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print(f"La palabra {palabra} es 'si' o 'yes'")
else:
    print(f"La palabra {palabra} NO es 'si' o 'yes'")

# Negacion (not)
print("Negacion (not):\n")

num_uno = int(input("Introduce un numero igual a 5: "))

if not num_uno == 5:
    print(f"El numero {num_uno} NO es igual a 5")
else:
    print(f"El numero {num_uno} es igual a 5")
print("\nFin.\n")