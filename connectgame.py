#
# A class defining the actual connect four game,
# which should be fed into AbstractGame in order
# to be decorated and have some kind of error checking.
#

from board import Board

class ConnectGame:

    def __init__(self,
            width = 7,
            height = 6,
            win_length = 4,
            board = None,
            current_player = None):

        self.width = width
        self.height = height
        self.win_length = win_length
        self.players = [1,0]
        self.blank_char = '_'
        self.board = Board(width, height, self.blank_char) if board == None else board
        self.current_player = self.players[0] if current_player == None else current_player

    def move_turn(self):
        return self.current_player

    def move_list(self):
        return self.board.free_at_top_indices()

    def move_immutable(self, move_index):
        new_board = self.board.with_moved(move_index, self.current_player)
        new_current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]
        return ConnectGame(
                width = self.width,
                height = self.height,
                board = new_board,
                current_player = new_current_player)

    def game_over(self):
        
        indices = self.board.free_at_top_indices()
        if (len(indices) == 0):
            return True
        
        for win in self._wins():
            if win != 0:
                return True
        
        return False


    def game_winner(self):
        for idx, win in enumerate(self._wins()):
            if win != 0:
                return self.players[idx]
        return None


    def _wins(self):
        return [ self.board.lines_of_length(self.win_length, player) for player in self.players ]



