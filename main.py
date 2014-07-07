import sys
from MainWindow import MainWindow
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Nodes import *

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("WireFrame Model")
    G = mainWindow.viewingWindow.graph
    B = Bridge()
    B.position = QPointF(100,100)
    C = Concept()
    C.position = QPointF(200,200)
    b0 = G.AddBridge(B)
    c0 = G.AddConcept(C)
    G.ConnectBridgeToConcept(b0,c0)
    mainWindow.show()
    app.exec_()

if __name__ == '__main__':
    main()
