from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ViewingWindow(QWidget):
    def __init__(self,*args):
        super(ViewingWindow,self).__init__(*args)
        self.initUI()

    def initUI(self):
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,QColor(255,0,0))
        self.setPalette(palette)

    def sizeHint(self):
        return QSize(300,300)

    def minimumSizeHint(self):
        return QSize(300,300)
