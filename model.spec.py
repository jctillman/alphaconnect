#
# Test abstract game interface for things
#

import unittest
import random

from model import Connect4Model
from agent import Agent
from mcts import MCTS
from abstractgame import AbstractGame
from connectgame import ConnectGame
from compare import compare
from connect4adapter import connect4adapter_value
import numpy as np

def agent(hardness):
    def quick_mcts(agi):
        return MCTS(agi, iteration_number=hardness)
    return Agent(quick_mcts, temperature = 1)

def game_creator():
    return AbstractGame(ConnectGame())

class TestModelTrains(unittest.TestCase):

        def test_model_overfits(self):
            m = Connect4Model()

            times_to_play = 5
            one_wins, two_wins, record = compare(
                    agent(10),
                    agent(10),
                    times_to_play,
                    game_creator, verbose=False)

            X, Y = connect4adapter_value(record)

            loss_one = m.train(np.array(X),np.array(Y))
            loss_two = m.train(np.array(X),np.array(Y))
            self.assertTrue(loss_one > loss_two)
        
        def test_model_fits(self):
            m = Connect4Model()

            for n in range(50):
                times_to_play = 20
                one_wins, two_wins, record = compare(
                        agent(150),
                        agent(150),
                        times_to_play,
                        game_creator, verbose=False)

                X, Y = connect4adapter_value(record)

                loss = m.train(np.array(X),np.array(Y))
                print loss

            
if __name__ == '__main__':
    unittest.main()
