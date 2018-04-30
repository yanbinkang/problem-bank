import unittest
import tic_tac_toe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.g = tic_tac_toe.Game()

    def test_winner(self):
        self.g.make_a_move(1, 'O')
        self.g.make_a_move(4, 'X')
        self.g.make_a_move(2, 'O')
        self.g.make_a_move(5, 'X')
        self.g.make_a_move(3, 'O')
        assert self.g.announce_winner('O') == "We have a winner"

    def test_tie(self):
        self.g.make_a_move(1, 'O')
        self.g.make_a_move(2, 'X')
        self.g.make_a_move(3, 'O')
        self.g.make_a_move(5, 'X')
        self.g.make_a_move(4, 'O')
        self.g.make_a_move(6, 'X')
        self.g.make_a_move(9, 'O')
        self.g.make_a_move(7, 'X')
        self.g.make_a_move(8, 'O')
        assert self.g.announce_winner('O') == "It's a tie"



if __name__ == '__main__':
    unittest.main()
