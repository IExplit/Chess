class ChessGame:
    
    history = []
    pieces = []
    
    def __init__(self, board, player1, player2) -> None:
        self.board = board
        self.player1 = player1
        self.player2 = player2