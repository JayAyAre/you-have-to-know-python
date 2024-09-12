"""
    Los metodos mas comunes de los diccionarios son:

        - clear()
        - get()
        - items()
        - keys()
        - values()
        - pop()
        - popitem()
        - update()

    Los diccionarios son estructuras de datos con clave-valor, donde la clave es inmutable pero el valor no.
        Por lo tanto, los diccionarios son mutables.

    Ademas, los diccionarios son indexables, y se pueden iterar sobre ellos.

    Los diccionarios tienen un orden, y no se pueden modificar.

"""

# Formas de crear un diccionario

# Forma 1
print()
diccionario = {"a": 1, "b": 2, "c": 3}
print(diccionario)

# Forma 2
print()
diccionario = dict(ave=1, bird=2, coche=3)
print(diccionario)

# forma 3
print()
diccionario = dict([("a", 1), ("b", 2), ("c", 3)])
print(diccionario)

# Como acceder a los elementos de un diccionario

# Forma 1
print()
diccionario = {"a": 1, "b": 2, "c": 3}
print(diccionario["a"])
print(diccionario["b"])
print(diccionario["c"])

# Forma 2, con el metodo get
print()
diccionario = {"a": 1, "b": 2, "c": 3}
print(diccionario.get("a"))
print(diccionario.get("b"))
print(diccionario.get("c"))
print(diccionario.get("d", 0))

# Iterar un diccionario

# Forma 1
print()
diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de iterar sobre un diccionario: \n\t {
      diccionario}")
for clave, valor in diccionario.items():
    print("\t", clave, valor)

# Forma 2
print()
diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de iterar sobre un diccionario: \n\t {
      diccionario}")
for clave in diccionario:
    print("\t", clave)

# Metodos de un diccionario

# Metodo clear(), borra el contenido del diccionario

diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de usar el metodo clear(): \n\t {
      diccionario}")
diccionario.clear()
print("\t", diccionario)

# Metodo get(), devuelve un valor, o un valor por defecto si no existe

diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de usar el metodo get(): \n\t {
      diccionario}")
print("\t", diccionario.get("a"))
print("\t", diccionario.get("b"))
print("\t", diccionario.get("c"))
print("\t", diccionario.get("d"))
print("\t", diccionario.get("d", 0))

# Metodo items(), devuelve en tuplas las claves y valores

diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de usar el metodo items(): \n\t {
      diccionario}")
for clave, valor in diccionario.items():
    print("\t", clave, valor)
print(diccionario.items())

# Metodo keys(), devuelve las claves

diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de usar el metodo keys(): \n\t {
      diccionario}")
print("\t", diccionario.keys())

# Metodo values(), devuelve los valores

diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de usar el metodo values(): \n\t {
      diccionario}")
print("\t", diccionario.values())

# Metodo pop(), elimina un elemento del diccionario y devuelve su valor

diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de usar el metodo pop(): \n\t {
      diccionario}")
elemento = diccionario.pop("a")
print("\t", diccionario)
print("\t", elemento)

# Si la clave no existe, salta error
try:
    elemento = diccionario.pop("d")
except KeyError:
    print("\t La clave no existe")

# Sin embargo, si se pasa un elemento opcional, se devuelve el valor por defecto si no existe
elemento = diccionario.pop("d", 0)
print("\t", elemento)

# Metodo popitem(), Elimina el ultimo elemento del diccionario y devuelve una tupla con la clave y el valor, en versiones anteriores eliminaba un elemento aleatorio

diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de usar el metodo popitem(): \n\t {
      diccionario}")
print("\t", diccionario.popitem())

# Metodo update(), actualiza el diccionario con otro diccionario

diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de usar el metodo update(): \n\t {
      diccionario}")
diccionario.update({"d": 4, "e": 5})
print("\t", diccionario)

# En caso de que existan claves repetidas, se sobreescriben

diccionario = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario original antes de usar el metodo update(): \n\t {
      diccionario}")
diccionario.update({"a": 4, "e": 5})
print("\t", diccionario)
