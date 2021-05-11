import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog, QHBoxLayout, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon



class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.data = None

    def initUI(self, widgetStatat1=None, widgetStatat2=None, layout=None):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        openAct = QAction(QIcon('open.png'), '&Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open file dialog')
        openAct.triggered.connect(self.openFile)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        fileMenu.addSeparator()
        fileMenu.addAction(openAct)

        layoutH = QHBoxLayout()
        layoutV = QVBoxLayout()

        layoutV.setContentsMargins(0,0,0,0)



        widgetTable = QWidget()
        widgetTable.setStyleSheet('background-color: blue;')

        widgetStat = QWidget()
        widgetStat.setLayout(layoutV)

        widgetStat1 = QWidget()
        widgetStat1.setStyleSheet('background-color: red;')

        widgetStat2 = QWidget()
        widgetStat2.setStyleSheet('background-color: green;')

        layoutV.addWidget(widgetStat1,1)
        layoutV.addWidget(widgetStat2,1)
        
        layoutH.addWidget(widgetTable, 2)
        layoutH.addWidget(widgetStat, 2)


        widget = QWidget()
        widget.setLayout(layoutH)
        self.setCentralWidget(widget)

        self.setGeometry(500, 500, 500, 400)
        self.setWindowTitle('Simple menu')
        self.show()


    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File","",
                                                  "All Files (*);;Excel Files (*.xlsx) ;;"
                                                  "CSV Files (*.csv)", options=options)

        if fileName:
            f = open(fileName, "r")
            self.data = [i.split(";") for i in f.read().split("\n")]
            print(self.data)



def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()