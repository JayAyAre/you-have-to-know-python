"""
https://www.youtube.com/watch?v=VwvhR1e-xkE

La intruccion import permite incorportar modulos y bibliotecas en nuestro codigo.
permitiendo reutilizacion y organizacion de codigo.

Esto posibilita aprovechar las numerosas funcionalidades que python ofrece.
ampliando las capacidades del programa de manera modular.

Un modulo es simplemente un archivo que contiene definiciones
como funciones, clases, constantes, variables, etc.

por otro lado, una biblioteca es un conjunto de modulos
organizados de manera especifica para abordar un proposito en particular.

python cuenta con una gran cantidad de modulos y bibliotecas.

entre ellas:
    Tiempo y fechas:
        - datetime: Funciones para manipular fechas y horas.
        - time: Funciones para manipular tiempo y reloj.
    Proceso de text:
        - re: Expresiones regulares.
        - string: Funciones para manipular cadenas de texto.
    Manejo de datos:
        - pandas: Estructura de datos y análisis de datos.
        - json: Funciones para manipular datos en formato json.
    Matematicas y ciencias:
        - math: Funciones matemáticas.
        - numpy: operaciones numericas avanzadas.
    Python nos provee muchas mas secciones

Nos centraremos en math: https://docs.python.org/3/library/math.html
"""

# importar un modulo completo
# Por convencion, al incio deben estar todos los imports

import math

sqrt = math.sqrt(9)
print(f"sqrt(9) = {sqrt}")

sen = math.sin(math.pi/2)
print(f"sen(pi/2) = {sen}")

# importar con un alias

print("\n")

import math as hola

print(f"sqrt(9) = {hola.sqrt(9)}")

# Importar solo lo necesario de un modulo

from math import sqrt, pi
print(f"sqrt(9) = {sqrt(9)}")
print(f"pi = {pi}")

# Importar todo de un modulo (Evitar)

from math import * # Se cargan todas las funciones

print(f"sqrt(9) = {sqrt(9)}")
print(f"pi = {pi}")
print(f"tan(pi/2) = {tan(pi/2)}")