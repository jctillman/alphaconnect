#
# General interface for games, so that I can 
# extend results from AlphaConnect Zero to 
# other things without a great deal of work.
#

from checks import check_for_method, check_is

class AbstractGame:

    def __init__(self, game_instance):
        self.instance = game_instance

        check_for_method("move_turn")
        check_for_method("move_list")
        check_for_method("move_immutable")
        check_for_method("game_over")
        check_for_method("game_winner")

    def move_turn(self):
        return check_is(int, self.instance.move_turn())

    def move_list(self):
        return check_is(list, self.instance.move_list())

    def move_immutable(self, move):
        return self.instance.move_immutable(move)

    def game_over(self):
        return check_is(bool, self.instance.game_over())

    def game_winner(self):
        return self.instance.game_winner())
    
    def move_mutable(self, move):
        self.instance = self.instance.move_immutable(move)
        return None
