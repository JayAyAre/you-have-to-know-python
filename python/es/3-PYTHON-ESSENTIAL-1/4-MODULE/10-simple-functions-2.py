"""
    Some simple functions: evaluating the BMI

        The function is easy:

            BMI = (weight in kilograms)/(height in meters)**2

        The formula gets two values, weight and height

        it seems the function will get two parameters, and its name will be
"""


def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))
print(bmi(4, height=5))

# print(bmi(4, weight = 5)) Error
# print(bmi(weight = 4, 5)) Error

"""
    evaluating BMI and converting imperial units to metric units

        There are two things we need to pay attention

            - First, the  test invocation ensures that the protection works properly
            - Second, , take a look at the way the backslash (\) symbol is used. If you use it in Python code and end a line with it, it will tell 
                Python to continue the line of code in the next line of code.
"""


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))

"""
    We need to pay attention also to convert imperial units
        to metrics one

    This is our helper function, named lb_to_kg:
"""


def lb_to_kg(lb):
    return lb * 0.45359237


print(lb_to_kg(1))

# Now, ft and in to meters


def ft_and_inch_to_m(ft, inch=0.0):  # We cant use in, because its a keyword
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(1, 1))
print(ft_and_inch_to_m(6, 0))


"""
    Our code will be:

    def ft_and_inch_to_m(ft, inch = 0.0):
        return ft * 0.3048 + inch * 0.0254


    def lb_to_kg(lb):
        return lb * 0.45359237


    def bmi(weight, height):
        if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
            return None

        return weight / height ** 2


    print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))
"""

print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7)))
