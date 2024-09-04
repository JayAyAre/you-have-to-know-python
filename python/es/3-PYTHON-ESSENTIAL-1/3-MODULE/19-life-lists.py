"""
    The inner life of lists

        Now we want to show you one important,
            and very surprising, feature of lists, which strongly distinguishes them from ordinary variables.

        We want you to memorize it - it may affect your future programs, and cause severe problems if forgotten or overlooked.
"""

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)


"""
    The program:

        - creates a one-element list named list_1;
        - assigns it to a new list named list_2;
        - changes the only element of list_1;
        - prints out list_2

    The surprising part is the fact that the program will output: [2], not [1], which seems to be the obvious solution.

    You could say that:

        - the name of an ordinary variable is the name of its content;
        - the name of a list is the name of a memory location where the list is stored.

    The assignment: list_2 = list_1 copies the name of the array
        not its contents. In effect, the two names (list_1 and list_2) identify the same location in the computer memory.
        Modifying one of them affects the other, and vice versa.

    How do you cope with that?
"""

"""
    Powerful slices

        Fortunately, the solution is at your fingertips - its name is the slice.

        A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.
        
        This is exactly what you need. Take a look at the snippet below:

            list_1 = [1]
            list_2 = list_1[:]
            list_1[0] = 2
            print(list_2)
        
        This inconspicuous part of the code described as [:] is able to produce a brand new list.

        One of the most general forms of the slice looks as follows:

            my_list[start:end]

        NOTE: slice of this form makes a new (target) list, taking elements from the source list
            - the elements of the indices from start to end - 1.

            my_list = [10, 8, 6, 4, 2]
            new_list = my_list[1:3]
            print(new_list)

        The new_list list will have end - start (3 - 1 = 2) elements - the ones with indices equal to 1 and 2 (but not 3).
"""

print("\n\n")
# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

"""
    Slices - negative indices

        Look at the snippet below:

            my_list[start:end]

        To repeat:

            - start is the index of the first element included in the slice;
            - end is the index of the first element not included in the slice.

        This is how negative indices work with the slice.
"""

print("\n\n")
my_list = [10, 8, 6, 4, 2]
new_list = my_list[0:-1]
print(new_list)

"""
    If the start specifies an element lying further than the one described by the end
        (from the list's beginning point of view), the slice will be empty:
"""

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

"""
    if you omit the start, the start by default is 0, and if you omit the end, the end is the length of the list.
"""

print("\n\n")
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
new_list = my_list[0:]
print(new_list)

"""
    if you omit the end and the start, the slice will include all the elements of the list.
"""

print("\n\n")
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

"""
    The previously described del instruction is able to delete more than just a list's element at once - it can delete slices too:

    NOTE: in this case, the slice doesn't produce any new list!
"""

print("\n\n")
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# If you use del with slice, omiting the start and the end will delete all the elements of the list.

print("\n\n")
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# But if you dont indicate a slicing, the del instruction will delete the list itself.

print("\n\n")
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list) # Will threow an error.