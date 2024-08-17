"""
https://www.youtube.com/watch?v=niW_BNlb5G0&list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz&index=55ç

Al trabajar con listas, es posible ordenarlas, para ello usaremos el metodo sort.

Con este metodo, podemos ordenarla de forma ascendente o descendente.

sintaxis:
    lista.sort() # Ordena de forma ascendente
    lista.sort(reverse=True) # Ordena de forma descendente
"""

lista_numeros = [5, 2, 8, 1, 9, 3, 4, 7, 6]
print("\nMi lista de numeros es:", lista_numeros, end="\n\n")

print("Mi lista ordenada de forma ascendente:", end="\n\n")
lista_numeros.sort()
print(lista_numeros, end="\n\n")

print("Mi lista ordenada de forma descendente:", end="\n\n")
lista_numeros.sort(reverse=True)
print(lista_numeros, end="\n\n")

vocales = ["a",'i',"o","u",'e']

print("\nMi lista de vocales es:", vocales, end="\n\n")

print("Mi lista ordenada de forma ascendente:", end="\n\n")
vocales.sort()
print(vocales, end="\n\n")

print("Mi lista ordenada de forma descendente:", end="\n\n")
vocales.sort(reverse=True)
print(vocales, end="\n\n")