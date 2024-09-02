"""
    The while loop and the else branch

        Both loops, while and for, have one interesting (and rarely used) feature.

        Loops may have the else branch too, like ifs
        The loop's else branch is always executed once, regardless of whether the loop has entered its body or not.
"""

i = 5
while i < 10:
    print(i)
    i += 1
    if i == 7:
        break
else:
    print("while else:", i)

"""
    The for loop and the else branch

        for loops behave a bit differently - take a look at the snippet in the editor and run it.
"""

i = 10
for i in range(1, 20):
    print(i)
    if i == 15:
        break
else:
    print("for else:", i)

"""
    When the loop's body isn't executed, the control variable retains the value it had before the loop.

    NOTE

        if the control variable doesn't exist before the loop starts, it won't exist when the execution reaches the else branch.

        And other things, if we exit the for or while loop with a break, it wont execute the else branch.
        We use the else branch on while and for loops to confirm that the loop has been successfully executed. (The loops has been
            Executed or not, if we exit with a break, else branch wont execute)

"""
theflag = "o"
mylist =  "hello"
for i in mylist:
    if i == theflag:
        break
    print(i)
else:
    raise ValueError("List argument missing terminal flag.")

# Go to LAB-10