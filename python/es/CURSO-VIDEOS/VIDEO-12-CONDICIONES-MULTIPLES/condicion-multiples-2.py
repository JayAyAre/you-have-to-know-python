print("=================================")
print("Convertidor de numeros a letras!!")
print("================================= ")

numero_entrada = int(input("Cual es el numero que deseas convertir a letras? "))

if numero_entrada == 0:
    print("El numero en letras es: Zero")
elif numero_entrada == 1:
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
    print("El programa unicamente admite numeros entre 0 y 5")

print("Fin.")