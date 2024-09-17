# Funciones

from audioop import mul


def my_function():
    print("Hello World from my_function")


my_function()
my_function()

# Funciones con parametros


def sum_two_numbers(a, b):
    return a + b


print(sum_two_numbers(5, 10))

# Funciones con parametros opcionales


def sum_two_numbers(a, b=0):
    return a + b


# Llamadas en funcion de argumentos posicionales

sum_two_numbers(5, 10)
sum_two_numbers(10, 5)

# Llamadas en funcion de argumentos nombrados

sum_two_numbers(a=5, b=10)
sum_two_numbers(b=10, a=5)

# sum_two_numbers(a=5, 10)  # Error

# Numero desconocido de argumentos posicionales


def multiply_numbers(*my_args):
    total = 1
    for arg in my_args:
        total *= arg
    return total


multiply_numbers(5, 10, 15)
multiply_numbers(5, 10, 15, 20)


# Numero desconocido de argumentos nombrados
def multiply_numbers(**my_variables):
    total = 1
    for key, value in my_variables.items():
        total *= value
    return total


multiply_numbers(a=5, b=10, c=15)
multiply_numbers(a=5, b=10, c=15, d=20)

print(multiply_numbers(a=5, b=10, c=15, d=20))

# Podemos indicar que tipo de dato queremos recibir como parametro, sin embargo
# No afecta al comportamiento de la funcion, si se le indica otro tipo de dato, se ejecutara sin errores.
# Esto unicamente sirve para informar que tipo de dato se espera recibir como parametro


def rest_numbers(first_number: int, second_number: float):
    return first_number - second_number

# Scope local


my_number = 5


def my_function():
    my_number = 10
    print(my_number)


my_function()
print(my_number)

# Scope global

my_number = 5


def my_function():
    global my_number
    my_number = 10
    print(my_number)


my_function()
print(my_number)

# Por otro lado, no podemos llamar variables creadas dentro de funciones

my_number = 5


def my_function():
    print(my_number)
    my_number_2 = 10
    print(my_number_2)


print(my_number)
my_function()
# Error print(my_number_2)
