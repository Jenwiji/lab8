import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
class freeHandDraw(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("A Simple Paint Program")   

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)
        self.myPixmap = QPixmap(400,400)
        self.setMinimumSize(400,400)
        self.painter = QPainter(self.myPixmap)
        self.pen = QPen(Qt.black)
        self.painter.setPen(self.pen)
        self.painter.fillRect(0,0,400,400, Qt.white)
        self.setPixmap(self.myPixmap)
        self.last = None

        self.label = QLabel(self)
        self.label.setText("Drag the mouse to draw")
        self.label.setGeometry(QRect(130, 320, 200, 20))

        self.pbt = QPushButton("clear", self)
        self.pbt.clicked.connect(self.clear)
        self.pbt.setGeometry(QRect(100, 350, 200, 20))