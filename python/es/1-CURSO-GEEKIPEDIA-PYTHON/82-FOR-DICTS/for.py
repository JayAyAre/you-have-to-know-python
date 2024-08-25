"""
https://www.youtube.com/watch?v=B10alyprBOc

Como recorrer un diccionario usando for

sintaxsis 1:
    for clave, valor in diccionario.items():
        print(clave, valor)

sintaxsis 2:
    for clave in diccionario:
        print(clave)
"""

dict_name = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"Mi diccionario: {dict_name}\n")

for key in dict_name:
    print(f"Clave: {key}\tValor: {dict_name[key]}")

print("\n")
for key, value in dict_name.items():
    print(f"Clave: {key}\tValor: {value}")
