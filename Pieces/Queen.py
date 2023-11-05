import os

from Pieces.Piece import Piece
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop


class Queen(Piece):
    
    NAME = 'Queen'

    def __init__(self, side, square, condition = 'Start') -> None:
        super().__init__(side, square, condition)
        self.IMG = f"{os.getcwd()}\\imgs\\WhiteQueen.png" if self.side == 'White' else f"{os.getcwd()}\\imgs\\BlackQueen.png"
        
    def get_moves(self):
        
        rook = Rook(self.board, self.position, self.side)
        bishop = Bishop(self.board, self.position, self.side)
        rook.get_moves()
        bishop.get_moves()
        movements = rook.movements + bishop.movements
        for pos in movements:
            self.board.positions[pos]['threats'][self.side].append(self)
        self.movements = movements
        
        