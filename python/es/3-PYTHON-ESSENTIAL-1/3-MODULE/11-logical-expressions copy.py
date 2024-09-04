"""
    Logical expressions

        Let's create a variable named var and assign 1 to it. The following conditions are pairwise equivalent:
"""
var = 1
# Example 1:
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))

"""
    You may be familiar with De Morgan's laws. They say that:

    The negation of a conjunction is the disjunction of the negations.

    The negation of a disjunction is the conjunction of the negations.

    Let's write the same thing using Python:

    not (p and q) == (not p) or (not q)
    not (p or q) == (not p) and (not q)
"""

"""
    Logical values vs. single bits

        Logical operators take their arguments as a whole regardless of how many bits they contain.
        The operator are aware only of two values: True and False.
            will be false if are the bits are 0, and true if at least one of the bits is 1.

"""

i = 1
j = not not i
print(i, j)

"""
    NOTE

    Bitwise operators

        However, there are four operators that allow you to manipulate single bits of data. They are called bitwise operators.

        They cover all the operations we mentioned before in the logical context, and one additional operator.
            This is the xor (as in exclusive or) operator, and is denoted as ^ (caret).

            & (ampersand) - bitwise conjunction;
            | (bar) - bitwise disjunction;
            ~ (tilde) - bitwise negation;
            ^ (caret) - bitwise exclusive or (xor).

        Let's make it easier:

            & requires exactly two 1s to provide 1 as the result;
            | requires at least one 1 to provide 1 as the result;
            ^ requires exactly one 1 to provide 1 as the result.

        Let us add an important remark: the arguments of these operators must be integers; we must not use floats here.

        The difference in the operation of the logical and bit operators is important: the logical operators do not penetrate
            into the bit level of its argument. They're only interested in the final integer value.

        Bitwise operators are stricter: they deal with every bit separately
"""

"""
    Logical vs bit operations continued

        Lest assume we have these two variables:

            i = 15
            j = 22

        If we assume that the integers are stored with 32 bits, the bitwise image of the two variables will be as follows:

            i: 00000000000000000000000000001111
            j: 00000000000000000000000000010110

        The assignment is given:

            log = i and j

        This is the result:

            log = True

        But if we do it with a bit operator:

            log = i & j

        the result is:

            log = 00...00110
            log = 6

        Each of these two-argument operators can be used in abbreviated form.

            x = x & y	x &= y
            x = x | y	x |= y
            x = x ^ y	x ^= y
"""

i = 15
j = 22
log = i & j
print(log)

log = i | j
print(log)

log = i ^ j
print(log)

print("\n\n")
"""
    How do we deal with single bits?

        We'll now show you what you can use bitwise operators for.

            flag_register = 0x1234

        Each bit of the variable stores one yes/no value. You've also been told that only one of these bits is yours - the third
            (remember that bits are numbered from zero, and bit number zero is the lowest one, while the highest is number 31).
            The remaining bits are not allowed to change, because they're intended to store other data. Here's your bit marked
            with the letter x:

            flag_register = 0000000000000000000000000000x000

        tasks:

            1. Check the state of your bit, you want to find out the value of your bit

                    x & 1 = x
                    x & 0 = 0

                If you apply the & operation to the flag_register variable along with the following bit image:

                    00000000000000000000000000001000

                (note the 1 at your bit's position) as the result, you obtain one of the following bit strings:

                    00000000000000000000000000001000 if your bit was set to 1
                    00000000000000000000000000000000 if your bit was set to 0

                Such a sequence of zeros and ones, whose task is to grab the value or to change the selected bits,
                    is called a bit mask.

                Let's build a bit mask to detect the state of your bit. It should point to the third bit.
                    That bit has the weight of 23 = 8. A suitable mask could be created by the following declaration:

                    the_mask = 8

                    if flag_register & the_mask:
                        # My bit is set.
                    else:
                        # My bit is reset.

            2. Reset your bit - you assign a zero to the bit while all the other bits must remain unchanged;
                let's use the same property of the conjunction as before, but let's use a slightly different mask - exactly as below:

                    11111111111111111111111111110111

                Note that the mask was created as a result of the negation of all the bits of the_mask variable.
                    Resetting the bit is simple, and looks like this (choose the one you like more):

                    flag_register = flag_register & ~the_mask
                    flag_register &= ~the_mask
"""

# Task 1

flag_register = 0x1234 # in binary form: 0001001000110100
the_mask = 8 # in binary form: 1000

if flag_register & the_mask:
    print("My third bit is 1.")
else:
    print("My third bit is 0.")

# Task 2

flag_register = 0x1234
the_mask = 4
the_mask = ~the_mask # in binary form: 11...0111

bit = flag_register & the_mask
print(bit, bin(bit), "My third bit is reset")

"""
    3. Set your bit, you want to assign to 1 your bit, use the following disjunction property:

        flag_register = flag_register | the_mask
        flag_register |= the_mask

    4. Negate your bit, you want to assign to opposite value your bit, use the following xor property:

        flag_register = flag_register ^ the_mask
        flag_register ^= the_mask
"""

# Task 3

flag_register = 0x1234
the_mask = 8

bit = flag_register | the_mask
print(bit, bin(bit), "My third bit is set")

# Task 4

flag_register = 0x1234
the_mask = 8

bit = flag_register ^ the_mask
print(bit, bin(bit), "My third bit is negated")