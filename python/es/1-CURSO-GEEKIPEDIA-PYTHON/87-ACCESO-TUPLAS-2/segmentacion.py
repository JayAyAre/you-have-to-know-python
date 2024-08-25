"""
https://www.youtube.com/watch?v=v3DxrsKISe8

En esta leccion, vamos a enfocarnos en el segundo metodo, el operador de segmentacion.

Este operador se utiliza para obtener una subsecuencia de una tupla, una lista, o un string.

sintaxis:
    tupla[inicio:fin:saltos] => Es muy similar a la sintaxis de la lista

    incio: Indica el indice del primer elemento de la subsecuencia
    fin: Indica el indice del ultimo elemento de la subsecuencia
    saltos: Indica el numero de elementos que se van a omitir en la subsecuencia
Los indices deben ser enteros.
"""

vocales = ("a", "e", "i", "o", "u")

print(f"Vocales: {vocales}")

print(f"Los elementos [0:2] son: {vocales[0:2]}")
print(f"Los elementos [0:2:1] son: {vocales[0:2:1]}")
print(f"Los elementos [0:4:2] son: {vocales[0:4:2]}")
print(f"Los elementos al reves son: {vocales[::-1]}")
