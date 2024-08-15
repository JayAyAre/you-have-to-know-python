"""
https://www.youtube.com/watch?v=SlIPMihC6KE

Cabe destacar que este serie nuestro primer algoritmo matematico

Se nos solicita un programa que imprima la sucesion de fibonacci
desde el numero 0 hasta el 1597, de manera horizontal.

asi:
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

Requisitos:
    - Maximo 7 lineas de codigo
    - Imprimir de manera horizontal
"""

print("Fibonacci Sequence")
x = 0
y = 1
while x <= 1597:
    print(x, y, end=" ")
    x += y
    y += x

# Otra forma de hacerlo:
print("\nFibonacci Sequence")
x, y = 0 , 1
while x <= 1597:
    print(x, end=" ")
    x, y = y, x + y
    """
        La siguiente linea es una sentencia de asignacion
        que asigna el valor de y a x y luego suma el valor de x y 'y'
        y asigna el resultado a y. Pero no lo hace una linea y luego otra.
        Lo que sucede una asignación simultánea, lo que significa que los
        valores del lado derecho se calculan utilizando los valores iniciales de x e y

        Es decir:
            x = 0
            y = 1

            luego hace teniendo en cuenta que x = 0 y y = 1.
            x = y (1)
            y = x + y (0 + 1) no reemplazamos los valores iniciales de x y y
    """
