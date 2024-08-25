def saludar(nombre, saludo):
    mensaje = f"{saludo}, {nombre}!"
    print(mensaje)


saludar("Ana", "Hola")

# Con palabras clave:

saludar(saludo="Hola", nombre="Ana")
# saludar(saludo="Hola", "Ana") # Error
# saludar(nombre="Ana", "hola") # Error
