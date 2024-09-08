# What is the expected output of the following code snippet?

x = "DataScience" "4U"
print(x)

# Primero exponente y luego multiplicador

print(5 * 3 ** 1 * 5)

"""
    Dara 0 cuando sea igual a 0, o al divisor en negativo o positivo
    Siempre tiene el mismo signo que el dividendo, en este caso, el 3

    pasos:
        1. El resultado siempre es entre 0 y b - 1, por lo que sumamos el divisor hasta que entre al rango

"""

# -4 + 3 = -1, -1 + 3 = 2. Entro al rango a la segunda vez, el resultado es 2
print(-4 % 3)
print(-3 % 3)  # -3 + 3 = 0, es 0, entonces es 0
print(-2 % 3)  # -2 + 3 = 1, es 1, entonces es 1
print(-1 % 3)  # -1 + 3 = 2, es 2, entonces es 2
print(0 % 3)

# En caso del divisor sea negativo, el resultado es el modulo de la división
print(4 % -3)
print(3 % -3)
print(2 % -3)
print(1 % -3)
print(0 % -3)

# Que saldra en pantalla?

print()
lst = [3, 5, 2, 1]
sorted(lst)
print(lst)
