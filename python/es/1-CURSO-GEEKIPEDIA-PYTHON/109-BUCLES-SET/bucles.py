"""
https://www.youtube.com/watch?v=Y2TbOe6iGYM

Como recorrer los conjuntos con bucles.
"""

nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Recorrer los elementos del conjunto con for
for num in nums:
    print(num)

# Recorrer los elementos del conjunto con while
index = 0
conjunto_lista = list(nums)
while index < len(conjunto_lista):
    elemento = conjunto_lista[index]
    print(elemento)
    index += 1
