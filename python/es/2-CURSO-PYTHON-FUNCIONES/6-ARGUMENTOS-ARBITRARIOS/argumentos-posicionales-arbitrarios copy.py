def sum_numeros(numeros):
    resultado = sum(numeros)
    print(resultado)

# sum_numeros(1, 2, 3) # Marca un error ya que indico 1 parametro, y 3 argumentos

# *args
# Son los argumentos posicionales arbitrarios

def sum_numeros_2(*numeros): # Indicamos que reciba cualquier numero de argumentos
    resultado = sum(numeros) # Ademas, empaqueta los argumentos en una tupla
    print(numeros)
    print(resultado)


sum_numeros_2(1, 2, 3)


