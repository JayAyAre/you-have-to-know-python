"""
    Flaots

        This one data type is designe to represent and store the numbers that have
        a non-empyt fractional part.

        These may have a fractional part after a decimal point.

        for example:
            0.5
            2.342
            -32.42

        Note: you should ensure that your number doesn't contain any commas at all.
            Python will not accept that

        and you can write zero point numbers like this:
            0.4
            .4

        and the value of 4.0 can be written as:
            4.0
            4.
"""

print(3.4) # float
print(4.) # float
print(4.0) # float
print(0.5) # float
print(.5) # float
print(3000) # integer
print(3e3) # float





"""
    Ints vs. floats

        Look at these numbers:
            4
            4.0

        the decimal point is essentially importan in recognizing floating-point numbers in python.

        4 is an integer, and 4.0 is a float.

        On the other hand, it's not only points that make a float. You can also use the letter e.
        When you want to use any numbers that are very large or very small, you can
        use scientific notation.

        Take, for example, the speed of light, expressed in meters per second. Written directly
        it would look like this: 300000000.

        to avoid writing out so many zeros, we can use: 3 x 10^8
        It reads: three times ten to the power of eight.

        In python, if we want to write a number with a scientific notation, we have to use the letter 'e'.
        like this: 3e8 or 3E8

        Note:
            the exponent (the value after the E) has to be an integer;
            the base (the value in front of the E) may be an integer.
"""

print(6.62607015e-34)
print(6.62607015E-34)
print(0.0000000000000000000001) # Will print 1e-22



"""
    Coding floats

        With record that are very small numbers that are so closing to zero, like a physical constant
        like planck's constant, that is 6.62607015e-34, we can use scientific notation.

        on python, you will have to write:
            6.62607E-34
            6.62607e-34

        sometimes, python can decide to represent your numbers in that format

        Python always chooses the more economical form of the number's presentation
"""