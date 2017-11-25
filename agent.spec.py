
#
# Test that agent makes moves, either deterministically
# or stochastically, as desired.
#

import unittest

from abstractgame import AbstractGame
from connectgame import ConnectGame
from agent import Agent
from mcts import MCTS

#
# Unfortunately, I'd either need to write a gigantic
# stub for AbstractGame, or do integration tests, 
# so for now I'm just doing integration test
#

agent_creators = [
    lambda: Agent(MCTS)
]

game_creators = [
    lambda: AbstractGame(ConnectGame()) 
]

class TestAbstractGame(unittest.TestCase):

        # Can make some kind of instance
        def test_agent_creation_new(self):
            for creator in agent_creators:
                inst = creator()
                self.assertTrue(True)

        def test_can_make_moves(self):
            for a_creator in agent_creators:
    
                for g_creator in game_creators:
                    
                    g = g_creator()
                    a = a_creator()

                    while not g.game_over():
                        move = a.move(g)
                        g = g.move_immutable(move)
                
                    self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
