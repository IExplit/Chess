from Pieces.Piece import Piece

class Bishop(Piece):
    
    NAME = 'Bishop'
    
    def __init__(self, side, square, condition = 'Start') -> None:
        super().__init__(side, square, condition)
        
    def get_moves(self):
        
        movements = []
        x, y = self.position
        start_points = [(x-1, y+1), (x+1, y+1), (x+1, y-1), (x-1, y-1)]
        
        for i in range(3, 7):
            x, y = start_points[i-3]

            while (x, y) in self.board.positions.keys():
                if self.board.get_pos((x, y)).get('piece') and self.side != self.board.get_pos((x, y))['piece']['side']:
                    movements.append((x, y))
                    break
                if self.board.get_pos((x, y)).get('piece') and self.side == self.board.get_pos((x, y))['piece']['side']:
                    break
                movements.append((x, y))
                self.board.positions[(x, y)]['threats'][self.side].append(self)
                if i % 2 != 0:
                    if i % 3 == 0:
                        x -= 1
                        y += 1
                    elif i % 3 != 0:
                        x += 1
                        y -= 1
                elif i % 2 == 0:
                    if i % 3 == 0:
                        x -= 1
                        y -= 1
                    elif i % 3 != 0:
                        y += 1
                        x += 1
                        
        self.movements = movements
        
    