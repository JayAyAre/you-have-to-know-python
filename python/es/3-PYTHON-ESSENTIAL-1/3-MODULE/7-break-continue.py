"""
    The break and continue statements

        So far, we've treated the body of the loop as an indivisible and inseparable sequence of instructions
            that are performed completely at every turn of the loop. However, as developer,
            you could be faced with the following choices:

            - it appears that it's unnecessary to continue the loop as a whole; you should refrain from
                execution of the loop's body and go further;
            - it appears that you need to start the next turn of the loop without completing the execution of the
                correct turn

        Python provides two special instructions for the implementation of both these tasks.
            an experienced programmer is able to code any algorithm without these instructions.
            Such additions, which don't improve the language's expressive power, but only simplify the developer's work,
            are sometimes called "syntactic candy" or "syntactic sugar".

        These two instructions are:

            - the break statement, which is used to terminate the execution of the loop;
            - the continue statement, which is used to skip the rest of the loop's body and go to the next turn.

        Both these words are keywords.
"""

# Example 1

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

# Example 2

largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

# Go to LAB-7, LAB-8, LAB-9