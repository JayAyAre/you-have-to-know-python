"""
https://www.youtube.com/watch?v=_Px4BJbkll8

rstrip se utiliza para eliminar caracteres al final de la cadena.

Si no se especifica ningun caracter, se eliminan todos los caracteres al final de la cadena.
"""

cadena = "hola mundo\t\n\t\n"
print(cadena.rstrip()) # imprime "hola mundo"
print(cadena.rstrip("\t\nhola")) # imprime "hola mund"