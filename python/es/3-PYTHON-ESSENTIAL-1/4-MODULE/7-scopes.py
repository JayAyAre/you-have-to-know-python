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
    var = 3
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

"""
    in other words,  this name becomes global (it has a global scope, and it doesn't matter whether
        it's the subject of read or assign).

"""
