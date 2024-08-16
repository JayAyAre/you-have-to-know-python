"""
https://www.youtube.com/watch?v=4AYusdQ_4Xk

Se nos pide un programa que invierta una cadena de caracteres.
y a su vez, esta tendra que ser ingresada por el usuario.

Requisitos:
    - No cambiar la cadena de caracteres ingresada por el usuario
    - Usar un bucle for
"""

print("".center(100, '='))
print("Programa que invierte un string".center(100, '='))
print("".center(100, '=') + "\n")

string_original = input("Introduce la cadena de caracteres a invertir: ")
string_invertida = ""
index = 0
for char in string_original:
    string_invertida = char + string_invertida[index:]

print(f"La cadena de caracteres invertida es: {string_invertida}")

"""
Otra forma de hacerlo:
    string_original = input("Introduce la cadena de caracteres a invertir: ")
    string_invertida = ""
    index = 0

    for char in string_original[::-1]:
        string_invertida[index] += char
        index += 1

    print(f"La cadena de caracteres invertida es: {string_invertida}")
"""