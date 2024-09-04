"""
    Computer logic

        Have you noticed that the conditions we've used so far have been very simple, not to say, quite primitive?
        Let's look at this sentence:

            If we have some free time, and the weather is good, we will go for a walk.

        We've used the conjunction and, which means that going for a walk depends on the simultaneous fulfilment of
            these two conditions. in the language of logic, such a connection of conditions is called a conjunction.

        If we use 'or', this will be the connection between the two conditions, and depend of one of both conditions
            being fulfilled, but not necessarily both. This is called a disjunction.

        It's clear that Python must have operators to build conjunctions and disjunctions.
            Without them, the expressive power of the language would be substantially weakened
            they are called logical operators.

    AND

        One logical operator is the 'and' operator, which means that the two conditions must be fulfilled simultaneously.
        It's a binary operator with a priority that is lower than the one expressed by the comparison operators.

            counter > 0 and value == 100

        The result provided by the 'and' operator can be determined on the basis of the truth table

        if we consider the conjuntion 'A and B', the result is True if both A and B are True, otherwise it's False.
"""

print("AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()

"""
    OR

        A disjunction operator is the word 'or', and have lower priority than and operator.
            This operator means that only one of the two conditions or both must be fulfilled.

        will give True if one of the two conditions is True, Only will give False if both conditions are False.
"""

print("OR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()

"""
    NOT

        The not operator is unary, performing a logical negation

        This operator is written as the word not, and its priority is very high: the same as the unary + and -

        His result is the opposite of the input.
"""