import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QTabWidget,QLabel,QLineEdit)
from PyQt5.QtCore import pyqtSlot
from Subsistems.ResiterSubsistem import NameSubsistem
from Widjets.ClientWidjet import UClientWidjet
from Widjets.BookingWidjet import UBookingWidjet
from Widjets.RoomWidjet import URoomWidjet
class UMainAppWidjet(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ShowRoomWidjet = None
        self.ShowBookingWidjet = None
        self.ShowClientWidjet = None
        self.initUI()


    def initUI(self):

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

        MainCanvansWidjet = QWidget()
        self.setCentralWidget(MainCanvansWidjet)

        GlobalLayout = QVBoxLayout()
        MainCanvansWidjet.setLayout(GlobalLayout)

        MiddelHLayout = QHBoxLayout()
        GlobalLayout.addLayout(MiddelHLayout)

        MiddleTabs = QTabWidget()
        MiddelHLayout.addWidget(MiddleTabs)

        self.ShowClientWidjet = UClientWidjet()
        self.ShowBookingWidjet = UBookingWidjet()
        self.ShowRoomWidjet = URoomWidjet()
        MiddleTabs.addTab(self.ShowClientWidjet, "Clients")
        MiddleTabs.addTab(self.ShowBookingWidjet, "Bookings")
        MiddleTabs.addTab(self.ShowRoomWidjet, "Rooms")

        ButtonTaskLayout = QVBoxLayout()
        MiddelHLayout.addLayout(ButtonTaskLayout)

        self.PushAddButton = QPushButton("Add")
        self.PushChangeButton = QPushButton("Change")
        self.DeleteButton = QPushButton("Delete")
        ButtonTaskLayout.addWidget(self.PushAddButton)
        ButtonTaskLayout.addWidget(self.PushChangeButton)
        ButtonTaskLayout.addWidget(self.DeleteButton)


        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = UMainAppWidjet()
    sys.exit(app.exec_())
