print("".center(80, "="))
print("Ejercicio 2".center(80, "="))
print("".center(80, "="))

fruits = {"manzanas": 5, "peras": 2, "naranjas": 4}

print("\n", fruits)

fruits.setdefault("bananas", 5)
print("Agregamos ('bananas', 5) al diccionario")
print("\n", fruits)


fruits.setdefault("mangos", 6)
print("Agregamos ('mangos', 6) al diccionario")
print("\n", fruits)

fruits.setdefault("uvas", 3)
print("Agregamos ('uvas', 3) al diccionario")
print("\n", fruits)

# Se puede usar tambien el metodo update
