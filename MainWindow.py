import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class MainMenu(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Chess')
        
        self.btn_stockfish = QPushButton(self)
        self.btn_stockfish.setGeometry(12, 12, 110, 50)
        self.btn_stockfish.setText('Stockfish')
        self.btn_local = QPushButton('Local')
        self.btn_one_pc = QPushButton('One pc')
        x, y = 500, 500
        self.pic = QLabel(self)
        self.pic.setGeometry(150, 12, x, y)
        self.pixmap = QPixmap(f"{os.getcwd()}\\imgs\\hh.png")
        self.pic.setPixmap(self.pixmap.scaledToWidth(y))

app = QApplication(sys.argv)
window = MainMenu()
window.show()
app.exec()