"""
Sucede cuando una funcion se ejecuta dentro de otra funcion
de tal manera que se definen variables locales en el ambito de la funcion
que se ejecuta


"""
# Funciones anidadas

def exterior():
    x = 10 # x es de ambito local de exterior()

    def interior():
        x = 20 # a es de ambito encerrado
        print(x) # Imprime 20

    interior()
    print(x) # Imprime 10

exterior()


def exterior():
    x = 10 # x es de ambito local de exterior()

    def interior():
        # No podemos usar global x
        # Para poner modificarla, agregamos nonlocal x
        nonlocal x
        x = 20 # a es de ambito encerrado
        print(x) # Imprime 20

    interior()
    print(x) # Imprime 20

exterior()

