"""
https://www.youtube.com/watch?v=e5m5kCIlv98

Combinaremos el desempaquetado de una tupla con el uso de un bucle for.
"""

tupla = ("001", "manzana", "rojo"), ("002", "pera", "verde")
print(f"Tupla: {tupla}")
for code, fruit, color in tupla:
    print(f"Codigo: {code}, Fruta: {fruit}, Color: {color}")

for tup in tupla:
    print(f"Tupla: {tup}")
