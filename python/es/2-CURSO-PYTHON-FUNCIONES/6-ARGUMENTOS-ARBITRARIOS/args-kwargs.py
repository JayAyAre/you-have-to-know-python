def funcion_combinada(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos palabra clave:", kwargs)

funcion_combinada(1, 2, 3, a=4, b=5, c=6)