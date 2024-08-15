"""
rstrip se utiliza para eliminar caracteres al inicio de la cadena.

Si no se especifica ningun caracter, se eliminan todos los caracteres al inicio de la cadena.
"""

cadena = "\t\n\t\nhola mundo"
print(cadena.lstrip()) # imprime "hola mundo"
print(cadena.lstrip("\t\n hola")) # imprime "mundo"
