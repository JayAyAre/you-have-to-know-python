def cuadrado(x):
    return x * x

def cubo(x):
    return cuadrado(x) * x

def aplicar_funcion_a_lsita(funcion, lista):
    resultado = []
    for number in lista:
        resultado.append(funcion(number))
    return resultado

print(aplicar_funcion_a_lsita(cubo, [1, 2, 3, 4, 5]))
