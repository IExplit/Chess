import os

from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QTableView

class GameWindow(QWidget):
    def __init__(self, game = None):
        super().__init__()
        
        self.game = game
        self.pieces = {}
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('Chess')
        self.setFixedSize(1210, 700)
        
        self.btn_first_pos = QPushButton(self)
        self.btn_first_pos.setGeometry(750, 220-40, 90, 40)
        self.btn_first_pos.setText('<<')
        
        self.btn_prev_pos = QPushButton(self)
        self.btn_prev_pos.setGeometry(750+90, 220-40, 90, 40)
        self.btn_prev_pos.setText('<')
        
        self.btn_next_pos = QPushButton(self)
        self.btn_next_pos.setGeometry(750+90*2, 220-40, 90, 40)
        self.btn_next_pos.setText('>')
        
        self.btn_last_pos = QPushButton(self)
        self.btn_last_pos.setGeometry(750+90*3, 220-40, 90, 40)
        self.btn_last_pos.setText('>>')
        
        self.btn_return = QPushButton(self)
        self.btn_return.setGeometry(750, 220+260, 90, 40)
        self.btn_return.setText('<--')
        
        self.btn_draw = QPushButton(self)
        self.btn_draw.setGeometry(750+90, 220+260, 90, 40)
        self.btn_draw.setText('1/2')
        
        self.btn_surrender = QPushButton(self)
        self.btn_surrender.setGeometry(750+90*2, 220+260, 90, 40)
        self.btn_surrender.setText('###')
        
        self.btn_flip = QPushButton(self)
        self.btn_flip.setGeometry(750+90*3, 220+260, 90, 40)
        self.btn_flip.setText('˄˅')
        
        self.history_tbl = QTableView(self)
        self.history_tbl.setGeometry(750, 220, 360, 260)
        
        self.lbl_player1 = QLabel(self)
        self.lbl_player1.setGeometry(750, 220+260+40*2, 90*3, 40)
        self.lbl_player1.setStyleSheet("QLabel{font-size: 30pt;}")
        self.lbl_player1.setText('Player1')
        
        self.lbl_player2 = QLabel(self)
        self.lbl_player2.setGeometry(750, 220-40*3, 90*3, 40)
        self.lbl_player2.setStyleSheet("QLabel{font-size: 30pt;}")
        self.lbl_player2.setText('Player2')
        
        self.lbl_board = QLabel(self)
        self.lbl_board.setGeometry(50, 50, 600, 600)
        self.pixmap_board = QPixmap(f"{os.getcwd()}\\imgs\\Board.png")
        self.lbl_board.setPixmap(self.pixmap_board.scaledToWidth(600))
        
        
        for piece in self.game.players[1].alive_pieces + self.game.players[0].alive_pieces:
            print(piece.side, piece.IMG)
            self.pieces[piece] = QLabel(self)
            self.pieces[piece].setGeometry(50+75*abs(piece.position[0]-97), 50+75*abs(8-piece.position[1]), 75, 75)
            pixmap = QPixmap(piece.IMG)
            self.pieces[piece].setPixmap(pixmap.scaledToWidth(75))
        
        
        
        
        
        
        
        
        
        
        
        
        """------------------------------------"""
        
        self.lbl_char_a = QLabel(self)
        self.lbl_char_a.setGeometry(52, 650-25, 20, 25)
        self.lbl_char_a.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_a.setText('a')
        
        self.lbl_char_b = QLabel(self)
        self.lbl_char_b.setGeometry(52+75, 650-25, 20, 25)
        self.lbl_char_b.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_b.setText('b')
        
        self.lbl_char_c = QLabel(self)
        self.lbl_char_c.setGeometry(52+75*2, 650-25, 20, 25)
        self.lbl_char_c.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_c.setText('c')
        
        self.lbl_char_d = QLabel(self)
        self.lbl_char_d.setGeometry(52+75*3, 650-25, 20, 25)
        self.lbl_char_d.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_d.setText('d')
        
        self.lbl_char_e = QLabel(self)
        self.lbl_char_e.setGeometry(52+75*4, 650-25, 20, 25)
        self.lbl_char_e.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_e.setText('e')
        
        self.lbl_char_f = QLabel(self)
        self.lbl_char_f.setGeometry(52+75*5, 650-25, 20, 25)
        self.lbl_char_f.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_f.setText('f')
        
        self.lbl_char_g = QLabel(self)
        self.lbl_char_g.setGeometry(52+75*6, 650-25, 20, 25)
        self.lbl_char_g.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_g.setText('g')
        
        self.lbl_char_h = QLabel(self)
        self.lbl_char_h.setGeometry(52+75*7, 650-25, 20, 25)
        self.lbl_char_h.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_h.setText('h')
        
        self.lbl_char_1 = QLabel(self)
        self.lbl_char_1.setGeometry(50+75*8-15, 650-75, 20, 25)
        self.lbl_char_1.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_1.setText('1')
        
        self.lbl_char_2 = QLabel(self)
        self.lbl_char_2.setGeometry(50+75*8-15, 650-75*2, 20, 25)
        self.lbl_char_2.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_2.setText('2')
        
        self.lbl_char_3 = QLabel(self)
        self.lbl_char_3.setGeometry(50+75*8-15, 650-75*3, 20, 25)
        self.lbl_char_3.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_3.setText('3')
        
        self.lbl_char_4 = QLabel(self)
        self.lbl_char_4.setGeometry(50+75*8-15, 650-75*4, 20, 25)
        self.lbl_char_4.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_4.setText('4')
        
        self.lbl_char_5 = QLabel(self)
        self.lbl_char_5.setGeometry(50+75*8-15, 650-75*5, 20, 25)
        self.lbl_char_5.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_5.setText('5')
        
        self.lbl_char_6 = QLabel(self)
        self.lbl_char_6.setGeometry(50+75*8-15, 650-75*6, 20, 25)
        self.lbl_char_6.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_6.setText('6')
        
        self.lbl_char_7 = QLabel(self)
        self.lbl_char_7.setGeometry(50+75*8-15, 650-75*7, 20, 25)
        self.lbl_char_7.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_7.setText('7')
        
        self.lbl_char_8 = QLabel(self)
        self.lbl_char_8.setGeometry(50+75*8-15, 650-75*8, 20, 25)
        self.lbl_char_8.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_8.setText('8')