"""
Este metodo nos permite alinear unicamente a la izquierda del string.

sintax:
    nombre_variable.rjust(longitud, caracter)
        longitud: tiene que ser un entero positivo y mayor que la longitud del texto
        caracter: tiene que ser un caracter unicamente, por ejemplo " " o "-"
"""

nombre = "Hola Mundo"
print("Antes de aplicar ljust: ", nombre)
print(f"\nLongitud de {nombre}: {len(nombre)}")
print("\nDespues de aplicar ljust: ", nombre.ljust(20, "="))
print(f"Se agregaron {len(nombre.ljust(20, '=')) - len(nombre)} caracteres")