'''
https://youtu.be/1CDE1pdVDGw?si=wEXQcLR6f8wXr-oO

Las cadenas de caracteres mejor conocidas como strings, es una serie de caracteres compuestas
por letras, numeros, signos y simbolos, que dentro de sus funciones destaca la interaccion
con el usuario

existen distintas operaciones para manipular una cadena de caracteres (strings). Dentro
de las cuales se encuentran:

-Asignacion -> +=
-Concatenacion -> +
-Busqueda -> .find
-Extraccion -> []
-Comparacion -> ==


'''

# ASIGNACIÓN
# Consiste en asignar una cadena de caracteres a otra

mensaje = "Hola"
mensaje += " "
mensaje += "jordi"
print(mensaje)

# con esto conseguimos que mensaje sea "Hola jordi". conseguimos
# que se junten varias cadenas de caracteres

# CONCATENACION
# Consiste en unir dos o mas cadenas para una de mayor tamaño

mensaje = "Hola"
espacio = " "
nombre = "jordi"
resultado = mensaje + espacio + nombre
print(mensaje + espacio + nombre)
print(resultado)

numero1 = 5
numero2 = 4
resultado = str(numero1 + numero2)
print("Resultado " + resultado)

# BUSQUEDA
# Consiste en localizar dentro de una cadena, una cadena mas pequeña o subcadena
# usaremos el metodo .find()

mensaje = "Hola jordi"
nombre = "jordi"
subcadena = mensaje.find(nombre)
print(subcadena)

# EXTRACCION
# Consiste en extraer una subcadena de caracteres de una cadena

mensaje = "Hola ernesto" # Hay que tener en cuenta, que se hace desde el indice incluido
subcadena = mensaje[5:10] # hasta el indice marcado -1
print(subcadena)

'''

es decir: esto

- h o l a   e r n e s t o
- 0 1 2 3 4 5 6 7 8 9 10 11

si ponemos 5:10, ira desde la "e" incluida, hasta la 10 - 1, es decir, el 9 incluido
el cual es la "s"

'''

# COMPARACION
# se utiliza para comparar si dos cadenas de caracteres son iguales

mensaje1 = "hola"
mensaje2 = "hola"
mensaje3 = "hol"
print(mensaje1 == mensaje2)
print(mensaje1 == mensaje3)