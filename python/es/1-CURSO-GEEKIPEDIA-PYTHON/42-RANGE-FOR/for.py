"""
https://www.youtube.com/watch?v=hvVxZdt2sSA

Usaremos range para generar secuencias de numeros inmutables e iterar sobre ellas.
con el bucle for
"""
print("Usamos range(10), el resultado es:")
numeros = range(10)
for numero in numeros:
    print(numero, end=" ")

print("\nUsamos range(10, 20), el resultado es:")
for numero in range(10, 20):
    print(numero, end=" ")

print("\nUsamos range(0, 11, 2), el resultado es:")
for numero in range(0, 11, 2):
    print(numero, end=" ")

print("\nUsamos range(10, 0, -1), el resultado es:")
for numero in range(10, 0, -1):
    print(numero, end=" ")