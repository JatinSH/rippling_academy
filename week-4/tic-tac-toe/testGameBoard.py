from gameBoard import gameBoard
import unittest


class testGameBoard(unittest.TestCase):

    def test1(self):
        game_board = gameBoard(
            [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
        self.assertEqual(game_board.display_grid(), None, "Incorrect!!")


unittest.main()
