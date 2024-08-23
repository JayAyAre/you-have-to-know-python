"""
https://www.youtube.com/watch?v=zMYj5efsqbA

Un conjunto es una coleccion de elementos no ordenados y con los elementos
unicos y no repetidos.

Al decir que no es ordenado, nos referimos a que pyhon no mantendra el orden
que hemos asignado a los elementos.

Pueden ser homogeneos o heterogeneos.

Un conjunto principalmente es mutable, sin embargo, los elementos
dentro de un conjunto son inmutables, por lo tanto, un conjunto no puede
tener listas, diccionarios, ni otros conjuntos.

Unicamente puede tener valores inmutables, por lo tanto, los elementos
como: enteros, booleanos, strings, tuplas, y cualquiera inmutable

sintaxis:
    conjunto = {elemento1, elemento2, ..., elementoN}

Ademas, podemos hacerlo con la funcion set()
    conjunto = set(objeto_iterable)
    unicamente admite objetos iterables y un argumento.

"""

conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_heterogeneo = {1, 2, (2, 3), "hola"}

print(conjunto_numeros)
print(conjunto_heterogeneo)
