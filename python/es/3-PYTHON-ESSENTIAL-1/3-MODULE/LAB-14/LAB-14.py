my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print("The list with unique elements only:")
print(my_list)
print(unique_list)
print(set(my_list))