"""
https://www.youtube.com/watch?v=KvAdtb_UBDk

Un subconjunto es un conjunto solo contiene elementos que tambien estan presentes
en otro conjunto mas grande.

Si tenemos A y B
Diremos que B es un subconjunto de A si todos los elementos de B estan presentes en A.

Si todos los elementos de B estan presentes en A, entonces B es un subconjunto de A.

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}

B es un subconjunto de A? Si

A = {1, 2, 3, 4, 5}
B = {1, 9}

B es un subconjunto de A? No, porque 9 no esta en A.

En python para comprobar si B es un subconjunto de A, usamos el metodo
issubset o bien utilizar <= y <

se utiliza para comprobar si un conjunto dado, es un subconjunto de otro.
Devuelve True si el conjunto dado es un subconjunto de otro, False en caso contrario.

Sintaxis:
    conjunto_b.issubset(conjunto_a)

    Primero colocamos el subconjunto que queremos comprobar en el lado izquierdo.
    Y en los parentesis, el conjunto mas grande.

Con los operadores <= y <, podemos comparar dos conjuntos para saber si un
conjunto es un subconjunto de otro.

el operador <= se utiliza para saber si un conjunto es un subconjunto
inclusivo de otro. Este operador devuelve True si el conjunto a la izquierda
es un subconjunto del conjunto de la derecha.

    conjunto_b.issubset(conjunto_a)
    Es lo mismo que:
    conjunto_b <= conjunto_a

A = {1, 2, 3, 4, 5}
B = {1, 2, 3, 4, 5}

B <= A? Si

el operador < se utiliza para saber si un conjunto es un subconjunto
estricto de otro conjunto. Devuelve True si el conjunto a la izquierda
es un subconjunto del conjunto de la derecha pero no son iguales.

A = {1, 2, 3, 4, 5}
B = {2, 4}

B < A? Si

A = {1, 2, 3, 4, 5}
B = {1, 2, 3, 4, 5}

B < A? No, porque A es igual a B.
"""
