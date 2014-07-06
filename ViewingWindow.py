from PyQt4.QtCore import *
from PyQt4.QtGui import *
from BridgeConceptGraph import BridgeConceptGraph

class ViewingWindow(QWidget):
    def __init__(self,*args):
        super(ViewingWindow,self).__init__(*args)
        self.graph = BridgeConceptGraph()
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
            drawBridgeToConceptEdges(qp,bridge, bridge.ForwardEdges)
        for concept in self.graph.concepts:
            drawConceptToBridgeEdges(qp,concept, concept.ForwardEdges)
        for bridge in self.graph.bridges:
            drawBridge(qp,bridge)
        for conept in self.graph.concepts:
            drawConcept(qp,concept)

    def drawBridgeToConceptEdges(self,bridge,qp,edges):
        pen = QPen()
        brush = QBrush()
        qp.setPen(pen)
        qp.setBrush(brush)
        for e in edges:
            qp.drawLine(bridge.position,self.graph.concepts[e].position)
            
    def drawConceptToBridgeEdges(self,concept,qp,edges):
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
        
    def drawEdge(self,qp,edge):
        pen = QPen()
        brush = QBrush()
        qp.setPen(pen)
        qp.setBrush(brush)
        qp.drawEllipse(bridge.position,bridge.radius,bridge.radius)

    def setGraph(self,graph):
        self.graph = graph
        
