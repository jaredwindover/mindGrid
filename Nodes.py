from PyQt4.QtGui import *
from PyQt4.QtCore import *

DEFAULT_TITLE = 'Default Title'
DEFAULT_TEXT = 'Default Text'
DEFAULT_RADIUS = 10

class Node:
    def __init__(self,
                 title = DEFAULT_TITLE,
                 text = DEFAULT_TEXT,
                 qcp=[QColor('white'),
                      QColor('black'),
                      QColor('red'),
                      QColor('green')],
                 radius=DEFAULT_RADIUS
    ):
        self.title = QString(title)
        self.text = QTextDocument(text)
        self.position = QPointF(0,0)
        self.highlighted = False
        self.palette = qcp
        self.radius = radius
        self.held = False
        self.hovered = False
        self.selected = False

class Bridge(Node):
    def __init__(self):
        Node.__init__(self,
                      'Default Bridge',
                      DEFAULT_TEXT,
                      [QColor(225,0,0),
                       QColor(150,0,0),
                       QColor('white'),
                       QColor(75,0,0)],
                      10
        )
    
class Concept(Node):
    def __init__(self):
        Node.__init__(self,
                      'Default Concept',
                      DEFAULT_TEXT,
                      [QColor(0,0,225),
                       QColor(0,0,150),
                       QColor('white'),
                       QColor(0,0,75)],
                      15
        )
