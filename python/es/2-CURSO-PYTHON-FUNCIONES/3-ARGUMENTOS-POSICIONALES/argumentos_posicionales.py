def nombre_completo(nombre, apellido):
    cadena = f"{nombre} {apellido}"
    print(cadena)

nombre_completo("Juan", "Perez")

# Las posiciones de los argumentos son importantes

nombre_completo("Perez", "Juan")