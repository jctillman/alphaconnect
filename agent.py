#
#
# Agent takes a function which takes an AGI, and returns
# a probability distribution over moves, and instead returns
# a move.  It uses a softmax, at a settable temperature.
#
#
import numpy
from utils import softmax

class Agent:

    def __init__(self,
            fnc,
            temperature = 1.0):

        self.fnc = fnc
        self.temperature = temperature

    def move(self, agi):

        moves = agi.move_list()
        moves_dist = self.fnc(agi)
        moves_dist_softmax = softmax(moves_dist, temperature = self.temperature)
        move = numpy.random.choice(moves,p=moves_dist_softmax)

        return move, moves_dist_softmax


