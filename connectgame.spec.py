#
# Testing the "connectgame" class
#
import random
import unittest
from connectgame import ConnectGame

class TestConnectGame(unittest.TestCase):

        # Test that when you start it up with generic 
        # stats, everything is created as it should be
        def test_connect_game_new_vanilla(self):
            a = ConnectGame()
            self.assertTrue(a.width == 7)
            self.assertTrue(a.height == 6)
            self.assertTrue(a.win_length == 4)
            self.assertTrue(len(a.board.board) == 6)
            self.assertTrue(len(a.board.board[0]) == 7)

        # Returns a standard list of normal moves,
        # after one has an oportunity to make them.
        def test_connect_game_normal_moves(self):
            a = ConnectGame()
            b = a.move_list()
            self.assertTrue(len(b) == 7)
            self.assertEqual(b, [0, 1, 2, 3, 4, 5, 6])

        # Decreases available moves 
        # after enough other moves have been made
        def test_connect_game_nonnormal_moves(self):
            a = ConnectGame()
            b = a.move_immutable(0)
            c = b.move_immutable(0)
            d = c.move_immutable(0)
            e = d.move_immutable(0)
            f = e.move_immutable(0)
            g = f.move_immutable(0)
            h = g.move_list()
            self.assertEqual(h, [1, 2, 3, 4, 5, 6])
            i = g.move_immutable(3)
            j = i.move_immutable(3)
            k = j.move_immutable(3)
            l = k.move_immutable(3)
            m = l.move_immutable(3)
            n = m.move_immutable(3)
            o = n.move_list()
            self.assertEqual(o, [1,2,4,5,6])
        
        # Alternates moves between 1 and 0
        # as one makes a move of some kind.
        def test_move_turn_alternate(self):
            a = ConnectGame()
            self.assertTrue(a.move_turn() == 1)
            b = a.move_immutable(0)
            self.assertTrue(b.move_turn() == 0)
            c = b.move_immutable(0)
            self.assertTrue(c.move_turn() == 1)

        # Run to completion about 100 times, checking each time
        # that it is either a win, a loss, or a draw -- so, 
        # that game_winner returns either a 1, 0, or None.
        def test_that_wins_happen(self): 
            num_tests = 50
            zero_wins = 0
            one_wins = 0
            for t in range(num_tests):
                tmp = ConnectGame()
                while not tmp.game_over():
                    moves = tmp.move_list()
                    move = random.choice(moves)
                    tmp = tmp.move_immutable(move)
                winner = tmp.game_winner()
                if winner == 1:
                    one_wins = one_wins + 1
                if winner == 0:
                    zero_wins = zero_wins + 1
            self.assertTrue(zero_wins > num_tests * 0.25)
            self.assertTrue(one_wins > num_tests * 0.25)

        def test_that_wins_dont_happen(self):

            num_tests = 150
            zero_wins = 0
            one_wins = 0
            for t in range(num_tests):
                tmp = ConnectGame()
                for n in range(6):
                    moves = tmp.move_list()
                    move = random.choice(moves)
                    tmp = tmp.move_immutable(move)
                winner = tmp.game_winner()
                if winner == 1:
                    one_wins = one_wins + 1
                if winner == 0:
                    zero_wins = zero_wins + 1
            self.assertTrue(zero_wins == 0)
            self.assertTrue(one_wins == 0)

if __name__ == '__main__':
    unittest.main()
