"""
    Key takeaways

        1. A variable is a named location reserved to store values in the memory. A variable is created or
            initialized automatically when you assign a value to it for the first time.

        2. Each variable must have a unique name - an identifier A legal identifier name must be a non-empty sequence of characters,
            must begin with the underscore(_), or a letter, and it cannot be a Python keyword.
            The first character may be followed by underscores, letters, and digits. Identifiers in Python are case-sensitive.

        3. Python is a dynamically-typed language, which means you don't need to declare variables in it.
            you can use a simple assignment operator in the form of the equal (=) sign, i.e., var = 1.

        4. You can also use compound assignment operators (shortcut operators) to modify values assigned to variables,
            var += 1, var -= 1, var *= 1, var /= 1, var %= 1, var **= 1, var //= 1.

        5. You can assign new values to already existing variables using the assignment operator or one of the compound operators

            var = 2
            print(var)

            var = 3
            print(var)

            var += 1
            print(var)

        6.  You can combine text and variables using the + operator, and use the print()

            var = "007"
            print("Agent " + var)

        Exercise 1

            What is the output of the following snippet?

                var = 2
                var = 3
                print(var)

        Exercise 2

            Which of the following variable names are illegal in Python?

                my_var
                m
                101
                averylongvariablename
                m101
                m 101
                Del
                del

        Exercise 3

            What is the output of the following snippet?

                a = '1'
                b = "1"
                print(a + b)

        Exercise 4

            What is the output of the following snippet?

                a = 6
                b = 3
                a /= 2 * b
                print(a)

"""