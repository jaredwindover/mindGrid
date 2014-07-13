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
    C0 = Concept()
    C0.position = QPointF(200,200)
    C1 = Concept()
    C1.position = QPointF(200,250)
    C2 = Concept()
    C2.position = QPointF(250,200)
    C3 = Concept()
    C3.position = QPointF(250,250)
    b0 = G.AddBridge(B)
    c0 = G.AddConcept(C0)
    c1 = G.AddConcept(C1)
    c2 = G.AddConcept(C2)
    c3 = G.AddConcept(C3)
    G.ConnectBridgeToConcept(b0,c0)
    G.ConnectConceptToBridge(c1,b0)
    G.ConnectConceptToBridge(c2,b0)
    G.ConnectConceptToBridge(c3,b0)
    mainWindow.show()
    mainWindow.viewingWindow.animate()
    app.exec_()

if __name__ == '__main__':
    main()
