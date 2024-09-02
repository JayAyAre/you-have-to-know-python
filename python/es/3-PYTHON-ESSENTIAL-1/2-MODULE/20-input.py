"""
    Input function

        The input function is a mirror reflection of the prrint function.

        Why? well, print sends data to the console. Input reads data from the console.

        Virtually all programs read and process data. A program which doesn't get a user's input is a deaf program.

            print("Tell me anything...")
            anything = input()
            print("Hmm...", anything, "... Really?")

        NOTE

            - the code prompts the user to input some data from the console
            - the input function will switch the console to input mode
            - you need to asign the input to a variable
            - we show the input data in the console
"""

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

"""
    The input() function with an argument

        The input() function can do something else: it can prompt the user without any help from print().

            anything = input("Tell me anything...")
            print("Hmm...", anything, "...Really?")

    NOTE

        - the input() function is invoked with one argument - it's a string containing a message;
        - the message will be displayed on the console before the user is given an opportunity to enter anything;
        - input() will then do its job.
        - the result of the input() function is a string.
"""

anything = input("Enter a number: ")
something = anything ** 2.0 # We will get an error if we don't convert the input to a float/int
print(anything, "to the power of 2 is", something)

"""
    The input() function - prohibited operations

        you tried to apply the ** operator to 'str' (string) accompanied with 'float'.

        This should be obvious - can you predict the value of "to be or not to be" raised to the power of 2?
        We can't. Python can't either.

    Type casting

        Python offers two simple functions to specify a type of data and solve this problem - here they are: int() and float().

        Their names are self-commenting:

            - int() converts a string to an integer, takes one argument and tries to convert it to an integer.
                if it fails, the program will fail too.
            - float() converts a string to a float, takes one argument and tries to convert it to a float.
                if it fails, the program will fail too.

        Now, if we use that function, we can solve the previous error.
"""

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

"""
    String operators - introduction

        + and * have a second function. They are able to do something more than just add and multiply.

    Concatenation

        The + operator when is applied to two strings, concatenates them.
        becomes a contatenation operator.

            string1 + string2
"""
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

"""
    Replication

        The * operator when is applied to a string, replicates it.

            string * number
            number * string

        It replicates the string the same number of times specified by the number.

        For example:

            - "James" * 3
            - 3 * "an"
            - 5 * "2"

        NOTE

            A number less than or equal to zero, produces an empty string.
"""

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

"""
    Type conversion: str()

        You already know how to use the int() and float() functions to convert a string into a number.

        This type of conversion is not a one-way street. You can also convert a number into a string
        A function capable of doing that is called str():

            str(number)

    The "right-angle triangle" again

    Go to LAB-9
"""