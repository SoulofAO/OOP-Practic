import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QTabWidget)
from PyQt5.QtCore import pyqtSlot
from Subsistems.ResiterSubsistem import NameSubsistem

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        GlobalLayout = QVBoxLayout()



        MainCanvansWidjet = QtWidgets.QWidget()
        self.setCentralWidget(MainCanvansWidjet)

        MiddleTabs = QTabWidget()
        GlobalLayout.addWidget(MiddleTabs)

        TableWidjetClients = QtWidgets.QTableWidget()
        NameSubsistem.RegisterNewObject()
        TableWidjetClients.setRowCount(3)
        TableWidjetClients.setColumnCount(2)
        TableWidjetClients.setHorizontalHeaderLabels(("brand","Price"))
        MiddleTabs.addTab(TableWidjetClients, "Clients")

        TableWidjetRooms = QtWidgets.QTableWidget()
        TableWidjetRooms.setRowCount(3)
        TableWidjetRooms.setColumnCount(2)
        TableWidjetRooms.setHorizontalHeaderLabels(("brand", "Price"))
        MiddleTabs.addTab(TableWidjetRooms, "Rooms")

        TableWidjetBookings = QtWidgets.QTableWidget()
        TableWidjetBookings.setRowCount(3)
        TableWidjetBookings.setColumnCount(2)
        TableWidjetBookings.setHorizontalHeaderLabels(("brand", "Price"))
        MiddleTabs.addTab(TableWidjetBookings, "Bookings")

        MainCanvansWidjet.setLayout(GlobalLayout)

        self.show()
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())