import os
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QTableView

from QLabelClicable import QLabelClicable

class GameWindow(QWidget):
    def __init__(self, game = None):
        super().__init__()
        
        self.reverse = 0
        self.selected_piece = None
        
        self.game = game
        self.positions = {}
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('Chess')
        self.setFixedSize(1210, 700)
        
        self.btn_first_pos = QPushButton(self)
        self.btn_prev_pos = QPushButton(self)
        self.btn_next_pos = QPushButton(self)
        self.btn_last_pos = QPushButton(self)
        self.btn_return = QPushButton(self)
        self.btn_draw = QPushButton(self)
        self.btn_surrender = QPushButton(self)
        self.btn_flip = QPushButton(self)
        self.history_tbl = QTableView(self)
        self.set_game_tools()
        
        self.lbl_player1 = QLabel(self)
        self.lbl_player2 = QLabel(self)
        self.set_players_names()
        
        self.lbl_board = QLabel(self)
        self.lbl_char_a = QLabel(self)
        self.lbl_char_b = QLabel(self)
        self.lbl_char_c = QLabel(self)
        self.lbl_char_d = QLabel(self)
        self.lbl_char_e = QLabel(self)
        self.lbl_char_f = QLabel(self)
        self.lbl_char_g = QLabel(self)
        self.lbl_char_h = QLabel(self)
        self.lbl_char_1 = QLabel(self)
        self.lbl_char_2 = QLabel(self)
        self.lbl_char_3 = QLabel(self)
        self.lbl_char_4 = QLabel(self)
        self.lbl_char_5 = QLabel(self)
        self.lbl_char_6 = QLabel(self)
        self.lbl_char_7 = QLabel(self)
        self.lbl_char_8 = QLabel(self)
        self.set_board()
        
        self.set_pieces(start=True)
    
    def set_game_tools(self):
        
        self.btn_first_pos.setGeometry(750, 220-40, 90, 40)
        self.btn_first_pos.setText('<<')
        
        self.btn_prev_pos.setGeometry(750+90, 220-40, 90, 40)
        self.btn_prev_pos.setText('<')
        
        self.btn_next_pos.setGeometry(750+90*2, 220-40, 90, 40)
        self.btn_next_pos.setText('>')
        
        self.btn_last_pos.setGeometry(750+90*3, 220-40, 90, 40)
        self.btn_last_pos.setText('>>')
        
        self.btn_return.setGeometry(750, 220+260, 90, 40)
        self.btn_return.setText('<--')
        
        self.btn_draw.setGeometry(750+90, 220+260, 90, 40)
        self.btn_draw.setText('1/2')
        
        self.btn_surrender.setGeometry(750+90*2, 220+260, 90, 40)
        self.btn_surrender.setText('###')
        
        self.btn_flip.setGeometry(750+90*3, 220+260, 90, 40)
        self.btn_flip.setText('˄˅')
        self.btn_flip.clicked.connect(self.flip_board)
        
        self.history_tbl.setGeometry(750, 220, 360, 260)
        
    def set_players_names(self):
        
        self.lbl_player1.setGeometry(750, 560-460*self.reverse, 90*3, 40)
        self.lbl_player1.setStyleSheet("QLabel{font-size: 30pt;}")
        self.lbl_player1.setText('Player1')
        
        self.lbl_player2.setGeometry(750, 100+460*self.reverse, 90*3, 40)
        self.lbl_player2.setStyleSheet("QLabel{font-size: 30pt;}")
        self.lbl_player2.setText('Player2')
    
    def set_board(self):
        
        coefs = [coef for coef in range(1, 9)]
        if self.reverse: coefs.reverse()
        
        self.lbl_board.setGeometry(50, 50, 600, 600)
        self.pixmap_board = QPixmap(f"{os.getcwd()}\\imgs\\Board.png")
        self.pixmap_board = self.pixmap_board.scaledToWidth(600)
        self.pixmap_board = self.pixmap_board.transformed(QTransform().rotate(90*self.reverse))
        self.lbl_board.setPixmap(self.pixmap_board)
        
        self.lbl_char_a.setGeometry(52, 650-25, 20, 25)
        self.lbl_char_a.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_a.setText('a')
        
        self.lbl_char_b.setGeometry(52+75, 650-25, 20, 25)
        self.lbl_char_b.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_b.setText('b')
        
        self.lbl_char_c.setGeometry(52+75*2, 650-25, 20, 25)
        self.lbl_char_c.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_c.setText('c')
        
        self.lbl_char_d.setGeometry(52+75*3, 650-25, 20, 25)
        self.lbl_char_d.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_d.setText('d')
        
        self.lbl_char_e.setGeometry(52+75*4, 650-25, 20, 25)
        self.lbl_char_e.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_e.setText('e')
        
        self.lbl_char_f.setGeometry(52+75*5, 650-25, 20, 25)
        self.lbl_char_f.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_f.setText('f')
        
        self.lbl_char_g.setGeometry(52+75*6, 650-25, 20, 25)
        self.lbl_char_g.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_g.setText('g')
        
        self.lbl_char_h.setGeometry(52+75*7, 650-25, 20, 25)
        self.lbl_char_h.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_h.setText('h')
        
        self.lbl_char_1.setGeometry(50+75*8-15, 650-75*coefs[0], 20, 25)
        self.lbl_char_1.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_1.setText('1')
        
        self.lbl_char_2.setGeometry(50+75*8-15, 650-75*coefs[1], 20, 25)
        self.lbl_char_2.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_2.setText('2')
        
        self.lbl_char_3.setGeometry(50+75*8-15, 650-75*coefs[2], 20, 25)
        self.lbl_char_3.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_3.setText('3')
        
        self.lbl_char_4.setGeometry(50+75*8-15, 650-75*coefs[3], 20, 25)
        self.lbl_char_4.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_4.setText('4')
        
        self.lbl_char_5.setGeometry(50+75*8-15, 650-75*coefs[4], 20, 25)
        self.lbl_char_5.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_5.setText('5')
        
        self.lbl_char_6.setGeometry(50+75*8-15, 650-75*coefs[5], 20, 25)
        self.lbl_char_6.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_6.setText('6')
        
        self.lbl_char_7.setGeometry(50+75*8-15, 650-75*coefs[6], 20, 25)
        self.lbl_char_7.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_7.setText('7')
        
        self.lbl_char_8.setGeometry(50+75*8-15, 650-75*coefs[7], 20, 25)
        self.lbl_char_8.setStyleSheet("QLabel{font-size: 15pt;}")
        self.lbl_char_8.setText('8')
        
    def get_pos_in_window(self, x, y):
        return (50+75*(x-97), 50+abs(75*(8-y)-525*self.reverse))
    
    def set_pixmap(self, label, img = ''):
        pixmap = QPixmap(img)
        label.setPixmap(pixmap.scaledToWidth(75))
        
    def set_pieces(self, start = False):
        
        for pos in self.game.board.positions.keys():
            x, y = pos
            piece = self.game.board.positions[pos]['piece']
            pos_in_window = self.get_pos_in_window(x, y)
            x1, y1 = pos_in_window
            if pos_in_window not in self.positions.keys():
                self.positions[pos_in_window] = {'piece': piece, 'label': QLabelClicable(self)}
            self.positions[pos_in_window]['piece'] = piece
            label = self.positions[pos_in_window]['label']
            label.setGeometry(x1, y1, 75, 75)
            if piece is not None:
                self.set_pixmap(label, piece.IMG)
                if piece.side == self.game.motion.side:
                    label.setCursor(Qt.PointingHandCursor)
                else:
                    label.setCursor(Qt.ArrowCursor)
            if start == True: label.clicked.connect(self.click)
        
        self.game.get_all_pl_moves(self.game.motion)
    
    def click(self):
        x, y, _, _ = self.sender().geometry().getRect()
        piece = self.positions[(x, y)]['piece']
        game = self.game
        if self.selected_piece is not None:
            for pos in self.selected_piece.movements:
                label = self.positions[self.get_pos_in_window(pos[0], pos[1])]['label']
                self.set_pixmap(label)
                label.setCursor(Qt.ArrowCursor)
            self.selected_piece = None
        if piece is not None and game.motion.side == piece.side:
            self.selected_piece = piece
            for pos in piece.movements:
                print(pos)
                label = self.positions[self.get_pos_in_window(pos[0], pos[1])]['label']
                self.set_pixmap(label, os.getcwd()+'\\imgs\\MovingDot.png')
                label.setCursor(Qt.PointingHandCursor)
            print(piece)
            print((x, y),self.positions[(x, y)]['piece'].position , sep='\n')
        
    def flip_board(self):
        self.reverse = abs(self.reverse - 1)
        self.set_board()
        self.set_pieces()
        self.set_players_names()