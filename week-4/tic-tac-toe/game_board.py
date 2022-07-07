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
