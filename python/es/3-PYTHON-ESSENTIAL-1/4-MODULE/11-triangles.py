"""
    Lets play with triangles now

        We know from the school than the sum of two arbitrary sides has to be
            longer than the third side

        It won't be a hard challenge. The function will have three parameters - one for each side.

        it will return True  if the sides can build a triangle, and False otherwise. In this case, is_a_triangle is a good name for such a function.
"""


def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# Compact version


def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# Compact version 2


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

"""
    triangles and pythagorean theorem

        It asks the user for three values. Then it makes use of the is_a_triangle function. The code is ready to run.

        In the second step, we'll try to ensure that a certain triangle is a right-angle triangle.

        We will need to make use of the Pythagorean theorem:

            c**2 = a**2 + b**2

        The hypotenuse is the longest side.
"""


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))


"""
    evaluating a triangle's area

        We can also evaluate a triangle's area. Heron's formula will be handy hera

            s = (a + b + c)/2 # This is the perimeter half by two
            A = sqrt(s(s - a)(s - b)(s - c)) # This is the area

"""

print("\n\n")


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    # This is the square root, is the same that x**(1/2)
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))

"""
    It's very close to 0.5, but it isn't exactly 0.5. What does it mean? Is it an error?

    No, it isn't. This is the specifics of floating-point calculations. We'll tell you more about it soon.
"""
