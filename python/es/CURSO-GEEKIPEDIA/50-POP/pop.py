"""
https://www.youtube.com/watch?v=3M_Iz1j8q30&list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz&index=51

En python, ademas de agragar elementos, podemos eliminar elementos de una lista.
ya sea el ultimo elemento o alguno en particular.

Con pop, podemos eliminar el ultimo elemento, o un elemento en particular.

sintaxis:
    lista.pop()
    lista.pop(indice)

Ademas, de eliminar un elemento en particular, podemos usar el metodo pop
para obtener el valor del elemento eliminado.
"""

vocales = ["a", "e", "i", "o", "u"]
print(f"Lista vocales:\n{vocales}")
print(vocales.pop())
print(f"Lista vocales despues de pop():\n{vocales}")

vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales:\n{vocales}")
print(vocales.pop(0))
print(f"Lista vocales despues de pop(0):\n{vocales}")

vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales:\n{vocales}")
print(vocales.pop(2))
print(f"Lista vocales despues de pop(2):\n{vocales}")

vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales:\n{vocales}")
print(vocales.pop(-1))
print(f"Lista vocales despues de pop(10):\n{vocales}")

vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales:\n{vocales}")
print(vocales.pop(10))
print(f"Lista vocales despues de pop(10):\n{vocales}")