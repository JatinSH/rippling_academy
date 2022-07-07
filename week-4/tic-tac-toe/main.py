class game_board:

    def __init__(self, tic_tac_toe_grid):
        self.tic_tac_toe_grid = tic_tac_toe_grid
        self.grid_rows = len(tic_tac_toe_grid)
        self.grid_columns = len(tic_tac_toe_grid[0])

    def display_grid(self):

        for grid_row in self.tic_tac_toe_grid:
            print("\n  ---   ---   ---\n|", end="")
            for item in grid_row:
                print("  %s  |" % (item), end="")
        print("\n  ---   ---   ---")

    def is_position_valid(self, x_positon, y_position):
        if(self.tic_tac_toe_grid[x_positon][y_position] == " "):
            return True
        else:
            return False

    def update_grid(self, x_position, y_position, player_symbol):
        if(self.is_position_valid(x_position, y_position)):
            self.tic_tac_toe_grid[x_position][y_position] = player_symbol
            return True
        else:
            return False


initial_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
game = game_board(initial_board)


class player:
    pass


print("WELCOME TO THE SQUID GAME'S : TIC TAC TOE!!")
game.display_grid()
print("Enter Coordinates: ")
user_input = input()
x_position = int(user_input[0])
print(x_position)
y_position = int(user_input[2])
print(y_position)
game.update_grid(x_position, y_position, "O")
game.display_grid()
