"""
https://www.youtube.com/watch?v=8tXEia5ZcCE

Cuando hemos trabajado con listas, hemos visto que pueden contener
booleanos, numeros, cadenas, etc.

Sin embargo, tambien podemos almacenar datos de tipo lista. de tal
manera que una lista puede contener otra lista.

un ejemplo es:

lista = [1 , 2, 3, [4, 5, 6]]

donde sus posiciones son:

lista[0] = 1
lista[1] = 2
lista[2] = 3
lista[3] = [4, 5, 6]

y asi accedemos a los datos de la lista anidada con:

lista[3][0] = 4
lista[3][1] = 5
lista[3][2] = 6

y si tenemos una lista anidada de una lista anidada, podemos
un ejemplo es:

lista = [1, 2, 3, [[4, 5, 6], [7, 8, 9]]]

acceder a los datos de la lista anidada de una lista anidada con:

lista[3][0][0] = 4
lista[3][0][1] = 5
lista[3][0][2] = 6
"""
lista = [1, 'a', True, [1, 2, ['f', 'g', 'h']]]
print("La lista es: ", lista)
print("El elemento [0] es: ", lista[0])
print("El elemento [3][1] es:", lista[3][1])
print("El elemento [3][1] es:",lista[3][2][1])