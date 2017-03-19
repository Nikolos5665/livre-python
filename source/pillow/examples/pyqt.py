from PIL import Image, ImageQt
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Viewer(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.rotateLeftButton = QPushButton("Rotate Left")
        self.rotateRightButton = QPushButton("Rotate Right")

        self.label = QLabel()
        self.image = Image.open("../../_static/pillow.png")
        
        self.initUI()
        self.displayImage()

        self.rotateLeftButton.clicked.connect(self.turnLeft)
        self.rotateRightButton.clicked.connect(self.turnRight)
        
        
    def initUI(self):
            
        hboxLabel = QHBoxLayout()
        hboxLabel.addStretch(1)
        hboxLabel.addWidget(self.label)
        hboxLabel.addStretch(1)

        hboxButtons = QHBoxLayout()
        hboxButtons.addStretch(1)
        hboxButtons.addWidget(self.rotateLeftButton)
        hboxButtons.addWidget(self.rotateRightButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hboxLabel)
        vbox.addStretch(1)
        vbox.addLayout(hboxButtons)
        
        self.setLayout(vbox)   
 
        
    def displayImage(self):

        self.label.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.image)))

    
    def turnLeft(self):
        
        self.image = self.image.rotate(90)
        self.label.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.image)))
        
        
    def turnRight(self):

       self.image = self.image.rotate(-90)
       self.label.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.image)))
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    viewer = Viewer()
    viewer.resize(450, 400)
    viewer.setWindowTitle('Image Viewer')
    viewer.show()

    sys.exit(app.exec_())
