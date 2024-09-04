"""
    The in and not in operators

        Python offers two very powerful operators, able to look through the list in order to check whether
            a specific value is stored inside the list or not.

        These operators are:

            elem in my_list
            elem not in my_list

        The first of them (in) checks if a given element (its left argument) is currently stored somewhere
            inside the list (the right argument) - the operator returns True in this case.

        The second (not in) checks if a given element (its left argument) is absent in a list -
            the operator returns True in this case.
"""

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

"""
    Lists - some simple programs

        Now we want to show you some simple programs utilizing lists.

        The first of them tries to find the greater value in the list. Look at the code in the editor.
"""

print("\n\n")
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13, 32]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

# Rewritten

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13, 32]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

# If you want to save computer power:

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13, 32]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)

# Lets find the location of a given value in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
else:
    print("absent")

if found:
    print("Element found at index", i)

"""
    - the target value is stored in the to_find variable;
    - the current status of the search is stored in the found variable (True/False)
    - when found becomes True, the for loop is exited.

    Now, Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.

    The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.

    The question is: how many numbers have you hit?
"""

list_1 = [5, 11, 9, 42, 3, 49]
list_2 = [3, 7, 11, 42, 34, 49]

hits = 0
for number in list_1:
    if number in list_2:
        hits += 1

print(hits)

# Go to LAB-14