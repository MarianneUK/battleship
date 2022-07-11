from random import randint

# creates the 6x6 grid
board = []

for x in range(6):
    board.append(["."] * 6)

def print_board(board):
    # prints the board in the console when called
    for row in board:
        print((" ").join(row))

# greets the player
print("Welcome to this simple single player game!")
user_name = input("What's your name?: ")
print(f"Let's play Battleship, {user_name}!")
print("There is 1 ship on the grid. You have 5 tries.")
print_board(board)