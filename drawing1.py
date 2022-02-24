import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(210,105,30))
        p.setBrush(QColor(210,105,30))
        p.drawPie(50, 150, 150, 100, 0, 180 * 16)
        p.drawRect(50, 200, 150, 150)

        p.setBrush(QColor(0,0,255))
        p.drawEllipse(70, 250, 10, 10)

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)

        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window1()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
