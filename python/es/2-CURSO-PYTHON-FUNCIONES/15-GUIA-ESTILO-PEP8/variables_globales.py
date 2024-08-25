# peps.python.org/pep-0008/

# Variables globales, Evitar su uso

def calcular_promedio(notas):
    """
    Calculates the average of the given list of numbers
    """
    total = sum(notas)
    return total / len(notas)

def imprimir_resultado(nombre, promedio):
    """
    Imprime el nombre y el promedio
    """
    print(f"El promedio de {nombre} es {promedio:.2f}")

# Uso directo sin variables globales
notas_juan = [1, 2, 3, 4, 5]
notas_pedro = [6, 7, 8, 9.3424234, 10]

promedio_juan = calcular_promedio(notas_juan)
imprimir_resultado("Juan", promedio_juan)

promedio_pedro = calcular_promedio(notas_pedro)
imprimir_resultado("Pedro", promedio_pedro)