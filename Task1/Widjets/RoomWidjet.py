import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QGridLayout, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QTabWidget,QLabel,QLineEdit)
from PyQt5.QtCore import pyqtSlot
from Subsistems.ResiterSubsistem import NameSubsistem
from Widjets.EditClassWidjet import UEditClassWidjet
from MainClasses.HotelRoom import UHotelRoom
from PyQt5 import QtWidgets, QtCore
class URoomWidjet(UEditClassWidjet):
    def handle_cell_clicked(self, row, col):
        MaxNumber = self.TableWidjetClients.item(row,0).text()
        Comfort = self.TableWidjetClients.item(row,1).text()
        Pay = self.TableWidjetClients.item(row,2).text()
        self.LastSaveID = int(self.TableWidjetClients.item(row, 3).text())
        self.WTextMaxNumberEdit.setText(MaxNumber)
        self.WTextComfortEdit.setText(Comfort)
        self.WTextPayEdit.setText(Pay)

    def GenerateTable(self):
        RoomsArray = NameSubsistem.GetReferencesByClass("UHotelRoom")
        self.TableWidjetClients.setRowCount(len(RoomsArray))
        self.TableWidjetClients.setColumnCount(4)
        c = 0
        for x in RoomsArray:
            self.TableWidjetClients.setItem(c,0,QTableWidgetItem(str(x.MaxNumber)))
            self.TableWidjetClients.setItem(c,1, QTableWidgetItem(str(x.Comfort)))
            self.TableWidjetClients.setItem(c,2, QTableWidgetItem(str(x.Pay)))
            SelfID = QTableWidgetItem(str(x.ID))
            SelfID.setFlags(QtCore.Qt.ItemIsEditable)
            self.TableWidjetClients.setItem(c, 3, SelfID)
            c=c+1
        self.TableWidjetClients.setHorizontalHeaderLabels(("MaxNumber","Comfort","Pay","ID"))
    def InitUI(self):
        super().InitUI()
        self.TableWidjetClients = QtWidgets.QTableWidget()
        self.MainLayout.addWidget(self.TableWidjetClients)
        self.GenerateTable()
        self.TableWidjetClients.cellClicked.connect(self.handle_cell_clicked)

        GridLayout = QGridLayout()
        self.MainLayout.addLayout(GridLayout)

        self.WTextMaxNumber= QLabel("MaxNumber")
        self.WTextMaxNumberEdit = QLineEdit()
        GridLayout.addWidget(self.WTextMaxNumber,0,0)
        GridLayout.addWidget(self.WTextMaxNumberEdit,0,1)

        self.WTextComfort = QLabel("Comfort")
        self.WTextComfortEdit = QLineEdit()
        GridLayout.addWidget(self.WTextComfort,1,0)
        GridLayout.addWidget(self.WTextComfortEdit,1,1)

        WHList = QHBoxLayout()
        self.WTextPay = QLabel("Pay")
        self.WTextPayEdit = QLineEdit()
        GridLayout.addWidget(self.WTextPay,2,0)
        GridLayout.addWidget(self.WTextPayEdit,2,1)
    def AddNew(self):
        MaxNumber = self.WTextMaxNumberEdit.text()
        Comfort = self.WTextComfortEdit.text()
        Pay = self.WTextPayEdit.text()
        HotelRoom = UHotelRoom()
        HotelRoom.Name = MaxNumber
        HotelRoom.Comfort = Comfort
        HotelRoom.Pay = Pay
        self.GenerateTable()
    def Save(self):
        MaxNumber = int(self.WTextMaxNumberEdit.text())
        Comfort = int(self.WTextComfortEdit.text())
        Pay = int(self.WTextPayEdit.text())
        HotelRoom = NameSubsistem.GetReferenceByID("UHotelRoom",self.LastSaveID)
        HotelRoom.Name = MaxNumber
        HotelRoom.Comfort = Comfort
        HotelRoom.Pay = Pay
        self.GenerateTable()
    def Remove(self):
        Object = NameSubsistem.GetReferenceByID("UHotelRoom",self.LastSaveID)
        NameSubsistem.DeleteObject(Object)
        self.GenerateTable()

