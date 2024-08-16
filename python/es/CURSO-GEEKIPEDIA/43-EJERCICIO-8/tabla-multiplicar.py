"""
https://www.youtube.com/watch?v=wqBthGFbwfg

Desarrolla un programa que muestre la tabla de multiplicar de un numero introducido
por el usuario.

Requisitos:
    - Usar el bucle for
    - Las tablas deben ser del 1 al 10

"""

print("".center(100,'-'))
print("TABLA DE MULTIPLICAR".center(100))
print("".center(100,'-'))

numero = int(input("\nIntroduce un numero: "))
for iterative_number in range(1, 11):
    print(f"{numero} x {iterative_number} = {numero * iterative_number}")

print("".center(100,'-'))