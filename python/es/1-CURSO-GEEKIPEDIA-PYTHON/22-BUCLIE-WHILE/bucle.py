"""
https://www.youtube.com/watch?v=aeXYFaIEELA

Cuando desarrollamos un programa, es posible que nos encontremos en la situacion
en la que debamos ejecutar codigo en repetidas ocasiones. La solucion
mas logica es repetir codigo, pero eso no es la solucion mas eficiente.

Para solucionar este problema, podemos utilizar bucles. Un bucle es un
bloque de codigo que se ejecuta en mas de una ocasion dependiendo de si
se cumple una condicion. Mientras que se cumpla, se repetira la ejecucion
del codigo.
"""

print("Esto es un bucle while")

# La sintaxis del bucle es: "while condicion: codigo"
contador = 3

while contador > 0:
    print("Estoy en un bucle while, contador: ", contador)
    contador -= 1

print("Estoy fuera del bucle while")

# Ejemplo 2

nombre = input("Introduce tu nombre: ")
x = 0
while x < 1000:
    print("Tu nombre es", nombre, x)
    x += 1

print("fin")