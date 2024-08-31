
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

"""
    Exponentiation

        A ** operator is an exponentiation operator, its left arguments is the base
        and its right argument is the exponent.

        Note: we've surrounded the double asterisks with spaces in our examples.
        It's not compulsory, but it improves the readability of the code.

    NOTE It's possible to formulate the following rules based on this result:

        - when both ** arguments are integers, the result is an integer, too;
        - when at least one ** argument is a float, the result is a float, too.
"""
print()
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)


"""
    Multiplication

        A * operator is a multiplication operator. Its left argument is the multiplicand,
        its right argument is the multiplier.

        our rule keep working:
        - when both * arguments are integers, the result is an integer, too;
        - when at least one * argument is a float, the result is a float, too.

"""

print()
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

"""
    Division

        A / operator is a division operator. Its left argument is the dividend,
        its right argument is the divisor.

        The result produced by the division operator is always a float,
"""

print()
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print(-6 // 4)
print(6. // -4)
print(-6 / 4)
print(6. / -4)
"""
    Integer division

        A // operator is an integer division operator. Its left argument is the dividend,
        its right argument is the divisor.

        It deffers from the standard / operator in two ways:
            - its result lacks the fractional part - it's absent (for integers),
                or is always equal to zero (for floats);
                this means that the results are always rounded;
            - it conforms to the integer vs float rule

        NOTE rounding always goes to the lesser integer.

        Now, if we try to divide with one value negative, we are going to remember that
        we always round to the lesser integer.
        So, if we divide -6 by 4, we get -2, not -1.

        NOTE
        Integer division can also be called floor division.
        You will definitely come across this term in the future.
"""
print()
print(14 % 4)
print(12 % 4.5)

"""
    Modulo or remainder

        A % operator is a modulo operator. Its left argument is the dividend,
        its right argument is the divisor.

        The result of the operator is a remainder left after the integer division.

        NOTE the operator is sometimes called modulo in other programming languages.

        14 // 4 gives 3 → this is the integer quotient;
        3 * 4 gives 12 → as a result of quotient and divisor multiplication;
        14 - 12 gives 2 → this is the remainder.

        12 // 4.5 gives 2 → this is the integer quotient;
        2 * 4.5 gives 9.0 → as a result of quotient and divisor multiplication;
        12 - 9.0 gives 3.0 → this is the remainder.

        NOTE the module operator keeps following the same rule

        As you probably know, division by zero doesn't work.

            Do not try to:

                - perform a division by zero; => 5 / 0 gives an error;
                - perform an integer division by zero; => 5 // 0 gives an error;
                - find a remainder of a division by zero. => 5 % 0 gives an error.
"""

print()
print(-4 + 4)
print(-4. + 8)

"""
    Addition

        A + operator is an addition operator. Its left argument is the summand,
        its right argument is the addend.

        our rule keep working-

"""

print()
print(6 - 3)
print(6 - 3.)
print(6. - 3)
print(6. - 3.)
print(-3)
print(-3.)

"""
    The subtraction operator, unary and binary operators

        The subtraction operator is obviously the - (minus)
        you should note that this operator also has another meaning
        - it can change the sign of a number.

        This is a great opportunity to present a very important distinction
        between unary and binary operators.

        the minus operator expects two arguments:
        the left (a minuend in arithmetical terms) and right (a subtrahend).

        Our rule keep working
"""