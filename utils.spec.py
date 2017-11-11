#
#
# Test misc utils
#
#
import unittest

from abstractgame import AbstractGame
from connectgame import ConnectGame
from utils import softmax, random_simulation, uct_factory

class TestUtils(unittest.TestCase):

        # Can softmax
        def test_board_creation_new(self):
            m = softmax([1,1])
            self.assertTrue(m[0] == 0.5)
            self.assertTrue(m[1] == 0.5)
            m = softmax([2,2,2,2])
            self.assertTrue(m[0] == 0.25)
            self.assertTrue(m[3] == 0.25)
            
        def test_random_simulation(self):
            total_plays = 100
            win_total = 0
            for n in range(total_plays):
                g = AbstractGame(ConnectGame())
                win_total = win_total + random_simulation(g,1)
            self.assertTrue(win_total > -5)
            self.assertTrue(win_total < 50)

        def test_uct_factory(self):
            
            vanilla = uct_factory(1)

            parent = { 'visits': 1 }
            child = { 'visits': 1, 'victories': 1, 'prob': 1 }

            self.assertEqual(vanilla(parent, child),0.5)

if __name__ == '__main__':
    unittest.main()
