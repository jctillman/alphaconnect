#
# Monte Carlo tree interface meant to 
# work with the Abstract Game interface.
# It assumes that all games will eventually 
# end if played randomly, at the moment, so 
# is better with games like Go or Connect 4
# or TicTacToe than games like Chess
# 
# It is NOT meant to make moves, but to take
# an abstract game, in a particular state, and to 
# return a probability distribution over the moves
# indicating the probability different moves should
# be made
#

import random
from utils import softmax, random_simulation, uct_factory, uniform
from math import sqrt, log

def MCTS(abstract_game_instance,
        iteration_number = 30,
        c = 140,
        value_estimator = uniform):

        # Get initial games states, and functions
        # to be used throughout
        inst = abstract_game_instance
        uct = uct_factory(c)

        # Intialize tree of game nodes...
        nodes = {}
        root_player = inst.move_turn()
        root_node = {
            'game': inst,
            'hash': inst.hash(),
            'prob': None,
            'visits': 1.0,
            'victories': 0.0,
            'parent_hash': None,
        }
        nodes[root_node['hash']] = root_node 

        # Function which, given a hash and a number
        # of victories, climbs the nodes corresponding
        # to that hash, until it reaches the root node
        for n in range(iteration_number):

            def can_drill_down(not_hit_new_node, game):
                not_game_over = not game.game_over()
                game_moves = len(game.move_list()) > 0
                return not_hit_new_node and not_game_over and game_moves

            def get_next_elements():

                not_hit_new_node = True
                prior_node_hash = None
                current_node = nodes[root_node['hash']]
                current_game = current_node['game']
                while can_drill_down(not_hit_new_node, current_game):

                    # Get list of possible states
                    # after moving
                    possible_moves = current_game.move_list()
                    possible_states = [ current_game.move_immutable(x) for x in possible_moves ]
                    possible_hashes = [ x.hash() for x in possible_states ]

                    # See if we haved visited all before
                    stats_for_all = all([ (x in nodes) for x in possible_hashes ])

                    # Randomly select, if we haven't gotten 
                    # all of the elements enough to have stats, otherwise
                    # select by UCB.  I think this is where we inert some 
                    # specification otherwise. 
                    if stats_for_all:
                        child_nodes = [ nodes[hsh] for hsh in possible_hashes ]
                        child_iter = range(len(child_nodes))
                        child_values = [ uct(current_node, child_nodes[x] ) for x in child_iter ]
                        highest_value = max(child_values)
                        highest_value_index = child_values.index(highest_value)
                        prior_node_hash = current_node['game'].hash()
                        current_node = child_nodes[highest_value_index]
                        current_game = current_node['game']
                    else:
                        prior_node_hash = current_game.hash()
                        next_state = random.choice(possible_states)
                        next_state_hash = next_state.hash()
                        if next_state_hash in nodes:
                            current_node = nodes[next_state_hash]
                            current_game = current_node['game']
                        else:
                            current_node = None
                            current_game = next_state
                            not_hit_new_node = False

                return current_game, prior_node_hash

            
            def propogate_up_from(hsh, vict):
                    climb_node = nodes[hsh]
                    while (climb_node['parent_hash'] is not None):
                        climb_node['visits'] = climb_node['visits'] + 1
                        climb_node['victories'] = climb_node['victories'] + vict
                        climb_node = nodes[climb_node['parent_hash']]

            new_game, prior_hash = get_next_elements();
            new_hash = new_game.hash()
            nodes[new_hash] = {
                'game': new_game,
                'hash': new_hash,
                'prob': value_estimator(new_game),
                'visits': 0,
                'victories': 0,
                'parent_hash': prior_hash,
            }
            new_victories = random_simulation(new_game, root_player)
            propogate_up_from(new_hash, new_victories)

        r = root_node['game']
        moves = r.move_list()
        root_children = [ nodes[r.move_immutable(m).hash() ] for m in moves ]
        print [ x['victories'] for x in root_children ]
        print [ x['visits'] for x in root_children ]
        return softmax([1,2,3]) 



