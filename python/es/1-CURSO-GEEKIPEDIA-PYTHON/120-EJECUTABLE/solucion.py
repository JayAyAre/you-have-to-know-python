import random

print("".center(80,"-"))
print("Adivida el numero secreto".center(80, '-'))
print("".center(80, "-"), "\n")

print("A continuacion se ha elegido un numero aleatorio entre 1 y 100")
print("Tu objetivo es adivinarlo antes del numero indicado de intentos")

REQUEST_NUMBER = "Ingrese el numero de intentos: "
while True:
    try:
        num_tries = int(input(REQUEST_NUMBER))
        if num_tries <= 0:
            print("El número de intentos debe ser mayor que cero.")
        else:
            break
    except ValueError:
        print("El número de intentos debe ser un número entero.")


num_secret = random.randint(1, 100)
print()

for num_try in range(num_tries):
    print(f"Intento {num_try + 1}/{num_tries}")
    while True:
        try:
            num_guess = int(input("Ingrese el numero que cree que es:\t"))
            if num_guess <= 0:
                print("Ingrese un numero mayor que cero.")
            else:
                break
        except ValueError:
            print("El numero debe ser un número entero.")
    if num_secret > num_guess:
        print("El numero es mayor")
    elif num_secret < num_guess:
        print("El numero es menor")
    else:
        print("HAS ADIVINADO, EL NUMERO ES", num_secret)
        break
    print()
else:
    print("No has adivinado el numero, el numero secreto era", num_secret)