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
            current_player = None,
            num_moves = 0,
            move_history = ''):

        self.num_moves = num_moves
        self.width = width
        self.height = height
        self.win_length = win_length
        self.players = [1,0]
        self.move_history = move_history
        self.blank_char = '_'
        self.board = Board(width, height, self.blank_char) if board == None else board
        self.current_player = self.players[0] if current_player == None else current_player

    def all_players(self):
        return self.players

    def move_turn(self):
        return self.current_player

    def move_list(self):
        return self.board.free_at_top_indices()

    def move_immutable(self, move_index):
        new_board = self.board.with_moved(move_index, self.current_player)
        new_current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]
        new_num_moves = self.num_moves + 1
        new_move_history = self.move_history + str(self.current_player) + str(move_index)
        return ConnectGame(
                width = self.width,
                height = self.height,
                board = new_board,
                current_player = new_current_player,
                num_moves = new_num_moves,
                move_history = new_move_history)

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

    def hash(self):
        return str(self.board.board) + "_" + str(self.current_player) + "_" + str(self.num_moves) + str(self.move_history)

    def _wins(self):
        return [ self.board.lines_of_length(self.win_length, player) for player in self.players ]



