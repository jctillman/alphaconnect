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

def make_node(agi, parent_hash, prob = 0.5):
    return {
        'game': agi,
        'hash': agi.hash(),
        'prob': prob,
        'visits': 0.0,
        'victories': {
            x: 0
            for x
            in (agi.all_players() + [None])
        },
        'parent_hash': parent_hash
    }

def get_next(nodes, agi, uct, evaluator):

    current_game = agi
    
    def can_go_down():
        not_over = not current_game.game_over()
        visited = nodes[current_game.hash()]['visits'] != 0
        return not_over and visited
    
    while can_go_down():

        current_hash = current_game.hash()
        current_node = nodes[current_hash]
        current_player = current_game.move_turn()

        pos_moves = current_game.move_list()
        pos_states = [ current_game.move_immutable(x) for x in pos_moves ]
        
        for pos_state in pos_states:
            pos_hash = pos_state.hash()
            if not pos_hash in nodes:
                pos_valuation = evaluator(pos_state);
                nodes[pos_hash] = make_node(pos_state, current_hash, pos_valuation)

        child_nodes = [ nodes[x.hash()] for x in pos_states ]
        child_iter = range(len(child_nodes))
        child_vals = [ 
                uct(
                    current_node['visits'],
                    child_nodes[x]['visits'],
                    child_nodes[x]['victories'][current_player],
                    child_nodes[x]['prob']
                ) for x in child_iter ]
        child_vals_with_idx = list(enumerate(child_vals))
        highest_val = max(child_vals_with_idx, key = lambda x: x[1] )
        highest_vals_idx = [ x[0] for x in child_vals_with_idx if x[1] >= highest_val[1] ]
        highest_index = random.choice(highest_vals_idx)
        current_game = child_nodes[highest_index]['game']

    return current_game


def add_upwards(nodes, agi_hash, vict_player):
        climb_node = nodes[agi_hash]
        while True:
            climb_node['visits'] = climb_node['visits'] + 1
            climb_node['victories'][vict_player] = climb_node['victories'][vict_player] + 1
            if climb_node['parent_hash'] is None:
                break
            else:
                climb_node = nodes[climb_node['parent_hash']]
            

def uniform_evaluator(agi_instance):
    return 1

def MCTS(base_agi, iteration_number = 250, c = 2, evaluator = uniform_evaluator):

        # Initialize a few things
        uct = uct_factory(c)
        nodes = { base_agi.hash(): make_node(base_agi, None) }

        for n in range(iteration_number):
            # Get game node, and parent of game node
            new_agi = get_next(nodes, base_agi, uct, evaluator)
            
            # Simulate...
            victorious_player = random_simulation(new_agi)
            
            # Backpropogate
            add_upwards(nodes, new_agi.hash(), victorious_player)

        r = nodes[base_agi.hash()]
        moves = r['game'].move_list()
        root_children = [ nodes[r['game'].move_immutable(m).hash() ] for m in moves ]
        turn = r['game'].move_turn()
#        print turn
#        print 'visit, ', r['visits'], 'victories, ', r['victories']
#        print 'moves, ', moves
#        print [ uct(r['visits'], x['visits'], x['victories'][turn], x['prob']) for x in root_children ]
#        for n in r['game'].all_players():
#            print str(n), str([ str(x['victories'][n]) for x in root_children ])
#        print [ x['visits'] for x in root_children ]

        return softmax([ x['visits'] for x in root_children ]) 



