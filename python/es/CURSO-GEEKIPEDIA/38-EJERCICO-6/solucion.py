print("".center(100, "="))
print("Programa que elimina una palabra de una cadena de texto".center(100, "="))
print("".center(100, "=") + "\n")

cadena = input("Introduce la cadena de texto: ")
palabra = input("Introduce la palabra a eliminar: ")

index = cadena.find(palabra)
substring = cadena[:index] + cadena[len(palabra) + index :]
print(f"La cadena con la palabra eliminada es: {substring}")
