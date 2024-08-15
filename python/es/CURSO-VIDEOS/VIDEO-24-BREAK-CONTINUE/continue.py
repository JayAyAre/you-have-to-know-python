# Continue

print("While con la sentencia continue\n")
counter = 0
while counter < 10:
    counter += 1
    if counter == 5:
        # Se detiene la iteracion del ciclo y continua con la siguiente iteracion
        continue
    print("valor de counter: ", counter)

print("\n Fin del programa.")