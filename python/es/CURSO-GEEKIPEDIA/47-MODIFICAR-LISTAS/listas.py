"""
https://www.youtube.com/watch?v=bz788gzeUcE

En python, si queremos trabajar con listas, tenemos la ventaja
de poder modificar su contenido.

Sintaxis:
    vocales = ["a", "e", "i", "o", "u"]
    vocales[0] = "A"
    vocales[1] = "E"
    vocales[2] = "I"
    vocales[3] = "O"
    vocales[4] = "U"

    La lista vocales es modificada. y quedara:
    ["A", "E", "I", "O", "U"]
"""

print("Nuestra lista de vocales es: ")
vocales = ["a", "e", "i", "o", "u"]
print(vocales)

vocales[0] = "A"
vocales[1] = "E"
vocales[2] = "I"
vocales[3] = "O"
vocales[4] = "U"

print("\nLa lista modificada es: ")
print(vocales)

vocales[2:4] = ["A", "E"]

print("\nLa lista modificada es: ")
print(vocales)

vocales[2:4] = ["A", "E", "I"]
print("\nLa lista modificada es: ")
print(vocales)

vocales[:1] = [1, 2]
print("\nLa lista modificada es: ")
print(vocales)

vocales[0:3] = "t", "m" # Elimina el elemento de la pos [2], ya que no se le asigna un valor
# Como se elimino un valor, la lista se redujo en un elemento.
print("\nLa lista modificada es: ")
print(vocales)

vocales[:] = "x"
print("\nLa lista modificada es: ")
print(vocales)