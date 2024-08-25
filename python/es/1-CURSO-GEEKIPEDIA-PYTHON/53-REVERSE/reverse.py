"""
https://www.youtube.com/watch?v=6EM2xZUliUM&list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz&index=54

En python es posible revertir el orden de una lista, para ello usaremos el metodo reverse.

Este metodo no crea una copia de la lista, sino que modifica la misma.

sintaxis:
    lista.reverse()
"""

vocales = ["a", "e", "i", "o", "u"]
print("Mi lista de vocales es:", vocales, end="\n\n")
print("Mi posicion [0] es:", vocales[0], end="\n\n")
vocales.reverse()
print("La lista inversa:", vocales, end="\n\n")
print("Mi posicion [0] es:", vocales[0], end="\n\n")

