"""

https://youtu.be/6mBL2p1O3AY?si=bnbuJ6aJwoZ-kekf

Al utilizar condiciones simples y compuestas, nos podemos encontrar con la necesidad de incluir mas
de una condicion a una misma estructura de condicion. Para ello, utilizamos la palabra clave "elif".

las condiciones multiples nos permite elegir una ruta entre varias rutas posibles con base al valor
de una variable que actua como selector.

En el momento que se ejecute la condicion, se procedera a ejecutar el bloque de codigo correspondiente

Multiples:
    if (condicion logica): -> indica el bloque de codigo que se ejecutara si se cumple la condicion logica
        instruccion 1
    elif (condicion logica): -> indica el bloque de codigo que se ejecutara si se cumple la condicion logica
        instruccion 2
    else: -> indica el bloque de codigo que se ejecutara si la condicion logica es falsa
        instruccion 3

"""

num_uno = 5

if num_uno >= 5:
    print("El numero es mayor o igual a 5")
elif num_uno < 3:
    print("El numero es menor a 3")
else:
    print("El numero es 3 o 4")

print("Fin.")