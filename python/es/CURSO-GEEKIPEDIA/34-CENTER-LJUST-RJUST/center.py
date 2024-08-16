"""
https://www.youtube.com/watch?v=QSZ1xhu_Wo4

En python es posible alinear el texto que imprimimos en pantalla, de acuerdo a las
necesidades del programador. Para ello tenemos el metodo center(), el cual alinea el texto
al centro de la pantalla. Ademas de alinear el texto al centro, tambien podemos alinear el texto
al principio o al final de la linea con el metodo ljust() y rjust().

Center nos permite alinear el texto al centro de la pantalla añadiendo
espacios o caracteres a la izquierda o a la derecha del texto.

sintax:
    nombre_variable.center(longitud, caracter)
        longitud: tiene que ser un entero positivo y mayor que la longitud del texto
        caracter: tiene que ser un caracter unicamente, por ejemplo " " o "-"

Con este metodo, lo centramos aumentando la longitud del string indicada por longitud.
"""

nombre = "Hola Mundo"
print("Antes de aplicar center: ", nombre)
print(f"\nLongitud de {nombre}: {len(nombre)}")
print("\nDespues de aplicar center: ", nombre.center(15, "="))