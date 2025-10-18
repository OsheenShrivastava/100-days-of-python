
# TODO-1 - Display Welcome message and show the players.
# TODO-2 - Display the board.
# TODO-3 - Ask Player X to choose the spot between 1-9 and show it on the board.
# TODO-4 - Check for Value Error if player has not entered anything or has entered character other than number,
#  Check if value entered is between 1 to 9, Check if spot entered is occupied or not.
# TODO-5 - If everything is fine in step 4 then place the symbol in the board and switch the player.
# TODO-6 - Check if the player has won using predefined winning positions. Compare board's winning positions with the
#  current player's symbol using FOR loop. If yes then that player has won.
# TODO-7 - Display the board 1 last time and the player's name.
# TODO-8 - Check if the board is full and no player has won then display draw position.


print("Welcome to Tic Tac Toe")
print("Player 1 is X, Player 2 is O")


def show_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_for_win(board, current_player):
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for position in winning_positions:
        if board[position[0]] == board[position[1]] == board[position[2]] == current_player:
            return True
    return False


def tic_tac_toe():

    board = [" "] * 9

    current_player = "X"

    game_on = True

    while game_on:
        show_board(board)

        try:
            move = int(input(f"Player {current_player}, choose between(1-9): "))-1

        except ValueError:
            print("Please enter a number.")
            continue


        if move < 0 or move > 8:
            print("Out of range. PLease try again.")
            continue


        if board[move] != " ":
            print("Spot is already occupied. PLease try again.")
            continue


        board[move] = current_player


        if check_for_win(board, current_player):
            show_board(board)
            print(f"Player {current_player} wins!")
            game_on = False


        if " " not in board:
            show_board(board)
            print(f"It's a draw. PLease try again.")
            game_on = False


        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


tic_tac_toe()