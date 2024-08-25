print("***** Usando el operador + ***** \n")
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(f"tupla1: {tupla1} | tupla2: {tupla2}")
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada, "\n")


print("***** Usando el operador += ***** \n")
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(f"tupla1: {tupla1} | tupla2: {tupla2}")
tupla1 += tupla2
print("tupla1: ", tupla1, "\n")


print("***** Usando la función tuple() ***** \n")
tupla1 = (1, 2, 3)
lista = [4, 5, 6]

print(f"tupla1: {tupla1} | lista: {lista}")
tupla_concatenada = tupla1 + tuple(lista)
print(tupla_concatenada)
