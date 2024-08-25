def modificar_valor(valor):
    valor = valor * 2 # Modifica el valor pero en ambito local
    print("Dentro de la funcion: valor = ", valor)

numero = 10

# Se pasan por valor automaticamente: string, int, float. los tipos de dato simples
modificar_valor(numero) # Pasamos una copia del valor a la funcion, sus cambios no afectaran al valor original
print("Fuera de la funcion: valor = ", numero)

def cambiar_valor(valor):
    valor = not valor
    print("Valor dentro de la función:", valor)

mi_booleano = True
cambiar_valor(mi_booleano)
print("Valor fuera de la función:", mi_booleano)