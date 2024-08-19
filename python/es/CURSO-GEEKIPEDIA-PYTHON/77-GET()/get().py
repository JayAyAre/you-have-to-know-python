"""
https://www.youtube.com/watch?v=it0yNzu8VDQ

El metodo get se utiliza para obtener los valores que estan asociados
a cada clave de un diccionario.

es util porque evita errores al intentar obtener un valor que no existe en el
diccionario

en lugar de dar error, devuelve un valor por defecto o None.
Ademas es mas eficiente para verificar si un valor existe en el diccionario que un if

la sintaxis es:
    diccionario.get(key, value)

ejemplos
    diccionario ={
        'a': 1,
        'b': 2,
        'c': 3
    }
    valor = diccionario.get('a')
    print(valor) # imprime 1
    valor = diccionario.get('z')
    print(valor) # imprime None
    valor = diccionario.get('z', -1)
    print(valor) # imprime -1
"""

fruit_dict = {"manzana": 1, "pera": 2, "naranja": 3}

print(fruit_dict)

precio = fruit_dict.get("manzana")
print(f"El precio de la manzana es {precio}")

precio = fruit_dict.get("mango")
print(f"El precio del mango es {precio}")

precio = fruit_dict.get("uva", "falta de stock")
print(f"El precio de la uva es {precio}")
