#
# Testing that the MCTS function returns
# reasonable results, although not really
# testing the internals of it.
#
#

import unittest
import random

from abstractgame import AbstractGame
from connectgame import ConnectGame
from mcts import MCTS

class TestAbstractGame(unittest.TestCase):

        def test_wants_block_bad(self):
                inst = AbstractGame(ConnectGame())
                a = inst.move_immutable(4)
                b = a.move_immutable(1)
                c = b.move_immutable(4)
                d = c.move_immutable(1)
                e = d.move_immutable(4)
                f = e.move_immutable(1)
                distribution = MCTS(f)
                highest = max(distribution)
                highest_index = distribution.index(highest)
                self.assertTrue(highest_index == 4)
        
        # Thinks the central move in the
        # game of connect 4 is pretty much the best,
        # from a blank board.  Note that although
        # it is pretty difficult to get Minimax
        # to know this, it is pretty easy for MCTS
        def test_wants_block_death(self):
                inst = AbstractGame(ConnectGame())
                a = inst.move_immutable(4)
                b = a.move_immutable(1)
                c = b.move_immutable(4)
                d = c.move_immutable(1)
                e = d.move_immutable(4)
                distribution = MCTS(e, iteration_number=1600)
                highest = max(distribution)
                highest_index = distribution.index(highest)
                self.assertTrue(highest_index == 4)

if __name__ == '__main__':
    unittest.main()
