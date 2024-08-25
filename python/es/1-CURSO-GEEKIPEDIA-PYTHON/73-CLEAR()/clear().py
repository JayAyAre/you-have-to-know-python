"""
https://www.youtube.com/watch?v=1MaOdhTJaSM

Clear es un método que borra el contenido de un diccionario, lista, tupla, etc.

la sintaxis es:
    diccionario.clear()
"""

diccionario = {"a": 1, "b": 2, "c": 3}

print("Mi diccionario inicial:\n", diccionario)
diccionario.clear()
print("Mi diccionario despues de ejecutar clear:\n", diccionario)

diccionario = {
    "juan": {"nombre": "Juan", "apellido": "Perez", "edad": 30},
    "maria": {"nombre": "Maria", "apellido": "Perez", "edad": 30},
}

print("Mi diccionario inicial:\n", diccionario)
diccionario["juan"].clear()
print("Borro el diccionario de Juan:\n", diccionario)
diccionario.clear()
print(f"Borro mi diccionario: {diccionario}")
