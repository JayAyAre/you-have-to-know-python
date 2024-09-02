"""
    Greater than operator

        You can also ask a comparison question using the > (greater than) operator.
        
        black_sheep > white_sheep  # Greater than

        True confirms it; False denies it.

"""

var = 2 > 1
print(var)

"""
    Greater than or equal to operator

        The greater than operator has another special, non-strict variant, but it's denoted
            differently than in classical arithmetic notation: >= (greater than or equal to).

        are binary operators with left-sided binding, and their priority is greater than that shown by == and !=.

        centigrade_outside ≥ 0.0  # Greater than or equal to

        on python its equivalent to:
            centigrade_outside >= 0.0

"""

var = 2 >= 1
print(var)

"""
    Comparison operators: less than or equal to

        As you've probably already guessed, the operators used in this case are: the < (less than) operator and its non-strict sibling:
            <= (less than or equal to).

        current_velocity_mph < 85  # Less than
        current_velocity_mph ≤ 85  # Less than or equal to
"""

var = 2 <= 1
print(var)

"""
    Making use of the answers

        There are at least two possibilities: first, you can memorize it (store it in a variable) and make use of it later.

        for example:

            var = 2 <= 1
            print(var)

        The second possibility is more convenient and far more common: you can use the answer you get to make a decision about the
            future of the program

        Now we need to update our priority table, and put all the new operators into it. It now looks as follows:

            1 - +, - unary
            2 - **
            3 - *, /, %, //
            4 - +, - binary
            5 - >=, <=, <, >
            6 - ==, !=
        
        Go LAB-1
"""