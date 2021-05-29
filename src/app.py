#!/usr/bin/env python3

import sys, time
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class MyMDIApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        workspace = QMdiArea()
        
        for i in range(8):
            textEdit = QTextEdit()
            textEdit.setPlainText("Dummy Text " * 100)
            textEdit.setWindowTitle("Document %i" % i)
            workspace.addSubWindow(textEdit)

        self.setCentralWidget(workspace)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.setGeometry(300, 300, 800, 600)
        self.show()


def main():
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myMDIApp = MyMDIApp()
        myMDIApp.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])


if __name__ =='__main__':
    main()

