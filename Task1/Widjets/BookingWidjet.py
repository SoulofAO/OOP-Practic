import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QGridLayout, QTableWidgetItem, QMessageBox
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
    def handle_cell_clicked(self, row, col):
        ClientID = self.TableWidjetClients.item(row,0).text()
        HotelRoomID = self.TableWidjetClients.item(row,1).text()
        DateOn = self.TableWidjetClients.item(row,2).text()
        DateOff = self.TableWidjetClients.item(row, 3).text()
        Comment = self.TableWidjetClients.item(row, 4).text()
        self.LastSaveID = int(self.TableWidjetClients.item(row, 5).text())

        self.WClientIDEdit.setText(ClientID)
        self.WTextHotelRoomEdit.setText(HotelRoomID)
        self.WTextDateOnEdit.setText(DateOn)
        self.WTextDateOffEdit.setText(DateOff)
        self.WTextCommentEdit.setText(Comment)

    def InitUI(self):
        super().InitUI()
        self.TableWidjetClients = QtWidgets.QTableWidget()
        ClientsArray = NameSubsistem.GetReferencesByClass("UBooking")
        self.TableWidjetClients.setRowCount(len(ClientsArray))
        self.TableWidjetClients.setColumnCount(6)
        self.MainLayout.addWidget(self.TableWidjetClients)
        c = 0
        for x in ClientsArray:
            ClientID = NameSubsistem.GetIDByReference(x.Client)
            HotelRoomID = NameSubsistem.GetIDByReference(x.HotelRoom)
            self.TableWidjetClients.setItem(c,0,QTableWidgetItem(str(ClientID)))
            self.TableWidjetClients.setItem(c,1, QTableWidgetItem(str(HotelRoomID)))
            self.TableWidjetClients.setItem(c,2, QTableWidgetItem(x.DateOn))
            self.TableWidjetClients.setItem(c,3, QTableWidgetItem(x.DateOff))
            self.TableWidjetClients.setItem(c,4, QTableWidgetItem(x.Comment))
            self.TableWidjetClients.setItem(c,5, QTableWidgetItem(str(x.ID)))
            c=c+1
        self.TableWidjetClients.setHorizontalHeaderLabels(("ClientID","HotelRoomID","DateOn","DateOff","Comment","ID"))
        self.TableWidjetClients.cellClicked.connect(self.handle_cell_clicked)

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