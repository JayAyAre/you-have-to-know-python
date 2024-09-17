# Strings

my_string = "Hola"
my_string = 'Hola'
my_string = "Hola" "mundo"
print(my_string)
print(len(my_string))

# Concatenación
my_string = "Hola" + "Mundo"
print(my_string)

# Salto de linea

my_string = "Hola\nMundo"
print(my_string)

# Tabulacion

my_string = "Hola\tMundo"
print(my_string)

# Escapar string

my_scaped_string = "\nEste es un string\nEscapado"
print(my_scaped_string)
my_scaped_string = "\\tEste es un string\\nEscapado"
print(my_scaped_string)

# Formato de strings
"""
    %s - String
    %d - Entero
    %f - Float
    %.2f - Float con dos decimales

"""

print(f"Hola {'Mundo'}")
print("Hola {a}".format(a="Mundo"))
print("Hola {}".format("Mundo"))

name, last_name, age = "Juan", "Perez", 33
print("My name is %s %s and I am %d years old" % (name, last_name, age))

print(f"My name is {name} {last_name} and I am {age} years old")

# No es acoonsejable esto

print("My name is " + name + " " + last_name +
      " and I am " + str(age) + " years old")

print("Pi: %.2f" % 3.141592653589793)

# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a, b)

# Division

language = "Python"
language_sliced = language[0:3]
print(language_sliced)

print(language[0:3:2])
print(language[0:6:2])
print(language[-1:-5:-1])

# Funciones

python = "Python"

print(python.lower())
print(python.upper())
print(python.title())
print(python.capitalize())
print(python.count("t"))
print(python.find("t"))
print(python.index("t"))
print(python.replace("t", "T"))
print(python.lower().islower())
