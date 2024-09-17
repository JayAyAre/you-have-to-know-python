# Sets

# Los sets son como listas pero no admiten elementos repetidos

set_1 = {1, 2, 3, 4, 5}
set_2 = {}  # Dict vacio
set_3 = set()
del set_2
print(type(set_1))

print(len(set_1))

print(set_1)
set_1.add(6)
print(set_1)

# Un set no es una estructura de datos ordenada
# Su forma de almacenar los elementos, es desordenada, por lo tanto no se puede usar []

set_1.add("jordi")
print(set_1)

set_1.add("jordi")
set_1.add("jordi")
print(set_1)

# Ademas, un set no admite repetidos

# print(set_1[0]) Type error: 'set' object does not support item assignment

print("jordi" in set_1)
print("Jordi" in set_1)

set_1.remove("jordi")
print(set_1)

set_1.clear()
print(set_1)

print(type(set_1))

# Usando el update, modifica el set

my_set = {1, 2, 3, 4, 5}
my_set.update({5, 6, 7, 8, 9, 10})
print(my_set)

# Usando el union, devuelve la unión de los sets

my_set = {1, 2, 3, 4, 5}
my_set_2 = my_set.union({5, 6, 7, 8, 9, 10})
print(my_set_2)

# usando el difference, devuelve la diferencia entre los sets

my_set = {1, 2, 3, 4, 5}
my_set_2 = my_set.difference({5, 6, 7, 8, 9, 10})
print(my_set_2)

# usando el intersection, devuelve la intersección entre los sets

my_set = {1, 2, 3, 4, 5}
my_set_2 = my_set.intersection({5, 6, 7, 8, 9, 10})
print(my_set_2)

# usando el symmetric_difference, devuelve la diferencia simétrica entre los sets

my_set = {1, 2, 3, 4, 5}
my_set_2 = my_set.symmetric_difference({5, 6, 7, 8, 9, 10})
print(my_set_2)
