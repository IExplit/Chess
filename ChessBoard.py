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
        threats = piece.attacked_pos if piece.NAME == 'Pawn' else piece.movements
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


board = ChessBoard()
r = Pawn(board, (104, 2), 'White')

board.add_piece(r)
r.get_moves()
print(r.movements)





"""board = ChessBoard()
board.add_piece(Pawn(board, (99, 5), 'Black', condition='Alive'))
board.add_piece(Pawn(board, (97, 5), 'Black', condition='Alive'))
board.add_piece(Pawn(board, (98, 4), 'White', condition='Alive'))
board.positions[(99, 5)]['piece'].get_moves()
board.positions[(97, 5)]['piece'].get_moves()
board.positions[(98, 4)]['piece'].get_moves()

print(board.positions[(99, 5)]['piece'].movements)
print(board.positions[(97, 5)]['piece'].movements)
print(board.positions[(98, 4)]['piece'].movements)
print('-----------')

board.add_piece(Pawn(board, (102, 5), 'White', condition='Alive'))
board.add_piece(Pawn(board, (103, 5), 'Black', condition='Alive', did_long_move=True))
board.positions[(102, 5)]['piece'].get_moves()
board.positions[(103, 5)]['piece'].get_moves()
print(board.positions[(102, 5)]['piece'].movements)
print(board.positions[(103, 5)]['piece'].movements)

print('-----------')
board.add_piece(Pawn(board, (100, 7), 'Black'))
board.add_piece(Pawn(board, (100, 2), 'White'))
board.positions[(100, 7)]['piece'].get_moves()
board.positions[(100, 2)]['piece'].get_moves()
print(board.positions[(100, 7)]['piece'].movements)
print(board.positions[(100, 2)]['piece'].movements)

print('-----------')
print(board.positions[(100, 2)])
print(board.positions[(99, 3)])
print(board.positions[(101, 3)])

print('-----------')
board.remove_piece((100, 2))
print(board.positions[(100, 2)])
print(board.positions[(99, 3)])
print(board.positions[(101, 3)])
print(board.positions[(101, 3)])

print('-----------')"""

"""board2 = ChessBoard()
kng1 = King(board2, (100, 6), 'White')
pwn1b = Pawn(board2, (100, 7), 'Black')
pwn1w = Pawn(board2, (100, 5), 'White')
board2.add_piece(kng1)
board2.add_piece(pwn1b)
board2.add_piece(pwn1w)
board2.positions[(100, 7)]['piece'].get_moves()
board2.positions[(100, 6)]['piece'].get_moves()
print(board2.positions[(99, 6)])
print(board2.positions[(101, 6)])
print(board2.positions[(100, 7)]['piece'].attacked_pos)
print(board2.positions[(100, 6)]['piece'].movements)
"""