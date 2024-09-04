"""
    Three-dimensional arrays

        Python does not limit the depth of list-in-list inclusion. Here you can see an example of a three-dimensional array:

        Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor.
            For this, you need an array which can collect and process information on the occupied/free rooms.

        First step - the type of the array's elements. In this case, a Boolean value (True/False) would fit.
"""

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:

rooms[1][9][13] = True

# and release the second room on the fifth floor located in the first building:

rooms[0][4][1] = False

# Check if there are any vacancies on the 15th floor of the third building:

vacancy = 0

for room_number in range(20):
    if rooms[2][14][room_number] == False:
        vacancy += 1


# The vacancy variable contains 0 if all the rooms are occupied, or the number of available rooms otherwise.
