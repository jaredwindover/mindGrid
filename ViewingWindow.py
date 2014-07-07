from PyQt4.QtCore import *
from PyQt4.QtGui import *
from BridgeConceptGraph import BridgeConceptGraph
from cursor import Cursor

class ViewingWindow(QWidget):
    def __init__(self,*args):
        super(ViewingWindow,self).__init__(*args)
        self.graph = BridgeConceptGraph()
        self.cursor = Cursor()
        self.cursor.leftClick.connect(self.onLeftClick)
        self.cursor.hover.connect(self.onHover)
        self.cursor.leftDrag.connect(self.onLeftDrag)
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

    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawGraph(qp)
        qp.end()

    def drawGraph(self, qp):
        for bridge in self.graph.bridges:
            self.drawBridgeToConceptEdges(qp,
                                          self.graph.bridges[bridge],
                                          self.graph.ForwardEdges[bridge])
        for concept in self.graph.concepts:
            self.drawConceptToBridgeEdges(qp,
                                          self.graph.concepts[concept],
                                          self.graph.ForwardEdges[concept])
        for bridge in self.graph.bridges:
            self.drawBridge(qp,self.graph.bridges[bridge])
        for conept in self.graph.concepts:
            self.drawConcept(qp,self.graph.concepts[concept])

    def drawBridgeToConceptEdges(self,qp,bridge,edges):
        pen = QPen()
        brush = QBrush()
        qp.setPen(pen)
        qp.setBrush(brush)
        for e in edges:
            qp.drawLine(bridge.position,self.graph.concepts[e].position)
            
    def drawConceptToBridgeEdges(self,qp,concept,edges):
        pen = QPen()
        brush = QBrush()
        qp.setPen(pen)
        qp.setBrush(brush)
        for e in edges:
            qp.drawLine(concept.position,self.graph.bridges[e].position)
            
    def drawBridge(self,qp,bridge):
        pen = QPen()
        brush = QBrush()
        qp.setPen(pen)
        qp.setBrush(brush)
        qp.drawEllipse(bridge.position,bridge.radius,bridge.radius)
        
    def drawConcept(self,qp,concept):
        pen = QPen()
        brush = QBrush()
        qp.setPen(pen)
        qp.setBrush(brush)
        qp.drawEllipse(concept.position,concept.radius,concept.radius)

    def setGraph(self,graph):
        self.graph = graph
        
    def mousePressEvent(self,event):
        self.cursor.update(event,'p')
        
    def mouseReleaseEvent(self,event):
        self.cursor.update(event,'r')
        
    def mouseMoveEvent(self,event):
        self.cursor.update(event,'m')

    def onLeftClick(self):
        pass

    def onLeftDrag(self):
        pass

    def onHover(self):
        pass
