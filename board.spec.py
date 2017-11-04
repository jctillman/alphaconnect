#
# Testing the "board" class
#
import unittest
from board import Board

class TestBoard(unittest.TestCase):

        def test_board_creation_new(self):
            a = Board(8,7,'*')
            self.assertTrue(a.width == 8)
            self.assertTrue(a.height == 7)
            self.assertTrue(a.blank_char == '*')

        def test_board_creation_new_default(self):
            a = Board()
            self.assertTrue(a.width == 7)
            self.assertTrue(a.height == 6)
            self.assertTrue(a.blank_char == '_')


        def test_board_creation_new_replacement(self):
            tmp = [ ['*'] * 7 for i in range(6) ]
            a = Board(7,6,'_', tmp)
            self.assertTrue(a.board == tmp)

        def test_board_free_at_top_indices(self):
            tmp = [
                    ['_','#','#','#','#','_','#'],
                    ['_','#','#','#','#','_','#'],
                    ['_','#','#','#','#','_','#'],
                    ['_','#','#','#','#','_','#'],
                    ['_','#','#','#','#','_','#'],
                    ['_','#','#','#','#','_','#'],
            ]
            a = Board(7,6,'_', tmp)
            self.assertEqual(a.free_at_top_indices(), [0,5])
            b = Board(7,6,'#', tmp)
            self.assertEqual(b.free_at_top_indices(), [1,2,3,4,6])

        def test_board_with_moved(self):
            tmp = [
                    ['_','_','_','_','_','_','_'],
                    ['_','_','_','_','_','_','_'],
                    ['_','_','_','_','_','_','_'],
                    ['_','_','_','_','_','_','_'],
                    ['r','_','_','_','_','_','_'],
                    ['b','r','_','_','_','_','b'],
            ]
            a = Board(7,6,'_')
            b = a.with_moved(1,'r')
            c = b.with_moved(0,'b')
            d = c.with_moved(0,'r')
            e = d.with_moved(6,'b')
            self.assertEqual(tmp, e.board)

        def test_board_horizontal_lines(self):
            tmp = [
                    ['_','_','_','r','r','r','r'],
                    ['_','_','_','r','b','b','b'],
                    ['_','_','_','b','b','b','b'],
                    ['_','_','r','r','r','r','r'],
                    ['r','r','r','r','b','b','b'],
                    ['b','r','b','r','r','r','r'],
            ]
            a = Board(7,6,'_', tmp)
            self.assertEqual(a.horizontal_lines_of_length(4,'r'),5)
            self.assertEqual(a.horizontal_lines_of_length(5,'r'),1)
            self.assertEqual(a.horizontal_lines_of_length(4,'b'),1)
            self.assertEqual(a.horizontal_lines_of_length(5,'b'),0)
        
        def test_board_vertical_lines(self):
            tmp = [
                    ['r','_','_','_','_','b','r'],
                    ['r','_','_','_','_','b','r'],
                    ['r','r','_','_','_','b','r'],
                    ['b','r','b','_','_','b','r'],
                    ['r','r','r','_','_','r','b'],
                    ['r','r','b','r','_','r','b'],
            ]
            a = Board(7,6,'_', tmp)
            self.assertEqual(a.vertical_lines_of_length(2,'r'),10)
            self.assertEqual(a.vertical_lines_of_length(3,'r'),5)
            self.assertEqual(a.vertical_lines_of_length(4,'r'),2)
            self.assertEqual(a.vertical_lines_of_length(2,'b'),4)
            self.assertEqual(a.vertical_lines_of_length(3,'b'),2)

        def test_board_diag_one_lines(self):
            tmp = [
                    ['r','_','_','_','_','r','r'],
                    ['r','r','_','_','_','r','r'],
                    ['d','r','r','_','_','r','r'],
                    ['b','b','b','_','_','r','r'],
                    ['b','b','b','_','b','b','b'],
                    ['b','b','b','_','b','b','b'],
            ]
            a = Board(7,6,'_', tmp)
            self.assertEqual(a.diag_one_lines_of_length(3,'r'),1)
            self.assertEqual(a.diag_one_lines_of_length(2,'r'),6)
            self.assertEqual(a.diag_one_lines_of_length(3,'b'),1)
            self.assertEqual(a.diag_one_lines_of_length(2,'b'),6)
        
        def test_board_diag_two_lines(self):
            tmp = [
                    ['r','_','_','_','_','r','r'],
                    ['r','r','_','_','_','r','r'],
                    ['d','r','r','_','_','r','r'],
                    ['b','b','b','_','_','r','r'],
                    ['b','b','b','_','b','b','b'],
                    ['b','b','b','_','b','b','b'],
            ]
            a = Board(7,6,'_', tmp)
            self.assertEqual(a.diag_two_lines_of_length(3,'r'),0)
            self.assertEqual(a.diag_two_lines_of_length(2,'r'),3)
            self.assertEqual(a.diag_two_lines_of_length(3,'b'),1)
            self.assertEqual(a.diag_two_lines_of_length(2,'b'),6)


        def test_board_lines(self):
            tmp = [
                    ['r','_','_','r','_','r','b'],
                    ['r','r','_','r','_','r','b'],
                    ['r','r','r','r','_','b','b'],
                    ['b','b','r','r','r','r','b'],
                    ['b','r','b','b','b','r','b'],
                    ['r','b','b','b','b','b','r'],
            ]
            a = Board(7,6,'_', tmp)
            self.assertEqual(a.lines_of_length(4,'r'),6)
            self.assertEqual(a.lines_of_length(4,'b'),4)

if __name__ == '__main__':
    unittest.main()

