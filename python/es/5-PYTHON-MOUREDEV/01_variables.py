# Variables en Python

# Se utiliza snake_case para nombrar variables

lugar_de_nacimiento = "Madrid"
print(lugar_de_nacimiento)

# Variables en una sola linea

nombre, apellido, edad, lugar_de_nacimiento = "Juan", "Perez", 30, "Madrid"
print(nombre, apellido, edad, lugar_de_nacimiento)

# ¿Forzamos el tipo?
# Esto es un tipado debil ya que sin embargo, podemos modificar el tipo de la variable

# Especificamos el tipado para expresar que queremos que sea un string
address: str = "Madrid"
address = 32
print(type(address))
print(address)
