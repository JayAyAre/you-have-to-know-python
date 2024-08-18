print("".center(100, "-"))
print("SUMA DE MATRICES".center(100))
print("".center(100, "-"))

num_matrices = int(input("Introduce la cantidad de matrices a sumar: "))

if num_matrices < 2:
    print("Debe sumar al menos 2 matrices")
    exit()

num_filas = int(input("Introduce la cantidad de filas  matriz: "))
num_columnas = int(input("Introduce la cantidad de columnas de la primera matriz: "))

if num_filas != num_columnas:
    print("Las matrices deben ser de la misma dimensión")
    exit()

resultado = []

# Llenado de matrices
matrices = []
for matriz_actual in range(num_matrices):
    matriz = []
    for fila_actual in range(num_filas):
        fila = []
        for columna_actual in range(num_columnas):
            elemento = int(
                input(
                    f"Matriz {matriz_actual + 1}, [{fila_actual}] [{columna_actual}]: "
                )
            )
            fila.append(elemento)
        matriz.append(fila)
    matrices.insert(matriz_actual, matriz)

# Suma de matrices

for row in range(num_filas):
    suma_fila = []
    for column in range(num_columnas):
        suma = 0
        for matriz in range(num_matrices):
            suma += matrices[matriz][row][column]
        suma_fila.append(suma)
    resultado.append(suma_fila)
# Impresion de resultados

print("La suma de las matrices es:")

for fila in range(num_filas):
    if fila != 1:
        for matriz in range(num_matrices):
            print(f"{matrices[matriz][fila]}", end="   ")
        print(f"   {resultado[fila]}")
    else:
        for matriz in range(num_matrices):
            print(f"{matrices[matriz][fila]}", end=" + ")
        print(f" = {resultado[fila]}")
