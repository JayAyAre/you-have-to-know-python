"""
    Why do we need functions?

        You've come across functions many times so far, but the view on their merits that we have
            given you has been rather one-sided. You've only invoked the functions by using them as tools to make life easier,
            and to simplify time-consuming and tedious tasks.

        When you want some data to be printed on the console, you use print().
            When you want to read the value of a variable, you use input(),
            coupled with either int() or float().

        You've also made use of some methods, which are in fact functions, but declared in a very specific way.

        Now you'll learn how to write your own functions, and how to use them.

        It often happens that a particular piece of code is repeated many times in your program.
            It's repeated either literally, or with only a few minor modifications,
            consisting of the use of other variables in the same algorithm.
            It also happens that a programmer cannot resist simplifying the work,
            and begins to clone such pieces of code using the clipboard and copy-paste operations.

        1. We can now define the first condition which can help you decide when to start writing your own functions:
            if a particular fragment of the code begins to appear in more than one place,
            consider the possibility of isolating it in the form of a function

        You can try to cope with the issue by commenting the code extensively, but soon you find that this dramatically
            worsens your situation - too many comments make the code larger and harder to read.
            Some say that a well-written function should be viewed entirely in one glance.

        A good and attentive developer divides the code (or more accurately: the problem) into well-isolated pieces,
            and encodes each of them in the form of a function.

        This considerably simplifies the work of the program, because each piece of code can be encoded separately,
            and tested separately. The process described here is often called decomposition.

        2. We can now state the second condition: if a piece of code becomes so large that reading and understating
            it may cause a problem, consider dividing it into separate, smaller problems,
            and implement each of them in the form of a separate function.
"""


"""
    Descomposition

        It often happens that the problem is so large and complex that it cannot be assigned to a single developer,
            and a team of developers have to work on it. The problem must be split between several developers in a way that
            ensures their efficient and seamless cooperation.

        This kind of decomposition has a different purpose to the one described previously
             - it's not only about sharing the work, but also about sharing the responsibility among many developers.

        Each of them writes a clearly defined and described set of functions, which when combined into the module
            (we'll tell you about this a bit later) will give the final product.

        3. This leads us directly to the third condition: if you're going to divide the work among multiple programmers,
            decompose the problem to allow the product to be implemented
            as a set of separately written functions packed together in different modules.

        Where do the functions come from?

            - From python itself, numerous functions like print(), input(), len(), etc. are built-in functions. Are
                integral part of python
            - From Pythons preinstalled modules - a lot of functions very useful one.
                but used significantly less often than built-in ones like: math, os, sys, etc.
            - Directly from the programmers - functions that are written by the programmer himself. From your code
            - there is one other possibility, but it's connected with classes, so we'll omit it for now.

    NOTE

        Conditions:

            1 - If a particular fragment of the code begins to appear in more than one place, consider the possibility of
                isolating it in the form of a function
            2 - If a piece of code becomes so large that reading and understating it may cause a problem, Funtions
            3 - If you're going to divide the work among multiple programmers, decompose the problem to allow the product
                to be implemented as a set of separately written functions packed together in different modules.
"""

"""
    Your first function

        It's rather simple, but we only want it to be an example of transforming a repeating part of a code into a function.
"""

print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())

"""
        It seems that you'd have to spend some time changing all the occurrences of the message (you'd use a clipboard, of course,
            but it wouldn't make your life much easier).
            It's obvious that you'd probably make some mistakes during the amendment process.
            and you (and your boss) would get a bit frustrated.

        is it possible to separate such a repeatable part of the code, name it and make it reusable?
            It would mean that a change made once in one place would be propagated to all the places where it's used.

        You need to define it. The word define is significant here.

        This is what the simplest function definition looks like:

            def function_name(arg1, arg2, ...):
                # function_body

        We're ready to define our prompting function. We'll name it message ‒ here it is:
"""


def message():
    print("Enter a value: ")
    x = int(input())
    return x


a = message()  # This is an invocation of the function.
b = message()
c = message(c)

print(a, b, c)

"""
    How functions work

        - when you invoke a function, Python remembers the place where it happened and jumps into the invoked function;
        - the body of the function is then executed;
        - reaching the end of the function forces Python to return to the place directly after the point of invocation.

    You mustn't invoke a function which is not known at the moment of invocation.

        we will get this message:

            NameError: name 'message' is not defined

    You mustn't have a function and a variable of the same name.

    The function named message becomes unavailable.
"""
