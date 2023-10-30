import os

from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QTableView

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('Chess')
        self.setFixedSize(1210, 700)
        
        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(750, 220-40, 90, 40)
        
        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(750+90, 220-40, 90, 40)
        
        self.btn3 = QPushButton(self)
        self.btn3.setGeometry(750+90*2, 220-40, 90, 40)
        
        self.btn4 = QPushButton(self)
        self.btn4.setGeometry(750+90*3, 220-40, 90, 40)
        
        self.btn5 = QPushButton(self)
        self.btn5.setGeometry(750, 220+260, 90, 40)
        
        self.btn6 = QPushButton(self)
        self.btn6.setGeometry(750+90, 220+260, 90, 40)
        
        self.btn7 = QPushButton(self)
        self.btn7.setGeometry(750+90*2, 220+260, 90, 40)
        
        self.btn8 = QPushButton(self)
        self.btn8.setGeometry(750+90*3, 220+260, 90, 40)
        
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
        self.pixmap_board = QPixmap(f"{os.getcwd()}\\imgs\\Board2.png")
        self.lbl_board.setPixmap(self.pixmap_board.scaledToWidth(600))