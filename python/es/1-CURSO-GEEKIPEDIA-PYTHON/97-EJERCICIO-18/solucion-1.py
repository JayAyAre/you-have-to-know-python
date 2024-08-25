print("".center(80, "="))
print("SUMA DE TUPLAS".center(80, "="))
print("".center(80, "="))

tupla1 = (1, 2, 3, 4, 5)
tupla2 = (8, 6, 4, 2, 0)

list = []
for num1, num2 in zip(tupla1, tupla2):
    list.append(num1 + num2)

print("Tupla 1:\t", tupla1)
print("\t\t +")
print("Tupla 2:\t", tupla2)
print("\t\t ===============")
print("Suma:\t\t", tuple(list))

"""

print("Tupla 1:".ljust(13), tupla1)
print("".ljust(14) + "+")
print("Tupla 2:".ljust(13), tupla2)
print("".ljust(14) + "===============")
print("Suma:".ljust(13), tuple(list))

"""
