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
        
        def test_wants_block_death(self):
                inst = AbstractGame(ConnectGame())
                a = inst.move_immutable(4)
                b = a.move_immutable(1)
                c = b.move_immutable(4)
                d = c.move_immutable(1)
                e = d.move_immutable(4)
                distribution = MCTS(e)
                highest = max(distribution)
                highest_index = distribution.index(highest)
                self.assertTrue(highest_index == 4)
        
        def test_several_moves_ahead(self):
                inst = AbstractGame(ConnectGame())
                a = inst.move_immutable(3)
                b = a.move_immutable(3)
                c = b.move_immutable(4)
                d = c.move_immutable(4)
                distribution = MCTS(d, iteration_number=1000)
                highest = max(distribution)
                highest_index = distribution.index(highest)
                self.assertTrue(highest_index == 5 or highest_index == 2)
        
        #def test_wants_center(self):
        #        inst = AbstractGame(ConnectGame())
        #        distribution = MCTS(inst, iteration_number=8500)
        #        highest = max(distribution)
        #        highest_index = distribution.index(highest)
        #        self.assertTrue(highest_index == 3)

if __name__ == '__main__':
    unittest.main()
