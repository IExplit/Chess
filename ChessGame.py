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
    
    history = {}
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
                if cnt == 7:
                    rook1 = Rook(board, (x, 1 if side == 'White' else 8), side)
                    rook2 = Rook(board, (x+cnt, 1 if side == 'White' else 8), side)
                    board.add_piece(rook1)
                    board.add_piece(rook2)
                    self.pieces.append(rook1)
                    self.pieces.append(rook2)
                elif cnt == 5:
                    knight1 = Knight(board, (x, 1 if side == 'White' else 8), side)
                    knight2 = Knight(board, (x+cnt, 1 if side == 'White' else 8), side)
                    board.add_piece(knight1)
                    board.add_piece(knight2)
                    self.pieces.append(knight1)
                    self.pieces.append(knight2)
                elif cnt == 3:
                    bishop1 = Bishop(board, (x, 1 if side == 'White' else 8), side)
                    bishop2 = Bishop(board, (x+cnt, 1 if side == 'White' else 8), side)
                    board.add_piece(bishop1)
                    board.add_piece(bishop2)
                    self.pieces.append(bishop1)
                    self.pieces.append(bishop2)
                elif cnt == 1:
                    queen = Queen(board, (x, 1 if side == 'White' else 8), side)
                    king = King(board, (x+cnt, 1 if side == 'White' else 8), side)
                    board.add_piece(queen)
                    board.add_piece(king)
                    self.pieces.append(queen)
                    self.pieces.append(king)
                cnt -= 2
            
            if side == 'White': pl1.alive_pieces = self.pieces.copy()
            elif side == 'Black': pl2.alive_pieces = self.pieces.copy()[16:]
        
    def get_all_pl_moves(self, player):
        for piece in player.alive_pieces:
            if piece.NAME == 'King':
                king = piece
                continue
            piece.get_moves()
        king.get_moves()
            
    def transformation(self, piece, new_piece):
        self.board.remove_piece(piece.position)
        self.board.add_piece()