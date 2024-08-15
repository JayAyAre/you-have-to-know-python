"""
https://www.youtube.com/watch?v=2185VEgp0VY

En python, la concatenacion es la operacion de unir dos cadenas de caracteres.
y hemos visto que podemos usar '+' para juntarlos, ademas tambien se pueden juntar
con otros numeros.

'hola' + 'mundo' es 'holamundo'
'hola' + str(1) es 'hola1'

ademas sabemos separar con , dentro de un print().

Pero existen alternativas, como por ejemplo format()

Nos permite mostrar los contenidos en una variable y utilizarlos dentro de una cadena.
Cuando lo usamos, la concatenacion se puede usar de string o de numero.

"""

# Concatenacion

# Forma 1

nombre, edad = "Juan", 30
# Nombre saldra en la posicion de {} en el string
# Es importante mantener el orden de los parametros
print("Hola {} tienes {} años".format(nombre, edad))

# Forma 2

print("Hola {nombre} tienes {edad} años".format(edad=23, nombre="Pepe"))

# Forma 3

nombre, edad = "Sofia", 19
print("Hola {1} tienes {0} años".format(edad, nombre))