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
    b0 = G.AddBridge(B)
    B.key = b0
    v = mainWindow.viewingWindow
    c0 = v.addConcept(QPointF(200,200))
    c1 = v.addConcept(QPointF(200,250))
    c2 = v.addConcept(QPointF(250,200))
    c3 = v.addConcept(QPointF(250,250))
    G.ConnectBridgeToConcept(b0,c0)
    G.ConnectConceptToBridge(c1,b0)
    G.ConnectConceptToBridge(c2,b0)
    G.ConnectConceptToBridge(c3,b0)
    mainWindow.show()
    mainWindow.viewingWindow.animate()
    app.exec_()

if __name__ == '__main__':
    main()
