"""
    Why do we need lists?

        It may happen that you have to read, store, process, and finally, print dozens, maybe hundreds,
            perhaps even thousands of numbers. Do you need to create a separate variable for each value?

            var1 = int(input())
            var2 = int(input())
            var3 = int(input())
            var4 = int(input())
            var5 = int(input())
            var6 = int(input())

        If you don't think that this is a complicated task, then take a piece of paper and write a program that:

        reads five numbers,
        prints them in order from the smallest to the largest (NB, this kind of processing is called sorting).

        Think of how convenient it would be to declare a variable that could store more than one value
            For example, a hundred, or a thousand or even ten thousand. It would still be one and the same variable

        We'll show you how to declare such multi-value variables.
            We'll write a program that sorts a sequence of numbers.

        Let's create a variable called numbers; it's assigned with not just one number,
            but is filled with a list consisting of five values (note: the list starts with an open square bracket
            and ends with a closed square bracket; the space between the brackets is filled with five numbers separated by commas).

        numbers = [10, 5, 7, 2, 1]

        numbers is a list consisting of five values, all of them numbers.

        The elements inside a list may have different types. Some of them may be integers, others floats, and yet others may be lists.

        Python has adopted a convention stating that the elements in a list are always numbered starting from zero.
            This means that the item stored at the beginning of the list will have the number zero.

        Before we go any further in our discussion, we have to state the following: our list is a collection of elements,
            but each element is a scalar.
"""

"""
    Indexing lists

        Let's assign a new value of 111 to the first element in the list. We do it this way:
"""

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content: ", numbers)  # Current list content.

# And now we want the value of the fifth element to be copied to the second element - can you guess how to do it?

numbers[1] = numbers[4]
print("New list content: ", numbers)  # Current list content.

# The value inside the brackets which selects one element of the list is called an index
# while the operation of selecting an element from the list is known as indexing.
# NOTE any expression can be the index, not only integers.

"""
    Accessing list content

        Each of the list's elements may be accessed separately. For example, it can be printed:

            print(numbers[0])

        if you want to print all the elements of the list, you can use the following syntax:

            print(numbers)

        The len() function

            The length of a list may vary during execution. New elements may be added to the list
                This means that the list is a very dynamic entity.

            If you want to check the list's current length, you can use a function named len() (its name comes from length).

            The function takes the list's name as an argument, and returns the number of elements currently stored

                len(numbers)

            The function len() is very useful when you want to check the length of a list.

"""

print("\nList length:", len(numbers))  # Printing the list's length.

"""
    Removing elements from a list

        Any of the list's elements may be removed at any time - this is done with an instruction named del (delete).
        NOTE: it's an instruction, not a function.

            del numbers[1]
            print(len(numbers))
            print(numbers)

        You can't access an element which doesn't exist -
            you can neither get its value nor assign it a value. Both of these instructions will cause runtime errors now:
"""

del numbers[1]
print("New list's length:", len(numbers))
print("\nNew list content:", numbers)

"""
    Negative indices are legal

        It may look strange, but negative indices are legal, and can be very useful.
        An element with an index equal to -1 is the last one in the list.

            print(numbers[-1])

        Similarly, the element with an index equal to -2 is the one before last in the list.

        The last accessible element in our list is numbers[-4] (the first one) - don't try to go any further!
"""

numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-len(numbers)])

# Go to LAB-12