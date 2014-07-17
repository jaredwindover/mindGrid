from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ViewingWindow import ViewingWindow


class MainWindow(QWidget):

    def __init__(self,*args):
        super(MainWindow,self).__init__(*args)
        self.initUI()

    def initUI(self):

        #Initializing layouts
        self.vLayout0 = QVBoxLayout()
        self.hLayout1a = QHBoxLayout()
        self.vLayout2a = QVBoxLayout()
        self.vLayout2b = QVBoxLayout()

        self.nodeTitle = QLineEdit()
        self.nodeContent = QTextEdit()
        self.vLayout2a.addWidget(self.nodeTitle)
        self.vLayout2a.addWidget(self.nodeContent)

        self.updateButton = QPushButton("Update")
        self.updateButton.clicked.connect(self.onUpdate)
        self.vLayout2b.addWidget(self.updateButton)

        #Composing Bottom Gui
        self.hLayout1a.addLayout(self.vLayout2a)
        self.hLayout1a.addLayout(self.vLayout2b)

        #Composing Final Layout
        self.viewingWindow = ViewingWindow(self)
        self.viewingWindow.nodeSelected.connect(self.updateText)
        self.vLayout0.addWidget(self.viewingWindow)
        self.vLayout0.addLayout(self.hLayout1a)

        self.setLayout(self.vLayout0)

    def updateText(self):
        try:
            title = self.viewingWindow.selectedNode.title
            text = self.viewingWindow.selectedNode.text
            self.nodeTitle.setText(title)
            self.nodeContent.setDocument(text)
        except:
            print "We had an error"
            print title
            print text
            pass
        
    def onUpdate(self):
        try:
            node = self.viewingWindow.selectedNode
            text = self.nodeContent.document()
            title = self.nodeTitle.text()
            node.title = title
            node.text = text
        except:
            pass
