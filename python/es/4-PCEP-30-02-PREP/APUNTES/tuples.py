"""
    Los metodos mas comunes de las tuplas son:
        - count()
        - index()

    a diferencia de las listas, las tuplas no son mutables, son inmutables
    lo que significa que no se pueden modificar, agregar, o borrar elementos

    pero por otro lado, son ordenables e indexables
"""

# Formas de crear una tupla

# Forma 1
tupla = (1, 2, 3)
print(tupla)

# Forma 2
tupla = tuple([1, 2, 3])
print(tupla)

# Forma 3
tupla = 1, 2, 3
print(tupla)

# Forma 4
tupla = 1,
print(tupla)

# Forma 5
tupla = (1, )  # Si usamos (1) no se crea una tupla
print(tupla)

# Una caracteristica de las tuplas, es que si contienen alguna estructura mutable, se puede modificar asi
tupla = ([1, 2, 3], 4)
print(tupla)
tupla[0].append(999)
print(tupla)

# Esto es gracias a que no estamos modificando la tupla, si no que modificamos la lista dentro de la tupla.

# Formas iterar en una tupla
print()
tupla = (1, 2, 3)
print(f"Tupla original antes de iterar sobre una tupla: \n\t {tupla}")
for elemento in tupla:
    print("\t", elemento)

# Tambien podemos asignar multiples variables a una tupla

tupla = (1, 2, 3)
print(f"Tupla original antes de asignar multiples variables a una tupla: \n\t {
      tupla}")
x, y, z = tupla
print("\t", x)

# Metodos de las tuplas

# Metodo count()

tupla = (1, 2, 3, 4, 5, 6, 3)
print(f"Tupla original antes de usar el metodo count(): \n\t {tupla}")
print("\t", tupla.count(3))
print("\t", tupla.count(6))
print("\t", tupla.count(70))

# Metodo index()

tupla = (1, 2, 3, 4, 5, 6, 3)
print(f"Tupla original antes de usar el metodo index(): \n\t {tupla}")
print("\t", tupla.index(3))
print("\t", tupla.index(6))
# Si no lo encuentra, salta error
try:
    print("\t", tupla.index(70))
except ValueError:
    print("\t No existe el elemento")
