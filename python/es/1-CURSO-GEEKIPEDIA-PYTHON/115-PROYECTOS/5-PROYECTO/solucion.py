print("".center(80,"-"))
print("CONVERSOR DE ROMANO A EMTERO".center(80, '-'))
print("".center(80, "-"), "\n")

while True:
    try:
        roman_to_convert = input("Ingrese un número romano: ").upper()
        break
    except ValueError:
        print("Ingresa un entero valido")

valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
resultado = 0
valor_anterior = 0

for posicion, caracter in enumerate(roman_to_convert):
    for valor, romano in valores[::-1]:
        if caracter == romano:
            resultado += valor
            if valor_anterior < valor and valor_anterior != 0:
                resultado -= valor_anterior*2
            valor_anterior = valor

print(resultado)