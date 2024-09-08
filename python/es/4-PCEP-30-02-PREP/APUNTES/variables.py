# La prioridad de los operadores es la siguiente:

"""
    1. ~, +, - unary, not
    2. **
    3. *, /, //, %, and
    4. +, -, or
    5. <<, >>
    6. <, >, >=, <=
    7. ==, !=
    8. &
    9. |
    10. =, +=, -=, *=, /=, //=, %=, &=, |=, ^=

"""

# Recordemos que la division de //, redondea hacia abajo siempre
print(5 // 2)
print(5.5 // 2)

# Ademas que la division siempre dara un float, y todas las demas operaciones, daran un float, si al
# menos una de las dos variables es un float

print()
print(5 // 2.0)
print(5.5 // 2.0)
print(5 // 2)
