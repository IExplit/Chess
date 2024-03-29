import os
from Pieces.Piece import Piece

class King(Piece):
   
   NAME = 'King'
   
   def __init__(self, board, position, side, condition = 'Start') -> None:
      super().__init__(board, position, side, condition)
      self.IMG = f"{os.getcwd()}\\imgs\\WhiteKing.png" if self.side == 'White' else f"{os.getcwd()}\\imgs\\BlackKing.png"
      self.check = False
      self.mate = False
   
   def __repr__(self) -> str:
        return f'{self.side}{self.NAME}({self.condition}, check = {self.check}, {self.position}, {self.movements})'
    
   def __str__(self):
      x, y, = self.position
      x =  chr(x)
      return f'K{x}{y}'
   
   def get_moves(self):

      movements = []
      attacked_pos = []
      x, y = self.position

      for v in range(x - 1, x + 2):
         for h in range(y - 1, y + 2):
                
            if (v, h) != self.position and (v, h) in self.board.positions.keys():

               pos = self.board.get_pos((v, h))
               pos_threats = pos['threats']
               pos_side = pos['piece'].side if pos['piece'] is not None else None

               if self.side == 'White' and self.side != pos_side and not pos_threats['Black']:
                  movements.append((v, h))
                  attacked_pos.append((v, h))

               if self.side == 'Black' and self.side != pos_side and not pos_threats['White']:
                  movements.append((v, h))
                  attacked_pos.append((v, h))

               if self.side != pos_side:
                  self.board.positions[(v, h)]['threats'][self.side].append(self)
                  
      if self.condition == 'Start':
         if (x-4, y) in self.board.positions.keys():
            if self.board.get_pos((x-4, y))['piece'] is not None and not self.board.get_pos((x-2, y))['piece'] and not self.board.get_pos((x-1, y))['piece']:
               if self.board.get_pos((x-4, y))['piece'].NAME == 'Rook' and self.board.get_pos((x-4, y))['piece'].side == self.side and self.board.get_pos((x-4, y))['piece'].condition == 'Start':
                  movements.append((x-2, y))
             
            if self.board.get_pos((x+3, y))['piece'] is not None and not self.board.get_pos((x+2, y))['piece'] and not self.board.get_pos((x+1, y))['piece']:
               if self.board.get_pos((x+3, y))['piece'].NAME == 'Rook' and self.board.get_pos((x-4, y))['piece'].side == self.side and self.board.get_pos((x-4, y))['piece'].condition == 'Start':
                  movements.append((x+2, y))
      
      self.attacked_pos = attacked_pos
      self.movements = movements

   def move(self, move):
      x, y = self.position
      x_move, y_move = move
      if move in self.movements and self.condition is not 'Die':
         if self.condition == 'Start' and move not in self.attacked_pos:
            if (x-2, y) == move:
               rook_coords = (x-4, y)
               rook = self.board.get_pos(rook_coords)['piece']
               rook_coords = (x-4+2, y)
            elif (x+2, y) == move:
               rook_coords = (x+3, y)
               rook = self.board.get_pos(rook_coords)['piece']
               rook_coords = (x+3-2, y)
            rook.move(rook_coords)
         self.board.remove_piece(self.position)
         self.position = move
         self.condition = 'Alive'
         self.board.add_piece(self)

      