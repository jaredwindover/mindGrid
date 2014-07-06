from PyQt4.QtGui import *
from PyQt4.QtCore import *

DEFAULT_TITLE = 'Default Title'
DEFAULT_TEXT = 'Default Text'
DEFAULT_RADIUS = 10

class Node:
    def __init__(self,
                 title = DEFAULT_TITLE,
                 text = DEFAULT_TEXT,
                 qcb=QColor('white'),
                 qch=QColor('black'),
                 radius=DEFAULT_RADIUS
    ):
        self.title = QString(title)
        self.text = QTextDocument(text)
        self.position = QPointF(0,0)
        self.highlighted = False
        self.baseColor = qcb
        self.highlightColor = qch
        self.radius = radius

class Bridge(Node):
    def __init__(self):
        super(Bridge,self).__init__('Default Bridge',
                                    DEFAULT_TEXT,
                                    QColor(0,255,255),
                                    QColor(0,255,0),
                                    30
        )
    
class Concept(Node):
    def __init__(self):
        super(Concept,self).__init__('Default Concept',
                                     DEFAULT_TEXT,
                                     QColor(255,0,255),
                                     QColor(255,0,0),
                                     30
        )
