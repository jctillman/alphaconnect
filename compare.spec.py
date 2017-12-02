
from abstractgame import AbstractGame
from connectgame import ConnectGame
from agent import Agent
from mcts import MCTS
from compare import compare
import unittest

#
# Unfortunately, I'd either need to write a gigantic
# stub for AbstractGame, or do integration tests, 
# so for now I'm just doing integration test
#

def agent(hardness):
    def quick_mcts(agi):
        return MCTS(agi, iteration_number=hardness)
    return Agent(quick_mcts, temperature = 0.05)

def game_creator():
    return AbstractGame(ConnectGame())

class TestCompare(unittest.TestCase):

        def test_better_wins_more(self):
            times_to_play = 4
            one_wins, two_wins, record = compare(
                    agent(40),
                    agent(360),
                    times_to_play,
                    game_creator, verbose=True)
            print one_wins, two_wins
            self.assertTrue(one_wins < two_wins) 
        
        def test_inverse_better_wins_more(self):
            times_to_play = 4
            one_wins, two_wins, record = compare(
                    agent(360),
                    agent(40),
                    times_to_play,
                    game_creator, verbose=True)
            print one_wins, two_wins
            self.assertTrue(two_wins < one_wins) 


if __name__ == '__main__':
    unittest.main()
