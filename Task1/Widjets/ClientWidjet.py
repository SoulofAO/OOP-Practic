import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QTabWidget,QLabel,QLineEdit)
from PyQt5.QtCore import pyqtSlot
from Subsistems.ResiterSubsistem import NameSubsistem
from Widjets.EditClassWidjet import UEditClassWidjet


class UClientWidjet(UEditClassWidjet):
    def InitUI(self):
        super().InitUI()
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

        GridLayout = QGridLayout()
        self.MainLayout.addLayout(GridLayout)

        self.WTextName = QLabel("Name")
        self.WTextNameEdit = QTextEdit()
        GridLayout.addWidget(self.WTextName,0,0)
        GridLayout.addWidget(self.WTextNameEdit,0,1)

        self.WTextFamily = QLabel("Family")
        self.WTextFamilyEdit = QTextEdit()
        GridLayout.addWidget(self.WTextFamily,1,0)
        GridLayout.addWidget(self.WTextFamilyEdit,1,1)

        self.WTextSecondName = QLabel("SecondName")
        self.WTextSecondNameEdit = QTextEdit()
        GridLayout.addWidget(self.WTextFamily,2,0)
        GridLayout.addWidget(self.WTextFamilyEdit,2,1)

        self.WTextPassport = QLabel("Passport")
        self.WTextPassportEdit = QTextEdit()
        GridLayout.addWidget(self.WTextPassport,3,0)
        GridLayout.addWidget(self.WTextPassportEdit,3,1)

        self.WTextComment = QLabel("Comment")
        self.WTextCommentEdit = QTextEdit()
        GridLayout.addWidget(self.WTextComment,4,0)
        GridLayout.addWidget(self.WTextCommentEdit,4,1)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = UClientWidjet()
    ex.setGeometry(300, 300, 250, 150)
    ex.setWindowTitle('Quit button')
    ex.show()
    sys.exit(app.exec_())
