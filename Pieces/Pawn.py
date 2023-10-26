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

            attacked_pos = []
            for v, h in [(x - 1, y + 1), (x + 1, y + 1)]:
                if (v, h) in self.board.positions.keys():
                    attacked_pos.append((v, h))

            if (v, h) in self.board.positions.keys() and self.board.get_pos((x, y + 1))['piece'] == None:
                movements.append((x, y + 1))

                if self.condition == 'Start':
                    movements.append((x, y + 2))

            for v, h in attacked_pos:

                if (v, h) in self.board.positions.keys():
                    
                    self.board.positions[(v, h)]['threats']['White'].append(self)

                    if self.board.get_pos((v, h))['piece'] != None \
                        or (self.board.get_pos((v, h - 1))['piece'] != None \
                            and self.board.get_pos((v, h - 1))['piece'].__dict__.get('did_long_move')) == True:
                        movements.append((v, h))
        
        elif self.side == 'Black':
            
            attacked_pos = []
            for v, h in [(x - 1, y - 1), (x + 1, y - 1)]:
                if (v, h) in self.board.positions.keys():
                    attacked_pos.append((v, h))

            if (v, h) in self.board.positions.keys() and self.board.get_pos((x, y - 1))['piece'] == None:
                movements.append((x, y - 1))

                if self.condition == 'Start':
                    movements.append((x, y - 2))

            for v, h in attacked_pos:
                if (v, h) in self.board.positions.keys():
                    self.board.positions[(v, h)]['threats']['Black'].append(self)

                    if self.board.get_pos((v, h))['piece'] != None \
                        or (self.board.get_pos((v, h + 1))['piece'] != None \
                            and self.board.get_pos((v, h + 1))['piece'].__dict__.get('did_long_move')) == True:
                        movements.append((v, h))
        
        self.attacked_pos = attacked_pos
        self.movements = movements
    
    def move(self, move):
        
        if move in self.movements and self.condition is not 'Die':
            
            _, y1 = self.position
            _, y2 = move

            if abs(y1-y2) == 2:
                self.did_long_move = True
            else:
                self.did_long_move = False
                
            self.board.remove_piece(self.position)
            self.position = move
            self.condition = 'Alive'
            self.board.add_piece(self)
