# Loops

# While loops

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1

print("While loop finished")

# While else
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("My condition is greater than 10")

print("While else loop finished")


# Break

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
    if my_condition == 5:
        break
else:
    print("My condition is greater than 10")

print("While else loop finished")

# For loops

my_list = [1, 2, 3, 4, 5]

for i in my_list:
    print(i)

my_tuple = (1, 2, 3, 4, 5)

for i in my_tuple:
    print(i)

my_set = {1, 2, 3, 4, 5}

for i in my_set:
    print(i)

my_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

for key, value in my_dictionary.items():
    print(key, value)

for key in my_dictionary:
    print(key)

print(my_dictionary)

# Continue

for i in range(10):
    if i == 5:
        continue
    print(i)

print("Continue loop finished")
