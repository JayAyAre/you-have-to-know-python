from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""
    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
        """)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            position = int(input("Enter the position of the square: "))
            if position < 1 or position > 9:
                print("Position must be between 1 and 9.")
                continue
            else:
                position -= 1
                row = position // 3
                column = position % 3
                if board[row][column] == COMPUTER_SYMBOL or board[row][column] == USER_SYMBOL:
                    print("This square is already taken.")
                    continue
                else:
                    board[row][column] = USER_SYMBOL
                    break
        except ValueError:
            print("Position must be a number.")
            continue
        except IndexError:
            print("Something went wrong. Try again.")
            continue
    display_board(board)


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    global finished
    for i in range(0, 3):
        j = 0
        if board[i][j] == sign and board[i][j + 1] == sign and board[i][j + 2] == sign:
            finished = True
            break

    for i in range(0, 3):
        j = 0
        if board[j][i] == sign and board[j + 1][i] == sign and board[j + 2][i] == sign:
            finished = True
            break

    if not finished:
        j = 0
        if board[j][0] == sign and board[j][1] == sign and board[j][2] == sign:
            finished = True
        elif board[0][j] == sign and board[1][j] == sign and board[2][j] == sign:
            finished = True

    if finished:
        print(f"Congratulations, {sign} has won!")


def draw_move(board):
    # The function draws the computer's move and updates the board.
    global first_move, finished
    if first_move:
        first_move = False
        board[1][1] = COMPUTER_SYMBOL
    else:
        while True and not is_full(board):
            random_position = randrange(1, 9)
            if board[random_position // 3][random_position % 3] != COMPUTER_SYMBOL \
                    and board[random_position // 3][random_position % 3] != USER_SYMBOL:
                board[random_position // 3][random_position %
                                            3] = COMPUTER_SYMBOL
                break
            else:
                continue
        display_board(board=board)


def is_full(board):
    # The function checks if the board is full.
    for row in board:
        for square in row:
            if square != COMPUTER_SYMBOL and square != USER_SYMBOL:
                return False
    return True


def create_board(board):
    # The function creates a new board with the initial state.
    # The board is a list of lists, where each list contains
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            row.append(i * 3 + j + 1)
        board.append(row)


COMPUTER_SYMBOL = 'X'
USER_SYMBOL = 'O'
ROWS_NUMBER = 3
COLUMNS_NUMBER = 3

board = []
finished = False
first_move = True
create_board(board)

print(board)
print("Welcome to Tic-Tac-Toe!")
display_board(board)
draw_move(board)
print("First move for the computer.")

while not finished:
    # The game is played until the player wins or the game ends.
    enter_move(board)
    victory_for(board, USER_SYMBOL)
    if is_full(board):
        print("The game is a draw.")
        break
    if not finished:
        draw_move(board)
        victory_for(board, COMPUTER_SYMBOL)
        if is_full(board):
            print("The game is a draw.")
            break

print("Game over.")
