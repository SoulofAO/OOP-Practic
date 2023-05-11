import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QGridLayout, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QTabWidget,QLabel,QLineEdit)
from PyQt5.QtCore import pyqtSlot
from Subsistems.ResiterSubsistem import NameSubsistem
from Widjets.EditClassWidjet import UEditClassWidjet
from MainClasses.Booking import UBooking
from PyQt5 import QtWidgets, QtCore

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
    def GenerateSelectComboBox(self):
        self.SelectClientComboBox.clear()
        ClientsArray = NameSubsistem.GetReferencesByClass("UClient")
        self.ArrayClients = []
        for x in ClientsArray:
            self.SelectClientComboBox.addItem(x.Name)
            self.ArrayClients.append(x.ID)

    def on_combo_box_changed(self,index):
        selected_item = self.SelectClientComboBox.currentText()
        self.WClientIDEdit.setText(str(self.ArrayClients[index]))

    def on_combo_box_activated(self):
        self.GenerateSelectComboBox()
    def GenerateTable(self):
        ClientsArray = NameSubsistem.GetReferencesByClass("UBooking")
        self.TableWidjetClients.setRowCount(len(ClientsArray))
        self.TableWidjetClients.setColumnCount(6)
        c = 0
        for x in ClientsArray:
            ClientID = NameSubsistem.GetIDByReference(x.Client)
            HotelRoomID = NameSubsistem.GetIDByReference(x.HotelRoom)
            ClientItem = QTableWidgetItem(str(ClientID))
            ClientItem.setFlags(QtCore.Qt.ItemIsEditable)
            HotelItem = QTableWidgetItem(str(HotelRoomID))
            HotelItem.setFlags(QtCore.Qt.ItemIsEditable)
            self.TableWidjetClients.setItem(c,0,ClientItem)
            self.TableWidjetClients.setItem(c,1, HotelItem)
            self.TableWidjetClients.setItem(c,2, QTableWidgetItem(x.DateOn))
            self.TableWidjetClients.setItem(c,3, QTableWidgetItem(x.DateOff))
            self.TableWidjetClients.setItem(c,4, QTableWidgetItem(x.Comment))
            SelfID = QTableWidgetItem(str(x.ID))
            SelfID.setFlags(QtCore.Qt.ItemIsEditable)
            self.TableWidjetClients.setItem(c,5, SelfID)
            c=c+1
        self.TableWidjetClients.setHorizontalHeaderLabels(("ClientID","HotelRoomID","DateOn","DateOff","Comment","ID"))
    def InitUI(self):
        super().InitUI()
        self.TableWidjetClients = QtWidgets.QTableWidget()
        self.MainLayout.addWidget(self.TableWidjetClients)
        self.GenerateTable()
        self.TableWidjetClients.cellClicked.connect(self.handle_cell_clicked)

        GridLayout = QGridLayout()
        self.MainLayout.addLayout(GridLayout)

        self.WClientID = QLabel("ClientID")
        self.WClientIDEdit = QLineEdit()
        GridLayout.addWidget(self.WClientID,0,0)
        GridLayout.addWidget(self.WClientIDEdit,0,1)
        self.SelectClientComboBox = QtWidgets.QComboBox()
        self.GenerateSelectComboBox()
        self.SelectClientComboBox.activated.connect(self.on_combo_box_activated)
        self.SelectClientComboBox.currentIndexChanged.connect(self.on_combo_box_changed)
        GridLayout.addWidget(self.SelectClientComboBox, 0, 2)

        self.WTextHotelRoom = QLabel("HotelRoomID")
        self.WTextHotelRoomEdit = QLineEdit()
        GridLayout.addWidget(self.WTextHotelRoom,1,0)
        GridLayout.addWidget(self.WTextHotelRoomEdit,1,1)

        self.WTextDateOn = QLabel("DateOn")
        self.WTextDateOnEdit = QLineEdit()
        GridLayout.addWidget(self.WTextDateOn,2,0)
        GridLayout.addWidget(self.WTextDateOnEdit,2,1)

        self.WTextDateOff = QLabel("DateOff")
        self.WTextDateOffEdit = QLineEdit()
        GridLayout.addWidget(self.WTextDateOff,3,0)
        GridLayout.addWidget(self.WTextDateOffEdit,3,1)

        self.WTextComment = QLabel("Comment")
        self.WTextCommentEdit = QTextEdit()
        GridLayout.addWidget(self.WTextComment,4,0)
        GridLayout.addWidget(self.WTextCommentEdit,4,1)
    def AddNew(self):
        ClientID = self.WClientIDEdit.text()
        HotelRoomID = self.WTextHotelRoomEdit.text()
        DateOn = self.WTextDateOnEdit.text()
        DateOff = self.WTextDateOffEdit.text()
        Comment = self.WTextCommentEdit.toPlainText()
        Booking = UBooking()
        Client = NameSubsistem.GetReferenceByID("UClient",int(ClientID))
        Booking.Client = Client
        HotelRoom = NameSubsistem.GetReferenceByID("UHotelRoom",int(HotelRoomID))
        Booking.HotelRoom = HotelRoom
        Booking.DateOn = DateOn
        Booking.DateOff = DateOff
        Booking.Comment = Comment
        self.GenerateTable()


    def Save(self):
        ClientID = int(self.WClientIDEdit.text())
        HotelRoomID = int(self.WTextHotelRoomEdit.text())
        DateOn = self.WTextDateOnEdit.text()
        DateOff = self.WTextDateOffEdit.text()
        Comment = self.WTextCommentEdit.toPlainText()
        Booking = NameSubsistem.GetReferenceByID("UBooking",self.LastSaveID)
        Client = NameSubsistem.GetReferenceByID("UClient",ClientID)
        Booking.Client = Client
        HotelRoom = NameSubsistem.GetReferenceByID("UHotelRoom",HotelRoomID)
        Booking.HotelRoom = HotelRoom
        Booking.DateOn = DateOn
        Booking.DateOff = DateOff
        Booking.Comment = Comment
        self.GenerateTable()
    def Remove(self):
        Object = NameSubsistem.GetReferenceByID("UBooking",self.LastSaveID)
        NameSubsistem.DeleteObject(Object)
        self.GenerateTable()
