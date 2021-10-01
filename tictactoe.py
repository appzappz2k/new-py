# ----- tic tac toe -----

# make board => store the markers
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# playing the game


def play_game():
    print("Welcome to tik tac toe")

    # display board initialy
    display_board()

    game_is_on()

# game running


def game_is_on():
    position = int(input("choose a position: "))

    board[position - 1] = "X"

    display_board()


# main
play_game()
