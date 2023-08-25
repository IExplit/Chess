from Pieces.Pawn import Pawn
from Pieces.King import King


class ChessBoard:

    white_final_fields = []
    black_final_fields = []

    def __init__(self) -> None:

        self.positions = {}
        
        for vertical in range(97, 105):
            for horizontal in range(1, 9):

                self.positions[(vertical, horizontal)] = {
                    'piece': None,
                    'treats': {
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
                'piece': piece.__dict__ if piece != None else None,
                'treats': self.positions[position]['treats']
            }

    def add_piece(self, piece):
        if piece.position in self.positions.keys():
            self.positions[piece.position]['piece'] = piece

    def remove_piece(self, position):
        piece = self.positions[position]['piece']
        treats = piece.attacked_pos if piece.NAME == 'Pawn' else piece.movements
        side = piece.side

        for treat in treats:
            self.positions[treat]['treats'][side].remove(piece)

        self.positions[position]['piece'] = None


"""board = ChessBoard()
board.add_piece(Pawn(board, (99, 5), 'Black', condition='alive'))
board.add_piece(Pawn(board, (97, 5), 'Black', condition='alive'))
board.add_piece(Pawn(board, (98, 4), 'White', condition='alive'))
board.positions[(99, 5)]['piece'].get_moves()
board.positions[(97, 5)]['piece'].get_moves()
board.positions[(98, 4)]['piece'].get_moves()

print(board.positions[(99, 5)]['piece'].movements)
print(board.positions[(97, 5)]['piece'].movements)
print(board.positions[(98, 4)]['piece'].movements)
print('-----------')

board.add_piece(Pawn(board, (102, 5), 'White', condition='alive'))
board.add_piece(Pawn(board, (103, 5), 'Black', condition='alive', did_long_move=True))
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

board2 = ChessBoard()
board2.add_piece(Pawn(board2, (100, 7), 'Black'))
board2.add_piece(King(board2, (100, 6), 'White'))
board2.positions[(100, 7)]['piece'].get_moves()
board2.positions[(100, 6)]['piece'].get_moves()
print(board2.positions[(99, 6)])
print(board2.positions[(101, 6)])
print(board2.positions[(100, 7)]['piece'].attacked_pos)
print(board2.positions[(100, 6)]['piece'].movements)
