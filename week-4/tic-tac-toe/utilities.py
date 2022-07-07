class utilities:

    def is_position_valid(self, current_board, x_positon, y_position):
        if(current_board[x_positon][y_position] == " "):
            return True
        else:
            return False

    def update_grid(self, current_board, x_position, y_position, player_symbol):

        if(self.is_position_valid(current_board, x_position-1, y_position-1)):
            current_board[x_position-1][y_position-1] = player_symbol
            return True
        else:
            return False

    def has_game_ended(self, current_board):
        if(current_board[0][0] == current_board[0][1] == current_board[0][2] != " "):
            return True
        elif(current_board[0][0] == current_board[1][0] == current_board[2][0] != " "):
            return True
        elif(current_board[0][0] == current_board[1][1] == current_board[2][2] != " "):
            return True
        elif(current_board[0][2] == current_board[1][2] == current_board[2][2] != " "):
            return True
        elif(current_board[2][0] == current_board[2][1] == current_board[2][2] != " "):
            return True
        elif(current_board[2][0] == current_board[1][1] == current_board[0][2] != " "):
            return True
        elif(current_board[0][1] == current_board[1][1] == current_board[2][1] != " "):
            return True
        elif(current_board[1][0] == current_board[1][1] == current_board[1][2] != " "):
            return True
        else:
            return False
