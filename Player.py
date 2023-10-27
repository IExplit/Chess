class Player:
    
    def __init__(self, name, side, alive_pieces = [], dead_pieces = []):
        self.name = name
        self.side = side
        self.alive_pieces = alive_pieces
        self.dead_pieces = dead_pieces