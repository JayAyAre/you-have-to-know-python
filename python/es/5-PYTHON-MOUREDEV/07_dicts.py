# Dicts

my_dict = {}
my_dict_2 = dict()

print(type(my_dict))
print(type(my_dict_2))

my_dict = {
    "Name": "Jordi",
    "Last Name": "Ramirez",
    "Age": 21,
    "Height": 17.60,
    1: 'python',
    "languages": ["Python", "JavaScript"]
}

print(my_dict)

print(len(my_dict))

# Mostrar los keys

print(my_dict.keys())

# Mostrar los values

print(my_dict.values())

# Mostrar los items

print(my_dict.items())

# Consultar un elemento

print(my_dict["Name"])
print(my_dict["Age"])

# Modificar un elemento

my_dict["Name"] = "Juan"
print(my_dict["Name"])

# Eliminar un elemento

del my_dict["Name"]

# Crear un nuevo elemento

my_dict["Name"] = "Juan"
print(my_dict["Name"])

# Metodo get para obtener un elemento

print(my_dict.get("Name", None))

print("Name" in my_dict)
print("Name_2" in my_dict)
print("Juan" in my_dict)

# Metodos para iterar

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.fromkeys("Name", "Juan"))

my_new_dict = my_dict.fromkeys(("Name",))
print(my_new_dict)
print(69.80 + 145.21)
print(1061.4 * .2)

my_new_dict = my_dict.fromkeys((1, 2, 3, 4, 5))
print(my_new_dict)

my_new_dict = my_new_dict.fromkeys(my_new_dict)
print(list(my_new_dict))
