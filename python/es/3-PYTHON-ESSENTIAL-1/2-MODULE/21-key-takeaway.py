"""
    Key takeaways

        1. The print() function sends data to the console, while the input() function gets data from the console.

        2. The input() function is a mirror reflection of the print() function.
            the prompt string. It allows you to write a message before the user input, e.g.:

                name = input("Enter your name: ")
                print("Hello, " + name + ". Nice to meet you!")

        3. 3. When the input() function is called, the program's flow is stopped, the prompt symbol keeps blinking
            (it prompts the user to take action when the console is switched to input mode) until the
            user has entered an input and/or pressed the Enter key.

        4. The result of the input() function is a string. You can add strings to each other using the concatenation (+) operator.
            Check out this code:

                num_1 = input("Enter the first number: ") # Enter 12
                num_2 = input("Enter the second number: ") # Enter 21

                print(num_1 + num_2) # the program returns 1221

        5. You can also multiply (* ‒ replication) strings, e.g.:

                my_input = input("Enter something: ") # Example input: hello
                print(my_input * 3) # Expected output: hellohellohello

        Exercise 1

            What is the output of the following snippet?

                x = int(input("Enter a number: ")) # The user enters 2
                print(x * "5")

        Exercise 2

            What is the expected output of the following snippet?

                x = input("Enter a number: ") # The user enters 2
                print(type(x))

     you've covered and got familiar with in Module 2:

        - the basic methods of formatting and outputting data offered by Python,
            together with the primary kinds of data and numerical operators, their mutual relations and bindings;
        - the concept of variables and variable naming conventions;
        - the assignment operator, the rules governing the building of expressions;
        - the inputting and converting of data;

"""