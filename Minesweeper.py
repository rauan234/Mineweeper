from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import sys



XSize = 1800
YSize = 800



def Startgame():
    GameIsRunning = 1
    
    menu.setpixmap('white_background.bmp')
    for mbutton in menu.menubuttons:
        mbutton.move(-100, -100)
    menu.show()
    
    GameIsRunning = 0
    
def Startai():
    GameIsRunning = 1
    GameIsRunning = 0
        
        

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 0
        self.top = 50
        self.width = XSize
        self.height = YSize
        
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.setpixmap('menu_image.bmp')
        
        self.menubuttons = []
        self.menubuttons.append(self.create_button(50, YSize - 150, 'Play', Startgame))
        self.menubuttons.append(self.create_button(50, YSize - 100, 'Watch AI playing', Startai))
 
        self.show()
        
    def create_button(self, xpix, ypix, text, function):
        button = QPushButton(text, self)
        button.setToolTip(text)
        button.move(xpix, ypix)
        button.clicked.connect(function)
        
        return button
    
    def setpixmap(self, path):
        label = QLabel(self)
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
 

 
if __name__ == '__main__':
    main_app = QApplication(sys.argv)
    menu = App()
    sys.exit(main_app.exec_())