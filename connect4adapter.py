
#
#
# Goal of this is to get output from the compare function 
# and turn it into something that is easy to train off.  I.e.,
# into something that
#
#

def connect4adapter_single(game, perspective=None):

    if perspective is None:
        perspective = game.move_turn()
    else:
        perspective = 1

    def convert(spot):
        if spot == '_':
            return 0.0
        if spot == perspective:
            return 1.0
        else:
            return -1.0
        raise Error("Failed to find what expected")
    
    return [ [ convert(y) for y in x ] for x in game.instance.board.board ]

def connect4adapter_value(record):

    X = []
    Y = []
    perspective = 1
    for game, outcome in record:
        for stateAndDistribution in game:
            state = stateAndDistribution[0]
            X.append(connect4adapter_single(state, perspective))
            Y.append(
                1 if outcome == perspective else -1
            )
    return X, Y
