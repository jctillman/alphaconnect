

from abstractgame import AbstractGame
from connectgame import ConnectGame
from agent import Agent
from mcts import MCTS
from compare import compare
from connect4adapter import connect4adapter_single, connect4adapter_value
import random

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

class TestConnect4Adapter(unittest.TestCase):

        def test_works_single(self):
            inst = game_creator()
            for n in range(7):
                inst = inst.move_immutable(random.choice(inst.move_list()))
            arr = connect4adapter_single(inst) 
            self.assertTrue(len(arr) == 6)
            self.assertTrue(len(arr[0]) == 7)
            
            for row in arr:
                for col in row:
                    if col * 1.0 != col:
                        raise Error("Bad output")


        def test_converts_value(self):
            times_to_play = 2
            one_wins, two_wins, record = compare(
                    agent(10),
                    agent(60),
                    times_to_play,
                    game_creator,
                    verbose=False)
            X, Y = connect4adapter_value(record)

            self.assertTrue(len(X) == len(Y))
            for x in X:
                self.assertTrue(len(x) == 6)
                self.assertTrue(len(x[0]) == 7)



if __name__ == '__main__':
    unittest.main()
