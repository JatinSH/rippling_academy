import os
from gameBoard import gameBoard
from game_start import game_start
import utilities

initial_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
game = gameBoard(initial_board)
[player1, player2] = game_start()
current_player = player1

while(True):

    game.display_grid()
    print("\n", current_player.player_name,
          ", enter coordinates in the form of \"row,column\" (1 index based) :  ", end="")

    user_input = input()
    x_position = int(user_input[0])
    y_position = int(user_input[2])

    if(not utilities.update_grid(game.tic_tac_toe_grid, x_position, y_position, current_player.player_symbol)):
        os.system('clear')
        print("The position is invalid!!")
        continue

    if(utilities.has_game_ended(game.tic_tac_toe_grid)):
        os.system('clear')
        game.display_grid()
        print("\n", current_player.player_name, " WINS!!")
        break

    if(current_player == player1):
        current_player = player2
    else:
        current_player = player1
    os.system('clear')
