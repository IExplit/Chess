from Pieces.Piece import Piece

class Knight(Piece):
    
    NAME = 'Knight'
    
    def __init__(self, side, square, condition = 'Start') -> None:
        super().__init__(side, square, condition)
        
    def get_moves(self):
        
        x, y = self.position
        movements = [
            (x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1),
            (x+1, y-2), (x-1, y-2), (x-2, y-1), (x-2, y+1),
        ]
        
        for x, y in movements:
            if (x, y) in self.board.positions.keys():
                if self.board.get_pos((x, y)).get('piece'):
                    if self.side == self.board.get_pos((x, y))['piece'].get('side'):
                        movements.remove((x, y))
            
            else:
                movements.remove((x, y))
        
        for i in movements:
            self.board.positions[i]['threats'][self.side].append(self)
            
        self.movements = movements
        
    