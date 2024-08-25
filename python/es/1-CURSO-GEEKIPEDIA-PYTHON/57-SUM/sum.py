"""
https://www.youtube.com/watch?v=uypyeOTndVQ

Al trabajar con listas, es posible que queramos sumar los elementos de una lista

para ello usaremos el metodo sum.

sintaxis:
    sum(objeto_iterable, inicio)
    objeto_iterable: lista, range...
    inicio: indica el valor inicial de la suma, debe ser entero
"""

numeros = [1,2,3,4,5]

suma = sum(numeros)
print("Los numeros son: ", numeros)
print(f"La suma de los numeros es: {suma}")

suma = sum(numeros, 2)

# True tiene un valor de 1 en True, y 0 en False
numeros = [1, 2.5, True]
print("Los numeros son: ", numeros)
print(f"La suma de los numeros es: {sum(numeros)}")

# Si intentamos sumar un string, salta un error
numeros = [1, 2.5, 'a']
print("Los numeros son: ", numeros)
print(f"La suma de los numeros es: {sum(numeros)}")