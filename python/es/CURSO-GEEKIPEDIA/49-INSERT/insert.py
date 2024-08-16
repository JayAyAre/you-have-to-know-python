"""
https://www.youtube.com/watch?v=L5plGtP-B44&list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz&index=50

En python, podemos añadir elementos en una determinada posicion de una lista.

Para ello, usamos el metodo insert.

sintaxis:
    lista.insert(indice, valor)
"""

letras = ["a", "b", "c", "d"]
print(f"Lista letras:\n{letras}")
letras.insert(0, 'e')
print(f"Lista letras despues de insert(0, 'e'):\n{letras}")

letras = ["a", "b", "c", "d"]
print(f"\nLista letras:\n{letras}")
letras.insert(2, 3)
print(f"Lista letras despues de insert(2, 3):\n{letras}")

letras = ["a", "b", "c", "d"]
print(f"\nLista letras:\n{letras}")
letras.insert(10, 4) # Si supera el tamaño de la lista, se añade al final de la lista.
print(f"Lista letras despues de insert(10, 4):\n{letras}")