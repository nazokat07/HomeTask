import typing
import PyQt5
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont

# font -> .ttf

class Window(QWidget):
    
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(1280, 720)
        self.setWindowTitle("PyQt5")
        self.label = QLabel(self, text='Hello PyQt5')
        self.label.move(50,20)
        font = QFont()
        font.setFamily('Roboto')
        font.setPointSize(20)
        self.label.setFont(font)

        self.label = QLabel(self, text='Hello PyQt5')
        self.label.move(300,300)
        font = QFont()
        font.setFamily('Italic')
        font.setPointSize(40)
        self.label.setFont(font)

        self.label = QLabel(self, text='Hello PyQt5')
        self.label.move(800,500)
        font = QFont()
        font.setFamily('Roboto')
        font.setPointSize(60)
        self.label.setFont(font)
        
        

def application():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()