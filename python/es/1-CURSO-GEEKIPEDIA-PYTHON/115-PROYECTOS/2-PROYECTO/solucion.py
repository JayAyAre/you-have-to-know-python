import random

print("".center(80,"-"))
print("Piensa un numero secreto".center(80, '-'))
print("".center(80, "-"), "\n")

print("Piensa en un numero aleatorio entre 1 y 100, tratare de adivinarlo!!")

num_min = 1
num_max = 100
num_secret = random.randint(num_min, num_max)
answers = ["menor", "mayor", "correcto"]
answer = ''
num_tries = 0
while answer != "correcto":
    num_tries += 1
    while True:
        try:
            print(f"Tu numero es {num_secret}?")
            print("Ingresa 'mayor', 'menor' o 'correcto'")
            answer = input("\n").lower()
            print()
            if answer not in answers:
                print("Ingresa un valor correcto")
        except ValueError:
            print("El numero debe ser un número entero")
        else:
            break
    if answer == 'menor':
        num_max = num_secret - 1
    elif answer == 'mayor':
        num_min = num_secret + 1
    elif answer == 'correcto':
        print(f"Tu numero es {num_secret}, lo adivine en {num_tries} intentos")
        break
    num_secret = random.randint(num_min, num_max)