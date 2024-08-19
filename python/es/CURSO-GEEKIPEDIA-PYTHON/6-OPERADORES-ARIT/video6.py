'''
https://youtu.be/6sOEpHItJHs?si=9uwCxOL6X5dqG50S

Los operadores aritmeticos son aquellos que manipulan datos numericos.
Estos son los mas sencillos de usar, y son usados para multiplicaciones,
divisiones
, sumas, restas, division, etc

Sus operadores son:

- suma => +
- resta => -
- multiplicación => *
- exponente => **
- modulo => %
- division => /
- division entera => //

'''

# SUMA
# Consiste en la reunion de dos o mas conjuntos "sumandos" en un conjunto
"""
Su signo es el + y se coloca entre los dos

"""
print("SUMA DE 5 + 3")
numero1 = 5
numero2 = 3
total = numero1 + numero2
print("RESULTADO:", total, "\n")
# print(f"La suma es {total}")
# print("La suma es " + str(total))

# RESTA
# Consiste en la reduccion de un numero sobre otro

print("RESTA DE 5 - 3")
numero1 = 5
numero2 = 3
total = numero1 - numero2
print("RESULTADO:", total, "\n")

# MULTIPLICACIÓN
# Es la operacion que consiste en hallar el resultado de sumar un numero tantas veces
# indice otro numero

print("MULTIPLICACION DE 5 Y 3")
numero1 = 5
numero2 = 3
total = numero1 * numero2
print("RESULTADO:", total, "\n")

# POTENCIACION
# Consiste en la multiplicacion de un numero por si mismo, las veces que nos
# indique otro numero

print("EXPONENCIACION DE 2 Y 3")
base = 2
exponente = 3
total = base ** exponente # 2 * 2 * 2
print("RESULTADO:", total, "\n")

# DIVISION
# Consiste en averiguar cuantas veces hay un numero contenido en otro

print("DIVISION DE 4 Y 2")
numero1 = 4
numero2 = 2
total = numero1 / numero2
print("RESULTADO:", total, "\n") # La division nos dara un resultado float

# MODULO
# Es el valor que se obtiene cuando un numero no puede ser dividido exacto por otro

print("MODULO DE 10 Y 3")
numero1 = 10
numero2 = 3
total = numero1 % numero2
print("RESULTADO:", total, "\n") # La division nos dara un resultado float

# DIVISION ENTERA
# Consiste en obtener el valor entero de un numero, el cual resulta de una division entre dos numeros 
# reales o decimales

print("DIVISION ENTERA DE 10 Y 3")
numero1 = 10
numero2 = 3
total = numero1 // numero2
print("RESULTADO:", total, "\n") # La division nos dara un resultado float

