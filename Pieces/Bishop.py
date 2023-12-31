import os

from Pieces.Piece import Piece

class Bishop(Piece):
    
    NAME = 'Bishop'
    
    def __init__(self, side, position, condition = 'Start') -> None:
        super().__init__(side, position, condition)
        self.IMG = f"{os.getcwd()}\\imgs\\WhiteBishop.png" if self.side == 'White' else f"{os.getcwd()}\\imgs\\BlackBishop.png"
        
    def __repr__(self) -> str:
        return f'{self.side}{self.NAME}({self.condition}, {self.position}, {self.movements})'
    
    def __str__(self):
        x, y, = self.position
        x =  chr(x)
        return f'B{x}{y}'

    def get_moves(self):
        
        movements = []
        x, y = self.position
        start_points = [(x-1, y+1), (x+1, y+1), (x+1, y-1), (x-1, y-1)]
        
        for i in range(3, 7):
            x, y = start_points[i-3]

            while (x, y) in self.board.positions.keys() \
                and not (self.board.get_pos((x, y)).get('piece') and self.side == self.board.get_pos((x, y))['piece'].side):
                if self.board.get_pos((x, y)).get('piece') and self.side != self.board.get_pos((x, y))['piece'].side:
                    movements.append((x, y))
                    self.board.positions[(x, y)]['threats'][self.side].append(self)
                    break
                if self not in self.board.positions[(x, y)]['threats'][self.side]:
                    self.board.positions[(x, y)]['threats'][self.side].append(self)
                movements.append((x, y))
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
        
    