def funcion_condicional(valor): # Una funcion puede devolver cualquier tipo de valor
    if valor > 0:
        return "Positivo"
    elif valor < 0:
        return "Negativo"
    else:
        return "Cero"

print(funcion_condicional(1))
print(funcion_condicional(-1))
print(funcion_condicional(0))