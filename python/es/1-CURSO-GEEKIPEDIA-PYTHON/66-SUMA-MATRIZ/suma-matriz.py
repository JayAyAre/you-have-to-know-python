"""
https://www.youtube.com/watch?v=cdwkj7BNnRw

Con varias matrices, podemos sumar, restar, multiplicar, dividir, etc.

Para sumar, consiste en sumar los elementos de la misma posición de las matrices.

Requisitos:
    - Las matrices deben ser de la misma dimensión (nxm)

"""

matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("La suma de las matrices es:")
matriz_3 = []

for fila in range(len(matriz_1)):
    row = []
    for columna in range(len(matriz_1[0])):
        row.append(matriz_1[fila][columna] + matriz_2[fila][columna])
    matriz_3.append(row)

for fila in range(len(matriz_1)):
    if fila != 1:
        print(f"{matriz_1[fila]}   {matriz_2[fila]}   {matriz_3[fila]}")
    else:
        print(f"{matriz_1[fila]} + {matriz_2[fila]} = {matriz_3[fila]}")
