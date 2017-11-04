#
# Support dropping on the board, recording where
# things are, adding 
#

from checks import check_for_method, check_is
from copy import deepcopy

class Board:

    def __init__(self,
            width = 7,
            height = 6,
            blank_char = '_',
            replacement = None):
        self.board =  (
                [ [blank_char] * width for i in range(height) ]
                if replacement == None
                else replacement)
        self.blank_char = blank_char
        self.width = width
        self.height = height

    def with_moved(self, move_index, piece):
        tmp = deepcopy(self.board)
        drop_index = None
        for i in range(0, self.height):
            if self.board[i][move_index] == self.blank_char:
                drop_index = i

        if drop_index == None:
            raise RuntimeError("You cannot move in drop index {0}".format(drop_index))
                    
        tmp[drop_index][move_index] = piece

        return Board(self.width, self.height, self.blank_char, tmp)


    def free_at_top_indices(self):
        return [ idx for idx, value in enumerate(self.board[0]) if value == self.blank_char ]

    def lines_of_length(self, length, player):
        return (self.horizontal_lines_of_length(length, player) +
            self.vertical_lines_of_length(length, player) + 
            self.diag_one_lines_of_length(length, player) +
            self.diag_two_lines_of_length(length, player))
    
    def horizontal_lines_of_length(self, length, player):
        total = 0
        for i in range(length, self.width+1):
            for ii in range(0, self.height):
                all_player = self.board[ii][i-length: i]
                if all(map(lambda x: x == player, all_player)):
                    total = total + 1
        return total
   
    def vertical_lines_of_length(self, length, player):
        total = 0
        for i in range(length - 1, self.height):
            for ii in range(0, self.width):
                all_player = [ self.board[i-iii][ii] for iii in range(length) ]
                if all(map(lambda x: x == player, all_player)):
                    total = total + 1
        return total

    def diag_one_lines_of_length(self, length, player):
        total = 0
        for i in range(length - 1, self.height):
            for ii in range(length - 1, self.width):
                all_player = [ self.board[i - iii][ii - iii] for iii in range(length) ]
                if all(map(lambda x: x == player, all_player)):
                    total = total + 1
        return total
    
    def diag_two_lines_of_length(self, length, player):
        total = 0
        for i in range(length - 1, self.height):
            for ii in range(0, self.width - length + 1):
                all_player = [ self.board[i - iii][ii + iii] for iii in range(length) ]
                if all(map(lambda x: x == player, all_player)):
                    total = total + 1
        return total


