import os
from Pieces.Piece import Piece

class Knight(Piece):
    
    NAME = 'Knight'

    def __repr__(self) -> str:
        return self.side + __name__
    
    def __init__(self, side, square, condition = 'Start') -> None:
        super().__init__(side, square, condition)
        self.IMG = f"{os.getcwd()}\\imgs\\WhiteKnight.png" if self.side == 'White' else f"{os.getcwd()}\\imgs\\BlackKnight.png"
        
    def get_moves(self):
        
        x, y = self.position
        movements = [
            (x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1),
            (x+1, y-2), (x-1, y-2), (x-2, y-1), (x-2, y+1),
        ]
        
        for x, y in movements.copy():
            if (x, y) in self.board.positions.keys():
                if self.board.get_pos((x, y)).get('piece'):
                    if self.side == self.board.get_pos((x, y))['piece'].side:
                        movements.remove((x, y))
            
            else:
                movements.remove((x, y))
        for move in movements:
            if self not in self.board.positions[move]['threats'][self.side]:
                    self.board.positions[move]['threats'][self.side].append(self)
            
        self.movements = movements
        
    