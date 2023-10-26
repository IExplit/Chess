class Player:
    
    def __init__(self, name, side, alive_pieces, died_pieces, time) -> None:
        self.name = name
        self.side = side
        self.alive_pieces = alive_pieces
        self.died_pieces = died_pieces
        self.time = time