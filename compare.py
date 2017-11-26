#
# Compare takes in two agents, and 
# an even number, N
#
# It has the two agents play N
# games, alternating who moves first.
# It returns the number of wins they make, and
# a complete record of the states that occurred while
# they were playing.
# 
# Used, of course, for comparing agents.
#
import numpy
from utils import softmax

def compare(one, two, times, game_creator, verbose = False):

    one_wins = 0
    two_wins = 0
    record = []

    def show(n):
        if verbose:
            print n

    for n in range(times):
        show("Playing game " + str(n))
        g = game_creator()
        player_agent_map = {}
        players = g.all_players()
        states = [g]       
        
        if n % 2 == 0:
             player_agent_map[players[0]] = one
             player_agent_map[players[1]] = two
        else:
             player_agent_map[players[1]] = one
             player_agent_map[players[0]] = two

        while not g.game_over():
            current_agent = player_agent_map[g.move_turn()]
            current_move = current_agent.move(g)
            g = g.move_immutable(current_move)
            states.append(g)			

        winner = g.game_winner()
        if n % 2 == 0 and winner == players[0]:
            one_wins += 1
            show("agent one wins")        
        elif n % 2 == 1 and winner == players[1]:
            one_wins += 1
            show("agent one wins")
        elif n % 2 == 0 and winner == players[1]:
            two_wins += 1
            show("agent two wins")
        elif n % 2 == 1 and winner == players[0]:
            two_wins += 1
            show("agent_two wins")
        
        record.append([ states, g.game_winner() ])

    return one_wins, two_wins

