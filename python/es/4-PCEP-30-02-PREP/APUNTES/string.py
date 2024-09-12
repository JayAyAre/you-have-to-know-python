"""
    Los metodos y funciones de la clase string mas comunes y que pueden ser usados
        para el examen PCEP 30 - 02 son:

            - str.upper()
            - str.lower()
            - str.strip()
            - str.split(), str.lstrip(), str.rstrip()
            - str.join()
            - str.replace()
            - str.find()
            - str.isalpha()
            - str.isdigit()
            - str.capitalize()
            - str.isupper(), str.islower(), str.isspace()
            - str.count()
            - str.title()
            - str.istitle()
            - str.swapcase()
            - str.startswith(), str.endswith()
            - str.center(), str.ljust(), str.rjust()
            - str.partition(), str.rpartition()
            - str.zfill()

    Ademas, recordemos que los string son ordenables y inmutables
        lo que quiere decir es que pueden ser indexados con [], pero no pueden ser modificados
"""

# Str.upper(), consiste en transformar todas las letras en mayusculas

print("\n" + "Metodo upper en 'hola mundo':")
print("\t" + "hola mundo".upper())
print()

# Str.lower(), consiste en transformar todas las letras en minusculas

print("Metodo lower en 'HOLA MUNDO':")
print("\t" + "HOLA MUNDO".lower())
print()

# Str.strip(), consiste en eliminar espacios en blanco al inicio y al final de la cadena. o caracteres.

print("Metodo strip en ' hola mundo ':")
print("\t" + " hola mundo ".strip())
print("\t" + "-hola mundo-".strip("-"))
print("\t" + "-hola mundo-".strip("-oh"))
print()

# str.lstrip(), consiste en eliminar espacios en blanco al inicio de la cadena

print("Metodo lstrip en ' hola mundo ':")
print("\t" + " hola mundo ".lstrip())
print("\t" + "-hola mundo-".lstrip("-"))
print("\t" + "-hola mundo-".lstrip("-oh"))
print()

# str.rstrip(), consiste en eliminar espacios en blanco al final de la cadena

print("Metodo rstrip en ' hola mundo ':")
print("\t" + " hola mundo ".rstrip())
print("\t" + "-hola mundo-".rstrip("-"))
print("\t" + "-hola mundo-".rstrip("-oh"))
print()

# Str.split(), consiste en dividir una cadena en una lista de cadenas, separadas por un delimitador

print("Metodo split en 'hola mundo':")
print("\t", "hola mundo".split())
print("\t", "hola,123 mundo".split(","))
print("\t", "hola,123 mundo".split(",123"))
print()

# str.join(), consiste en unir una lista de cadenas en una cadena. Donde el separador es donde se invoca el metodo

print("Metodo join en '-':")
print("\t" + "-".join(["mundo", "mundo"]))
print("\t" + "-".join(["mundo", "mundo", "mundo"]))
print()

# str.replace(), consiste en reemplazar una cadena por otra en una cadena

print("Metodo replace en 'hola mundo hola2':")
print("\t" + "hola mundo hola2".replace("hola", "pepino"))
print("\t" + "hola mundo hola2 mundo2".replace("hola", "pepino", 1))
print()

# str.find(), consiste en encontrar una cadena en otra, y devolver su posicion

print("Metodo find en 'hola mundo':")
print("\t", "hola mundo".find("hola"))
print("\t", "hola mundo".find("mundo"))
print("\t", "hola mundo".find("mundo"))
print("\t", "hola mundo".find("mundo"))  # Si no lo encuentra, salta error
print()

# str.isalpha(), consiste en devolver True si la cadena contiene solo letras, y False en caso contrario

print("Metodo isalpha en 'hola mundo':")
print("\t", "hola mundo".isalpha())
print()

# str.isdigit(), consiste en devolver True si la cadena contiene solo numeros, y False en caso contrario

print("Metodo isdigit en 'hola mundo':")
print("\t", "hola mundo".isdigit())
print()

# str.capitalize(), consiste en transformar la primera letra de la cadena en mayuscula

print("Metodo capitalize en 'hola mundo':")
print("\t", "hola mundo".capitalize())
print()

# str.isupper(), consiste en devolver True si la cadena contiene solo letras mayusculas, y False en caso contrario

print("Metodo isupper en 'hola mundo':")
print("\t", "hola mundo".isupper())
print()

# str.islower(), consiste en devolver True si la cadena contiene solo letras minusculas, y False en caso contrario

print("Metodo islower en 'hola mundo':")
print("\t", "hola mundo".islower())
print()

# str.isspace(), consiste en devolver True si la cadena contiene solo espacios en blanco, y False en caso contrario

print("Metodo isspace en 'hola mundo':")
print("\t", "hola mundo".isspace())
print()

# str.count(), consiste en contar el numero de veces que aparece una cadena en otra

print("Metodo count en 'hola mundo':")
print("\t", "hola mundo".count("hola"))
print("\t", "hola mundo".count("o"))
print()

# str.title(), consiste en transformar la primera letra de cada palabra en mayuscula

print("Metodo title en 'hola mundo':")
print("\t", "hola mundo".title())
print()

# str.istitle(), consiste en devolver True si la cadena es una palabra, y False en caso contrario

print("Metodo istitle en 'hola mundo':")
print("\t", "hola mundo".istitle())
print()

# str.swapcase(), consiste en cambiar la capitalizacion de todas las letras de una cadena

print("Metodo swapcase en 'hola MUNDO':")
print("\t", "hola MUNDO".swapcase())

# str.startswith(), consiste en devolver True si la cadena empieza por una cadena, y False en caso contrario

print("Metodo startswith en 'hola mundo':")
print("\t", "hola mundo".startswith("hola"))
print()

# str.endswith(), consiste en devolver True si la cadena termina por una cadena, y False en caso contrario

print("Metodo endswith en 'hola mundo':")
print("\t", "hola mundo".endswith("mundo"))
print()

# str.center(), consiste en centrar una cadena en una cadena de largo dado

print("Metodo center en 'hola mundo':")
print("\t", "hola mundo".center(20))
print("\t", "hola mundo".center(20, "*"))
print()

# str.ljust(), consiste en centrar a la izquierda una cadena en una cadena de largo dado

print("Metodo ljust en 'hola mundo':")
print("\t", "hola mundo".ljust(20))
print("\t", "hola mundo".ljust(20, "*"))
print()

# str.rjust(), consiste en centrar a la derecha una cadena en una cadena de largo dado

print("Metodo rjust en 'hola mundo':")
print("\t", "hola mundo".rjust(20))
print("\t", "hola mundo".rjust(20, "*"))
print()

# str.partition(), consiste en dividir una cadena en tres partes.

print("Metodo partition en 'hola mundo 2':")
print("\t", "hola mundo 2".partition(" "))
print("\t", "hola mundo 2".partition("x"))
print("\t", "hola mundo 2".partition("2"))
print()

# str.rpartition(), consiste en dividir una cadena en funcion de un separador pasado como argumento pero desde el final

print("Metodo rpartition en 'hola mundo 2':")
print("\t", "hola mundo 2".rpartition(" "))
print("\t", "hola mundo 2".rpartition("x"))
print("\t", "hola mundo 2".rpartition("2"))
print()

# str.zfill(), consiste en rellenar una cadena con ceros a la izquierda

print("Metodo zfill en '5':")
print("\t", "5".zfill(5))
print()
