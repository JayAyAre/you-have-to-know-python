"""
    Tuples and dictionaries can work together

        Let's imagine the following problem:

            - you need a program to evaluate the students' average scores;
            - the program should ask for the student's name, followed by her/his single score;
            - the names may be entered in any order;
            - entering an empty name finishes the inputting of the data (note 1: entering an empty score will raise
                the ValueError exception, but don't worry about that now,
                you'll see how to handle such cases when we talk about exceptions in the second part of the Python Essentials course series)
            - a list of all names, together with the evaluated average score, should be then emitted.
"""

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break

    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
