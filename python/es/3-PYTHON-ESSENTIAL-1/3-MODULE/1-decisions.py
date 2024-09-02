"""
    Questions and answers

        A computer executes a program and provides the answes
            The program must be able to react according to the received answers.

        The computer only will kno two kinds of answers:
            Yes, this is True;
            No, this is False.

        To ask questions, Python uses a set of very special operators

    Comparison: equality operator

        Question: are two values equal?

        To ask this question, you use the == (equal equal) operator.

    = is the asignment operator, it will assign the value of 'b' to 'a'
    == is the equality operator, it will compares if 'a' is equal to 'b'

        Question #1: What is the result of the following comparison?

            2 == 2 # this is True

        Question #2: What is the result of the following comparison?

            2 == 2. # this is True

        Question #3: What is the result of the following comparison?

            1 == 2 # this is False

        The == (equal to) operator compares the values of two operands. If they are equal,
        the result of the comparison is True. If they are not equal, the result of the comparison is False.
"""

var = 2 == 2.0
print(var)

var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

"""
    Inequality operator

        The != (not equal to) operator compares the values of two operands,
        too. Here is the difference: if they are equal, the result of the comparison is False, otherwise it is True.
"""

var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)