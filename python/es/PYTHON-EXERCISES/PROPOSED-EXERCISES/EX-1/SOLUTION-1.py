print("\n" + "".center(80, "="))
print("VIRAL CHALLENGE 123456789".center(80, "="))
print("".center(80, "="), "\n")

for i in range(1, 10):
    print(" " * (i - 1), end="")
    for j in range(i, 10):
        print(j, end="")
    print()

for i in range(8, 0, -1):
    print(" " * (i - 1), end="")
    for j in range(i, 10):
        print(j, end="")
    print()
