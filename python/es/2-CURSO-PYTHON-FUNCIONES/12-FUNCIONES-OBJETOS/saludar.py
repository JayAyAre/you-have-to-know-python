def saludar(nombre):
    return f"Hola, {nombre}!"

# Definimos la funcion como un objeto
mi_funcion = saludar

mensaje = mi_funcion("Juan")
print(mensaje)