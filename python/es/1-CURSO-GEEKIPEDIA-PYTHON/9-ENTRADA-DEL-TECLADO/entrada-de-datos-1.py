"""

https://youtu.be/vlka4aIRqUc?si=NvIMkanXcpct0eLG

En python se puede introducir entrada de datos del teclado con el objetivo de manejar
datos de entrada de usuarios.

Con la entrada de datos, puede ser un texto, un numero, una fecha, etc.

"""

# input es una funcion de python que nos permite solicitar datos desde el teclado
# En los parentesis, podemos escribir un mensaje que ayudara a leer al usuario lo que se le solicita

palabra = input("Ingrese una palabra: ")
numero_int = int(input("ingrese un numero entero: ")) # Convierte el texto ingresado a un numero entero
numero_float = float(input("ingrese un numero flotante: ")) # Convierte el texto ingresado a un numero flotante
numero_complex = complex(input("ingrese un numero complejo: ")) # Convierte el texto ingresado a un numero complejo

print("String: " + palabra)
print("Entero: ", numero_int)
print("Flotante: ", numero_float)
print("Complejo: ", numero_complex)

# Tenemos que observar que si ponemos mal el input, se nos va a dar un error
