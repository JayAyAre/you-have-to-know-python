def exponente(base, exp=2): # Esto hace que sea su valor por defecto
    resultado = base ** exp
    print(resultado)

exponente(2)
exponente(2, 3)
exponente(2, exp=4)
exponente(exp=5, base=2)

# Si hago esto, saldra error
# exponente(exp=5, 5)
