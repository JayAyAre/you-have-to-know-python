print("\n" + "".center(80, "="))
print("CALCULE THE MEDIAN OF A LIST OF NUMBERS".center(80, "="))
print("".center(80, "="), "\n")

list_numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_result = 0
for number in list_numbers_1:
    sum_result += number

median = sum_result / len(list_numbers_1)
print("The median of the list is:\t", median)

"or"

median = sum(list_numbers_1) / len(list_numbers_1)
print("The median of the list is:\t", median)
