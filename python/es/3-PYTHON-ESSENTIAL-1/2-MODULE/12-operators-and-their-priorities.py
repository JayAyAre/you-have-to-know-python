print(2 + 3 * 5)

"""

    Operators and their priorities

        Also, you will very often find more than one operator in one expression,
        and then this presumption is no longer so obvious.

        Consider the following expression:

            2 + 3 * 5

        You probably remember from school that multiplications precede additions.

        The phenomenon that causes some operators to act before others is known as
        the hierarchy of priorities.
"""
print()
print(9 % 6 % 2)

"""
    Operators and their bindings

        The binding of the operator determines the order of computations performed by some
        operators with equal priority, put side by side in one expression.

        Most of Python's operators have left-sided binding, which means that the
        calculation of the expression is conducted from left to right.

        print(9 % 6 % 2)

        There are two possible ways of evaluating this expression:

            - from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1; => Correct
            - from right to left: first 6 % 2 gives 0, and then 9 % 0 causes a fatal error.
"""

print()
print (2 ** 2 ** 3)

"""
    Operators and their bindings: Exponentiation

        The exponentiation operator ** has right-sided binding.

        print(2 ** 2 ** 3)

        The two possible results are:

            - 2 ** 2 → 4; 4 ** 3 → 64
            - 2 ** 3 → 8; 2 ** 8 → 256 => Correct

        The result clearly shows that the exponentiation operator uses right-sided binding.
"""

print(2 * 3 % 5)

"""
    List of priorities from the highest (1) to the lowest (4) priorities.

        1	**
        2   +, -, (unary)
        3   *, /, //, %
        4   +, -, (binary)

    print(2 * 3 % 5) => 1
"""


"""
    Operators and parentheses

        Of course, you're always allowed to use parentheses, which can change the natural order of a calculation.
        You can use as many parentheses as you need, and they're often used to improve the readability of an expression
        
        An example of an expression with multiple parentheses is here:

            print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
"""