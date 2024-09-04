"""
    Binary left shift and binary right shift

        Python offers another operation relating to single bits: shifting. This is applied
            only to integer values.

        You already apply this operation very often and quite unconsciously.
            How do you multiply any number by ten? Take a look:

            12345 * 10 = 123450

        As you can see, multiplying by ten is in fact a shift of all the digits to the left
            and filling the resulting gap with zero.

        Division by ten? Take a look:

            12345 / 10 = 1234

        Dividing by ten is nothing but shifting the digits to the right.

        The same kind of operation is performed by the computer, but with one difference:
            as two is the base for binary numbers (not 10)
            shifting a value one bit to the left thus corresponds to multiplying it by two;
            shifting one bit to the right is like dividing by two

        The shift operators in python are a pair of digraphs: << and >>.

            value << bits
            value >> bits

        The left argument of these operators is an integer value whore bits are shifted.
            The right argument is the number of bits to be shifted.

        17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8
        17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68
"""

var = 17
var_right = var >> 1
var_left = var << 1
print(var, var_left, var_right)