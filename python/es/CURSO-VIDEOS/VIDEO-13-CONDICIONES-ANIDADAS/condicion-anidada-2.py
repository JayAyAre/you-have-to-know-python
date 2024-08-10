print("==============================")
print("Conversor")
print("==============================\n")

print("Presiona 1 para convertir de numero a palabra (1-5)")
print("Presiona 2 para convertir de palabra a numero (1-5)\n")

opcion = int(input("Indica tu opcion: \n"))

if opcion == 1:
    numero_entrada = int(input("Ingresa un numero :\n"))
    if numero_entrada == 1:
        print("El numero en letras es: Uno")
    elif numero_entrada == 2:
        print("El numero en letras es: Dos")
    elif numero_entrada == 3:
        print("El numero en letras es: Tres")
    elif numero_entrada == 4:
        print("El numero en letras es: Cuatro")
    elif numero_entrada == 5:
        print("El numero en letras es: Cinco")
    else:
        print("El programa unicamente admite numeros entre 1 y 5")
elif opcion == 2:

    palabra = input("Ingresa una palabra (Uno, Dos, Tres, Cuatro, Cinco)\n")

    palabra = palabra.lower() # convertimos a minusculas

    if palabra == "uno":
        print("El numero en palabra es: 1")
    elif palabra == "dos":
        print("El numero en palabra es: 2")
    elif palabra == "tres":
        print("El numero en palabra es: 3")
    elif palabra == "cuatro":
        print("El numero en palabra es: 4")
    elif palabra == "cinco":
        print("El numero en palabra es: 5")
    else:
        print("El programa unicamente admite numeros entre 1 y 5")
else:
    print("Opcion invalida")

print("Fin.")