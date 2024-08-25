def cuadrado(x):
    return x * x

def cubo(x):
    return cuadrado(x) * x

# Funcion de orden superior porque toma otra funcion como parametro y devuelve otra funcion
def aplicar(funcion, x):
    return funcion(x)

resultado = aplicar(cuadrado, 5)
print(resultado)
resultado = aplicar(cubo, 5)
print(resultado)