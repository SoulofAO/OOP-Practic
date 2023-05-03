import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
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
        self.initUI()
    def InitUI(self):
        TableWidjetClients = QtWidgets.QTableWidget()
        ClientsArray = NameSubsistem.GetReferencesByClass("UClient")
        TableWidjetClients.setRowCount(len(ClientsArray))
        TableWidjetClients.setColumnCount(5)
        self.MainLayout.addWidget(TableWidjetClients)
        c = 0
        for x in ClientsArray:
            TableWidjetClients.setItem(0,c,x.Name)
            TableWidjetClients.setItem(1, c, x.Family)
            TableWidjetClients.setItem(2, c, x.Second_Name)
            TableWidjetClients.setItem(3, c, x.passport)
            TableWidjetClients.setItem(4, c, x.Comment)
            c=c+1
        TableWidjetClients.setHorizontalHeaderLabels(("Name","Family","Second_Name","passport","Comment"))

        BottomLayout = QVBoxLayout()
        self.MainLayout.addWidget(BottomLayout)

        WHList = QHBoxLayout()
        self.WTextName = QLabel("Name")
        self.WTextNameEdit = QTextEdit()
        WHList.addWidget(self.WTextName)
        WHList.addWidget(self.WTextNameEdit)
        BottomLayout.addLayout(WHList)

        WHList = QHBoxLayout()
        self.WTextFamily = QLabel("Family")
        self.WTextFamilyEdit = QTextEdit()
        WHList.addWidget(self.WTextFamily)
        WHList.addWidget(self.WTextFamilyEdit)
        BottomLayout.addLayout(WHList)

        WHList = QHBoxLayout()
        self.WTextSecondName = QLabel("SecondName")
        self.WTextSecondNameEdit = QTextEdit()
        WHList.addWidget(self.WTextFamily)
        WHList.addWidget(self.WTextFamilyEdit)
        BottomLayout.addLayout(WHList)

        WHList = QHBoxLayout()
        self.WTextSecondName = QLabel("SecondName")
        self.WTextSecondNameEdit = QTextEdit()
        WHList.addWidget(self.WTextSecondName)
        WHList.addWidget(self.WTextSecondNameEdit)
        BottomLayout.addLayout(WHList)

        WHList = QHBoxLayout()
        self.WTextPassport = QLabel("Passport")
        self.WTextPassportEdit = QTextEdit()
        WHList.addWidget(self.WTextPassport)
        WHList.addWidget(self.WTextPassportEdit)
        BottomLayout.addLayout(WHList)

        WHList = QHBoxLayout()
        self.WTextComment = QLabel("Comment")
        self.WTextCommentEdit = QTextEdit()
        WHList.addWidget(self.WTextComment)
        WHList.addWidget(self.WTextCommentEdit)
        BottomLayout.addLayout(WHList)