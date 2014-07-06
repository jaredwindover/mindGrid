import sys
from MainWindow import MainWindow
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("WireFrame Model")
    mainWindow.show()
    app.exec_()

if __name__ == '__main__':
    main()
