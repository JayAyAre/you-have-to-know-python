"""
https://www.youtube.com/watch?v=KIrcdiQKxYw

Desarrollar una calculadora con las siguientes operaciones:
    -> Suma
    -> Resta
    -> Multiplicación
    -> División
    -> División entera
    -> Exponente
    -> Modulo o resto
Requisitos:
    - Debe funcionar con una unica variable
    - Debe pedir dos numeros
"""
print("=================")
print("Calculadora")
print("=================\n")

print("Opciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo")
print("8. Salir\n")

number = int(input("Introduce la opción deseada: "))

if number == 8:
    print("Saliendo del programa")
    exit()

RESULT_MESSAGE = "El resultado es: "
REQUEST_FIRST_NUMBER = "Introduce el primer numero: "
REQUEST_SECOND_NUMBER = "Introduce el segundo numero: "

if number >= 1 and number < 8:
    if number == 1:
        number = float(input(REQUEST_FIRST_NUMBER))
        number += float(input(REQUEST_SECOND_NUMBER))
    elif number == 2:
        number =  float(input(REQUEST_FIRST_NUMBER))
        number -= float(input(REQUEST_SECOND_NUMBER))
    elif number == 3:
        number =  float(input(REQUEST_FIRST_NUMBER))
        number *= float(input(REQUEST_SECOND_NUMBER))
    elif number == 4:
        number = float(input(REQUEST_FIRST_NUMBER))
        number /= float(input(REQUEST_SECOND_NUMBER))
    elif number == 5:
        number = float(input(REQUEST_FIRST_NUMBER))
        number //= float(input(REQUEST_SECOND_NUMBER))
    elif number == 6:
        number = float(input(REQUEST_FIRST_NUMBER))
        number %= float(input(REQUEST_SECOND_NUMBER))
    elif number == 7:
        number = float(input(REQUEST_FIRST_NUMBER))
        number **= float(input(REQUEST_SECOND_NUMBER))
else:
    print("Opción no disponible")

print(RESULT_MESSAGE, round(number, 2))



