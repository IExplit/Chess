from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel


class QLabelClicable(QLabel):
    clicked=pyqtSignal()
    
    def mousePressEvent(self, event):
        self.clicked.emit()