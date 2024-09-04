"""
    Key takeaways

        1. You can pass information to functions by using parameters. Your functions can have as many parameters as you need.

            One parameter:

                def hi(name):
                    print("Hi,", name)

                hi("Greg")

            Two parameters:

                def hi(first_name, last_name):
                    print("Hi,", first_name, last_name)

                hi("Greg", "Smith")

        2. You can pass arguments to a function using the following techniques:

                - positional argument passing in which the order of arguments passed matters (Ex. 1),
                - keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2),
                - a mix of positional and keyword argument passing (Ex. 3).

                    Ex. 1
                    def subtra(a, b):
                        print(a - b)

                    subtra(5, 2)    # outputs: 3
                    subtra(2, 5)    # outputs: -3


                    Ex. 2
                    def subtra(a, b):
                        print(a - b)

                    subtra(a=5, b=2)    # outputs: 3
                    subtra(b=2, a=5)    # outputs: 3

                    Ex. 3
                    def subtra(a, b):
                        print(a - b)

                    subtra(5, b=2)    # outputs: 3
                    subtra(5, 2)    # outputs: 3

            It's important to remember that positional arguments mustn't follow keyword arguments.
                That's why if you try to run the following snippet:

                    subtra(a=5, 2)    # Syntax Error

        3. You can use the keyword argument passing technique to pre-define a value for a given argument:

                def name(first_name, last_name="Smith"):
                    print(first_name, last_name)

                name("Andy")    # outputs: Andy Smith
                name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")

        Exercise 1

            What is the output of the following snippet?

                def intro(a="James Bond", b="Bond"):
                    print("My name is", b + ".", a + ".")

                intro()

        Exercise 2

            What is the output of the following snippet?

                def intro(a="James Bond", b="Bond"):
                    print("My name is", b + ".", a + ".")

                intro(b="Sean Connery")

        Exercise 3

            What is the output of the following snippet?

                def intro(a, b="Bond"):
                    print("My name is", b + ".", a + ".")

                intro("Susan")

        Exercise 4

            What is the output of the following snippet?

                def add_numbers(a, b=2, c):
                    print(a + b + c)

                add_numbers(a=1, c=3)
"""
