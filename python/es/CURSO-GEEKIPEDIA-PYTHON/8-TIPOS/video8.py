"""
https://www.youtube.com/watch?v=EaWsOcc7R2M&list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz&index=9

Un tipo de datos es un atributo de los datos que indica a la computadora y al programador
sobre la clase de datos que se va a manejar.

Existen los siguientes tipos de datos:
    - Enteros y largos
    - Flotantes
    - Numeros complejos
    - Cadenas
    - Booleanos

"""


"""

Los numeros ENTEROS son aquellos que no tienen decimales, son solo enteros.
y se representan con int para enteros y long para enteros grandes.

Los numeros FLOTANTES son aquellos que tienen decimales, son solo flotantes.
y se representan con float para flotantes y double para flotantes grandes.

Los numeros COMPLEJOS son aquellos que tienen una parte real y una parte imaginaria.
La gran mayoria de lenguajes de programacion carecen de este tipo, pero en python se puede
representar con complex.

Las CADENAS son aquellos que contienen caracteres, son solo cadenas de caracteres.
Se llaman strings en python, y no son mas que texto encerrado entre comillas simples, o dobles.
En triples cadenas, ponemos escribir el texto en varias lineas y se respetaran los saltos de linea sin
necesidad de poner \n en cada linea.

Los BOOLEANOS son solo dos valores, verdadero o falso.
Son muy importantes para condiciones y los bucles.
En python se representan con bool


"""

# ENTEROS
# Recordemos que python usa el tipado dinamico.

# Los numeros long no los trataremos porque son enteros demasiado grandes.

numero = 15
print(numero, type(numero))

# FLOTANTES

numero_flotante = 15.5
print(numero_flotante, type(numero_flotante))

# COMPLEJOS
# Los complejos son numeros usandos principalmente para ingenieria y desarrollo/investigacion de ciencia.

numero_complejo = 5 + 6j # Parte real + Parte imaginaria
print(numero_complejo, type(numero_complejo))

# CADENAS

cadena = "Hola jordi"
print(cadena, type(cadena))
cadena_larga = """Hola
    Jordi
    Soy
    Un
    String
Largo"""
print(cadena_larga, type(cadena_larga))

# BOOLEANOS

verdadero_falso = 3 == 3
print(verdadero_falso, type(verdadero_falso))




