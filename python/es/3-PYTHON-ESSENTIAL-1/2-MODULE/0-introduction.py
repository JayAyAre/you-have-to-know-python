"""

    Now, on module 2 we will learn about Data types, variables, basic input/output, and the basics operators

    we will learn:
        -how to write and run simple Python programs;
        -what Python literals, operators, and expressions are;
        -what variables are and what are the rules that govern them;
        -how to perform basic input and output operations.
"""
my_list = [1, 2]
for v in range(2):
    my_list.insert(-1, my_list[v])
print(my_list)

foo = (1, 2, 3)
foo.index(0)
