"""
    Functions and scopes

        The scope of a name (e.g., a variable name) is the part of a code where the name is properly recognizable.

        For example, the scope of a function's parameter is the function itself. The parameter is inaccesible outside the function.
"""

# Example 1


def scope_test():
    x = 123


scope_test()
# print(x)    # NameError: name 'x' is not defined

"""
    Now lets see trying to access the variable x inside the function scope_test().

    The answer will be: a variable existing outside a function has a scope inside the functions' bodies.

    but this rule has a very important exception
"""


def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

# Lets change it

print("\n\n")


def my_function2():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function2()
print(var)

"""
    What's happened?

        - the var variable created inside the function is not the same as when defined outside it -
            it seems that there two different variables of the same name;
        - moreover, the function's variable shadows the variable coming from the outside world.

    NOTE

        our rule will be:
            A variable existing outside a function has a scope inside the functions' bodies,
            excluding those of them which define a variable of the same name.

            It also means that the scope of a variable existing outside a function is supported only when getting
            its value (reading). Assigning a value forces the creation of the function's own variable.
"""

"""
    Global keyword

        you should now have arrived at the following question: does this mean that a function is not able to modify
            a variable defined outside it? This would create a lot of discomfort.

        There's a special Python method which can extend a variable's scope in a way which includes the functions' bodies
        Such an effect is caused by a keyword named global:
"""

print("\n\n")


def my_function():
    global var
    var = 2223
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

"""
    in other words,  this name becomes global (it has a global scope, and it doesn't matter whether
        it's the subject of read or assign).

    This should be sufficient evidence to show that the global keyword does what it promises.
"""

"""
    How the function interacts with its arguments

        Run the program and check.
"""

print("\n\n")


def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)  # Will print 1

# Exmaple 2

print("\n\n")


def my_function2(n):
    global var_2
    print("I got", var_2)
    var_2 += 1
    print("I have", var_2)


var_2 = 1
my_function2(var_2)
print(var_2)  # Will print 1

"""
    The conclusion is obvious - changing the parameter's value doesn't propagate outside the function
    (in any case, not when the variable is a scalar, like in the example).

    This also means that a function receives the argument's value, not the argument itself. This is true for scalars.

    But with collection of values, the function receives the collection itself.
"""

print("\n\n")


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


"""
    On the previous example, we tried to modify the list my_list_2 inside the function.
    This is not possible, because the list is passed by value.

    but lets see what happens if we try to delete.
"""

print("\n\n")


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

"""
    NOTE

        Can you explain it?

        Lets try it:

            - if the argument is a list, then changing the value of the corresponding parameter doesn't affect the list
                (remember: variables containing lists are stored in a different way than scalars).
            - but if you change a list identified by the parameter (note: the list, not the parameter!),
                the list will reflect the change.

        In conclusion:

            - Scalars
                - are passed by value
                - are not modified by the function
                - If we use the global keyword, the variable is modified
            - Lists
                - are passed by reference
                - are modified by the function
                - but if we assign another value to the parameter, the original list is not modified
                    (Because is referecing another list our parameter, if we modified the list itself
                    will be reflected in the original list)

"""
