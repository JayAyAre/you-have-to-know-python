"""
https://www.youtube.com/watch?v=Lgk4zXVVOIA

Una cadena de caracteres es una sucesion que puede contener caracteres de cualquier tipo.

un ejemplo de cadenas de caracteres es:
    "Diana se peina sola"
    "1234567890"
    "hola mundo"

es posible acceder a partes especificas de una cadena de caracteres, las cuales
seran llamadas subcadenas o substrings.

un substring es una sucesion de caracteres que se encuentra en una cadena de caracteres.

un ejemplo de substrings es:
    Diana
    Diana se
    peina
    sola
    s
    se

    y todas estan incluidas en la cadena 'Diana se peina sola'

sintax:
    cadena_variable[inicio : final : saltos]
    asi podemos obtener 1 caracter, o mas de 2 caracteres

    inicio: Establece donde inicia el substring
    Final: Establece donde termina el substring
    Saltos: Establece el numero de saltos que realizara el indice para obtener el substring
    Los valores asignados deben ser numeros enteros
        Los numeros enteros seran desde la izquierda
        Los numeros negativos seran desde la derecha
            -1 sera la ultima posicion del indice
            -2 sera la penultima posicion del indice
            -3 sera la tercera posicion del indice
            etc...
"""

string = "0123456789"

print("\n"+"1 Parametro".center(70, '='))

substring = string[0]
print(f"\nEl substring de {string} [0] es {substring}")

substring = string[1]
print(f"\nEl substring de {string} [1] es {substring}")

substring = string[2]
print(f"\nEl substring de {string} [2] es {substring}")

substring = string[-1]
print(f"\nEl substring de {string} [-1] es {substring}")

substring = string[-2]
print(f"\nEl substring de {string} [-2] es {substring}")

print("\n"+"2 Parametros".center(70, '='))

substring = string[0:2]
print(f"\nEl substring de {string} [0:2] es {substring}")

substring = string[:3]
print(f"\nEl substring de {string} [:3] es {substring}")

substring = string[2:]
print(f"\nEl substring de {string} [2:] es {substring}")

substring = string[-4:-1]
print(f"\nEl substring de {string} [-4:-1] es {substring}")

substring = string[:]
print(f"\nEl substring de {string} [:] es {substring}")

print("\n"+"3 Parametros".center(70, '='))

substring = string[1:6:2] # Cojera los indices 1,3,5
print(f"\nEl substring de {string} [1:6:2] es {substring}")

substring = string[::3]
print(f"\nEl substring de {string} [::3] es {substring}")