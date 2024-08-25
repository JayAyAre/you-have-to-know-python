"""
Este metodo nos permite alinear unicamente a la derecha del string.

sintax:
    nombre_variable.rjust(longitud, caracter)
        longitud: tiene que ser un entero positivo y mayor que la longitud del texto
        caracter: tiene que ser un caracter unicamente, por ejemplo " " o "-"
"""

nombre = "Hola Mundo"
print("Antes de aplicar rjust: ", nombre)
print(f"\nLongitud de {nombre}: {len(nombre)}")
print("\nDespues de aplicar rjust: ", nombre.rjust(20, "="))
print(f"Se agregaron {len(nombre.rjust(20, '=')) - len(nombre)} caracteres")