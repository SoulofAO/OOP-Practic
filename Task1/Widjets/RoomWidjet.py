import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QGridLayout, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QTabWidget,QLabel,QLineEdit)
from PyQt5.QtCore import pyqtSlot
from Subsistems.ResiterSubsistem import NameSubsistem
from Widjets.EditClassWidjet import UEditClassWidjet


class URoomWidjet(UEditClassWidjet):
    def InitUI(self):
        super().InitUI()
        TableWidjetClients = QtWidgets.QTableWidget()
        RoomsArray = NameSubsistem.GetReferencesByClass("UHotelRoom")
        TableWidjetClients.setRowCount(len(RoomsArray))
        TableWidjetClients.setColumnCount(3)
        self.MainLayout.addWidget(TableWidjetClients)
        c = 0
        for x in RoomsArray:
            TableWidjetClients.setItem(c,0,QTableWidgetItem(str(x.MaxNumber)))
            TableWidjetClients.setItem(c,1, QTableWidgetItem(str(x.Comfort)))
            TableWidjetClients.setItem(c,2, QTableWidgetItem(str(x.Pay)))
            c=c+1
        TableWidjetClients.setHorizontalHeaderLabels(("MaxNumber","Comfort","Pay"))


        GridLayout = QGridLayout()
        self.MainLayout.addLayout(GridLayout)

        self.WTextMaxNumber= QLabel("MaxNumber")
        self.WTextMaxNumberEdit = QTextEdit()
        GridLayout.addWidget(self.WTextMaxNumber,0,0)
        GridLayout.addWidget(self.WTextMaxNumberEdit,0,1)

        self.WTextComfort = QLabel("Comfort")
        self.WTextComfortEdit = QTextEdit()
        GridLayout.addWidget(self.WTextComfort,1,0)
        GridLayout.addWidget(self.WTextComfortEdit,1,1)

        WHList = QHBoxLayout()
        self.WTextPay = QLabel("Pay")
        self.WTextPayEdit = QTextEdit()
        GridLayout.addWidget(self.WTextPay,2,0)
        GridLayout.addWidget(self.WTextPayEdit,2,1)
