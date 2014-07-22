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
        self.resetPrevious = False
        self.leftDown = False
        self.rightDown = False
        self.middleDown = False
        self.leftClickOnRelease = False
        self.rightClickOnRelease = False
        self.middleClickOnRelease = False
        self.leftPullOnDrag = False
        self.rightPullOnDrag = False
        self.middlePullOnDrag = False
        self.leftPress = SignalSlotObject()
        self.rightPress = SignalSlotObject()
        self.middlePress = SignalSlotObject()
        self.leftClick = SignalSlotObject()
        self.rightClick = SignalSlotObject()
        self.middleClick = SignalSlotObject()
        self.leftRelease = SignalSlotObject()
        self.rightRelease = SignalSlotObject()
        self.middleRelease = SignalSlotObject()
        self.click = SignalSlotObject()
        self.leftHover = SignalSlotObject()
        self.rightHover = SignalSlotObject()
        self.middleHover = SignalSlotObject()
        self.hover = SignalSlotObject()
        self.leftDrag = SignalSlotObject()
        self.rightDrag = SignalSlotObject()
        self.middleDrag = SignalSlotObject()
        self.leftPull = SignalSlotObject()
        self.rightPull = SignalSlotObject()
        self.middlePull = SignalSlotObject()
        self.drag = SignalSlotObject()
        
    def setX(self,a):
        if (self.resetPrevious): self._px = self.x
        self.x = a

    def setY(self,a):
        if (self.resetPrevious): self._py = self.y
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
        self.resetPrevious = False
        self.setButtons(e.buttons())
        
        if prm == 'p':
            if e.button() == Qt.LeftButton:
                self.leftClickOnRelease = True
                self.leftPullOnDrag = True
                self.leftPress.emit()
            elif e.button() == Qt.RightButton:
                self.rightClickOnRelease = True
                self.rightPullOnDrag = True
                self.rightPress.emit()
            elif e.button() == Qt.MiddleButton:
                self.middleClickOnRelease = True
                self.middlePullOnDrag = True
                self.middlePress.emit()
        elif prm == 'r':
            if e.button() == Qt.LeftButton:
                self.leftRelease.emit()
                self.leftPullOnDrag = False
                if self.leftClickOnRelease:
                    self.leftClick.emit()
                    self.click.emit()
            elif e.button() == Qt.RightButton:
                self.rightRelease.emit()
                self.rightPullOnDrag = False
                if self.rightClickOnRelease:
                    self.rightClick.emit()
                    self.click.emit()
            elif e.button() == Qt.MiddleButton:
                self.middleRelease.emit()
                self.middlePullOnDrag = False
                if self.middleClickOnRelease:
                    self.middleClick.emit()
                    self.click.emit()
        elif prm == 'm':
            buttonDown = False
            if self.leftDown:
                self.leftClickOnRelease = False
                if self.leftPullOnDrag:
                    self.leftPull.emit()
                    self.leftPullOnDrag = False
                self.leftDrag.emit()
                self.drag.emit()
                buttonDown = True
            else:
                self.leftHover.emit()
            if self.rightDown:
                self.rightClickOnRelease = False
                if self.rightPullOnDrag:
                    self.rightPull.emit()
                    self.rightPullOnDrag = False
                self.rightDrag.emit()
                self.drag.emit()
                buttonDown = True
            else:
                self.rightHover.emit()
            if self.middleDown:
                self.middleClickOnRelease = False
                if self.middlePullOnDrag:
                    self.middlePull.emit()
                    self.middlePullOnDrag = False
                self.middleDrag.emit()
                self.drag.emit()
                buttonDown = True
            else:
                self.middleHover.emit()
            if not buttonDown:
                self.hover.emit()
        else:
            pass
