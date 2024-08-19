"""
https://www.youtube.com/watch?v=MMGFqdGuqwA

La sintaxis para acceder a un valor en un diccionario es:
    diccionario[clave]

ejemplo:
    diccionario = {"nombre": "Juan", "edad": 25, "sexo": "Masculino"}
    print(diccionario["nombre"])
    Esto imprimira Juan
"""

diccionario = {
    "nombre": "Juan",
    "edad": 25,
}
print("Accedemos a 'nombre' y obtenemos: ", diccionario["nombre"])
print("Accedemos a 'edad' y obtenemos: ", diccionario["edad"])

diccionario = {
    1: [1, 2, 3],
    "diccionario": {
        "nombre": "Juan",
        "edad": 25,
        "sexo": "Masculino",
        "lista": [1, 2, 3, 4, 5],
        "diccionario": {"uno": 1, "dos": 2, "tres": 3},
    },
}

print("Accedemos a 1 y obtenemos: ", diccionario[1])
print("Accedemos a 'diccionario' y obtenemos: ", diccionario["diccionario"])
print(
    "Accedemos a 'diccionario'['nombre'] y obtenemos: ",
    diccionario["diccionario"]["nombre"],
)

# Si ponemos una clave que no existe, obtenemos error-
