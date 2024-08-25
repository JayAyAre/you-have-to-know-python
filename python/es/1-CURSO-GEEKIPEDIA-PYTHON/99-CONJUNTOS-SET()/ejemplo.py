conjunto = {5, 1, 3, 4, 2}
print(
    f"Mi conjunto es: {conjunto}"
)  # Mi conjunto es: {5, 1, 3, 4, 2} pero printea {1, 2, 3, 4, 5}

# Python no ordena los numeros ingresados en un set.

print("El conjunto {5, 1, 3, 4, 2} es", conjunto)

conjunto = {-1, 0, -2, 5, 1, 4}
print("El conjunto {-1, 0, -2, 5, 1, 4} es", conjunto)

conjunto = {"a", "b", "c", "d", "e", "f"}
print("El conjunto {'a', 'b', 'c', 'd', 'e', 'f'} es", conjunto)

conjunto_heterogeneo = {1, 2, (2, 3), "hola"}
print("El conjunto {1, 2, (2, 3), 'hola'} es", conjunto_heterogeneo)

conjunto_duplicado = {1, 2, 2, 2}
# Como hay valores duplicados, los elimina y proporciona un conjunto unicamente con valores unicos.
print("El conjunto {1, 2, 2, 2} es", conjunto_duplicado)

# conjunto_con_listas = {1, 2, [1, 2, 3]}  Indica un error, unhashable type: 'list'
# print("Conjunto con listas {}:")
# print("El conjunto {1, 2, 2, 2, [1, 2, 3]} es", conjunto_con_listas)

lista = ["a", "b", 6, 7, 8, 9, 10]
conjunto = set(lista)
print("El conjunto {'a', 'b', 6, 7, 8, 9, 10} es", conjunto)

conjunto = set("Hola mundo")
print("El conjunto {'Hola mundo'} es", conjunto)
