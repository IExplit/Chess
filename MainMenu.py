import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

from CreatePlayers import CreatePlayers
from GameWindow import GameWindow

class MainMenu(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Chess')
        
        self.btn_stockfish = QPushButton(self)
        self.btn_stockfish.setGeometry(12, 650, 120, 70)
        self.btn_stockfish.setText('Играть с ботом')

        self.btn_local = QPushButton(self)
        self.btn_local.setGeometry(120+12*2, 650, 120, 70)
        self.btn_local.setText('Играть по \n локальной сети')

        self.btn_one_pc = QPushButton(self)
        self.btn_one_pc.setGeometry(120*2+12*3, 650, 120, 70)
        self.btn_one_pc.setText('Играть на \n одном пк')
        self.btn_one_pc.clicked.connect(self.one_pc_game)

        self.btn_settings = QPushButton(self)
        self.btn_settings.setGeometry(120*3+12*4, 650, 120, 70)
        self.btn_settings.setText('Настройки')

        self.pic = QLabel(self)
        self.pic.setGeometry(12, 12, 600, 600)
        self.pixmap = QPixmap(f"{os.getcwd()}\\imgs\\hh.png")
        self.pic.setPixmap(self.pixmap.scaledToWidth(600))

    def one_pc_game(self):
        self.game_window = GameWindow()
        self.game_window.show()

app = QApplication(sys.argv)
window = MainMenu()
window.show()
app.exec()