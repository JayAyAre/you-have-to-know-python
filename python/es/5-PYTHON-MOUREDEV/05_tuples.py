# Tuplas

# Son como listas, pero no se pueden modificar

# Como definir una tupla

my_tuple = (1, 2, 3, 4, 5)
my_tuple_2 = ()
my_tuple_3 = tuple()
my_tuple_4 = 1, 2, 3, 4, 5
my_tuple_5 = 1,
print(my_tuple_2)

my_tuple = (21, 1.76, "Jordi", "Ramirez", "Jordi")
print(my_tuple[0])
print(my_tuple[1])

print(my_tuple.count("Jordi"))
print(my_tuple.index("Jordi"))
print(my_tuple.index("Jordi"))

# TypeError: 'tuple' object does not support item assignment
# my_tuple[0] = "Juan"

# Concatenar tuplas

my_tuple_1 = (1, 2, 3)
my_tuple_2 = (4, 5, 6)
my_tuple_3 = my_tuple_1 + my_tuple_2
print(my_tuple_3)

print(my_tuple_3[3:6])

my_tuple_3 = list(my_tuple_3)
print(my_tuple_3)

# del my_tuple_3[2]

del my_tuple_3
# print(my_tuple_3)
