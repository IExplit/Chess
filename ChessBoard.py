from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Knight import Knight
from Pieces.Queen import Queen


class ChessBoard:

    white_final_fields = []
    black_final_fields = []

    def __init__(self) -> None:

        self.positions = {}
        
        for vertical in range(97, 105):
            for horizontal in range(1, 9):

                self.positions[(vertical, horizontal)] = {
                    'piece': None,
                    'threats': {
                        'White': [],
                        'Black': []
                    }
                }
                
                if horizontal == 8:
                    self.white_final_fields.append((vertical, horizontal))
                
                elif horizontal == 1:
                    self.black_final_fields.append((vertical, horizontal))

    def get_pos(self, position):
        if position in self.positions.keys():
            piece = self.positions[position]['piece']
            return {
                'piece': piece,
                'threats': self.positions[position]['threats']
            }

    def add_piece(self, piece):
        if piece.position in self.positions.keys():
            self.positions[piece.position]['piece'] = piece

    def remove_piece(self, position):
        piece = self.positions[position]['piece']
        name = piece.NAME
        threats = piece.attacked_pos if name == 'Pawn' or name == 'King' else piece.movements
        side = piece.side

        for threat in threats:
            self.positions[threat]['threats'][side].remove(piece)

        self.positions[position]['piece'] = None
        
    def arrange_pieces(self):
        for side in ('White', 'Black'):
            cnt = 7
            for x in range(97, 101):
                self.add_piece(Pawn(self, (x, 2 if side == 'White' else 7), side))
                self.add_piece(Pawn(self, (x+cnt, 2 if side == 'White' else 7), side))
                if cnt == 7:
                    self.add_piece(Rook(self, (x, 1 if side == 'White' else 8), side))
                    self.add_piece(Rook(self, (x+cnt, 1 if side == 'White' else 8), side))
                elif cnt == 5:
                    self.add_piece(Knight(self, (x, 1 if side == 'White' else 8), side))
                    self.add_piece(Knight(self, (x+cnt, 1 if side == 'White' else 8), side))
                elif cnt == 3:
                    self.add_piece(Bishop(self, (x, 1 if side == 'White' else 8), side))
                    self.add_piece(Bishop(self, (x+cnt, 1 if side == 'White' else 8), side))
                elif cnt == 1:
                    self.add_piece(Queen(self, (x, 1 if side == 'White' else 8), side))
                    self.add_piece(King(self, (x+cnt, 1 if side == 'White' else 8), side))
                cnt -= 2
