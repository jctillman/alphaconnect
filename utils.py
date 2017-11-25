#
#
# Misc utils
#
#
import math
import random

def softmax(lst, temperature=1.0):
    maxed = max(lst)
    powered = [
            math.exp((x - maxed) / float(temperature))
            for x in lst
            ]
    powered_sum = sum(powered)
    return [ x / powered_sum for x in powered ]

#
# MCTS needs something that lets you randomly
# simulate a game from a point, and find who 
# is the winner or loser.  Value draw at zero,
# win at one, and loss at -1
#
def random_simulation(ag_instance):
    inst = ag_instance
    while not inst.game_over():
        inst = inst.move_immutable(random.choice(inst.move_list()))
    winner = inst.game_winner()
    return winner

def uct_factory(c):
        def uct(current_visits, child_visits, child_victories, child_prob):
            
            # Factor by which to exploit
            exploit = float(child_victories / (max(1.0, child_visits)))
            
            # Factor by which to explore
            factor = float(c) * float(child_prob)
            numerator = math.log( float(current_visits) )
            denominator = float(max(1.0, child_visits))
            explore = factor * math.sqrt(numerator / denominator)
           
            return exploit + explore
        return uct

def uniform(ag_instance):
    return 1
