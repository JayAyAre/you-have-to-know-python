"""
https://www.youtube.com/watch?v=8LGdagGDi1g

Un superconjunto tambien conocido como superset, se refiere a un conjunto
que contiene todos los elementos de otro conjunto.

A = {1, 2, 3, 4, 5}
B = {2, 5}

El superconjunto es el que tiene mayor longitud.
A es un superconjunto de B? SI
B es un subconjunto de A? SI

A = {1, 2, 3, 4, 5}
B = {2, 6}

A es un superconjunto de B? NO, porque 6 no esta en A.
B es un subconjunto de A? NO, porque 6 no esta en B.

A = {1, 2, 3, 4, 5}
B = {1, 2, 3, 4, 5}

A es un superconjunto de B? SI
B es un subconjunto de A? SI

Para comprobar esto, usamos el metodo issuperset o bien utilizar >= y >

sintaxis:
    conjunto_a.issuperset(conjunto_b)
    Primero colocamos el conjunto mas grande en el lado izquierdo.
    Y en los parentesis, el conjunto mas pequeño.

con el operador >= se utiliza para saber si un conjunto es un superconjunto
inclusivo de otro. Este operador devuelve True si el conjunto a la izquierda
es un superconjunto del conjunto de la derecha

A = {1, 2, 3, 4, 5, 6}
B = {1, 2, 3, 4}

A >= B? SI
A > B? SI

A = {1, 2, 3, 4, 5}
B = {1, 2, 3, 4, 5}

A >= B? SI
A > B? NO, porque A es igual a B.
"""
