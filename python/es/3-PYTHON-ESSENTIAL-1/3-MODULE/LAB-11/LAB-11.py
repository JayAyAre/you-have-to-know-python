c0 = int(input("Enter the number: "))

steps = 0
while c0 != 1:
    steps += 1
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 *= 3
        c0 += 1
    print(int(c0))

print("The number of steps is:", steps)