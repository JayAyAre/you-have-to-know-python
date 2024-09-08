"""
    Key takeaways

        1. In Python, there is a distinction between two kinds of errors:

            syntax errors (parsing errors), which occur when the parser comes across a statement that is incorrect. 
                For example: Trying to execute the following line:

                    print("Hello, World!)

            exceptions, which occur even when a statement/expression is syntactically correct; 
                these are the errors that are detected during execution when your code results in an error which is not 
                uncoditionally fatal. For example:
                Trying to execute the following line:

                    print(1/0)

            will cause a ZeroDivisionError exception, and result in the following (or similar) message 
                being displayed in the console:

                    ZeroDivisionError: division by zero

        2. You can "catch" and handle exceptions in Python by using the try-except block.

            while True:
                try:
                    number = int(input("Enter an integer number: "))
                    print(number/2)
                    break
                except:
                    print("Warning: the value entered is not a valid number. Try again...")

        3. You can handle multiple exceptions in your code block. Look at the following examples:

            while True:
                try:
                    number = int(input("Enter an int number: "))
                    print(5/number)
                    break
                except ValueError:
                    print("Wrong value.")
                except ZeroDivisionError:
                    print("Sorry. I cannot divide by zero.")
                except:
                    print("I don't know what to do...")

        4. Some of the most useful Python built-in exceptions are: ZeroDivisionError, ValueError, TypeError,
            AttributeError, and SyntaxError. One more exception that, in our opinion, deserves your attention is
            the KeyboardInterrupt exception, which is raised when the user hits the interrupt key (CTRL-C or Delete).
            Run the code above and hit the key combination to see what happens.

        5. Last but not least, you should remember about testing and debugging your code.
            Use such debugging techniques as print debugging; if possible – ask someone to read your code and
            help you to find bugs in it or to improve it; try to isolate the fragment of code that is problematic
            and susceptible to errors: test your functions by applying predictable argument values, and try to handle
            the situations when someone enters wrong values; comment out the parts of the code that obscure the issue. Finally,
            take breaks and come back to your code after some time with a fresh pair of eyes.

        Exercise

            What is the output of the following program if the user enters 0?

                try:
                    value = int(input("Enter a value: "))
                    print(value/value)
                except ValueError:
                    print("Bad input...")
                except ZeroDivisionError:
                    print("Very bad input...")
                except:
                    print("Booo!")

        Go to project 1

        Congratulations! You have completed Module 4.

            You have learned about the following topics:

                - the defining and using of functions − their rationale, purpose, conventions, and traps;
                - the concept of passing arguments in different ways and setting their default values,
                    along with the mechanisms of returning the function's results;
                - name scope issues;
                - new data aggregates: tuples and dictionaries, and their role in data processing;
                - the concept of exceptions, and the importance of code testing and debugging.

        You've reached the end of the Python Essentials 1 course, and completed a major milestone in
            your Python programming education.

        Having completed the course, you're also prepared to attempt the qualification PCEP
            - Certified Entry-Level Python Programmer certification exam, which is an interim step to the PCAP -
            Certified Associate in Python Programming certification
"""
