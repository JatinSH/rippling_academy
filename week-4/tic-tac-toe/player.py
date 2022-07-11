class player:

    def __init__(self, player_symbol, player_name):
        self.player_symbol = player_symbol
        self.player_name = player_name

    def second_player_symbol(self, player1_symbol):
        if(player1_symbol == "O"):
            self.player_symbol = "X"
        else:
            self.player_symbol = "O"
