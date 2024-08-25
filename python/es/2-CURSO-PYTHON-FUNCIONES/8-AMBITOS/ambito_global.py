y = 20 # variables de ambito global

# No me deja modificar variables globales desde una funcion
def funcion():
    y = 30 # variables de ambito local
    print("Impresion desde el ambito local", y) # 30


funcion()
# Si intento hacer print(y), funcionara porque y existe en el ambito global
print("Impresion desde el ambito global", y) # 20

# Si quiero modificar variables globales desde una funcion
def funcion_gloabal():
    # No podemos hacer: global y = 40
    global y # Indica que y es una variable global
    y = 40 # Modifica la variable global
    print("Impresion desde el ambito local", y) # 40

funcion_gloabal()
print("Impresion desde el ambito global", y) # 40