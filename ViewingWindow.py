from math import pi
from time import clock
from pickle import dump, load

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from BridgeConceptGraph import BridgeConceptGraph
from cursor import Cursor
from SignalSlotObject import SignalSlotObject
from Utility import *
from Nodes import Bridge,Concept
from Arrow import getArrowPath

class ViewingWindow(QWidget):
    def __init__(self,*args):
        super(ViewingWindow,self).__init__(*args)
        self.graph = BridgeConceptGraph()
        self.nodeSelected = SignalSlotObject()
        self.cursor = Cursor()
        self.cursor.leftClick.connect(self.onLeftClick)
        self.cursor.leftHover.connect(self.onHover)
        self.cursor.leftDrag.connect(self.onLeftDrag)
        self.cursor.leftPress.connect(self.onLeftPress)
        self.cursor.leftRelease.connect(self.onLeftRelease)
        self.cursor.rightClick.connect(self.onRightClick)
        self.cursor.rightDrag.connect(self.onRightDrag)
        self.cursor.rightPress.connect(self.onRightPress)
        self.cursor.rightRelease.connect(self.onRightRelease)
        self.cursor.rightPull.connect(self.onRightPull)
        self.cursor.rightHover.connect(self.onHover)
        self.leftClickB = False
        self.leftDragB = False
        self.HoverB = False
        self.leftPressB = False
        self.leftReleaseB = False
        self.rightClickB = False
        self.rightDragB = False
        self.rightPressB = False
        self.rightReleaseB = False
        self.rightPullB = False
        self.selectedNode = None
        self.heldNode = None
        self.hoverNode = None
        self.edgeDragNode = None
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
        self.drawUI(qp)
        qp.end()

    def drawUI(self,qp):
        pen = QPen()
        brush = QBrush(QColor(0,100,0,200))
        qp.setPen(pen)
        qp.setBrush(brush)
        if self.edgeDragNode != None:
            qp.drawPath(
                getArrowPath(self.edgeDragNode.position,
                             QPointF(self.cursor.x,
                                     self.cursor.y),
                             4,
                             40,
                             20,
                             pi/3,
                             0,
                             0
                         )
            )

    def drawGraph(self, qp):
        for index, concept in self.graph.concepts.items():
            self.drawConceptToBridgeEdges(qp,
                                          concept,
                                          self.graph.ForwardEdges[index])
        for index, bridge in self.graph.bridges.items():
            self.drawBridgeToConceptEdges(qp,
                                          bridge,
                                          self.graph.ForwardEdges[index])
        for index in self.graph.concepts:
            self.drawConcept(qp,self.graph.concepts[index])
        for index in self.graph.bridges:
            self.drawBridge(qp,self.graph.bridges[index])

    def drawBridgeToConceptEdges(self,qp,bridge,edges):
        pen = QPen()
        brush = QBrush(QColor(100,0,0,200))
        qp.setPen(pen)
        qp.setBrush(brush)
        for e in edges:
            qp.drawPath(
                getArrowPath(bridge.position,
                             self.graph.concepts[e].position,10,65,30, pi/3,0,self.graph.concepts[e].radius))
            
    def drawConceptToBridgeEdges(self,qp,concept,edges):
        pen = QPen()
        brush = QBrush(QColor(0,0,100,200))
        qp.setPen(pen)
        qp.setBrush(brush)
        for e in edges:
            qp.drawPath(
                getArrowPath(concept.position,
                             self.graph.bridges[e].position,6,40,20, pi/3,0,self.graph.bridges[e].radius))
            
    def drawBridge(self,qp,bridge):
        self.drawNode(qp,bridge)
        pen = QPen(QColor(0,0,0))
        font = QFont()
        font.setItalic(True)
        font.setBold(True)
        qp.setPen(pen)
        qp.setFont(font)
        bTitle = bridge.title
        pos = bridge.position + QPointF(1,-1)*bridge.radius
        qp.drawText(pos,bTitle)
        
    def drawConcept(self,qp,concept):
        self.drawNode(qp,concept)
        pen = QPen(QColor(0,0,0))
        bgBrush = QBrush(QColor(255,255,255,20))
        font = QFont()
        font.setBold(True)
        qp.setPen(pen)
        qp.setFont(font)
        qp.setBackgroundMode(Qt.OpaqueMode)
        qp.setBackground(bgBrush)
        cTitle = concept.title
        pos = concept.position + QPointF(1,-1)*concept.radius
        qp.drawText(pos,cTitle)

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
        self.HoverB = True

    def onLeftPress(self):
        self.leftPressB = True

    def onLeftRelease(self):
        self.leftReleaseB = True

    def onRightClick(self):
        self.rightClickB = True

    def onRightDrag(self):
        self.rightDragB = True

    def onRightPress(self):
        self.rightPressB = True

    def onRightRelease(self):
        self.rightReleaseB = True

    def onRightPull(self):
        self.rightPullB = True

    def getClosestNode(self,pos):
        try:
            G = self.graph
            distances=[(node,norm(pos - node.position)) for node in G.Nodes()]
            r = reduce(ltIndex(1),distances)
            return r
        except:
            return (None,None)
        
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
            
        if (self.HoverB):
            if node == None: pass
            elif (dist < node.radius):
                self.unhover()
                self.hover(node)
            else:
                self.unhover()
            self.leftHoverB = False
            
        if (self.leftPressB):
            if node == None: pass
            elif (dist < node.radius):
                self.unhold()
                self.unhover()
                self.hold(node)
            self.leftPressB = False
            
        if (self.leftReleaseB):
            self.unhold()
            self.leftReleaseB = False
            
        if (self.leftClickB):
            if node == None: pass
            elif (dist < node.radius):
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

        if (self.rightClickB):
            if node == None: self.addConcept(pos)
            elif (dist < node.radius):
                self.deleteNode(node)
            else:
                self.addConcept(pos)
            self.rightClickB = False

        if (self.rightPullB):
            if node == None:
                pass
            elif dist < node.radius:
                self.edgeDragNode = node
            elif self.selectedNode != None:
                self.edgeDragNode = self.selectedNode
            else:
                pass
            self.rightPullB = False
                
        if (self.rightDragB):
            pass
            
        if (self.rightPressB):
            pass

        if (self.rightReleaseB):
            if self.edgeDragNode != None and self.edgeDragNode != node:
                if dist < node.radius:
                    if isinstance(self.edgeDragNode,Bridge):
                        if isinstance(node,Concept):
                            self.graph.ConnectBridgeToConcept(
                                self.edgeDragNode.key,
                                node.key)
                    elif isinstance(self.edgeDragNode,Concept):
                        if isinstance(node,Bridge):
                            self.graph.ConnectConceptToBridge(
                                self.edgeDragNode.key,
                                node.key)
                        elif isinstance(node,Concept):
                            k =self.addBridge((pos + self.edgeDragNode.position)/2)
                            self.graph.ConnectConceptToBridge(self.edgeDragNode.key,k)
                            self.graph.ConnectBridgeToConcept(k,node.key)
            self.edgeDragNode = None
            self.rightReleaseB = False

    def update(self):
        self.readCursorEvents()
        #print "Held Node: ",self.heldNode
        #print "Selected Node: ",self.selectedNode
        #print "Hovered Node: ",self.hoverNode
        self.repaint()

    def animate(self):
        t1 = clock()
        self.update()
        QTimer.singleShot(max(0,1000/self.fps-(clock()-t1)),self.animate)
            
    def select(self,node):
        self.selectedNode = node
        self.selectedNode.selected = True
        self.nodeSelected.emit()

    def unselect(self,node=None):
        if self.selectedNode == node or node == None:
            try:
                self.selectedNode.selected = False
                self.selectedNode = None
            except:
                pass

    def hold(self, node):
        self.heldNode = node
        self.heldNode.held = True

    def unhold(self, node=None):
        if self.heldNode == node or node == None:
            try:
                self.heldNode.held = False
                self.heldNode = None
            except:
                pass
            
    def hover(self,node):
        self.hoverNode = node
        self.hoverNode.hovered = True

    def unhover(self, node=None):
        if self.hoverNode == node or node == None:
            try:
                self.hoverNode.hovered = False
                self.hoverNode = None
            except:
                pass

    def deleteNode(self,node):
        self.unselect(node)
        self.unhold(node)
        self.unhover(node)
        try:
            self.graph.RemoveBridge(node.key)
        except:
            self.graph.RemoveConcept(node.key)

    def addConcept(self,pos):
        C = Concept()
        C.position = pos
        k = self.graph.AddConcept(C)
        C.key = k
        return k

    def addBridge(self,pos):
        B = Bridge()
        B.position = pos
        k = self.graph.AddBridge(B)
        B.key = k
        return k

    def writeTo(self, filename):
        f = open(filename,'w')
        dump(self.graph,f)
        f.close()

    def readFrom(self,filename):
        f = open(str(filename),'r')
        self.graph = load(f)
        f.close()
