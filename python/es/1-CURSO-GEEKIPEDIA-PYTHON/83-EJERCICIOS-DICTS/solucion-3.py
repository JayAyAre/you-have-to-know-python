print("".center(80, "="))
print("Ejercicio 3".center(80, "="))
print("".center(80, "="))

fruits = {"manzanas": 5, "peras": 2, "naranjas": 4}

print("\n", fruits)

print("Eliminamos 'peras' del diccionario con pop")
fruits.pop("peras")
print(
    fruits, "No existe"
)  # Si no existe, salta error. En caso de que tenga un valor por defecto, devuelve ese valor


fruits = {"manzanas": 5, "peras": 2, "naranjas": 4}
print("Eliminamos 'peras' del diccionario con del")
del fruits["peras"]  # Si no existe, salta error
print(fruits)
