"""
    Factorials

        Another function is factorials, an factorial is this:

            0! = 1
            1! = 1
            2! = 1 * 2
            3! = 1 * 2 * 3
            ...

        its marked with an exclamation mark, and is equal to the product
            of all natural numbers from one up to its argument
"""


def factorial_function(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return None
    else:
        total = 1
        for i in range(2, n+1):
            total *= i
        return total


n = 3
print(n, factorial_function(n))

"""
    Fibonacci numbers

        They are a sequence of integer numbers build using a very simple rule

            -the first element of the sequence is equal to one (Fib1 = 1)
            -the second is also equal to one (Fib2 = 1)
            -every subsequent number is the the_sum of the two preceding numbers:
                (Fibi = Fibi-1 + Fibi-2)

        What do you think about implementing this as a function?
"""


def fibonacci_iterations(iterations):
    if iterations < 1:
        return None
    elif iterations < 3:
        return 1
    fib_1 = fib_2 = 1
    for i in range(3, iterations + 1):
        fib_1, fib_2 = fib_2, fib_2 + fib_1
    return fib_2


for n in range(1, 10):  # testing
    print(n, "->", fibonacci_iterations(n))

"""
    Analyze the for loop body carefully,
        and find out how we move the elem_1 and elem_2
        variables through the subsequent Fibonacci numbers.
"""


"""
    Recursion

        This term may describe many different concepts, but one of them is especially interesting - 
            the one referring to computer programming.

        In this field, recursion is a technique where a function invokes itself.

        The Fibonacci numbers definition is a clear example of recursion. We already told you that:

            Fibi = Fibi-1 + Fibi-2
"""


def fib_recursive(n):
    if n < 1:
        return None
    elif n < 3:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Factorial recursive


def recursive_factorial(n):
    if n < 0:
        return None
    elif n < 1:
        return 1
    else:
        return recursive_factorial(n - 1) * n


print(recursive_factorial(3))
