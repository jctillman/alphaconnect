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

def make_node(agi, parent_hash):
    return {
        'game': agi,
        'hash': agi.hash(),
        'prob': 1.0,
        'visits': 0.0,
        'victories': 0.0,
        'parent_hash': parent_hash
    }

def get_next(nodes, agi):

    parent_hash = None
    current_game = agi
    
    def can_go_down():
        not_over = not current_game.game_over()
        has_move = len(current_game.move_list()) > 0
        not_in = current_game.hash() in nodes
        return not_over and has_move and not_in
    
    while can_go_down():

        current_hash = current_game.hash()
        current_node = nodes[current_hash]
        
        pos_moves = current_game.move_list()
        pos_states = [ current_game.move_immutable(x) for x in pos_moves ]
        pos_hash = [ x.hash() for x in pos_states ]
        
        nodes_present = [ ( x in nodes ) for x in pos_hash ]
        nodes_all = all(nodes_present)

        print "S"
        if nodes_all:
            child_nodes = [ nodes[x] for x in pos_hash ]
            child_iter = range(len(child_nodes))
            child_vals = [ uct(current_node, child_node[x]) for x in child_iter ]
            highest = max(child_vals)
            highest_index = child_vals.index(highes)
            parent_hash = current_hash
            current_game = child_nodes[highest_index]['game']
        else:
            parent_hash = current_hash
            current_game = random.choice(pos_states)

    return current_game, parent_hash


def add_upwards(nodes, agi_hash, victs):
        print nodes.keys()
        print "@@@@@@"
        print agi_hash in nodes
        print agi_hash
        climb_node = nodes[agi_hash]
        while (climb_node['parent_hash'] is not None):
            climb_node['visits'] = climb_node['visits'] + 1
            climb_node['victories'] = climb_node['victories'] + victs
            climb_node = nodes[climb_node['parent_hash']]

def MCTS(agi, iteration_number = 30, c = 140 ):

        # Always the same, no matter what
        nodes = {}
        uct = uct_factory(c)
        player = agi.move_turn()

        # Intialize tree of game nodes...
        root_hash = agi.hash()
        nodes[root_hash] = make_node(agi, None)

        for n in range(iteration_number):
            new_agi, agi_parent_hash = get_next(nodes, agi)
            nodes[new_agi.hash()] = make_node(new_agi, agi_parent_hash) 
            print "ASD"
            victory = random_simulation(new_agi, player)
            add_upwards(nodes, new_agi.hash(), victory)
            print "DAASS"
        r = root_node['game']
        moves = r.move_list()
        root_children = [ nodes[r.move_immutable(m).hash() ] for m in moves ]
        print [ x['victories'] for x in root_children ]
        print [ x['visits'] for x in root_children ]
        return softmax([1,2,3]) 



