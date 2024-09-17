# Operadores

# Basicas

print(2 + 1)
print(2 - 1)
print(2 * 1)
print(2 / 1)

# Modulo

print(2 % 1)
print(10 % 3)

# Exponente

print(2 ** 2)

# Division entera

print(10 // 3)

# Concatenación, solo para strings

print("Hola" + "Mundo")

# Duplicacion o multiplicación de strings

print("Hola" * 3)

# En las operaciones, si alguno de los dos es float, el resultado es float
# Excepto en division, donde el resultado es float aunque ambos sean int

# Operadores comparativos

print("\n", 2 < 1)
print(2 > 1)
print(2 <= 1)
print(2 >= 1)
print(2 == 1)
print(2 != 1)

# Con strings, Comprueba una ordenacion alfabetica por UNICODE

print("\n" + "Hola" < "Mundo")
print("Hola" > "Mundo")
print("Hola" <= "Mundo")
print("Hola" >= "Mundo")
print("Hola" >= "Bola")
print("Hola" >= "Zola")
print("Hola" == "Mundo")
print("Hola" != "Mundo")
print("A" < "B")

# Operadores lógicos

print()
print(3 > 2 and "Hola" > "Mundo")
print(3 > 2 or "Hola" > "Mundo")
print(3 > 2)
print(not (3 > 2))

"""
    Orden de evaluación

        0. Parentesis (El mas importante)
        1. ~, +, - unary,
        2. **
        3. *, /, //, %,
        4. +, -,
        5. <<, >>
        6. <, >, >=, <=
        7. ==, !=
        8. &
        9. ^
        10. |
        11. =, +=, -=, *=, /=, //=, %=, &=, |=, ^=
        12. not
        13. and
        14. or
"""
