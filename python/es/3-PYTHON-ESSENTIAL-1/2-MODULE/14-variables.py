"""
    What are variables?

        it's quite a normal question to ask how to store the results of these operations,
            in order to use them in other operations, and so on.

        Python will help us to keep and save the results of these operations on specials
            "boxes" called variables. The contents of these variables can be changed
            in the course of the program.

        What does every Python variable have?

            a name;
            a value (the content of the container)

        You must also name them.

        If you want to give them a name, you must follow some strict rules:
            1 - The name of the variable must be composed of upper-case or lower-case letter,
                digits, and the character underscore (_);
            2 - The name of the variable must begin wit a letter
            3 - the underscore character is a letter
            4 - upper- and lower-case letters are treated as different
            5 - the name of the variable must not be any of Python's reserved words

    Correct and incorrect variable names

        Note that the same restrictions apply to function names.

        Python does not impose restrictions on the length of variable names,
        but that doesn't mean that a long variable name is always better than a short one.

        The next ones, are some incorrect variable names:
            - 10t => Doesn't start with a letter
            - Exchange rate => Contains a space
            - Adiós_señora => This wont cause an error, but it's not a good name because
                by convention, the best way and language to encoded is on english alphabet.

        NOTE

        The PEP 8 -- Style Guide for Python Code recommends the following naming
            convention for variables and functions in Python:

            - variable names should be lowercase, with words separated by underscores to improve readability
                like: var, variable_name, my_variable, etc.
            - function names follow the same convention.
            - It's also possible to use mixed cade like myVariable, but only in contexts where that's
                already the prevailing style, to retain backwards compatibility with the adopted convention.

    Keywords

        Take a look at the list of words that play a very special role in every Python program.

            ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
            'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

        They are called keywords or (more precisely) reserved words. They are reserved because you mustn'ot use them as
            name, neither as a variable name, nor as a function name.

    Creating variables

        What can you put inside a variable? Anything.

        Let's talk now about two important things - how variables are created,
            and how to put values inside them (or rather - how to give or pass values to them).

    NOTE

        A variable comes into existence as a result of assigning a value to it.
        If you assign any value to a nonexistent variable, the variable will be automatically created.

        The creation is extremely simple: just use the name of the desired variable, then the equal sign (=),
            and then the value you want to assign to it.

"""

var = 1
print(var)

"""
    It consists of two simple instructions:

        - The first of them creates a variable named var, and assigns a literal with an integer value equal to 1.
        - The second prints the value of the newly created variable to the console.

    NOTE

        print() has yet another side to it - it can handle variables too.
            Do you know what the output of the snippet will be? It will be 1.
"""

"""
    Using variables

        You're allowed to use as many variable declarations as you need to achieve your goal, like this:

        like:
            var = 1
            account_balance = 1000.0
            client_name = 'John Doe'
            print(var, account_balance, client_name)
            print(var)

        You're not allowd to use a variable which doesn't exist, this will cause an error.

        like:
            var = 1
            print(var_2)

    NOTE

        You can use the print() function and combine text and variables using the + operator.

        like:

            var = "3.8.5"
            print("Python version is " + var)

    Assigning a new value to an already existing variable

        How do you assign a new value to an already created variable? In the same way.
            You just need to use the equal sign. The equal sign is in fact an assignment operator.
"""

var = 1
print(var)
var = var + 1
print(var)

"""
        The code will send two lines to the console:
            - the first one will print the value of the variable var, which is 1;
            - the second one will print the value of the variable var, which is 2.
"""
