from datetime import date

from ChessBoard import ChessBoard
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Knight import Knight
from Pieces.Queen import Queen
from Player import Player


class ChessGame:
    
    history = []
    pieces = []
    
    def __init__(
        self, board, white_player_name = 'Player1', black_player_name = 'Player2',
        event = '???', site = 'Explit\'s Chess Application', date = date.today(), 
        ):
        
        white_player = Player(white_player_name, 'White')
        black_player = Player(black_player_name, 'Black')
        self.board = board
        self.players = [white_player, black_player]
        self.motion = white_player
        self.event = event
        self.site = site
        self.date = date
    
    
    def arrange_pieces(self):
        board = self.board
        pl1, pl2 = self.players
        for side in ('White', 'Black'):
            cnt = 7
            for x in range(97, 101):
                pawn1 = Pawn(board, (x, 2 if side == 'White' else 7), side)
                pawn2 = Pawn(board, (x+cnt, 2 if side == 'White' else 7), side)
                board.add_piece(pawn1)
                board.add_piece(pawn2)
                self.pieces.append(pawn1)
                self.pieces.append(pawn2)
                print(f'add {pawn1, pawn2}]')
                if cnt == 7:
                    rook1 = Rook(board, (x, 1 if side == 'White' else 8), side)
                    rook2 = Rook(board, (x+cnt, 1 if side == 'White' else 8), side)
                    board.add_piece(rook1)
                    board.add_piece(rook2)
                    self.pieces.append(rook1)
                    self.pieces.append(rook2)
                    print(f'add {rook1, rook2}]')
                elif cnt == 5:
                    knight1 = Knight(board, (x, 1 if side == 'White' else 8), side)
                    knight2 = Knight(board, (x+cnt, 1 if side == 'White' else 8), side)
                    board.add_piece(knight1)
                    board.add_piece(knight2)
                    self.pieces.append(knight1)
                    self.pieces.append(knight2)
                    print(f'add {knight1, knight2}]')
                elif cnt == 3:
                    bishop1 = Bishop(board, (x, 1 if side == 'White' else 8), side)
                    bishop2 = Bishop(board, (x+cnt, 1 if side == 'White' else 8), side)
                    board.add_piece(bishop1)
                    board.add_piece(bishop2)
                    self.pieces.append(bishop1)
                    self.pieces.append(bishop2)
                    print(f'add {bishop1, bishop2}]')
                elif cnt == 1:
                    queen = Queen(board, (x, 1 if side == 'White' else 8), side)
                    king = King(board, (x+cnt, 1 if side == 'White' else 8), side)
                    board.add_piece(queen)
                    board.add_piece(king)
                    self.pieces.append(queen)
                    self.pieces.append(king)
                    print(f'add {queen, king}]')
                cnt -= 2
            
            if side == 'White': pl1.alive_pieces = self.pieces.copy()
            elif side == 'Black': pl2.alive_pieces = self.pieces.copy()[16:]
        
    def get_all_pl_moves(self, player):
        for piece in player.alive_pieces:
            piece.get_moves()
            print(piece.position, piece.movements)
        
    def movement(self, piece, move, transformation = False):
        final_fields = self.board.white_final_fields.copy() + self.board.black_final_fields.copy()
        pl1, pl2 = self.players
        piece.move(move)
        piece.get_moves()
        self.motion = pl2 if self.motion == pl1 else pl1
        self.get_all_pl_moves(self.motion)
            
    def transformation(self, piece, new_piece):
        self.board.remove_piece(piece.position)
        self.board.add_piece()