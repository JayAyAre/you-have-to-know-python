"""
https://www.youtube.com/watch?v=yGABt1CS2IQ

Las expresiones de comprension son una construccion de python que permite
crear una nueva secuencia como listas, tuplas, diccionarios, etc.

aplicando una operacion o expresion a cada elemento de un conjunto.
Ademas permiten filtrar elementos en base a una condicion.

Son una forma concisa de realizar operaciones en conjuntos de forma
legible y concisa.

Lista de comprensions:
    Crea una nueva lista aplicando una expresion a cada elemento de un iterable y,
    opcionalmente, filtra elementos con una condicion.

Conjunto de comprensions:
    Crea un conjunto en lugar de una lista, garantizando que los elementos son
    unicos y no repetidos. filtra elementos con una condicion.

Diccionario de comprensions:
    Crea un nuevo diccionario aplicando una expresion a cada elemento de un iterable
    para determinar tanto las claves como los valores. filtra elementos con una condicion.

La sintaxis es:
    lista = [Expresion for elemento in iterable]

Si queremos realizar un filtro, podemos hacerlo asi:
    lista = [Expresion for elemento in iterable if condicion]

La sintaxis es igual que un bucle for, pero a diferencia añadimos una expresion antes.
"""

# Para ejemplificar la expresion, haremmos una lista con numeros del 0 al 9 elevados al cuadrado

print("Generaremos la lista a continuacion")
print("El primer metodo sera sin metodos de compresion")

lista = []
for number in range(10):
    lista.append(number**2)

print("Lista sin compresion:")
print(lista)
print()

lista = []
print("El segundo metodo sera con compresion")
lista = [number**2 for number in range(10)]
print("Lista con compresion:")
print(lista)

# Si queremos hacer lo mismo, pero unicamente con numeros pares

print("Lista de cuadrados de numeros pares")
lista = [number**2 for number in range(10) if number % 2 == 0]
print("Lista con compresion:")
print(lista)

# Creamos un diccionario con expresiones de compresion

print("Creamos un diccionario con expresiones de compresion")

personas = [("Eduardo", 26), ("Maria", 30), ("Gerardo", 20), ("Valentina", 25)]

personas_dict = {}
for name, age, in personas:
    personas_dict[name] = age

print("Diccionario sin compresion:")
print(personas_dict)

print("Diccionario con compresion:") # Si es un diccionario, pondremos clave:valor
dict_compresion = {name: age for name, age in personas}


# Crear una tupla con los cuadrados de los números del 1 al 5
cuadrados = (x**2 for x in range(1, 6))
print(cuadrados)  # Output: <generator object <genexpr> at 0x00000203D5C2C580>

# Iterando sobre el generador
for cuadrado in cuadrados:
    print(cuadrado)

# Convirtiendo a lista
lista_cuadrados = list(cuadrados)
print(lista_cuadrados)  # Output: [1, 4, 9, 16, 25]