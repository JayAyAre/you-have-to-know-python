"""
https://www.youtube.com/watch?v=lFOtwcw0LBs

Range permite generar secuencias de numeros inmutables.
Estas mismas se generan a partir de un rango de numeros especificado.

Generalmente se utiliza como objeto iterable para los bucles for

Ademas nos permite trabajar con un minimo de un argumento y un maximo de
tres argumentos de forma simultanea.

Sintax:
    range(stop)
    stop: Un valor entero el cual indica DESDE donde se va a generar el rango (no incluido)

    range(start, stop)
    start: Un valor entero el cual indica DESDE donde se va a generar el rango
    stop: Un valor entero el cual indica HASTA donde se va a generar el rango (no incluido)

    range(start, stop, step)
    start: Un valor entero el cual indica DESDE donde se va a generar el rango
    stop: Un valor entero el cual indica HASTA donde se va a generar el rango (no incluido)
    step: Un valor entero el cual indica el paso que se va a realizar en el rango

    si se usa por ejemplo range(10), se genera:
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
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