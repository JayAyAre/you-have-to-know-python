"""
https://www.youtube.com/watch?v=ygNU_1yWfus

usaremos el modulo random para generar numeros aleatorios
o para rellenar una lista con numeros aleatorios, etc
"""
import random as r


# Randint(), devuelve un numero aleatorio en un rango especificado [a,b]

num = r.randint(1, 100)
print(f"num = random.randint(1, 10): {num}")

# random(), devuelve un numero aleatorio en el rango [0.0,1.0]
num = r.random()

print(f"num = random.random(): {num}")

# randrange(), devuelve un numero aleatorio de la secuencia generada por (start, stop, step)
num = r.randrange(1, 100, 2)
print(f"num = random.randrange(1, 10, 2): {num}")