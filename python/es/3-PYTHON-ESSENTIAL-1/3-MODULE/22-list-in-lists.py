"""
        Lists in lists

                Lists can consist of scalars (namely numbers) and elements of a much more complex structure
                        Let's have a closer look at the case where a list's elements are just lists.

                We often find such arrays in our lives. Probably the best example of this is a chessboard.

                A chessboard is composed of rows and columns. There are eight rows and eight columns. Each column is
                        marked with the letters A through H. Each line is marked with a number from one to eight.

                The location of each field is identified by letter-digit pairs. Thus, we know that the bottom left corner of
                        the board (the one with the white rook) is A1, while the opposite corner is H8.

                Let's assume that we're able to use the selected numbers to represent any chess piece.
                        We can also assume that every row on the chessboard is a list.
"""

WHITE_PAWN = "A"
row = []

for i in range(8):
    row.append(WHITE_PAWN)

"""
        The same effect may be achieved by means of a list comprehension,
                the special syntax used by Python in order to fill massive lists.

        A list comprehension is actually a list, but created on-the-fly during program execution, and is not described statically.
"""

row = [WHITE_PAWN for i in range(8)]

# Example 1

squares = [x ** 2 for x in range(10)]

# Example 2

twos = [2 ** i for i in range(8)]

# Example 3

odds = [x for x in squares if x % 2 != 0]

"""
	List in lists: two-dimensional arrays

			Let's also assume that a predefined symbol named EMPTY designates an empty field on the chessboard.

			So, if we want to create a list of lists representing the whole chessboard, it may be done in the following way:
"""

board = []
EMPTY = "-"
for i in range(8):
    row = [EMPTY for j in range(8)]
    board.append(row)

"""
	NOTE

		- the inner part of the loop creates a row consisting of eight elements
  			(each of them equal to EMPTY) and appends it to the board list;
		- the outer part repeats it eight times;
		- in total, the board list consists of 64 elements (all equal to EMPTY)

	The board variable is now a two-dimensional array. It's also called, by analogy to algebraic terms, a matrix.

	As list comprehensions can be nested, we can shorten the board creation in the following way:
"""

board = [[EMPTY for i in range(8)] for j in range(8)]

[print(row) for row in board]

"""
	Glancing at the figure shown above, let's set some chess pieces on the board. First, let's add all the rooks:

	board[0][0] = ROOK
	board[0][7] = ROOK
	board[7][0] = ROOK
	board[7][7] = ROOK


	If you want to add a knight to C4, you do it as follows:

	board[4][2] = KNIGHT


	And now a pawn to E5:

	board[3][4] = PAWN


	And now - experiment with the code in the editor.
"""

print("\n\n")
EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[0][1] = "Hola"
board[3][1] = "Hola"


[print(row) for row in board]

"""
	Multidimensional nature of lists: advanced applications

		Let's go deeper into the multidimensional nature of lists.
  			To find any element of a two-dimensional list, you have to use two coordinates:

			a vertical one (row number)
			and a horizontal one (column number).

		magine that you develop a piece of software for an automatic weather station. The device records
  			the air temperature on an hourly basis and does it throughout the month.
			This gives you a total of 24 x 31 = 744 values. Let's try to design a list capable of storing all these results.

		First, you have to decide which data type would be adequate for this application. In this case, a float would be best

		Then you take an arbitrary decision that the rows will record the readings every hour
  			on the hour (so the row will have 24 elements)
			and each of the rows will be assigned to one day of the month (let's assume that each month has 31 days,
   			so you need 31 rows).
			Here's the appropriate pair of comprehensions (h is for hour, d for day):

		temps = [[0.0 for h in range(24)] for d in range(31)]

		The whole matrix is filled with zeros now

		Now it's time to determine the monthly average noon temperature. Add up all 31 readings recorded
  			at noon and divide the sum by 31.
"""

print("\n\n")
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

"""
	NOTE

		the day variable used by the for loop is not a scalar - each pass through the temps matrix
			assigns it with the subsequent rows of the matrix; hence, it's a list. It has to be indexed
   			with 11 to access the temperature value measured at noon.

	Now find the highest temperature during the whole month - see the code:
"""

print("\n\n")
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

highest = -100.0

for day in temps:
    highest = [hour for hour in day if hour > highest]

print("The highest temperature was:", highest)


# Now count the days when the temperature at noon was at least 20 ℃:

print("\n\n")
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")
