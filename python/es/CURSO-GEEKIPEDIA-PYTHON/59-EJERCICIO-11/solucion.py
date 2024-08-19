print("".center(100, "="))
print("ELIMINAR VALORES DE UNA LISTA".center(100))
print("".center(100, "="), end="\n\n")

lista_original = ["A", "B", "b", "c", "E", "E", "f"]
print("La lista original es: ", lista_original)
input_element = input("Ingrese el elemento a eliminar: ")

while input_element in lista_original or input_element.swapcase() in lista_original:
    if input_element in lista_original:
        index = lista_original.index(input_element)
        lista_original.pop(index)
    elif input_element.swapcase() in lista_original:
        index = lista_original.index(input_element.swapcase())
        lista_original.pop(index)
"""
Otra solucion:
    for _ in lista_original:
        if input_element.upper() in lista_original:
            lista_original.remove(input_element.upper())
        elif input_element.lower() in lista_original:
            lista_original.remove(input_element.lower())
"""

print("La lista quedaria asi: ", lista_original)
