#Simple_drawing_window3
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Simple_drawing_window3(QWidget):
    def __init__(self):
        self.image = QPixmap("images/tiger.png")
        self.x = 0
        self.y = 0
        self.w = 100
        self.h = 100
        self.score = 0
        self.miss = 0
        self.gameover = False
   
        
    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)

    def random_pos(self, arena_w, arena_h):
        self.x = random.randint(0, arena_w - self.w)
        self.y = random.randint(0, arena_h - self.h)

    def is_hit(self, mouse_x, mouse_y):
        if(mouse_x >= self.x and mouse_x <= self.x + self.w ):
            self.score +=100
            return True
        else:
            self.miss += 1