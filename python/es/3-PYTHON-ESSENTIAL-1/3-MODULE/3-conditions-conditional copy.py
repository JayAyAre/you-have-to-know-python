"""
    Conditions and conditional execution

        You already know how to ask Python questions, but you still don't know how to make reasonable use of the answers.
            You have to have a mechanism which will allow you to do something if a condition is met, and not do it if it isn't.

        Python offers a special instruction. Due to its nature and its application, it's called a conditional instruction

        if true_or_not:
            do_this_if_true

        If the true_or_not expression represents the truth, the indented block of code is executed.
        if the true_or_not expression does not represent the truth, the indented block of code is not executed.

            if the_weather_is_good:
                go_for_a_walk()
            have_lunch()
"""

n = 100
if n >= 100:
    print("The number is greater than or equal to 100")
print("hello")

"""
    Conditional execution: the if statement

        if sheep_counter >= 120: # Evaluate a test expression
            sleep_and_dream() # Execute if test expression is True

        You can read it as: if sheep_counter is greater than or equal to 120, then fall asleep and dream
            (i.e., execute the sleep_and_dream function.)

        We've said that conditionally executed statements have to be indented. This creates a very legible structure.

    Conditional execution: the if-else statement

        We can say, for example: If the weather is good, we will go for a walk, otherwise we will go to a theater.

        Now we know what we'll do if the conditions are met, and we know what we'll do if not everything goes our way

        Python allows us to express such alternative plans. This is done with a second
            slightly more complex form of the conditional statement, the if-else statement:

            if true_or_false_condition:
                perform_if_condition_true
            else:
                perform_if_condition_false

        If the true_or_false_condition is True, the indented block of code is executed. and the else's block is not executed.
        if the true_or_false_condition is False, the indented block of code is not executed and the else's block is executed.

        Now lets test this:

            if the_weather_is_good:
                if nice_restaurant_is_found:
                    have_lunch()
                else:
                    eat_a_sandwich()
            else:
                if tickets_are_available:
                    go_to_the_theater()
                else:
                    go_shopping()

        this use of the if statement is known as nesting; remember that every else refers to the if which lies at the same
            indentation level; you need to know this to determine how the ifs and elses pair up;
        
        consider how the indentation improves readability, and makes the code easier to understand and trace.

"""

n = 100
if n >= 100:
    print("The number is greater than or equal to 100")
else:
    print("The number is less than 100")

"""
    The elif statement

        The second special case introduces another new Python keyword: elif. As you probably suspect,
            it's a shorter form of else if.

        elif is used to check more than just one condition, and to stop when the first statement which is true is found.

        Have you noticed how many times we've used the word otherwise? This is the stage where the elif keyword plays its role.

        if the_weather_is_good:
            go_for_a_walk()
        elif tickets_are_available:
            go_to_the_theater()
        elif table_is_available:
            go_for_lunch()
        else:
            play_chess_at_home()

        At the previous example, we've used some if, elifs, and else statements.
            our program will executes the first condition which is True, and will stop there.
            If any of the conditions is False, the program will continue to the next condition, and so on.
            until the last statement, which one is else.

        NOTE

            - you mustn't use else without a preceding if;
            - else is always the last branch of the cascade, regardless of whether you've used elif or not;
            - else is an optional part of the cascade, and may be omitted;
            - if there is an else branch in the cascade, only one of all the branches is executed;
            - if there is no else branch, it's possible that none of the available branches is executed.

"""



# Example 1

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)



# Example 2

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# NOTE if any of the if-elif-else branches contains just one instruction, you may code it in a more compact way



# Exmaple 3

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

"""
    Pseudocode and introduction to loops

        Now you know to find the largest number between some numbers, but what happens if you have
            two thousand numbers to check?

        we'll try to write the algorithm, and when we're happy with it, we'll implement it.
        for that, we will use pseudocode, which is a way to write the algorithm in a more abstract way.

            largest_number = -999999999
            number = int(input())
            if number == -1:
                print(largest_number)
                exit()
            if number > largest_number:
                largest_number = number
            # Go to line 02

        Performing a certain part of the code more than once is called a loop. The meaning of this term is probably obvious to you.
            Lines 02 through 08 make a loop. We'll pass through them as many times as needed to review all the entered values.

        NOTE

            python often comes with a lot of built-in functions, which are called "built-in" because they are already built into the language.
                there is one built-in function which is called "max()" and it returns the largest value of a list of numbers.
"""

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)

"""
    By the same fashion, you can use the min() function to return the lowest number.
        You can rebuild the above code and experiment with it in the Sandbox.

    Go to LAB-2, 3, and 4
"""