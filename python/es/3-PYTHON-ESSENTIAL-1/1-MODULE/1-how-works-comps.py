"""

How does a computer program work?

    A program makes a computer usable, without a program, a computer is nothing more than a object.
        like a piano without his player.

    Computer are able to perform very complex tasks but this isn't innate. They only can very simple
    operations. A computer can't understant by itself what is the meaning of a mathematical equation.

    A computer can compute the average speed during a long journey, but it is necesary to instruct
    the computer how to do it. This is done by writing a program.

        - Accept a number representing the distance traveled.
        - Accept a number representing the time spent traveling.
        - Divide the former value by the latter and store the result in a variable.
        - display the result.

    This four steps make a program. Language is the keyword.



Natural Language vs Programming Language

    Computers have their own language, too, called machine language, which is very rudimentary.

    A complete set of known commands is called an instruction list, sometimes abbreviated to IL.
    Different types of computers may vary depending on the size of their ILs,
    and the instructions could be completely different in different models.



What makes a language?

    We can say that each language consist of the following elements:
        -an alphabet: a set of symbols used to build words of a certain language
        -a lexis: set of words the language offers its users
        -a syntax: a set of rules used to determine if a certain string of words forms a valid sentence
        -semantics: a set of rules determining if a certain phrase makes sense

    The IL is, in fact, the alphabet of a machine language.

    Such languages are often called high-level programming languages.
    They are at least somewhat similar to natural ones in that they use symbols,
    words and conventions readable to humans.
    These languages enable humans to express commands to computers that are much more complex than
    those offered by ILs.

    A program written in a high-level programming language is called a source code. Similarly, the file
    containing the source code is called a source file.



Compilation vs. interpretation

    such a composition has to be correct in many senses:
        -alphabetically - a program need to be written in a recognizable script.
        -lexically - each programming language has its dictionary and you need to master it; thankfully,
            it's much simpler and smaller than the dictionary of any natural language;
        -syntactically - each language has its rules and they must be obeyed;
        -semantically - the program has to make sense.

    Once a program is written, you have to translate it into machine language, the computer can done it by itself.
    making the whole process fast and efficient.

    There are two ways of transforming a program from a high-level language into machine language:
        -Compilation: the source program is translated once (however, this act must be repeated each time you modify the source code)
            by getting a file (e.g., an .exe file if the code is intended to be run under MS Windows)
            containing the machine code; now you can distribute the file worldwide;
            the program that performs this translation is called a compiler or translator;

        -Interpretation: You can translate the source code each time it has to be run;the program performing this kind of transformation
        is called an interpreter, as it interprets the code every time it is intended to be executed; it also means that you
        cannot just distribute the source code as-is, because the end-user also needs the interpreter to execute it.



What does the interpreter actually do?

    Let's assume once more that you have written a program. Now, it exists as a computer file:
    a computer program is actually a piece of text, so the source code is usually placed in text files.
    It has to be written in pure text.

    The interpreter reads the source code in a way that is common in Western culture:
    from top to bottom and from left to right. There are some exceptions - they'll be covered later in the course.

    You may ask now: which is better? The "compiling" model or the "interpreting" model? There is no obvious answer. If there had been,
    one of these models would have ceased to exist a long time ago. Both of them have their advantages and their disadvantages.

    Python is an interpreted language. This means that it inherits all the described advantages and disadvantages.
    Of course, it adds some of its unique features to both sets.

    If you want to program in Python, you'll need the Python interpreter. You won't be able to run your code without it.
    Fortunately, Python is free. This is one of its most important advantages.

    Due to historical reasons, languages designed to be utilized in the interpretation manner are often called scripting languages,
    while the source programs encoded using them are called scripts.



What is python?

    Python is a widely-used, interpreted, object-oriented, and high-level programming language
    with dynamic semantics, used for general-purpose programming.

    The name "python" come from a BBC television series called "Monty Python's Flying Circus".

Who created Python?

    One of the amazing features of Python is the fact that it is actually one person's work.
    Python was created by Guido van Rossum, born in 1956 in Haarlem, the Netherlands. Of course,
    Guido van Rossum did not develop and evolve all the Python components himself.


Python goals

    In 1999, Guido van Rossum defined his goals for Python:

    -an easy and intuitive language just as powerful as those of the major competitors;
    -open source, so anyone can contribute to its development;
    -code that is as understandable as plain English;
    -suitable for everyday tasks, allowing for short development times

    Python isn't a young language anymore. It is mature and trustworthy, Python is a very good investment.

What makes Python special?

    - it's easy to learn
    - it's easy to teach
    - it's easy to use for writing new software
    - it's easy to understand
    - it's easy to obtain, install and deploy

    Of course, Python has its drawbacks, too:

        - it's not a speed demon - Python does not deliver exceptional performance;
        - in some cases it may be resistant to some simpler testing techniques
             - this may mean that debugging Python code can be more difficult than with other languages;
             fortunately, making mistakes is also harder in Python.



    Python rivals

    Python has to direct rivals, with comparable properties and pedispositions, These are:
        - Perl - A scripting languange
        - Ruby - A scripting language

    Where can wee see python in action?

        We see it every day and almost everywhere, its used for internet services, like
        tools, cloud storage, social media, etc.

        Many developing tools are written in Python, and more anr more are written in python
        every day.


    Why not python?
        Python is growing popularity, but there are still some niches where python is absent or
        is rarely seen:
            - Low level programming:  if you want to implement an extremely effective driver or graphical engine,
                you wouldn't use Python;
            - Application for mobile devices: although this territory is still waiting to be conquered by Python,
                it will most likely happen someday.

    Note: We recommend use python 3, because this is the current python version.


    CPython
        Is one of a possible number of solutions to the most painful of python's traits:
        the lack of efficiency. Large and complex mathematical computations are fast and easy to encoded
        in python but the resulting code execution may be extremely time-consuming.

    Jython
        "J" is for "Java". Imagine a Python written in Java instead of C. This is useful, for example,
        if you develop  large and complex systems written entirely in Java and want
        to add some Python flexibility to them.

        Jython can communicate with existing Java infrastructure more effectively.
        This is why some projects find it useful and necessary.

    There are many more different Pythons in the world.
    You'll find them if you look, but this course will focus on CPython.
"""