"""
https://www.youtube.com/watch?v=5YbUzvjAV-Y

Podemos usar el metodo capitalize() para convertir el primer caracter de cada palabra
de un string a mayusculas. Ademas de comprobar si un string esta completamente en mayusculas o no.
sintax:
    nombre_variable.capitalize()

A diferencia del metodo title, capitalize solo cambia la primera letra de la primera palabra.
mientras que title cambia la primera letra de cada palabra.
"""

nombre = "el VIAJE eS la RecoMpensa"
print("Antes de aplicar capitalize: ", nombre)
print("Despues de aplicar capitalize: ", nombre.capitalize())