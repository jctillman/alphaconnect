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

        def test_aa_wants_wim(self):
                print "Testing can win."
                for n in range(15):
                    print "Passed " + str(n)
                    inst = AbstractGame(ConnectGame())
                    a = inst.move_immutable(4)
                    b = a.move_immutable(1)
                    c = b.move_immutable(4)
                    d = c.move_immutable(1)
                    e = d.move_immutable(4)
                    f = e.move_immutable(1)
                    distribution = MCTS(f, iteration_number=70)
                    highest = max(distribution)
                    highest_index = distribution.index(highest)
                    self.assertTrue(highest_index == 4)
        
        def test_bb_wants_block_death(self):
                print "Testing can block opponent victory."
                for n in range(15):
                    print "Passed " + str(n)
                    inst = AbstractGame(ConnectGame())
                    a = inst.move_immutable(4)
                    b = a.move_immutable(1)
                    c = b.move_immutable(4)
                    d = c.move_immutable(1)
                    e = d.move_immutable(4)
                    distribution = MCTS(e, iteration_number=700)
                    highest = max(distribution)
                    highest_index = distribution.index(highest)
                    self.assertTrue(highest_index == 4)
        
        def test_cc_several_moves_ahead(self):
                print "Testing can look a few moves ahead..."
                for n in range(10):
                    print "Passed " + str(n)
                    inst = AbstractGame(ConnectGame())
                    a = inst.move_immutable(3)
                    b = a.move_immutable(3)
                    c = b.move_immutable(4)
                    d = c.move_immutable(4)
                    distribution = MCTS(d, iteration_number=500)
                    highest = max(distribution)
                    highest_index = distribution.index(highest)
                    self.assertTrue(highest_index == 5 or highest_index == 2)
        
        def test_dd_wants_center(self):
                print "Testing wants center..."
                for n in range(10):
                    print "Passed " + str(n)
                    inst = AbstractGame(ConnectGame())
                    distribution = MCTS(inst, iteration_number=2200)
                    highest = max(distribution)
                    highest_index = distribution.index(highest)
                    self.assertTrue(highest_index == 3)

if __name__ == '__main__':
    unittest.main()
