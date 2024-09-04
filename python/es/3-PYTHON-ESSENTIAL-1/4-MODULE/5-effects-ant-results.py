"""
    Effects and results: the return instruction

        Of course, functions - like their mathematical siblings - may have results.

        To get functions to return a value (but not only for this purpose) you use the return instruction.

        The return instruction has two different variants - let's consider them separately.

    return without an expression

        When used inside a function, it causes the immediate termination of the function's execution,
            and an instant return (hence the name) to the point of invocation.

        NOTE

            When used inside a function, it causes the immediate termination of the function's execution,
                and an instant return (hence the name) to the point of invocation.
"""

print("\n\n")


def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        # the return instruction will cause its termination just before the wishes.
        return

    print("Happy New Year!")


happy_new_year()
happy_new_year(False)

"""
    return with an expression
        The second return variant is extended with an expression:

        def function():
            return expression

    There are two consequences of using it:

        - it causes the immediate termination of the function's execution (nothing new compared to the first variant)
        - moreover, the function will evaluate the expression's value and will return (hence the name once again)
            it as the function's result.
"""

print("\n\n")


def boring_function():
    return 123


x = boring_function()

print("The boring_function has returned its result. It's:", x)

"""
    The only disadvantage is that the result has been irretrievably lost.

    Dont forget:

        - you are always allowed to ignore the function's result, and be satisfied with the function's effect
            (if the function has any)

        - if a function is intended to return a useful result, it must contain the second variant of the return instruction.
"""

"""
    A few words about None

        Its data doesn't represent any reasonable value - actually, it's not a value at all;
            hence, it mustn't take part in any expressions.

        NOTE

            None is a keyword.

        There are only two kinds of circumstances when None can be safely used:

            - when you assign it to a variable (or return it as a function's result)
            - when you compare it with a variable to diagnose its internal state.

        value = None
        if value is None:
            print("Sorry, you don't carry any value")

        Don't forget this: if a function doesn't return a certain value using a return expression clause,
            it is assumed that it implicitly returns None.
"""

print("\n\n")

# Example 1


def return_none():
    return None


x = return_none()

if x == None:
    print("The return_none function has returned its result. It's:", x)
print("The return_none function has returned its result. It's:", x)  # None

# Example 2


def return_none2():
    print("Hello!")


print(return_none2())

# Example 3


def strange_function(n):
    if (n % 2 == 0):
        return True


print(strange_function(6))
print(strange_function(5))

"""
    lists and functions

        There are two additional questions that should be answered here.

        The first is: may a list be sent to a function as an argument?
            Of course it may! Any entity recognizable by Python can play the role of a function argument
        
        So, if you pass a list to a function, the function has to handle it like a list.
"""

print("\n\n")


def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s


# You shouldn't put an non-list argument to this function.
print(list_sum([5, 4, 3]))

# This is caused by the fact that a single integer value mustn't be iterated through by the for loop.

"""
    The second question is: may a list be a function result?

        Yes, of course! Any entity recognizable by Python can be a function result.
"""

print("\n\n")


def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_list_fun(5))

# Go to LAB-1 until LAB-5, both included.
