"""
    Parameterized functions

        A parameter is actually a variable, but there are two important factors that make parameters different and special:

            - parameters exist only inside functions in which they have been defined
            - assigning a value to the parameter is done at the time of the function's invocation,
                by specifying the corresponding argument.

        - parameters live inside functions (this is their natural environment)
        - arguments exist outside functions, and are carriers of values passed to corresponding parameters.

                def function(number):
                    ###

            Number only will exist inside the function.

                def message(number):
                    print("Enter a number:", number)

        NOTE

            Remember: specifying one or more parameters in a function's definition is also a requirement,
                and you have to fulfil it during invocation. You must provide as many arguments as there are defined parameters.
"""


def message(number):
    print("Enter a number:", number)


# message()  # will cause an error, TypeError: message() missing 1 required positional argument: 'number'

# Example 1


def message(number):
    print("Enter a number:", number)


print("\n\n")
message(1)

#  The value of the argument used during invocation (1) has been passed into the function,
#  setting the initial value of the parameter named number.

"""
    It's legal, and possible, to have a variable named the same as a function's parameter.

    A situation like this activates a mechanism called shadowing:

        - parameter x shadows any variable of the same name, but...
        - ... only inside the function defining the parameter.

    The parameter named number is a completely different entity from the variable named number.

    A function can have as many parameters as you want
"""

# Example 2


def message(what, number):
    print("Enter", what, "number", number)


print("\n\n")
message("telephone", 11)
message("price", 5)
message("number", "number")

# Now, message function will require two arguments.

"""
    Positional parameters passing

        A technique which assigns the ith (first, second, and so on) argument to the it
            function parameter is called positional parameter passing, while arguments passed in
            this way are named positional arguments.

    NOTE

        positional parameter passing is intuitively used by people in many social occasions.
"""

# Example 1


def my_function(a, b, c):
    print(a, b, c)


print("\n\n")
my_function(1, 2, 3)

# Example 2


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


print("\n\n")
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

# But if we use it in hungary

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

# We will see an result unexpected. Its reversed.

"""
    Keyword argument passing

        Python offers another convention for passing arguments, where the meaning of the argument is
            dictated by its name, not by its position - it's called keyword argument passing.

        The position doesn't matter here - each argument's value knows its destination on the basis of the name used.

        Of course, you mustn't use a non-existent parameter name.
"""


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


print("\n\n")
introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")

"""
    Mixing positional and keyword arguments

        You can mix both fashions if you want -
            there is only one unbreakable rule: you have to put positional arguments before keyword arguments.
"""


def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


print("\n\n")
adding(1, 2, 3)
adding(1, 2, c=3)
# adding(1, b = 2, 3) will cause an error, TypeError: adding() got multiple values for argument 'c'
# Also you cant assign two values to the same parameter. adding(3, a = 1, b = 2)

"""
    More details
    
        it happens at times that a particular parameter's values are in use more often than others.
            Such arguments may have their default (predefined) value

"""


def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


print("\n\n")
introduction("James")
introduction("James", "Bond")
