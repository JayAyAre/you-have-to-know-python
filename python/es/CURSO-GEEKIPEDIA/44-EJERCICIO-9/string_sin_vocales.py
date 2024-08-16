"""
https://www.youtube.com/watch?v=q5txLirbIgM

Desarrolla un promgrama que reciba un texto y muestre el texto sin las vocales.

En caso de que no haya vocales, el bucle finaliza su ejecucion.

Requisitos:
    - Usar un bucle for / while
    - El usuario puede introducir cualquier texto (Mayusculas y minscalas)
"""

print("".center(100,'-'))
print("QUITA LAS VOCALES".center(100))
print("".center(100,'-'))

string = input("\nIntroduce un texto: ")
fin_bucle = input("\nIntroduce con que letra finaliza el bucle: ")
resultado = ""
for char in string:
    if char.lower() == fin_bucle.lower():
        break
    elif char.lower() not in "aeiou":
        resultado += char

print(resultado)