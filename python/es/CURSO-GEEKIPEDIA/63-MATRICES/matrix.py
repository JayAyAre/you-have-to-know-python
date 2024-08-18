"""
https://www.youtube.com/watch?v=pgqMaCQnWNc

Las matrices son una forma de almacenar datos bidimensional, cuyos
elementos se almacenan en filas y columnas.

es bidimensional porque tiene un ancho y un largo.
ancho: numero de filas
largo: numero de columnas

Para crear matrices, una manera comun es usar listas anidadas
con lo cual podemos crear matrices de cualquier tamaño.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

una matriz puede tener n cantidad de filas y m cantidad de columnas.

una representacion de una matriz 3x3 (nxm) es:

    1 2 3
    4 5 6
    7 8 9

Para acceder a los elementos de una matriz, tenemos en cuenta que las filas y columnas empiezan en 0.
un ejemplo es:

Mostrar el valor 5

matriz[1][1] = 5

Mostrar el valor 3

matriz[0][2] = 3
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Mi matriz es:", matrix)

print("Otra forma de mostrarla")
print(f"\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}")

print("Numero 8:", matrix[2][1])
print("Numero 1:", matrix[0][0])
print("Numero 4:", matrix[1][0])
print("Numero 3:", matrix[0][2])
