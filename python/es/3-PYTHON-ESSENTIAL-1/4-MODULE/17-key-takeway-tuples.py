"""
    Key takeaways: tuples

        1.  Tuples are ordered and unchangeable (immutable) collections of data.
            They can be thought of as immutable lists. They are written in round brackets:

                my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
                print(my_tuple)

                my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
                print(my_list)

        2. You can create an empty tuple like this:

                my_tuple = ()
                print(my_tuple)

                or

                my_tuple = tuple()
                print(my_tuple)

        3. A one-element tuple may be created as follows:

                one_elem_tuple_1 = ("one", )    # Brackets and a comma.
                one_elem_tuple_2 = "one",       # No brackets, just a comma.

        4. You can access tuple elements by indexing them:

                my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
                print(my_tuple[3])    # outputs: [3, 4]

        5. Tuples are immutable

                my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
                my_tuple[2] = "guitar"    # The TypeError exception will be raised.

            However, you can delete a tuple as a whole:

                my_tuple = 1, 2, 3,
                del my_tuple
                print(my_tuple)    # NameError: name 'my_tuple' is not defined

        6. You can loop through a tuple elements,
            check if a specific element is (not)present in a tuple,
            use the len() function to check how many elements there are in a tuple
            or even join/multiply tuples.

                # Example 1
                tuple_1 = (1, 2, 3)
                for elem in tuple_1:
                    print(elem)

                # Example 2
                tuple_2 = (1, 2, 3, 4)
                print(5 in tuple_2)
                print(5 not in tuple_2)

                # Example 3
                tuple_3 = (1, 2, 3, 5)
                print(len(tuple_3))

                # Example 4
                tuple_4 = tuple_1 + tuple_2
                tuple_5 = tuple_3 * 2

                print(tuple_4)
                print(tuple_5)

        NOTE

            You can also create a tuple using a Python built-in function called tuple()

                my_tuple = tuple((1, 2, "string"))
                print(my_tuple)

                my_list = [2, 4, 6]
                print(my_list)    # outputs: [2, 4, 6]
                print(type(my_list))    # outputs: <class 'list'>
                tup = tuple(my_list)
                print(tup)    # outputs: (2, 4, 6)
                print(type(tup))    # outputs: <class 'tuple'>

            By the same fashion, when you want to convert an iterable to a list, you can use a
                Python built-in function called list():

"""
