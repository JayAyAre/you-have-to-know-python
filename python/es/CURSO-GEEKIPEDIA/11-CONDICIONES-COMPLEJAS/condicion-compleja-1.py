"""

https://youtu.be/43NYFfUM5uU?si=S89kYKbQjPsBY2a4

Son aquellas condiciones que nos permiten una instruccion a ejecutar en funcion de
la condicion establecida. De tal manera que habran dos bloques de codigo, uno que
se ejecutara si la condicion es verdadera y otro que se ejecutara si la condicion
es falsa.

Jamas se ejecutaran ambos bloques de codigo, solo se ejecutara el que corresponda
a la condicion una vez se verifica.

Compuestas:
    if (condicion logica): -> indica el bloque de codigo que se ejecutara si se cumple la condicion logica
        instruccion 1
    else: -> indica el bloque de codigo que se ejecutara si la condicion logica es falsa
        instruccion 2

"""

num_uno = 5

if num_uno == 5:
    print("El numero es 5")
else:
    print("El numero NO es 5")

print("Fin.")