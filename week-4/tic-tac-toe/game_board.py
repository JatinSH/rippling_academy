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
        if(self.is_position_valid(x_position-1, y_position-1)):
            self.tic_tac_toe_grid[x_position-1][y_position-1] = player_symbol
            return True
        else:
            return False

    def has_game_ended(self):
        if(self.tic_tac_toe_grid[0][0] == self.tic_tac_toe_grid[0][1] == self.tic_tac_toe_grid[0][2] != " "):
            return True
        elif(self.tic_tac_toe_grid[0][0] == self.tic_tac_toe_grid[1][0] == self.tic_tac_toe_grid[2][0] != " "):
            return True
        elif(self.tic_tac_toe_grid[0][0] == self.tic_tac_toe_grid[1][1] == self.tic_tac_toe_grid[2][2] != " "):
            return True
        elif(self.tic_tac_toe_grid[0][2] == self.tic_tac_toe_grid[1][2] == self.tic_tac_toe_grid[2][2] != " "):
            return True
        elif(self.tic_tac_toe_grid[2][0] == self.tic_tac_toe_grid[2][1] == self.tic_tac_toe_grid[2][2] != " "):
            return True
        elif(self.tic_tac_toe_grid[2][0] == self.tic_tac_toe_grid[1][1] == self.tic_tac_toe_grid[0][2] != " "):
            return True
        elif(self.tic_tac_toe_grid[0][1] == self.tic_tac_toe_grid[1][1] == self.tic_tac_toe_grid[2][1] != " "):
            return True
        elif(self.tic_tac_toe_grid[1][0] == self.tic_tac_toe_grid[1][1] == self.tic_tac_toe_grid[1][2] != " "):
            return True
        else:
            return False
