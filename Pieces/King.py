import os
from Pieces.Piece import Piece

class King(Piece):
   
   NAME = 'King'
     
   def __repr__(self) -> str:
      return self.side + __name__

   def __init__(self, board, position, side, condition = 'Start') -> None:
      super().__init__(board, position, side, condition)
      self.IMG = f"{os.getcwd()}\\imgs\\WhiteKing.png" if self.side == 'White' else f"{os.getcwd()}\\imgs\\BlackKing.png"
      self.check = False
      self.mate = False
   
   def get_moves(self):

      movements = []
      x, y = self.position

      for v in range(x - 1, x + 2):
         for h in range(y - 1, y + 2):
                
            if (v, h) != self.position and (v, h) in self.board.positions.keys():

               pos = self.board.get_pos((v, h))
               pos_threats = pos['threats']
               pos_side = pos['piece'].side if pos['piece'] is not None else None

               if self.side == 'White' and self.side != pos_side and not pos_threats['Black']:
                  movements.append((v, h))

               if self.side == 'Black' and self.side != pos_side and not pos_threats['White']:
                  movements.append((v, h))
                  
               if self.position != pos_side:
                  self.board.positions[(v, h)]['threats'][self.side].append(self)
                  
      if self.condition == 'Start':
         if (x-4, y) in self.board.positions.keys():
            print(x-4, y)
            print(self.board.get_pos((x-4, y))['threats'])
            if self.board.get_pos((x-4, y))['piece'] is not None:
               if self.board.get_pos((x-4, y))['piece'].NAME == 'Rook' and self.board.get_pos((x-4, y))['piece'].side == self.side and self.board.get_pos((x-4, y))['piece'].condition == 'Start':
                  movements.append((x-2, y))
             
            if self.board.get_pos((x+3, y))['piece'] is not None:
               if self.board.get_pos((x-3, y))['piece'].NAME == 'Rook' and self.board.get_pos((x-4, y))['piece'].side == self.side and self.board.get_pos((x-4, y))['piece'].condition == 'Start':
                  movements.append((x+2, y))

      self.movements = movements


      