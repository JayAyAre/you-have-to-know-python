"""
https://www.youtube.com/watch?v=Mh23v5fnL9s

el metodo update() se utiliza para agregar multiples elementos a un conjunto
a la vez.

puede utilizar como un argumento un objeto iterable.
como una lista, una tupla, un diccionario, etc.

de esta manera, agregara los elementos del objeto iterable a un conjunto.

sintaxis:
    nombre_conjunto.update()
    nombre_conjunto.update(objeto_iterable)
"""

colores = {"rojo", "verde", "azul"}

nuevos_colores = {
    "naranja",
    "amarillo",
    "azul",
}  # Puede ser un diccionario, lista, tupla, etc.

print(f"Colores originales: {colores}")
print(f"Colores nuevos: {nuevos_colores}")

colores.update(nuevos_colores)
print(f"Colores actualizados: {colores}")
