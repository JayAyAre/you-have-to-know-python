"""
    Bubble sort

        Now that you can effectively juggle the elements of lists, it's time to learn how to sort them. Many sorting
            algorithms exist, easy to understand, but unfortunately not too efficient, either.
            It's used very rarely, and certainly not for large and extensive lists.

        Let's say that a list can be sorted in two ways:

            - increasing (or more precisely - non-decreasing) -
                if in every pair of adjacent elements, the former element is not greater than the latter;
            - decreasing (or more precisely - non-increasing) -
                if in every pair of adjacent elements, the former element is not less than the latter.

        we will have this list

            list = [8, 10, 6, 2, 4]

        we'll take the first and the second elements and compare them; if we determine that they're
            in the wrong order (i.e., the first is greater than the second), we'll swap them round;
            if their order is valid, we'll do nothing. A glance at our list confirms the latter -
            the elements 01 and 02 are in the proper order, as in 8 < 10.

        one first lap will like this:

            list = [8, 6, 2, 4, 10]

        The first pass through the list is already finished. We're still far from finishing our job,
        but something curious has happened in the meantime. The largest element, 10, has already gone to the end of the list.

        Look - 10 is at the top. We could say that it floated up from the bottom to the surface,
            just like the bubble in a glass of champagne
            The sorting method derives its name from the same observation - it's called a bubble sort.

        With the second lap will have:

            list = [6, 2, 4, 8, 10]

        with the third:

            list = [2, 4, 6, 8, 10]

        As you can see, the essence of this algorithm is simple: we compare the adjacent elements,
        and by swapping some of them, we achieve our goal.
"""

"""
    Sorting a list

        How many passes do we need to sort the entire list?

        We solve this issue in the following way: we introduce another variable; its task is to observe
            if any swap has been done during the pass or not; if there is no swap, then the list is already sorted
            We create a variable named swapped, and we assign a value of False to it, to indicate that there are no swaps.
            Otherwise, it will be assigned True.
"""

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # no swaps yet

while swapped == True:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            swapped = True
    print(my_list)

print("\n\n")

"""
    Buble sort interactive version
    
        Python, however, has its own sorting mechanisms. No one needs to write their own sorts,
            as there is a sufficient number of ready-to-use tools.

        If you want Python to sort your list, you can do it like this:

            my_list.sort()
"""

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# Descending

my_list = [8, 10, 6, 2, 4]
my_list.sort(reverse=True)
print(my_list)

# Interactive version

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
