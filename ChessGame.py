from datetime import date

class ChessGame:
    
    players = []
    motion = None
    history = []
    pieces = []
    
    def __init__(
        self, board, player1, player2,
        event = '???', site = 'Explit\'s Chess Application', date = date(), 
        ):
        self.board = board
        self.players.append(player1)
        self.players.append(player2)
        self.event = event
        self.site = site
        self.date = date
        