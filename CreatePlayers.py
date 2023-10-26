from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class CreatePlayers(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('Chess')
        self.btn_stockfish = QPushButton(self)
        self.btn_stockfish.setGeometry(12, 650, 120, 70)
        self.btn_stockfish.setText('lolo')