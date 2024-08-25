"""
https://www.youtube.com/watch?v=ULP1758dNcM

Se utiliza para recorrer elementos de un objeto iterable, como listas, tuplas, diccionarios, etc.
al mismo tiempo se lleva un contador de la posicion de cada elemento en el iterable.add()

Con la funcion enumerate() podemos pasarle un argumento e incluso 2

sintaxis:
    enumerate(iterable, start=0)

    Si no pasamos el argumento start, el contador inicial es 0
"""

frutas = ["manzana", "pera", "fresa", "limon"]
print("Mi lista de frutas es:", frutas)

print("\nRecorrido con for:")
for posicion, fruta in enumerate(frutas, start=101): # Primero nos devuelve la posicion, luego el elemento
    print(f"Posicion: {posicion}, Fruta: {frutas}")

print("\nConvertido a lista:")
enumerated_list = list(enumerate(frutas, start=1))

print("Mi lista de enumerados es:", enumerated_list)