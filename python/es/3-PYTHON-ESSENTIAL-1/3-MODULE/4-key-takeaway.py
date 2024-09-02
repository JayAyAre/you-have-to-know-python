"""
    Key takeaway

        1. The comparison operators are used to compare values.

        2. When you want to execute some code only if a certain condition is met, you can use a conditional statement:

            a single if statement, e.g.:

                x = 10

                if x == 10: # condition
                    print("x is equal to 10")  # Executed if the condition is True.
            
            a series of if statements, e.g.:

                x = 10

                if x > 5: # condition one
                    print("x is greater than 5")  # Executed if condition one is True.

                if x < 10: # condition two
                    print("x is less than 10")  # Executed if condition two is True.

                if x == 10: # condition three
                    print("x is equal to 10")  # Executed if condition three is True.
           
            Each if statement is tested separately.

            an if-else statement, e.g.:

                x = 10

                if x < 10:  # Condition
                    print("x is less than 10")  # Executed if the condition is True.

                else:
                    print("x is greater than or equal to 10")  # Executed if the condition is False.

            a series of if statements followed by an else, e.g.:

                x = 10

                if x > 5:  # True
                    print("x > 5")

                if x > 8:  # True
                    print("x > 8")

                if x > 10:  # False
                    print("x > 10")

                else:
                    print("else will be executed")

            Each if is tested separately. The body of else is executed if the last if is False.


            The if-elif-else statement, e.g.:

                x = 10

                if x == 10:  # True
                    print("x == 10")

                if x > 15:  # False
                    print("x > 15")

                elif x > 10:  # False
                    print("x > 10")

                elif x > 5:  # True
                    print("x > 5")

                else:
                    print("else will not be executed")

            Nested conditional statements, e.g.:

                x = 10

                if x > 5:  # True
                    if x == 6:  # False
                        print("nested: x == 6")
                    elif x == 10:  # True
                        print("nested: x == 10")
                    else:
                        print("nested: else")
                else:
                    print("else")

        Exercise 1

            What is the output of the following snippet?

                x = 5
                y = 10
                z = 8

                print(x > y)
                print(y > z)

        Exercise 2

            What is the output of the following snippet?

                x, y, z = 5, 10, 8

                print(x > z)
                print((y - 5) == x)

        Exercise 3

            What is the output of the following snippet?

                x, y, z = 5, 10, 8
                x, y, z = z, y, x

                print(x > z)
                print((y - 5) == x)

        Exercise 4

            What is the output of the following snippet?

                x = 10

                if x == 10:
                    print(x == 10)
                if x > 5:
                    print(x > 5)
                if x < 10:
                    print(x < 10)
                else:
                    print("else")

        Exercise 5

            What is the output of the following snippet?

                x = "1"

                if x == 1:
                    print("one")
                elif x == "1":
                    if int(x) > 1:
                        print("two")
                    elif int(x) < 1:
                        print("three")
                    else:
                        print("four")
                if int(x) == 1:
                    print("five")
                else:
                    print("six")

        Exercise 6

            What is the output of the following snippet?

                x = 1
                y = 1.0
                z = "1"

                if x == y:
                    print("one")
                if y == int(z):
                    print("two")
                elif x == y:
                    print("three")
                else:
                    print("four")


"""