

#
# DONE
# Needed -- a an agent abstraction that
# can be constructed USING 
# 1) MCTS only
# 2) Neural networks only
# 3) A combo of MCTS and neural networks.
#
# Should really just be a wrapper over a function 
# that takes the a board set, and returns a move
#

# DONE
#
# Adapter to take the output of the above and put it into tensorflow stuff.
#


# A NN that takes something from the output, and can either
# be trained or have some kind of output.


# Something that, in sequence, does this
# 1. Initializes some kind of neural network, and repeatedly

# a. Runs a MCTS against itself, using the above NN to evaluate initial states.
#    Keep random move temperature HIGHER during training.
#
# b. Train NN on value data from the date generated in a.
#
# c. To keep score, train success rate of newly-trained
#    item against a vanilla MCTS, using more rollouts.
#    Something like 250 rollouts (5) games and 750 rollouts (another 5 games)

# So for each of these, we're going to have many cases of
# several agents playing each other, then recording what proportion each wins,
# or which wins.  So some kind of solid "playing each other"
# abstraction is going to be important.
  
