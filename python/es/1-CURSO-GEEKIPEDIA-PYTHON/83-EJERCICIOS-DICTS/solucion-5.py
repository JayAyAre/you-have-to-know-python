print("".center(80, "="))
print("Ejercicio 5".center(80, "="))
print("".center(80, "="))

fruits = {"manzanas": 5, "peras": 2, "naranjas": 4}

print("\n", fruits)

print("La clave manzana esta en el diccionario?")
print("manzanas" in fruits)

if fruits.get("manzanas"):
    print("True")
else:
    print("False")
