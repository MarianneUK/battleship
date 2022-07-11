from random import randint

# creates the 5x5 grid
board = []

for x in range(5):
    board.append(["."] * 5)

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

# randomly assigns a ship on a row and a column
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row, ship_col) #to ensure the functions are working

# calculates and displays the user's number of turns
for turn in range(5):
    print(f"Turn {turn +1}")
    # asks user for input and ensure int data type
    user_row = int(input("Row (0-4):"))
    user_col = int(input("Col (0-4):"))

    # if statements upon user's input
    if user_row == ship_row and user_col == ship_col:
        print(f"{user_name} sunk my battleship :-(")
        new_game(input("Do you want to play again? y/n"))