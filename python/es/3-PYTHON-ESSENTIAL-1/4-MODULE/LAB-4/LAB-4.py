def aux_is_not_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return True
    return False


def is_prime(num):
    if (num < 2) or aux_is_not_prime(num):
        return False
    else:
        return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
