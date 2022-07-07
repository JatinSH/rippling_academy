from player import player


def game_start():

    print("WELCOME TO THE SQUID GAME'S : TIC TAC TOE!!\n")

    print("Player 1, enter your name: ", end="")
    player1_name = input()

    print("\nPlayer 1, enter your symbol (O or X): ", end="")
    player1_symbol = input()

    player1 = player(player1_symbol, player1_name)

    print("\nPlayer 2, enter your name: ", end="")
    player2_name = input()

    player2 = player("", player2_name)
    player2.second_player_symbol(player1_symbol)

    return [player1, player2]
