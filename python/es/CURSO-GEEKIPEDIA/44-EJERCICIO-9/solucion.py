print("".center(100, "-"))
print("QUITA LAS VOCALES".center(100))
print("".center(100, "-"))

string = input("\nIntroduce un texto: ")
fin_bucle = input("\nIntroduce con que letra finaliza el bucle: ")
resultado = ""
for char in string:
    if char.lower() == fin_bucle.lower():
        break
    elif char.lower() not in "aeiou":
        resultado += char

print(resultado)
