class Piece:
    
    def __init__(self, board, position, side, condition = 'Start') -> None:
        self.board = board
        self.movements = []

        if side in ['White', 'Black']:
            self.side = side
        
        if condition == 'Start' or condition == 'alive' or condition == 'Die':
            self.condition = condition
        
        if 97 <= position[0] <= 104 and 1 <= position[1] <= 8:
            self.position = position


    def __repr__(self) -> str:
        return __name__


    def move(self, move):
        if move in self.movements and self.condition is not 'Die':
            self.position = move
            self.condition = 'alive'

    
    def kill(self):
        self.condition = 'Die'
