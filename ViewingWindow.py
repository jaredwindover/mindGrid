from time import clock

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from BridgeConceptGraph import BridgeConceptGraph
from cursor import Cursor
from Utility import *

class ViewingWindow(QWidget):
    def __init__(self,*args):
        super(ViewingWindow,self).__init__(*args)
        self.graph = BridgeConceptGraph()
        self.cursor = Cursor()
        self.cursor.leftClick.connect(self.onLeftClick)
        self.cursor.hover.connect(self.onHover)
        self.cursor.leftDrag.connect(self.onLeftDrag)
        self.cursor.leftPress.connect(self.onLeftPress)
        self.cursor.leftRelease.connect(self.onLeftRelease)
        self.leftClickB = False
        self.leftDragB = False
        self.leftHoverB = False
        self.leftPressB = False
        self.leftReleaseB = False
        self.selectedNode = None
        self.heldNode = None
        self.hoverNode = None
        self.fps = 30
        self.initUI()

    def initUI(self):
        self.setAutoFillBackground(True)
        self.setMouseTracking(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,QColor(0,100,0))
        self.setPalette(palette)

    def sizeHint(self):
        return QSize(800,500)

    def minimumSizeHint(self):
        return QSize(300,300)

    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawGraph(qp)
        qp.end()

    def drawGraph(self, qp):
        for index, bridge in self.graph.bridges.items():
            self.drawBridgeToConceptEdges(qp,
                                          bridge,
                                          self.graph.ForwardEdges[index])
        for index, concept in self.graph.concepts.items():
            self.drawConceptToBridgeEdges(qp,
                                          concept,
                                          self.graph.ForwardEdges[index])
        for index in self.graph.bridges:
            self.drawBridge(qp,self.graph.bridges[index])
        for index in self.graph.concepts:
            self.drawConcept(qp,self.graph.concepts[index])

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
        self.drawNode(qp,bridge)
        
    def drawConcept(self,qp,concept):
        self.drawNode(qp,concept)

    def drawNode(self,qp,node):
        if node.selected:
            pen = QPen(node.palette[2])
            brush = QBrush(node.palette[2])
        elif node.held:
            pen = QPen(node.palette[0])
            brush = QBrush(node.palette[0])
        elif node.hovered:
            pen = QPen(node.palette[1])
            brush = QBrush(node.palette[1])
        else:
            pen = QPen(node.palette[3])
            brush = QBrush(node.palette[3])
        qp.setPen(pen)
        qp.setBrush(brush)
        qp.drawEllipse(node.position,node.radius,node.radius)
        

    def setGraph(self,graph):
        self.graph = graph
        
    def mousePressEvent(self,event):
        self.cursor.update(event,'p')
        
    def mouseReleaseEvent(self,event):
        self.cursor.update(event,'r')
        
    def mouseMoveEvent(self,event):
        self.cursor.update(event,'m')

    def onLeftClick(self):
        self.leftClickB = True

    def onLeftDrag(self):
        self.leftDragB = True
        
    def onHover(self):
        self.leftHoverB = True

    def onLeftPress(self):
        self.leftPressB = True

    def onLeftRelease(self):
        self.leftReleaseB = True

    def getClosestNode(self,pos):
        G = self.graph
        distances=[(node,norm(pos - node.position)) for node in G.Nodes()]
        r = reduce(ltIndex(1),distances)
        return r
        
    def readCursorEvents(self):
        pos = QPointF(self.cursor.x,self.cursor.y)
        (node,dist) = self.getClosestNode(pos)
        #Due to the ascynchronous design, it's necessary to order these
        #properly
        if (self.leftDragB):
            try:
                self.heldNode.position = pos
            except:
                pass
            self.leftDragB = False
            
        if (self.leftHoverB):
            if (dist < node.radius):
                self.unhover()
                self.unhold()
                self.hover(node)
            else:
                self.unhover()
            self.leftHoverB = False
            
        if (self.leftPressB):
            if (dist < node.radius):
                self.unhold()
                self.unhover()
                self.hold(node)
            self.leftPressB = False
            
        if (self.leftReleaseB):
            self.unhold()
            self.leftReleaseB = False
            
        if (self.leftClickB):
            if (dist < node.radius):
                self.unhover()
                self.unhold()
                if not self.selectedNode == node:
                    self.unselect()
                    self.select(node)
                else:
                    self.unselect()
            else:
                self.unselect()
            self.leftClickB = False

    def update(self):
        self.readCursorEvents()
        print "Held Node: ",self.heldNode
        print "Selected Node: ",self.selectedNode
        print "Hovered Node: ",self.hoverNode
        self.repaint()

    def animate(self):
        t1 = clock()
        self.update()
        QTimer.singleShot(max(0,1000/self.fps-(clock()-t1)),self.animate)
            
    def select(self,node):
        self.selectedNode = node
        self.selectedNode.selected = True

    def unselect(self):
        try:
            self.selectedNode.selected = False
            self.selectedNode = None
        except:
            pass

    def hold(self, node):
        self.heldNode = node
        self.heldNode.held = True

    def unhold(self):
        try:
            self.heldNode.held = False
            self.heldNode = None
        except:
            pass

    def hover(self,node):
        self.hoverNode = node
        self.hoverNode.hovered = True
        

    def unhover(self):
        try:
            self.hoverNode.hovered = False
            self.hoverNode = None
        except:
            pass
