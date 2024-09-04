"""
    Fucntions vs methods
    
        A method is a specific kind of function - it behaves like a function and looks like a function,
            but differs in the way in which it acts, and in its invocation style.

        A function doesn't belong to any data - it gets data, it may create new data and it (generally) produces a result.

        A method does all these things, but is also able to change the state of a selected entity.

        A method is owned by the data it works for, while a function is owned by the whole code.

            FUNCTION
                result = function(arg)

            METHOD
                result = data.method(arg)

        NOTE

            Note: the name of the method is preceded by the name of the data which owns the method. Next, you add a dot,
                followed by the method name, and a pair of parenthesis enclosing the arguments.

            it can change the internal state of the data from which it has been invoked.
"""

# FUNCTION

print(len("Hello, world!"))

# METHOD

print("Hello, world!".upper())

"""
    Adding elements to a list: append() and insert()

        A new element may be glued to the end of the existing list:

            list.append(value)

        is performed by a method named append(). It takes its argument's value and puts it at the end of the list

        The insert() method is a bit smarter, it can add a new element at any place in the list

            list.insert(location, value)
"""
print("\n\n")
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

numbers.insert(1, 333)
print(numbers)

"""
    You can start a list's life by making it empty
        and then adding new elements to it as needed.

"""

print("\n\n")
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

"""
    Making use of lists

        The for loop has a very special variant that can process lists very effectively - let's take a look at that

        Let's assume that you want to calculate the sum of all the values stored in the my_list list.

        you need a variable whose sum will be stored and initially assigned a value of 0 - its name will be total.
            (Note: we're not going to name it sum as Python uses the same name for one of its built-in functions - sum()
            Using the same name would generally be considered a bad practice.)
            Then you add to it all the elements of the list using the for loop. Take a look at the snippet in the editor.
"""

my_list = [10, 1, 8, 3, 5]
total = 0

# Way 1

for i in range(len(my_list)):
    total += my_list[i]

print(total)
print(sum(my_list))

# Way 2

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

"""
    Lists in action

        Let's leave lists aside for a short moment and look at one intriguing issue.
        
        Imagine that you need to rearrange the elements of a list, i.e., reverse the order of the elements: the first and the
            fifth as well as the second and fourth elements will be swapped. The third one will remain untouched.

        Question: how can you swap the values of two variables?

        Take a look at the snippet:
"""

variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2


"""
    If you do something like this, you would lose the value previously stored in variable_2.
    Changing the order of the assignments will not help. You need a third variable that serves as an auxiliary storage.
"""

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

"""
    Python offers a more convenient way of doing the swap - take a look:
"""
# Example 1

variable_1 = 1
variable_2 = 2
variable_1, variable_2 = variable_2, variable_1

# Example 2

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Example 3

my_list = [10, 1, 8, 3, 5]
print(my_list)

for i in range(len(my_list) // 2):
    my_list[i], my_list[len(my_list) - i - 1] = my_list[len(my_list) - i - 1], my_list[i]

print(my_list)

# Go to LAB-13
