"""
https://www.youtube.com/watch?v=zvPe3jcxLs4

En python, el metodo count nos permite saber la cantidad de veces que aparece
una cadena o caracter especifico en otra cadena o caracter.

Se encarga de buscar una subcaneda en particular dentro de otra cadena.

sintax:
    cadena_variable.count(subcadena)
"""

nombre = "Hola, esto es un ejemplo de cadenas"
print(nombre.count("esto"))
print(nombre.count("Hola"))
print(nombre.count("a"))
print(nombre.count("e"))
print(nombre.count("o"))

print("\nCon varios parametros:")
nombre = "mi mama me mima"
print(nombre.count("m"))
print(nombre.count("m", 3)) # Le indico que empieze en la tercera posicion, es decir en ' '
print(nombre.count("m", 13)) # Si pongo un numero mayor, se situara en la ultima posicion
print(nombre.count("m", -1)) # Si pongo negativo, se situara alrevez.

"""
si pongo negativo, sera asi

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
m i   m a m a   m e   m i m a
el -1 perteneceria al 14

si pongo dos parametros, marcaremos el principio y el final
si coloco 3 y 7, unicamente revisara la frase "mama"
"""