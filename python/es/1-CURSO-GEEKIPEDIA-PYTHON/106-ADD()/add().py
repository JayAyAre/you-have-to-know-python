"""
https://www.youtube.com/watch?v=6gTDUR_sbMs

add() sirve para agregar un elemento a un conjunto, este metodo solo permite
trabajar con un argumento de manera simultánea.

sintaxis:
    nombre_conjunto.add()

frutas = {"manzana", "pera", "uva"}

frutas.add("naranja")
"""

frutas = {"manzana", "pera", "uva"}
print(f"Lista original de frutas: {frutas}")

frutas.add("naranja")
print(f"Lista con 'naranja' agregada: {frutas}")

frutas.add("pera")
print(f"Lista con 'pera' agregada: {frutas}")
