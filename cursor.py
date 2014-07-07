from PyQt4.QtCore import *
from SignalSlotObject import SignalSlotObject

###
##Cursor class:
#_stores information about the current
#_state of the mouse
###

class Cursor():
    def __init__(self):
        self.x = 0
        self.y = 0
        self._px = 0
        self._py = 0
        self.leftDown = False
        self.rightDown = False
        self.middleDown = False
        self.leftClickOnRelease = False
        self.rightClickOnRelease = False
        self.middleClickOnRelease = False
        self.leftClick = SignalSlotObject()
        self.rightClick = SignalSlotObject()
        self.middleClick = SignalSlotObject()
        self.click = SignalSlotObject()
        self.hover = SignalSlotObject()
        self.leftDrag = SignalSlotObject()
        self.rightDrag = SignalSlotObject()
        self.middleDrag = SignalSlotObject()
        self.drag = SignalSlotObject()
        
    def setX(self,a):
        if self.x != a:
            self._px = self.x
            self.x = a

    def setY(self,a):
        if self.y != a:
            self._py = self.y
            self.y = a

    def setButtons(self,b):
        b = int(b)
        a = b % 2
        self.leftDown = (a == 1)
        b = (b - a) / 2
        a = b % 2
        self.rightDown = (a == 1)
        b = (b - a) / 2
        a = b % 2
        self.middleDown = (a == 1)

    def update(self,e,prm='o'):
        self.setX(e.x())
        self.setY(e.y())
        self.setButtons(e.buttons())
        
        if prm == 'p':
            if e.button() == Qt.LeftButton:
                self.leftClickOnRelease = True
            elif e.button() == Qt.RightButton:
                self.rightClickOnRelease = True
            elif e.button() == Qt.MiddleButton:
                self.middleClickOnRelease = True
        elif prm == 'r':
            if e.button() == Qt.LeftButton and self.leftClickOnRelease:
                self.leftClick.emit()
                self.click.emit()
            elif e.button() == Qt.RightButton and self.rightClickOnRelease:
                self.rightClick.emit()
                self.click.emit()
            elif e.button() == Qt.MiddleButton and self.middleClickOnRelease:
                self.middleClick.emit()
                self.click.emit()
        elif prm == 'm':
            buttonDown = False
            if self.leftDown:
                self.leftDrag.emit()
                self.drag.emit()
                buttonDown = True
            if self.rightDown:
                self.rightDrag.emit()
                self.drag.emit()
                buttonDown = True
            if self.middleDown:
                self.middleDrag.emit()
                self.drag.emit()
                buttonDown = True
            if not buttonDown:
                self.hover.emit()
        else:
            pass
