print("".center(100, "-"))
print("TABLA DE MULTIPLICAR".center(100))
print("".center(100, "-"))

numero = int(input("\nIntroduce un numero: "))
for iterative_number in range(1, 11):
    print(f"{numero} x {iterative_number} = {numero * iterative_number}")

print("".center(100, "-"))
