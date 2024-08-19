print("".center(80, "="))
print("CONTADOR DE LETRAS EN UN STRING".center(80, "="))
print("".center(80, "="))

string = input("Ingrese un string para contar las letras: ")

letter_count = dict.fromkeys(string, 0)


for letter in string:
    letter_count[letter] += 1

# for letter in letter_count:
#     for letter_in_string in string:
#         if letter_in_string == letter:
#             letter_count[letter] += 1

print(f'\nA continuación la frecuencia de cada caracter en la frase "{string}":')
for key in letter_count:
    print(f'El caracter "{key}" aparece: {letter_count[key]} veces ')
