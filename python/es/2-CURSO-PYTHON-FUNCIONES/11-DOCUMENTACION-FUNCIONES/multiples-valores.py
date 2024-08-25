"""
La documentacion de una funcion se escribe en la parte de arriba de la funcion.
y se llama docstring.

Generamos primero 3 comillas dobles y escribimos siempre al inicio de la funcion.

"""

def operaciones_basicas(a, b):
    """
    Realiza operaciones basicas con los valores de a y b.
    entre ellas suma, resta, multiplicacion y division.

    Args:
        a (int or float): (int o float) Primer valor
        b (int or float): (int o float) Segundo valor

    Returns:
        tupla: Una tupla con los resultados de las operaciones.
                - Suma (int o float): Suma de a y b
                - Resta (int o float): Resta de a y b
                - Multiplicacion (int o float): Multiplicacion de a y b
                - Division (float): Cociente de a dividido por b (si b no es 0)
    """

    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division # Devuelve los resultados en forma de tupla

resultados = operaciones_basicas(2, 3)
print(resultados)

def operaciones_basicas2(a, b):
    """
    Realiza operaciones basicas con los valores de a y b.
    entre ellas suma, resta, multiplicacion y division.

    :param a: (int o float) Primer valor
    :param b: (int o float) Segundo valor
    :return: Una tupla con los resultados de las operaciones.
                - Suma (int o float): Suma de a y b
                - Resta (int o float): Resta de a y b
                - Multiplicacion (int o float): Multiplicacion de a y b
                - Division (float): Cociente de a dividido por b (si b no es 0)
    """

    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division # Devuelve los resultados en forma de tupla

resultados = operaciones_basicas2(2, 3)
print(resultados)

# help(operaciones_basicas)
# help(operaciones_basicas.__doc__)