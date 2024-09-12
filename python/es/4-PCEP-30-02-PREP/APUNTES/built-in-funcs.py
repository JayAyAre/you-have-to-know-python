"""
    Como sabemos, python nos proporciona muchas funciones por defecto, que son
        las que se encuentran en el modulo builtins.

    Estas funciones son:
        - input(). Para recibir datos del usuario.
        - print(). Para mostrar datos en la consola.
        - len(). Para obtener la longitud de secuencias (cadenas, listas, etc.).
        - type(). Para verificar el tipo de un objeto.
        - int(), float(), str(). Para convertir entre tipos de datos básicos.
        - range(). Para generar una secuencia de números.
        - list(), tuple(), set(), dict(). Para crear colecciones.
        - min(), max(). Para encontrar el valor mínimo o máximo en una secuencia.
        - sum(). Para sumar los elementos de una secuencia.
        - sorted(). Para ordenar elementos en una secuencia.
        - abs(). Para obtener el valor absoluto de un número.
        - round(). Para redondear un número a un número determinado de decimales.
        - isinstance(). Para verificar si un objeto es de un tipo específico.
        - id(). Para obtener el identificador único de un objeto.
        - ord(), chr(). Para convertir entre caracteres y sus valores Unicode.
        - bool(). Para convertir a valores booleanos (True o False).
"""

# Metodo print(), Permite mostrar datos en la consola

print("\nUsando la funcion print")
print("\t", "Hola mundo")

# Ademas admite varios argumentos

print("\nUsando la funcion print")
print("\t", "Hola mundo", 1, 2, 3)

# Tiene un argumento llamando sep y end

print("\nUsando la funcion print")
# Por defecto, el separador es un espacio
print("\t", "Hola", "mundo", sep="-")
# Por defecto, el end es una nueva linea \n
print("\t", "Hola", "mundo", end="-")

# Metodo input(), Permite recibir datos del usuario por la consola

print("\nUsando la funcion input")
# Permite un input de texto para enseñar por consola
nombre = input("Ingrese su nombre: ")
print("\t", nombre)

# Metodo len(), Permite obtener la longitud de secuencias

lista = [1, 2, 3, 4, 5]
print("\nUsando la funcion len en: ", lista)
print("\t", len(lista))

# Metodo type(), Permite obtener el tipo de un objeto

print("\nUsando la funcion type")
lista = [1, 2, 3, 4, 5]
print("\t", type(lista))
print("\t", type(1))
print("\t", type(1.0))
print("\t", type("Hola"))
print("\t", type(True))

# Metodo int(), Permite convertir a enteros

print("\nUsando la funcion int")
numero = int(5.999)
print("\t", numero)


# Metodo float(), Permite convertir a flotantes

print("\nUsando la funcion float")
numero = float(5)
print("\t", numero)

# Metodo str(), Permite convertir a cadenas

print("\nUsando la funcion str")
numero = str(5)
print("\t", numero)

# Metodo bool(), Permite convertir a valores booleanos (True o False)

print("\nUsando la funcion bool")
numero = bool(5)
print("\t", numero)
numero = bool(0)
print("\t", numero)

# Metodo range(), Permite generar una secuencia de números

print("\nUsando la funcion range")
numero = range(5)
print("\t", numero)
numero = range(5, 10)
print("\t", numero)
numero = range(5, 10, 2)
print("\t", numero)

# Metodo list(), Permite crear listas en funcion de un iterable

print("\nUsando la funcion list")
numero = list(range(5))
print("\t", numero)
numero = list(range(5, 10))
print("\t", numero)
numero = list(range(5, 10, 2))
print("\t", numero)

# Metodo tuple(), Permite crear tuplas en funcion de un iterable

print("\nUsando la funcion tuple")
numero = tuple(range(5))
print("\t", numero)
numero = tuple(range(5, 10))
print("\t", numero)
numero = tuple(range(5, 10, 2))
print("\t", numero)

# Metodo set(), Permite crear conjuntos en funcion de un iterable

print("\nUsando la funcion set")
numero = set(range(5))
print("\t", numero)
numero = set(range(5, 10))
print("\t", numero)
numero = set(range(5, 10, 2))
print("\t", numero)

# Metodo dict(), Permite crear diccionarios en funcion de un iterable

print("\nUsando la funcion dict")
numero = dict([("a", 1), ("b", 2), ("c", 3)])
print("\t", numero)
numero = dict(ave=1, bird=2, coche=3)
print("\t", numero)

# Metodo min(), Permite encontrar el valor mínimo en un iterable

print("\nUsando la funcion min")
numero = min(range(5))
print("\t", numero)
numero = min(range(5, 10))
print("\t", numero)
numero = min(range(5, 10, 2))
print("\t", numero)

# Metodo max(), Permite encontrar el valor máximo en un iterable

print("\nUsando la funcion max")
numero = max(range(5))
print("\t", numero)
numero = max(range(5, 10))
print("\t", numero)
numero = max(range(5, 10, 2))
print("\t", numero)

# Metodo sum(), Permite sumar los elementos de un iterable

print("\nUsando la funcion sum")
numero = sum(range(5))
print("\t", numero)
numero = sum(range(5, 10))
print("\t", numero)

# Metodo sorted(), Permite ordenar elementos en un iterable

print("\nUsando la funcion sorted")
numero = sorted(range(5))
print("\t", numero)
numero = sorted(range(5, 10))
print("\t", numero)
numero = sorted(range(5, 10, 2))
print("\t", numero)

# Metodo abs(), Permite obtener el valor absoluto de un número

print("\nUsando la funcion abs")
numero = abs(-5)
print("\t", numero)
numero = abs(5)
print("\t", numero)

# Metodo round(), Permite redondear un número a un número determinado de decimales

print("\nUsando la funcion round")
numero = round(5.559)
print("\t", numero)
numero = round(5.559, 1)
print("\t", numero)
numero = round(5.559, 2)
print("\t", numero)

# metodo isinstance, Para verificar si un objeto es de un tipo específico.

print("\nUsando la funcion isinstance")
lista = [1, 2, 3, 4, 5]
print("\t", isinstance(lista, list))
print("\t", isinstance(lista, tuple))
print("\t", isinstance(lista, set))
print("\t", isinstance(lista, dict))
numero = 5
print("\t", isinstance(numero, int))
print("\t", isinstance(numero, float))
print("\t", isinstance(numero, str))
print("\t", isinstance(numero, bool))

# metodo id(), Para obtener el identificador único de un objeto.

print("\nUsando la funcion id")
lista = [1, 2, 3, 4, 5]
print("\t", id(lista))
numero = 5
print("\t", id(numero))

# metodo ord(), Para convertir de caracteres a unicode.

print("\nUsando la funcion ord")
numero = "a"
print("\t", ord(numero))
numero = "á"
print("\t", ord(numero))

# metodo chr(), Para convertir de unicode a caracteres.
print("\nUsando la funcion chr")
numero = 97
print("\t", chr(numero))
numero = 225
print("\t", chr(numero))

# metodo bool(), Para convertir a valores booleanos (True o False).
