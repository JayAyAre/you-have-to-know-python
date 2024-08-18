print("".center(100, "="))
print("Programa que invierte un string".center(100, "="))
print("".center(100, "=") + "\n")

string_original = input("Introduce la cadena de caracteres a invertir: ")
string_invertida = ""
index = 0

for char in string_original[::-1]:
    string_invertida[index] += char
    index += 1

print(f"La cadena de caracteres invertida es: {string_invertida}")
