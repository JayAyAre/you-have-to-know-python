def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division # Devuelve los resultados en forma de tupla

resultados = operaciones_basicas(2, 3)
print(resultados)