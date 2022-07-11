from random import randint

# creates the 6x6 grid
board = []

for x in range(6):
    board.append(["."] * 6)

def print_board(board):
    # prints the board in the console when called
    for row in board:
        print((" ").join(row))

