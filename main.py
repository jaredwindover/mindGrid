import sys
import copy_reg
from MainWindow import MainWindow
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Nodes import *

def main():
    #Add this so we can pickle QTextDocuments
    copy_reg.pickle(QTextDocument,pickle_QtD,unpickle_QtD)
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("WireFrame Model")
    mainWindow.show()
    mainWindow.centralWidget().viewingWindow.animate()
    app.exec_()


def pickle_QtD(qtd):
    return QTextDocument, (qtd.toPlainText(),)

def unpickle_QtD(tup):
    re = QTextDocument()
    re.setPlainText(tup[0])
    return re
    
if __name__ == '__main__':
    main()
