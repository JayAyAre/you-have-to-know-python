"""
https://www.youtube.com/watch?v=2oQFv5tmfwM

En python, un diccionario es una estructura de datos
que contiene elementos de datos NO ordenados.

y al igual que un lista, un diccionario puede ser homogeneo
(Mismo tipo de elementos) o heterogeneo (Diferentes tipos de elementos)

Pueden ser mutables (modificables)

Sintaxis:
    diccionario = {key: valor}
    key => Es la llave que hace referencia al valor
    valor => Es el valor que se guarda en el diccionario

si queremos mas de 1 elemento en el diccionario, debemos usar:
    diccionario = {key1: valor1, key2: valor2}

Ademas, podemos tener claves de todo tipo de valores, por ejemplo:
    diccionario = {1: "uno", 'a': "dos", 3: "tres"}
    pero evidentemente no es recomendable.

Los diccionarios pueden tener las mismas claves que uno dentro del otro.
    un ejemplo:
        diccionario = {
            "diccionario": {
                "diccionario": {
                    1: "uno",
                    2: "dos",
                    3: "tres",
            }
        }

Por otro lado, si un diccionario tiene claves repetidas, el valor de la clave repetida
se quedara con el ultimo valor asignado.
"""

# Imprimimos el diccionario vacio
diccionario_vacio = {}

print(f"Asi luce un diccionario vacio: {diccionario_vacio}")
print()

# Diccionario homogeneo
diccionario_homoneo = {
    "nombre": "Juan",
    "edad": 25,
    "sexo": "Masculino",
}

print(f"Asi luce un diccionario homogeneo: {diccionario_homoneo}")
print()

# Diccionario heterogeneo

diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "sexo": "Masculino",
    "lista": [1, 2, 3, 4, 5],
    "diccionario": {"uno": 1, "dos": 2, "tres": 3},
}

print(f"Asi luce un diccionario heterogeneo: {diccionario}")
print()

# Diccionario con claves de tipo string
diccionario_string = {
    "nombre": "Juan",
    "edad": 25,
    "sexo": "Masculino",
    "lista": [1, 2, 3, 4, 5],
    "diccionario": {"uno": 1, "dos": 2, "tres": 3},
}
