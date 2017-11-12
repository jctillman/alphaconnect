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

def make_node(agi, parent_hash, initial_visits=0.0):
    node_candidate = {
        'game': agi,
        'hash': agi.hash(),
        'prob': 1.0,
        'visits': initial_visits,
        'victories': { None: 0 },
        'parent_hash': parent_hash
    }
    for n in agi.all_players():
        node_candidate['victories'][n] = 0
    return node_candidate 

def get_next(nodes, agi, uct):

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

        if nodes_all:
            child_nodes = [ nodes[x] for x in pos_hash ]
            child_iter = range(len(child_nodes))
            child_vals = [ uct(current_node, child_nodes[x]) for x in child_iter ]
            highest = max(child_vals)
            highest_index = child_vals.index(highest)
            #print "highest index", highest_index, "highest value", highest
            parent_hash = current_hash
            current_game = child_nodes[highest_index]['game']
        else:
            parent_hash = current_hash
            current_game = random.choice(pos_states)

    return current_game, parent_hash


def add_upwards(nodes, agi_hash, vict_player):
        climb_node = nodes[agi_hash]
        while (climb_node['parent_hash'] is not None):
            climb_node['visits'] = climb_node['visits'] + 1
            climb_node['victories'][vict_player] = climb_node['victories'][vict_player] + 1
            for n in climb_node['game'].all_players():
                if n is not vict_player:
                    climb_node['victories'][n] = climb_node['victories'][n] - 1
            climb_node = nodes[climb_node['parent_hash']]
        climb_node['visits'] = climb_node['visits'] + 1
        climb_node['victories'][vict_player] = climb_node['victories'][vict_player] + 1
        for n in climb_node['game'].all_players():
            if n is not vict_player:
                climb_node['victories'][n] = climb_node['victories'][n] - 1

def MCTS(agi, iteration_number = 130, c = 3.0 ):

        # Always the same, no matter what
        nodes = {}
        uct = uct_factory(c)
        player = agi.move_turn()

        # Intialize tree of game nodes...
        root_hash = agi.hash()
        nodes[root_hash] = make_node(agi, None, initial_visits=1)

        for n in range(iteration_number):
            # Get game node, and parent of game node
            new_agi, agi_parent_hash = get_next(nodes, agi, uct)
            
            # Add...
            if not new_agi.hash() in nodes:
                nodes[new_agi.hash()] = make_node(new_agi, agi_parent_hash) 
            
            # Simulate...
            victory = random_simulation(new_agi, player)
            
            # Backpropogate
            add_upwards(nodes, new_agi.hash(), victory)

        r = nodes[root_hash]
        moves = r['game'].move_list()
        root_children = [ nodes[r['game'].move_immutable(m).hash() ] for m in moves ]
        print sum([ x['visits'] for x in root_children ])
        #print [ x['victories'] for x in root_children ]
        print [ x['visits'] for x in root_children ]
        return softmax([ x['visits'] for x in root_children ]) 



