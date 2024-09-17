# Condicionales

my_condition = True

if my_condition:  # Lo mismo que if my_condition == True
    print("Se ejecuta la condicion")

print("Se ejecuta fuera de la condicion")

my_condition = 5 * 2

if my_condition:
    print("Se ejecuta la condicion")

print("Se ejecuta fuera de la condicion")

my_condition = 5*3

if my_condition > 10 and my_condition < 16:
    print("Es mayor que 10 y menor que 16")


elif my_condition > 16:
    print("Es mayor o igual a 16")
else:
    print("Es menor que 16")

# Usar elif o else, son totalmente opcionales. y recordemos que unicamente se ejecutara el primero que
# cumpla su condicion, o en caso de que no cumpla ninguna, se ejecutara el else
