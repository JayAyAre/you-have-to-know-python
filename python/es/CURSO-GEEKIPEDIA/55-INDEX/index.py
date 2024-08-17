"""
https://www.youtube.com/watch?v=unoXxXRMOVk

Al trabajar con listas, es posible que queramos saber cual es el indice de un elemento en particular. ya sea
para eliminarlo, o para insertarlo en una posicion determinada. Para ello usaremos el metodo index.

El metodo index nos permite trabajar con un argumento minino,
o con un maximo de 3 argumentos de fomra simultanea.

Sintaxis:
    lista.index(elemento) # Puede ser cualquier tipo de dato
    lista.index(elemento, inicio) # Inicio es opcional, por defecto es 0, indica el indice del primer elemento 
        para empezar a buscar el elemento
    lista.index(elemento, inicio, fin) # Inicio y fin son opcionales,
        fin indica el indice del ultimo elemento para buscar el elemento
"""

vocales = ["a", "e", "i", "o", "u","a"]
print("\nMi lista de vocales es:", vocales, end="\n\n")

# Este metodo es igual que remove, cuando encuentra el primer elemento que coincida con el parametro
# Lo devuelve. Es decir, si hay mas de un elemento que coincida, devuelve el indice del primer elemento

print("Uso el metodo index con el elemenro 'i':", vocales.index("i"), end="\n\n")

print("Uso el metodo index con el elemenro 'e':", vocales.index("e"), end="\n\n")


print("Uso el metodo index con el elemenro 'a':", vocales.index("a"), end="\n\n")

# Si le indico un inicio como 2, revisara primero el elemento vocales[2], y luego el siguiente
print("Uso el metodo index con el elemento 'a' y el inicio 2:", vocales.index("a", 2), end="\n\n")

# Revisa los elementos desde [2] hasta [5]
print("Uso el metodo index con el elemento 'a', el indice 2 y el fin 6:", vocales.index("a", 2, 6), end="\n\n")
