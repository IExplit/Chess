from Pieces.Piece import Piece


class King(Piece):
     
   def __repr__(self) -> str:
      return self.side + __name__

   def __init__(self, board, position, side, condition = 'Start') -> None:
      super().__init__(board, position, side, condition)
      self.check = False
      self.mate = False
   
   def get_moves(self):
      print(True)

      movements = []
      x, y = self.position

      for v in range(x - 1, x + 2):
         for h in range(y - 1, y + 2):

            print(self.position)
            print((v, h))
                
            if (v, h) != self.position and (v, h) in self.board.positions.keys():
               print(True)

               pos = self.board.get_pos((v, h))
               pos_treats = pos['treats']
               pos_side = pos['piece'].get('side') if pos['piece'] is not None else None

               if self.side == 'White' and self.side != pos_side and not pos_treats['Black']:
                  movements.append((v, h))

               if self.side == 'Black' and self.side != pos_side and not pos_treats['White']:
                  movements.append((v, h))

      self.movements = movements


      