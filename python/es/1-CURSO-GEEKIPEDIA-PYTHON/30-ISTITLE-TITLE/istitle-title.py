"""
https://www.youtube.com/watch?v=9yZnegffzYw

En python, es posible convertir la primera letra de cada palabra de un string
en mayuscula. y asu vez, convertir el resto en minuscula.

Para ello tenemos el método istitle() que nos devuelve True si la primera letra
de cada palabra es mayúscula y False si no.

sintax:
    nombre_variable.istitle()
    nombre_variable.title()

"""

nombre = "CarLiTos GOnZaLeS"
nombre_minusculas = "Carlitos Gonzales"
print(nombre)
print(nombre.istitle()) # Resivsa si cada palabra empieza por una letra mayúscula, y luego si el resto es minuscula.
print(nombre_minusculas.istitle())
# print(nombre.title())

"""
el metodo title nos permite establecer el string en mayusculas la primera letra de cada palabra
y en minusculas el resto.
"""

print(nombre.title())