"""
    Leaving comments in code: why, how, and when

        You may want to put in a few words addressed not to Python but to humans. This can be
        to used in the code workflow to explain what the code is doing, or to provide a
        reminder of what the code is doing. Comments are a great way to do this.

        This is omitted at runtime and is called a comment.

        In python, a comment is a piece of text that begins with a hash (#)

        you can do it just like this:
"""

# This program evaluates the hypotenuse c.
# a and b are the lengths of the legs.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of square root.
print("c =", c)

"""
        responsible developers describe each important piece of code

        but in the other hand, we must do things some define not ambiguous variable names
        at the time of writing the code. the name square_area will obviously be better than aunt_jane.

        The first name is self-commenting, the second is not.
"""

# This is a test program.
x = 1
y = 2
# y = y + x
print(x + y)

"""
        NOTE

            If you want to quickly comment or uncomment multiple lines, select the lines and use CTRL + /
            on windows, or CMD + / on macOS.

        Go LAB-8
"""