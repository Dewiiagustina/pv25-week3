import sys
import random
from PyQt6.QtWidgets import*
from PyQt6.QtCore import*
from PyQt6.QtGui import QFont

class Koordinatxy(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assigment Week 3 Event Handler using PyQT5")
        self.setGeometry(100,100,500,400)
        
        self.label=QLabel(self)
        self.label.setFont(QFont("Arial",10))
        self.label.setStyleSheet("color:yellow;")
        self.label.adjustSize()
        self.label.move(self.width() // 2, self.height()//2)
        
        self.setMouseTracking(True)
        
    def mouseMoveEvent(self,event):
        cursor_pos = event.position().toPoint()
        label_pos = self.label.pos()
        distance = (cursor_pos - label_pos).manhattanLength()
        
        self.label.setText(f"x:{cursor_pos.x()}, y:{cursor_pos.y()}")
        self.label.adjustSize()
        
        if distance <100:
            self.moveLabelAway(cursor_pos)
    
    def moveLabelAway(self, cursor_pos):
        max_x = self.width() - self.label.width()
        max_y = self.height() - self.label.height()
        
        while True:
            new_x = random.randint(0,max_x)
            new_y =  random.randint(0, max_y)
            
            new_pos=QPoint(new_x, new_y)
            if(new_pos - cursor_pos).manhattanLength()>100:
                self.label.move(new_x,new_y)
                break
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Koordinatxy()
    window.show()
    sys.exit(app.exec())