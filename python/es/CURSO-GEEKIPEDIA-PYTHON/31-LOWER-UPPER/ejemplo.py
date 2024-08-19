nombre = input("Introduce un nombre: ")

print(f"\n\t¿Todas las letras son minusculas? \n\t {nombre.islower()}")
nombre_minisculas = nombre.lower()
print(f"\n\tEl nombre en minusculas es: \n\t {nombre_minisculas}")
print(f"\n\t¿Todas las letras son mayusculas? \n\t {nombre_minisculas.isupper()}")
nombre_mayuscas = nombre_minisculas.upper()
print(f"\n\tEl nombre en mayusculas es: \n\t {nombre_mayuscas}")