from Piece import Piece

class Rook(Piece):

    def __init__(self, side, square, condition = 'Start') -> None:
        super().__init__(side, square, condition)