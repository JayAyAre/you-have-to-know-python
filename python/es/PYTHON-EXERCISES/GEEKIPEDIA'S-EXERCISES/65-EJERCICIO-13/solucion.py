print("".center(100, "-"))
print("CREADOR DE MATRICES".center(100, "-"))
print("".center(100, "-"), "\n")

num_filas = int(input("Ingrese el numero de filas: "))
num_columnas = int(input("Ingrese el numero de columnas: "))

matriz = []
for filas in range(num_filas):
    fila = []
    for columnas in range(num_columnas):
        elemento = int(
            input(f"Ingrese el valor de la posicion [{filas}][{columnas}]: ")
        )
        fila.append(elemento)
    matriz.append(fila)

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
