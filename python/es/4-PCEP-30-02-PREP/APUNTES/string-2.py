# Los strings tienen diferentes comportamientos como estos:

name = "Pepino" "4U"
print(name)

# Se pueden declarar de estas formas
name = "Pepino"
print(name)
name = """Pepino"""
print(name)
name = 'Pepino'
print(name)

# No tienen limite, su limite es la memoria disponible

# Secuencia de escape

name = "Pepino\'s\'"
print(name)

name = "\110"
print(name)

# Formato de strings

# podemos concatenar strings con el operador +

print("Hola" + " mundo")
print("Hola" + " " + "mundo")

# Podemos usar el operador % para formatear strings

age = 5
name = "El numero es: %d" % age
print(name)

s = "Los números son %d y %d." % (5, 10)
print(s)

# O format

s = "Los números son {} y {}".format(5, 10)
print(s)  # Los números son {} y {}".format(5, 10)

# y fstrings

s = f"Los números son {5} y {10}."
print(s)

# Ejemplos

# Ejemplo 1

s1 = "Parte 1"
s2 = "Parte 2"
print(s1 + " " + s2)  # Parte 1 Parte 2

# Ejemplo 2

s = "Hola "
print(s*3)  # Hola Hola Hola

# Ejemplo 3

print("mola" in "Python mola")  # True

# Ejemplo 4

print(chr(8364))  # €
print(ord("€"))  # 110

# Ejemplo 5

print(len("Esta es mi cadena"))

# Ejemplo 6

x = str(10.4)
print(x)  # 10.4
print(type(x))  # <class 'str'>

# Ejemplo 7

x = "abcde"
print(x[0:5:2])  # ace
