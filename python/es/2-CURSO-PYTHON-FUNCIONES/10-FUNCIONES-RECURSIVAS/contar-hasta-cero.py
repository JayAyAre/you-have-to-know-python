# Las funciones recursivas son funciones que se llaman a sí mismas.

def contar_hasta_cero(n):
    if n <= 0:
        print("Ha llegado a {}".format(n))
        return
    print(n)
    n -= 1
    contar_hasta_cero(n)

contar_hasta_cero(5)