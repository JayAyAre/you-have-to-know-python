"""
https://www.youtube.com/watch?v=raLm2cPsrA8

Al manejar matrices, es posible que queramos tener acceso a cada uno de sus elementos
ya que de esta forma podemos manipular y trabajar con la informacion condenida en ella.

Para ello nos apoyaremos en el bucle for
"""

# Asi recorremos cada fila de la matriz
print("Asi printo toda sus filas")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matrix:
    print(fila)

# Asi recorremos toda la matriz, usando un ciclo anidado

print("Asi printo toda la matriz")
for fila in matrix:
    for elemento in fila:
        print(elemento, end=" ")
    print()
