"""

https://youtu.be/yJg0_7r3f-M?si=NFAy4DY4tcXNBLWE

Las sentencias condicionales anidadas se presentan cuando por el camino de verdadero o falso de
una sentencia condicional, se encuentra otra condicion adicional.

Es decir, cuando estamos con alguna condicion simple, compuesta o multiple, nos podemos encontrar
con una condicion adicional dentro de la misma ruta.

Anidadas:
    if (condicion logica): -> indica el bloque de codigo que se ejecutara si se cumple la condicion logica
        instruccion 1
        if (condicion logica): -> indica el bloque de codigo que se ejecutara si se cumple la condicion logica
            instruccion 2

"""

num_uno = 7

if num_uno >= 5:
    print("El numero es mayor o igual a 5")
    if num_uno == 7:
        print("El numero es 7")
elif num_uno < 3:
    print("El numero es menor a 3")
else:
    print("El numero es 3 o 4")

print("Fin.")