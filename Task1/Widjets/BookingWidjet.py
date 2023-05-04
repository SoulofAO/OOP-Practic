import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QGridLayout, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QTabWidget,QLabel,QLineEdit)
from PyQt5.QtCore import pyqtSlot
from Subsistems.ResiterSubsistem import NameSubsistem
from Widjets.EditClassWidjet import UEditClassWidjet


class UBookingWidjet(UEditClassWidjet):
    def __init__(self):
        super().__init__()
        self.WTextDateOnEdit = None
        self.WTextDateOn = None

    def InitUI(self):
        super().InitUI()
        TableWidjetClients = QtWidgets.QTableWidget()
        ClientsArray = NameSubsistem.GetReferencesByClass("UBooking")
        TableWidjetClients.setRowCount(len(ClientsArray))
        TableWidjetClients.setColumnCount(5)
        self.MainLayout.addWidget(TableWidjetClients)
        c = 0
        for x in ClientsArray:
            ClientID = NameSubsistem.GetIDByReference(x.Client)
            HotelRoomID = NameSubsistem.GetIDByReference(x.HotelRoom)
            TableWidjetClients.setItem(c,0,QTableWidgetItem(str(ClientID)))
            TableWidjetClients.setItem(c,1, QTableWidgetItem(str(HotelRoomID)))
            TableWidjetClients.setItem(c,2, QTableWidgetItem(x.DateOn))
            TableWidjetClients.setItem(c,3, QTableWidgetItem(x.DateOff))
            TableWidjetClients.setItem(c,4, QTableWidgetItem(x.Comment))
            c=c+1
        TableWidjetClients.setHorizontalHeaderLabels(("ClientID","HotelRoomID","DateOn","DateOff","Comment"))

        GridLayout = QGridLayout()
        self.MainLayout.addLayout(GridLayout)

        self.WClientID = QLabel("ClientID")
        self.WClientIDEdit = QTextEdit()
        GridLayout.addWidget(self.WClientID,0,0)
        GridLayout.addWidget(self.WClientIDEdit,0,1)

        self.WTextHotelRoom = QLabel("HotelRoomID")
        self.WTextHotelRoomEdit = QTextEdit()
        GridLayout.addWidget(self.WTextHotelRoom,1,0)
        GridLayout.addWidget(self.WTextHotelRoomEdit,1,1)

        self.WTextDateOn = QLabel("DateOn")
        self.WTextDateOnEdit = QTextEdit()
        GridLayout.addWidget(self.WTextDateOn,2,0)
        GridLayout.addWidget(self.WTextDateOnEdit,2,1)

        self.WTextDateOff = QLabel("DateOff")
        self.WTextDateOffEdit = QTextEdit()
        GridLayout.addWidget(self.WTextDateOff,3,0)
        GridLayout.addWidget(self.WTextDateOffEdit,3,1)

        self.WTextComment = QLabel("Comment")
        self.WTextCommentEdit = QTextEdit()
        GridLayout.addWidget(self.WTextComment,4,0)
        GridLayout.addWidget(self.WTextCommentEdit,4,1)