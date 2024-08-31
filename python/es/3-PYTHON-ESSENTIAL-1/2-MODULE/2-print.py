"""
    The print() function - instructions

        Python's syntax is quite specific in this area. Unlike most programming languages,
        Python requires that there cannot be more than one instruction in a line.
"""


print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")


"""
    This is a good opportunity to make some observations:

        -the program invokes the print() function twice, and you can see two separate lines in the console -
            this means that print() begins its output from a new line each time it starts its execution;
        -each print() invocation contains a different string, as its argument and the console content reflects it -
            this means that the instructions in the code are executed in the same order that they have been written;

"""

print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")


"""
    We have added an empty print() function invocation.
    it will print a new line each time it is executed.

"""

print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")


"""
    We have modified the code again, now, we've added a strange pair of characters:
    they are these characters:
        '\n'
    This character have two parts
        '\'
        'n'
    The first one is called the escape character. The word escape should be understood specifically.
    By itself dont mean anything in itself,  but is only a kind of announcement,
    that the next character after the backslash has a different meaning too.

    in this case, the letter 'n' placed after the backslash comes from the word 'new line'.
    so, this will print a new line each time it is executed.

    Both the backslash and the n form a special symbol named a newline character,
    which urges the console to start a new output line.

"""

# print("\")
print("\\")



"""
    Always remember that '\' is the escape character.  So if we want to print a backslash, we need to write '\\'
"""

print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

"""
    Here we are going to see what happens if we add multiple arguments to the print() function.
    for that we are going to use the comma character.

    the print function will to print all the arguments separated by the default separator, which oen is
    a space character.

    a print() function invoked with more than one argument outputs them all on one line;
    the print() function puts a space between the outputted arguments on its own initiative.

"""

print("My name is", "Python.")
print("Monty Python.")

"""
    The way in which we are passing the arguments into the print() function is called
    the positional way. The first argument will print first, the second argument second, and so on.
"""

print("My name is", "Python.", end=" ")
print("Monty Python.")


"""
    Python offers another way to pass rthe arguments to the print() function, the keyword arguments.
    these arguments is taken not from its location (position) but from the special word (keyword)
    used to identify them.

    now if we see, there are three arguments in the first print() function call,
    the first two arguments are strings, and have they are positional arguments.
    the third argument is a keyword argument, and it is called 'end'.

        -a keyword argument consists of three elements: a keyword identifying the argument (end here);
        -an equal sign (=); and a value assigned to that argument;
        -any keyword arguments have to be put after the last positional argument (this is very important)

    the 'end' keyword argument is used to specify the end of the string that will be printed.
    by default is a new line, like '\n', in this case we are using the 'end' keyword argument with ' '

    Note: no newlines have been sent to the output.
"""

print("My", "name", "is", "Monty", "Python.", sep="-")

"""
    Now we will see another keyword argument, this one is called 'sep'.
    the 'sep' keyword argument is used to specify the separator between the arguments on
    the print function output.

    in this case, we are using the '-' character as a separator. While by default, the separator
    is a space.

    the output of the print() function will be:
        My-name-is-Monty-Python.
"""

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

"""
    Both keyword arguments can be used together in one invocation of the print() function.

    the output of the print() function will be:
        My_name_is*Monty*Python.*

    Now, go to LAB-2
"""

