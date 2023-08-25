from Pieces.Piece import Piece

class Pawn(Piece):

    NAME = 'Pawn'

    def __repr__(self) -> str:
        return self.side + __name__


    def __init__(self, board, position, side, condition = 'Start', did_long_move = False) -> None:
        super().__init__(board, position, side, condition)
        self.did_long_move = did_long_move

    
    def get_moves(self):
        movements = []
        attacked_pos = []
        x, y = self.position

        if self.side == 'White':

            attacked_pos = [(x - 1, y + 1), (x + 1, y + 1)]

            if self.board.get_pos((x, y + 1))['piece'] == None:
                movements.append((x, y + 1))

                if self.condition == 'Start':
                    movements.append((x, y + 2))

            for v, h in attacked_pos:

                if (v, h) in self.board.positions.keys():
                    
                    self.board.positions[(v, h)]['treats']['White'].append(self)

                    if self.board.get_pos((v, h))['piece'] != None \
                        or (self.board.get_pos((v, h - 1))['piece'] != None \
                            and self.board.get_pos((v, h - 1))['piece'].get('did_long_move')) == True:
                        movements.append((v, h))
        
        elif self.side == 'Black':

            attacked_pos = [(x - 1, y - 1), (x + 1, y - 1)]

            if self.board.get_pos((x, y - 1))['piece'] == None:
                movements.append((x, y - 1))

                if self.condition == 'Start':
                    movements.append((x, y - 2))

            for v, h in attacked_pos:
                print(v, h)
                if (v, h) in self.board.positions.keys():
                    self.board.positions[(v, h)]['treats']['Black'].append(self)

                    if self.board.get_pos((v, h))['piece'] != None \
                        or (self.board.get_pos((v, h + 1))['piece'] != None \
                            and self.board.get_pos((v, h + 1))['piece'].get('did_long_move')) == True:
                        movements.append((v, h))
        
        self.attacked_pos = attacked_pos
        self.movements = movements
