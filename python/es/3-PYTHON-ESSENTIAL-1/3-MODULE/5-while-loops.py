"""
    Looping your code with while

        while there is something to do
            do it

        That is the basic structure of a while loop.

        In general, in python a loop can be represented as follows:

            while conditional_expression:
                instruction

        If you notice some similarities to the if instruction, that's quite all right.
            Indeed, the syntactic difference is only one: you use the word while instead of the word if.

        The semantic difference is more important: when the condition is met, if performs its statements only once;
            while repeats the execution as long as the condition evaluates to True.

        NOTE
            all the rules regarding indentation are applicable here, too. We'll show you this soon.


"""

i = 0
while i < 10:
    print(i)
    i += 1

"""
    An infinite loop

        An infinite loop, also called an endless loop, is a sequence of instructions in a program which repeat
            indefinitely (loop endlessly.)

        while True:
            print("I'm stuck inside a loop.")

        This loop will infinitely print "I'm stuck inside a loop." on the screen.
"""
# Example 1

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)



# Example 2

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)



# Example 3 using a counter

counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)



# Example 4

counter = 5
while counter: # If counter is zero, the loop is not executed.
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# Go to LAB-5
