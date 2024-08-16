"""
https://www.youtube.com/watch?v=ePWYQ9PetnM

Se nos pide un programa que elimine una palabra
que forme parte de una cadena de texto.

Requisitos:
    - La cadena de caracteres debe ser solicitada por teclado
    - La palabra a eliminar debe ser solicitada por teclado

"""
print("".center(100, '='))
print("Programa que elimina una palabra de una cadena de texto".center(100, '='))
print("".center(100, '=') + "\n")

cadena = input("Introduce la cadena de texto: ")
palabra = input("Introduce la palabra a eliminar: ")

index = cadena.find(palabra)
substring = cadena[:index] + cadena[len(palabra) + index:]
print(f"La cadena con la palabra eliminada es: {substring}")

"""
Otra forma de hacerlo:

cadena = input("Introduce la cadena de texto: ")
palabra = input("Introduce la palabra a eliminar: ")
cadena = cadena.replace(palabra, "")
print(f"La cadena con la palabra eliminada es: {cadena}")

"""