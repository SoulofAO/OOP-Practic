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

    def SaveButtonHandle(self):
        CurrentTab = self.MiddleTabs.currentWidget()
        CurrentTab.Save()
    def AddButtonHandle(self):
        CurrentTab = self.MiddleTabs.currentWidget()
        CurrentTab.AddNew()
    def RemoveButtonHandle(self):
        CurrentTab = self.MiddleTabs.currentWidget()
        CurrentTab.Remove()

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

        self.MiddleTabs = QTabWidget()
        MiddelHLayout.addWidget(self.MiddleTabs)

        self.ShowClientWidjet = UClientWidjet()
        self.ShowBookingWidjet = UBookingWidjet()
        self.ShowRoomWidjet = URoomWidjet()
        self.MiddleTabs.addTab(self.ShowClientWidjet, "Clients")
        self.MiddleTabs.addTab(self.ShowBookingWidjet, "Bookings")
        self.MiddleTabs.addTab(self.ShowRoomWidjet, "Rooms")

        ButtonTaskLayout = QVBoxLayout()
        MiddelHLayout.addLayout(ButtonTaskLayout)

        self.PushAddButton = QPushButton("Add")
        self.PushAddButton.clicked.connect(self.AddButtonHandle())
        self.PushSaveButton = QPushButton("Change")
        self.PushSaveButton.clicked.connect(self.SaveButtonHandle())
        self.DeleteButton = QPushButton("Delete")
        self.DeleteButton.clicked.connect(self.RemoveButtonHandle())

        ButtonTaskLayout.addWidget(self.PushAddButton)
        ButtonTaskLayout.addWidget(self.PushSaveButton)
        ButtonTaskLayout.addWidget(self.DeleteButton)


        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = UMainAppWidjet()
    sys.exit(app.exec_())
