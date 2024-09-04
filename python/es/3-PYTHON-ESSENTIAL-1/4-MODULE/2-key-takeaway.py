"""
    Key takeaways

        1. A function is a block of code that performs a specific task when the function is called (invoked).
            You can use functions to make your code reusable,
            better organized, and more readable. Functions can have parameters and return values.

        2. There are at least four basic types of functions in Python:

            - built-in functions, which are built into the language and are available to use without importing anything;
                https://docs.python.org/3/library/functions.html.
            - functions defined in the pre-installed modules;
            - functions defined by the user;
            - lambda functions.

        3. You can define your own function using the def keyword and the following syntax:

                def your_function(optional parameters):
                    # the body of the function

            You can define a function which doesn't take any arguments, e.g.:

                def message():    # defining a function
                    print("Hello")    # body of the function

                message()    # calling the function

            You can define a function which takes arguments, too, just like the one-parameter function below:

                def hello(name):    # defining a function
                    print("Hello,", name)    # body of the function


                name = input("Enter your name: ")

                hello(name)    # calling the function

        Exercise 1

            The input() function is an example of a:

                a) user-defined function
                b) built-in function

        Exercise 2

            What happens when you try to invoke a function before you define it? Example:

                hi()

                def hi():
                print("hi!")

        Exercise 3

            What will happen when you run the code below?

                def hi():
                    print("hi")

                hi(5)
"""
