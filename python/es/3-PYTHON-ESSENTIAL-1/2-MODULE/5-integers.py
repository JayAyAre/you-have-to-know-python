"""
    Integers

        The computer use for storing numbers the binary system.

        The numbers handled by modern computers are of two types:

            -integers, those whcih are devoid of the fractional part
            -floating point numbers or floats, tha contain the flacional part

        The characteristic of the numeric value which determines its kind, range,
        and application, is called the type.

        If you encode a literal and place it inside Python code,
        the form of the literal determines the representation (type) Python will use to store it in the memory.

        if we write wiht a pencil a number we can represent it in this way:
            - 111.111.111
            - 111,111,111
            - 111111111
            - 111 111 111

        Python won't accept things like these, its prohibited. Python only will allow u to write:
            - 111111111
            - 111_111_111

        For negative numbers, the minus sign (-) is used to indicate that the number is negative.
        for example:
            -111111111
            -111_111_111

        The following lines describe the same number: +11111111 and 11111111
"""

print(0o123) # Octal numbers
print(0O123) # Octal numbers
print(0x123) # Hexadecimal numbers
print(0X123) # Hexadecimal numbers

# To convert a number from octal to decimal, you can use the following formula:

print(int("0o123", 8)) # Octal numbers
print(int("0O123", 16)) # Octal numbers



"""
    Integers: octal and hexadecimal numbers

        There are two additional conventionns in python that are unknown to the world of mathematics.
        1 - Octal numbers

        if an integer is preceded by '0o' or '0O' it will be tracted as an octal number.
        it means that the number only and must contain digits between 0 and 7 inclusive.
        0o123 is an octal number with a (decimal) value equal to 83.



        2 - Hexadecimal numbers

        such numbers are preceded by '0x' or '0X'.
        0x123 is a hexadecimal number with a (decimal) value equal to 291
"""