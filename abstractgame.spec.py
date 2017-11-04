#
# Test abstract game interface for things
#

import unittest
from abstractgame import AbstractGame
from connectgame import ConnectGame

#
# Unfortunately, I'd either need to write a gigantic
# stub for AbstractGame, or do integration tests, 
# so for now I'm just doing integration test
#
class TestAbstractGame(unittest.TestCase):

        # Can make some kind of instance
        def test_board_creation_new(self):
            inst = AbstractGame(ConnectGame())
            assertTrue(inst.instance.width == 7)

if __name__ == '__main__':
    unittest.main()
