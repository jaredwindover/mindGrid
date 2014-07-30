from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ViewingWindow import ViewingWindow


class MainWindow(QMainWindow):
    def __init__(self,*args):
        super(MainWindow,self).__init__(*args)
        self.initUI()
        self.fileName = None

    def initUI(self):
        self.setCentralWidget(MainWidget())
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')

        saveAction = QAction('&save',self)
        saveAction.triggered.connect(self.save)
        fileMenu.addAction(saveAction)

        saveAsAction = QAction('&Save as',self)
        saveAsAction.triggered.connect(self.saveAs)
        fileMenu.addAction(saveAsAction)

        openAction = QAction('&open',self)
        openAction.triggered.connect(self.open)
        fileMenu.addAction(openAction)
        
        exitAction = QAction('&exit',self)
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

    def open(self):
        try:
            self.fileName = QFileDialog.getOpenFileName(self)
            self.readFrom(self.fileName)
        except:
            print "Error opening file"
            self.fileName = None

    def save(self):
        try:
            if self.fileName == None:
                self.saveAs()
            else:
                self.writeTo(self.fileName)
        except:
            print "Error saving file"

    def saveAs(self):
        try:
            self.fileName = QFileDialog.getSaveFileName(self)
            self.writeTo(self.fileName)
        except:
            print "Error saving file"
            self.fileName = None

    def readFrom(self,fileName):
        self.centralWidget().viewingWindow.readFrom(fileName)

    def writeTo(self,fileName):
        self.centralWidget().viewingWindow.writeTo(fileName)

class MainWidget(QWidget):

    def __init__(self,*args):
        super(MainWidget,self).__init__(*args)
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
        self.viewingWindow.nodeUnselected.connect(self.onUnselect)
        self.vLayout0.addWidget(self.viewingWindow)
        self.vLayout0.addLayout(self.hLayout1a)

        self.setLayout(self.vLayout0)

    def updateText(self):
        try:
            title = self.viewingWindow.selectedNode.title
            text = self.viewingWindow.selectedNode.text
            self.nodeTitle.setText(title)
            self.nodeContent.setDocument(text)
            self.nodeTitle.setFocus()
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

    def onUnselect(self):
        try:
            self.nodeTitle.setText(QString())
            self.nodeContent.setDocument(QTextDocument(QString()))
        except:
            pass
