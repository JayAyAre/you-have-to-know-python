"""
    Sequence types and mutability

        Before we start talking about tuples and dictionaries, we have to introduce two important concepts: sequence types
            and mutability.

        A sequence type is a type of data in Python which is able to store more than one value (or less than one, as a
            sequence may be empty),
            and these values can be sequentially (hence the name) browsed, element by element.

        a sequence is data which can be scanned by the for loopself.

        mutability is a property of any of Python's data that describes its readiness to be freely changed during program execution.
            There are two kinds of Python data: mutable and immutable.

            Mutable data can be freely updated at any time - we call such an operation in situ.

            list.append(1)

        Immutable data cannot be modified in this way.

        Imagine that a list can only be assigned and read over. You would be able neither to append an element to it,
            nor remove any element from it

        The data type we want to tell you about now is a tuple. A tuple is an immutable sequence type.
            It can behave like a list, but it mustn't be modified in situ.

    tuples

        The first and the clearest distinction between lists and tuples is the syntax used to create them - tuples prefer to
            use parenthesis, whereas lists like to see brackets, although it's also possible to create a tuple just
            from a set of values separated by commas.
"""

print("\n\n")
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
print(tuple_1)
print(tuple_2)

# each tuple element may be of a different type

# How we can create them? like this

tuple_1 = ()

# With one element

tuple_1 = (1, )
tuple_1 = 1,

"""
    How to use a tuple?

        The similarities may be misleading - don't try to modify a tuple's contents! It's not a list!

        However, we can access to the tuples to read them and see the inside value
"""

print("\n\n")
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)


# my_tuple.append(10000) ERROR
# del my_tuple[0] ERROR
# my_tuple[1] = -10 ERROR
# AttributeError: 'tuple' object has no attribute 'append'

"""
    What else can tuples do for you?

        the len() function accepts tuples, and returns the number of elements contained inside;
        the + operator can join tuples together (we've shown you this already)
        the * operator can multiply tuples, just like lists;
        the in and not in operators work in the same way as in lists.
"""

print("\n\n")
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)

"""
    One of the most useful tuple properties is their ability to appear on the left side of the assignment operator.
        You saw this phenomenon some time ago, when it was necessary to find an elegant tool to swap two variables' values.
"""

print("\n\n")
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)

#   NOTE the example presents one more important fact: a tuple's elements can be variables, and the can be expressions

print("\n\n")

a = 10
b = 20
c = 5

my_tuple = (a, b, c * 2, a + b, b - c)

print(my_tuple)

my_list = [a, b, c * 2, a + b, b - c]
print(my_list)
