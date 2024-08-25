print("".center(80,"-"))
print("CONVERSOR DE ENTERO A ROMANO".center(80, '-'))
print("".center(80, "-"), "\n")

while True:
    try:
        int_to_convert = int(input("Ingresa un entero: "))
        if 0 < int_to_convert < 4000:
            break
        else:
            print("El rango aceptable es de 1 a 3999")
    except ValueError:
        print("Ingresa un entero valido")

valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

resultado = ""

for valor, simbolo in valores:
    while int_to_convert >= valor:
        resultado += simbolo
        int_to_convert -= valor

print(resultado)
