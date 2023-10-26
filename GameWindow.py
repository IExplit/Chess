import os

from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('Chess')
        self.setFixedSize(1250, 700)

        self.pic = QLabel(self)
        self.pic.setGeometry(50, 50, 600, 600)
        self.pixmap = QPixmap(f"{os.getcwd()}\\imgs\\Board2.png")
        self.pic.setPixmap(self.pixmap.scaledToWidth(600))