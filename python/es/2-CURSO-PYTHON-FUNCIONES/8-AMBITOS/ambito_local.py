def funcion():
    x = 10 # variables de ambito local
    print(x)

funcion()
# Si intento hacer print(x), no funcionara porque x no existe en el ambito actual
# x solo existe en el ambito local de la funcion funcion()