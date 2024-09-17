# Listas
# Son como un array, son el reemplazo de los arrays en python pero con funciones incorporadas

my_list = [1, 2, 3, 4, 5]
my_other_list = []
my_other_list_2 = list()

print(my_list)
print(my_other_list)
print(my_other_list_2)

# La posicion inicial es 0
# Son colecciones de elementos
# Recordemos que pueden guardar cualquier tipo de dato

my_list[0] = "Hola"
my_list[1] = "Mundo"
print(my_list)
print(type(my_list))

# Para acceder a un elemento, usamos el []

print(my_list[0])
print(my_list[-1])

# print(my_list[5]) # IndexError: list index out of range
# print(my_list[-6]) # IndexError: list index out of range

# Contar elementos

print(my_list.count(3))

my_other_list = ["Jordi", "Perez", 21, 176.0]
name, last_name, age, height = my_other_list
print(name)

# No hacer esto

name, last_name, age, height = my_other_list[0], my_other_list[1], my_other_list[2], my_other_list[3]
print(name)

# Concatenar listas

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2

print(list_3)

# Añadir al final de la lista

print(f"Mi lista original es: {my_list}")
my_list.append(6)
print(f"Mi lista despues de ejecutar .append(6) es: {my_list}")

# Añadir en una posicion
my_list = [1, 2, 3, 4, 5]
print(f"Mi lista original es: {my_list}")
my_list.insert(-1, 6)
print(f"Mi lista despues de ejecutar .insert(2, 6) es: {my_list}")

# Eliminar elementosç

print(f"Mi lista original es: {my_list}")
del my_list[0]
print(f"Mi lista despues de ejecutar del my_list[0] es: {my_list}")

# Eliminar elementos con remove

print(f"Mi lista original es: {my_list}")
my_list.remove(2)
print(f"Mi lista despues de ejecutar my_list.remove(2) es: {my_list}")

# Eliminar elementos con pop

print(f"Mi lista original es: {my_list}")
my_list.pop()
print(f"Mi lista despues de ejecutar my_list.pop() es: {my_list}")
