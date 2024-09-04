hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

hat_list[2] = int(input("Enter a number: "))

del hat_list[len(hat_list) - 1]

print(len(hat_list))

print(hat_list)
