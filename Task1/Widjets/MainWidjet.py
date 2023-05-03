import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QTabWidget,QLabel,QLineEdit)
from PyQt5.QtCore import pyqtSlot
from Subsistems.ResiterSubsistem import NameSubsistem
class UMainAppWidjet(QMainWindow):

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
        ClientsArray = NameSubsistem.GetReferencesByClass("UClient")
        TableWidjetClients.setRowCount(len(ClientsArray))
        TableWidjetClients.setColumnCount(5)
        c = 0
        for x in ClientsArray:
            pushstring = x.Name + " " + x.Family + " " + x.Second_Name + " "+ x.passport + " "+ x.Comment
            TableWidjetClients.setItem(0,c,x.Name)
            TableWidjetClients.setItem(1, c, x.Family)
            TableWidjetClients.setItem(2, c, x.Second_Name)
            TableWidjetClients.setItem(3, c, x.passport)
            TableWidjetClients.setItem(4, c, x.Comment)
            c=c+1
        TableWidjetClients.setHorizontalHeaderLabels(("Name","Family","Second_Name","passport","Comment"))
        MiddleTabs.addTab(TableWidjetClients, "Clients")

        TableWidjetRooms = QtWidgets.QTableWidget()
        RoomsArray = NameSubsistem.GetReferencesByClass("UHotelRoom")
        TableWidjetRooms.setRowCount(len(RoomsArray))
        TableWidjetRooms.setColumnCount(3)
        c = 0
        for x in RoomsArray:
            TableWidjetClients.setItem(0, c, x.MaxNumber)
            TableWidjetClients.setItem(1, c, x.Comfort)
            TableWidjetClients.setItem(2, c, x.Pay)
            c=c+1
        TableWidjetRooms.setHorizontalHeaderLabels(("MaxNumber", "Comfort","Pay"))
        MiddleTabs.addTab(TableWidjetRooms, "Rooms")

        TableWidjetBookings = QtWidgets.QTableWidget()
        BookingsArray = NameSubsistem.GetReferencesByClass("UBookings")
        TableWidjetBookings.setRowCount(len(BookingsArray))
        TableWidjetBookings.setColumnCount(5)
        for x in BookingsArray:
            TableWidjetClients.setItem(0, c, x.Client.Name)
            TableWidjetClients.setItem(1, c, x.HotelRoom.ID)
            TableWidjetClients.setItem(2, c, x.DateOn)
            TableWidjetClients.setItem(3, c, x.DateOff)
            TableWidjetClients.setItem(4, c, x.Comment)
            
        TableWidjetBookings.setHorizontalHeaderLabels(("Client","HotelRoom","DateOn","DateOff","Comment"))
        MiddleTabs.addTab(TableWidjetBookings, "Bookings")
        MainCanvansWidjet.setLayout(GlobalLayout)

        BottomLayout = QVBoxLayout()
        GlobalLayout.addWidget(BottomLayout)

        List = QHBoxLayout()
        TextName = QLabel('Title')
        TextNameEdit = QLineEdit()
        List.addWidget(TextName)
        List.addWidget(TextNameEdit)
        BottomLayout.addLayout(List)

        List = QHBoxLayout()
        TextName = QLabel('Title')
        TextNameEdit = QLineEdit()
        List.addWidget(TextName)
        List.addWidget(TextNameEdit)
        BottomLayout.addLayout(List)

        self.show()
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = UMainAppWidjet()
    sys.exit(app.exec_())