try:
    valores_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    numero_romano = input("Ingresa un número romano para convertirlo a entero:")
    numero_romano = numero_romano.upper()

    num_entero = 0
    valor_anterior = 0

    for caracter in numero_romano[::-1]:
        valor_actual = valores_romanos.get(caracter, 0)

        if valor_actual < valor_anterior:
            num_entero -= valor_actual
        else:
            num_entero += valor_actual

        valor_anterior = valor_actual

    print("Resultado: ", num_entero)

except Exception as e:
    print(f"Ingresa un número romano válido: {e}")
