"""
https://www.youtube.com/watch?v=vu5SA3DnXBI

Para acceder a los elementos de una tupla, podemos usar 3 formas:
    - usando el indice del elemento
    - usando el operador de segmentacion
    - usando el desempaquetador de tuplas

En esta leccion, vamos a enfocarnos en el primer metodo, el indice del elemento.

sintaxis:
    tupla[indice] => Es muy similar a la sintaxis de la lista

"""

vocales = ("a", "e", "i", "o", "u")
print(f"Vocales: {vocales}")
print(f"El tipo de la tupla es: {type(vocales)}")

print(f"Mi primer elemento es: {vocales[0]}")
print(f"Mi segundo elemento es: {vocales[1]}")
print(f"Mi tercer elemento es: {vocales[2]}")

print(f"Mi posicion -1 es: {vocales[-1]}")
print(f"Mi posicion -2 es: {vocales[-2]}")
print(f"Mi posicion -3 es: {vocales[-3]}")
