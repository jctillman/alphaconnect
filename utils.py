#
#
# Misc utils
#
#
import math
import random

def softmax(lst):
    powered = [ math.exp(x) for x in lst ]
    powered_sum = sum(powered)
    return [ x / powered_sum for x in powered ]

#
# MCTS needs something that lets you randomly
# simulate a game from a point, and find who 
# is the winner or loser.  Value draw at zero,
# win at one, and loss at -1
#
def random_simulation(ag_instance, player):
    inst = ag_instance
    while not inst.game_over():
        inst = inst.move_immutable(random.choice(inst.move_list()))
    winner = inst.game_winner()
    return winner

def uct_factory(c):
        def uct(current, child):
            child_visits = float(child['visits'])
           
            current_player = current['game'].move_turn()
            current_player_victories = current['victories'][current_player] 

            # Factor by which to exploit
            exploit = float(child['victories'][current_player]) / (1.0 + child_visits)
            
            # Factor by which to explore
            factor = float(c) * child['prob']
            numerator = math.log( float(current['visits']) )
            denominator = 1.0 + child_visits
            explore = factor * math.sqrt( numerator / denominator )
           
            return exploit + explore
        return uct

def uniform(ag_instance):
    return 1
