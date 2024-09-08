"""
    Dictionaries

        Is another python data structure, which is a collection of key-value pairs.
            It's not a sequence type (but can be easily adapted to sequence processing) and it is mutable.

        The Python dictionary works in the same way as a bilingual dictionary. For example, you have an English word
            (e.g., cat) and need its French equivalent. You browse the dictionary in order to find the word
            and eventually you get it. Next, you check the French counterpart and it is (most probably) the word "chat".
        
        In Python's world, the word you look for is named a key. The word you get from the dictionary is called a value.

        This means that a dictionary is a set of key-value pairs. NOTE:

            - each key must be unique - it's not possible to have more than one key of the same value;
            - a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
            - a dictionary is not a list - a list contains a set of numbered values, while a dictionary holds pairs of values;
            - the len() function works for dictionaries, too - it returns the numbers of key-value elements in the dictionary;
            - a dictionary is a one-way tool - if you have an English-French dictionary, you can look for French equivalents
                of English terms, but not vice versa.


"""

# How to make a dictionary?

print("\n\n")

dictionary = {
    "apple": "aaa",
    "cat": "chat",
    "dog": "chien",
    "horse": "cheval",
    "aaas": "aasa"
}

phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# The list of pairs is surrounded by curly braces, while the pairs themselves are separated by commas, and the keys and values by colons.

"""
    Have you noticed anything surprising? The order of the printed pairs is different than in the initial assignment.
        What does that mean?

        First of all, it's a confirmation that dictionaries are not lists - they don't preserve the order of their data,
            as the order is completely meaningless. The order in which a dictionary stores its data is completely out of your control, 
            and your expectations.

        NOTE

            In Python 3.6x dictionaries have become ordered collections by default. Your results may vary depending on what Python version you're using.
"""

# How to use a dictionary?

print("\n\n")
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary["cat"])
print(dictionary["dog"])

"""
    Getting a dictionary's value resembles indexing, especially thanks to the brackets surrounding the key's value.

    NOTE:

        - if the key is a string, you have to specify it as a string; (1234 is not the same as "1234")
        - keys are case-sensitive: 'Suzy' is something different from 'suzy'.
        - dont use a non-existent key - it will raise an error. (You can use a if with in)
"""

print("\n\n")
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

"""
    NOTE:

        When you write a big or lengthy expression, it may be a good idea to keep it vertically aligned.
            This is how you can make your code more readable and more programmer-friendly, e.g.:
"""

# Example 1:
dictionary = {
    "cat": "chat",
    "dog": "chien",
    "horse": "cheval"
}

# Example 2:
phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310
                 }

# This kind of formatting is called a hanging indent.


"""
    keyword Keys

        Can dictionaries be browsed using the for loop, like lists or tuples?

            No and yes.

        No, because a dictionary is not a sequence type - the for loop is useless with it.

        Yes, because there are simple and very effective tools that can adapt any dictionary to the for loop requirements

        The first of them is a method named keys(), possessed by each dictionary.
            The method returns an iterable object consisting of all the keys gathered within the dictionary.
"""

print("\n\n")
dictionary = {"swedeen": "suecia", "cat": "chat",
              "dog": "chien", "horse": "cheval"}
for key in dictionary.keys():
    print(key)

"""
    sorted

        Do you want it sorted? You can use the sorted() function to sort a dictionary.
"""

print()
for key in sorted(dictionary.keys()):
    print(key)

"""
    Items

        Another way is using the items() method, which returns a list of tuples, each of which contains a key-value pair.
"""

print()
for key, value in dictionary.items():
    print(key, "->", value)

"""
    Also there is the method values(), which returns a list of values.
"""

print()
for value in dictionary.values():
    print(value)

"""
    Modyfing a dictionary

        Assigning a new value to an existing key is simple - as dictionaries are fully mutable,
            We're going to replace the value "chat" with "minou".
"""

print()
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)

"""
    Adding a new key

        Adding a new key-value pair to a dictionary is as simple as changing a value - you only have to assign a value to a new,
        previously non-existent key.

"""

print()
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)

# With update() method

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({'swan': 'cygne'})
print(dictionary)
dictionary.update({'swan': 'hello'})
print(dictionary)

"""
    Removing a key

        NOTE removing a key will always cause the removal of the associated value. Values cannot exist without their keys.
"""

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# Will cause a error if you try to delete a non-existent key
del dictionary['dog']
print(dictionary)

"""
    NOTE

        To remove the last item in a dictionary, you can use the popitem() method
"""

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

key, value = dictionary.popitem()
print(key, value)
print(dictionary)
