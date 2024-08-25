def multiplicador(factor):
    def funcion_interna(x):
        return x * factor
    return funcion_interna

multiplicador_2 = multiplicador(2)
multiplicador_5 = multiplicador(5)

print(multiplicador_2(10))
print(multiplicador_5(10))