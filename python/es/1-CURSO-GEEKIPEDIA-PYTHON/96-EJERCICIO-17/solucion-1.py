print("".center(80, "="))
print("SELECIONADOR DE NOMBRES".center(80, "="))
print("".center(80, "="))

tupla = ("Ana", "Gerardo", "Maria", "Carlos", "Valentina")

print("\nLa tupla original es:{}".format(tupla))

exist_number = int(input("Ingrese un numero del 0 al 4 incluidos: "))

while exist_number < 0 or exist_number > 4:
    print(
        "El numero ingresado no es valido, por favor ingrese un numero del 0 al 4 incluidos"
    )
    exist_number = int(input("Ingrese el numero"))

print(f"\nEl nombre escogido es: {tupla[exist_number]}")
