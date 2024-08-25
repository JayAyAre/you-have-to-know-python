# **kwargs
def imprimir_info(**info): # Acepta cualquier numero de argumentos y los agrupa en un diccionario
    print(info)
    for clave, valor in info.items():
        print(f"{clave}: {valor}")


imprimir_info(nombre="Juan", edad=25, pais="España")