"""
    Errors

        It seems indisputable that all programmers (including you) want to write error-free code and do their best to
            achieve this goal. Unfortunately, nothing is perfect in this world and software is no exception.
            Pay attention to the word exception as we’ll see it again very soon in a meaning that has nothing in common
            with the absolute.

        To err is human. It's impossible to make no mistakes, and it's impossible to write error-free code.

    Errors in data vs. errors in code

        Dealing with programming errors has (at least) two sides. The one appears when you get into trouble because your
            apparently correct – code is fed with bad data. For example, you expect the code will input an integer value, but
            your careless user enters some random letters instead.

        We're going to show you how to protect your code from this kind of failure and how not to provoke the user's anger.

        The other side of dealing with programming errors reveals itself when undesirable code behavior is caused by mistakes
            you made when you were writing your program.
            This kind of error is commonly called a “bug”, which is a manifestation of a well-established belief that if a program
            works badly.
"""

"""
    When data is not what it should be

        Let's write a piece of extremely trivial code – it will read a natural number (a non-negative integer) and print
            its reciprocal. In this way, 2 will turn into 0.5 (1/2) and 4 into 0.25 (1/4). Here’s the program:

"""

value = int(input('Enter a natural number: '))
print('The reciprocal of', value, 'is', 1/value)

# If we put a non-numeric value, the program will raise an exception

"""
    All the lines Python shows you are meaningful and important, but the last line seems to be the most valuable.
        The first word in the line is the name of the exception, which causes your code to stop. It's ValueError here.

    How do you deal with it? How do you protect your code from termination, the user from disappointment,
        and yourself from the user's dissatisfaction?

    The very first thought that can come to your mind is to check if the data provided by the user is valid and to
        refuse to cooperate if the data is incorrect

        type(value) is int

    But we will see on another course.

    In python, you can use the try-except block to catch exceptions and handle them in a specific way.
        "it's better to handle an error when it happens than to try to avoid it".

        - first, starting with the try keyword – this is the place where you put the code you suspect is risky and may be
            terminated in case of error; note: this kind of error is called an exception
            while the exception occurrence is called raising – we can say that an exception is (or was) raised;
        - second, the part of the code starting with the except keyword is designed to handle the exception; it's up to you what
            you want to do here

    So, we could say that these two blocks work like this:

        - the try keyword marks the place where you try to do something without permission;
        - the except keyword starts a location where you can show off your apology talents.
"""

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except:
    print('I do not know what to do.')

"""
    any part of the code placed between try and except is executed in a very special way – any error
        which occurs here won't terminate program execution. Instead, the control will immediately jump to the first line
        situated after the except keyword, and no other part of the try branch is executed;

    the code in the except branch is activated only when an exception has been encountered inside the try block.
        There is no way to get there by any other means;

    when either the try block or the except block is executed successfully, the control returns to the normal path of execution,
        and any code located beyond in the source file is executed as if nothing happened.

    How to deal with more than one exception

        The answer is obviously "no" – there is more than one possible way to raise an exception. For example,
            a user may enter zero as an input – can you predict what will happen next?

        Yes, you're right – the division placed inside the print() function invocation will raise the ZeroDivisionError.
        
        There are at least two approaches you can implement here.
"""

# Example 1, add another try-except block

try:
    value = int(input('Enter a natural number: '))
    try:
        print('The reciprocal of', value, 'is', 1/value)
    except:
        print('I do not know what to do.')
except ValueError:
    print('I do not know what to do.')

# Example 2, add another exception

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')


"""
    Two exceptions after one try

        Look at the code in the editor. As you can see, we've just introduced the second except branch.
            This is not the only difference – note that both branches have exception names specified.
            In this variant, each of the expected exceptions has its own way of handling the error, but it must
            be emphasized that only one of all branches can intercept the control – if one of the branches is executed,
            all the other branches remain idle.

        Additionally, the number of except branches is not limited, none of the exceptions can be specified more than once.
"""

"""
    The default exception and how to use it

        this time it has no exception name specified – we can say it's anonymous or (what is closer to its actual role)
            it's the default. You can expect that when an exception
            is raised and there is no except branch dedicated to this exception, it will be handled by the default branch.

        NOTE

            The default except branch must be the last except branch. Always!
"""

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')
except:
    print('Something strange has happened here... Sorry!')

"""
    Useful exceptions

        ZeroDivisionError

            This exception is raised when you try to divide a number by zero. (they are: /, //, and %)

        ValueError

            This exception is raised when you try to convert a string to a number, but the string is not a valid number.
                (they are: int() and float())

        TypeError

            This exception shows up when you try to apply a data whose type cannot be accepted in the current context.
                Look at the example:

                    short_list = [1]
                    one_value = short_list[0.5]

        AttributeError

            This exception arrives – among other occasions – when you try to activate a method which doesn't exist in an
                item you're dealing with. For example:

                    short_list = [1]
                    short_list.append(2)
                    short_list.depend(3)

        SyntaxError

            This exception is raised when you write a piece of code which is not valid. For example:

                print('Hello, world!')
                print('Hello, world!'

            The second line is not valid, because it's missing a closing quotation mark.
"""
