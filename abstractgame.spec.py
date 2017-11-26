#
# Test abstract game interface for things
#

import unittest
import random

from abstractgame import AbstractGame
from connectgame import ConnectGame

#
# Unfortunately, I'd either need to write a gigantic
# stub for AbstractGame, or do integration tests, 
# so for now I'm just doing integration test
#

game_creators = [ConnectGame]

class TestAbstractGame(unittest.TestCase):

        # Can make some kind of instance
        def test_board_creation_new(self):
            for creator in game_creators:
                inst = AbstractGame(creator())
                self.assertTrue(True)

        def test_can_play_till_end_mutably(self):
            for creator in game_creators:
                inst = AbstractGame(creator())
                num_moves = 0
                while (not inst.game_over()):
                    moves = inst.move_list()
                    num_moves = num_moves + 1
                    inst.move_mutable(random.choice(moves))
                self.assertTrue(True)
                self.assertTrue(num_moves > 2)
                self.assertTrue(num_moves < 1000)
            

if __name__ == '__main__':
    unittest.main()
