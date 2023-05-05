import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QGridLayout, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QTabWidget,QLabel,QLineEdit)
from PyQt5.QtCore import pyqtSlot
from Subsistems.ResiterSubsistem import NameSubsistem
from Widjets.EditClassWidjet import UEditClassWidjet
from MainClasses.Client import UClient

class UClientWidjet(UEditClassWidjet):
    def handle_cell_clicked(self, row, col):
        Name = self.TableWidjetClients.item(row,0).text()
        Family = self.TableWidjetClients.item(row,1).text()
        Second_Name = self.TableWidjetClients.item(row,2).text()
        passport = self.TableWidjetClients.item(row, 3).text()
        Comment = self.TableWidjetClients.item(row, 4).text()
        self.LastSaveID = int(self.TableWidjetClients.item(row, 5).text())
        self.WTextNameEdit.setText(Name)
        self.WTextFamilyEdit.setText(Family)
        self.WTextSecondNameEdit.setText(Second_Name)
        self.WTextPassportEdit.setText(passport)
        self.WTextCommentEdit.setText(Comment)
    def GenerateTable(self):
        ClientsArray = NameSubsistem.GetReferencesByClass("UClient")
        self.TableWidjetClients.setRowCount(len(ClientsArray))
        self.TableWidjetClients.setColumnCount(6)
        c = 0
        for x in ClientsArray:
            self.TableWidjetClients.setItem(c,0, QTableWidgetItem(x.Name))
            self.TableWidjetClients.setItem(c,1, QTableWidgetItem(x.Family))
            self.TableWidjetClients.setItem(c,2, QTableWidgetItem(x.Second_Name))
            self.TableWidjetClients.setItem(c,3, QTableWidgetItem(str(x.passport)))
            self.TableWidjetClients.setItem(c,4, QTableWidgetItem(x.Comment))
            self.TableWidjetClients.setItem(c,5, QTableWidgetItem(str(x.ID)))
            c=c+1
        self.TableWidjetClients.setHorizontalHeaderLabels(("Name","Family","Second_Name","passport","Comment","ID"))
    def InitUI(self):
        super().InitUI()
        self.TableWidjetClients = QtWidgets.QTableWidget()
        self.MainLayout.addWidget(self.TableWidjetClients)
        self.GenerateTable()
        self.TableWidjetClients.cellClicked.connect(self.handle_cell_clicked)

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
        GridLayout.addWidget(self.WTextSecondName,2,0)
        GridLayout.addWidget(self.WTextSecondNameEdit,2,1)

        self.WTextPassport = QLabel("Passport")
        self.WTextPassportEdit = QTextEdit()
        GridLayout.addWidget(self.WTextPassport,3,0)
        GridLayout.addWidget(self.WTextPassportEdit,3,1)

        self.WTextComment = QLabel("Comment")
        self.WTextCommentEdit = QTextEdit()
        GridLayout.addWidget(self.WTextComment,4,0)
        GridLayout.addWidget(self.WTextCommentEdit,4,1)
    def AddNew(self):
        Name = self.WTextNameEdit.toPlainText()
        Family = self.WTextFamilyEdit.toPlainText()
        Second_Name = self.WTextSecondNameEdit.toPlainText()
        passport = self.WTextPassportEdit.toPlainText()
        Comment = self.WTextCommentEdit.toPlainText()
        Client = UClient()
        Client.Name = Name
        Client.Family = Family
        Client.Second_Name = Second_Name
        Client.passport = passport
        Client.Comment = Comment
        self.GenerateTable()


    def Save(self):
        Name = self.WTextNameEdit.toPlainText()
        Family = self.WTextFamilyEdit.toPlainText()
        Second_Name = self.WTextSecondNameEdit.toPlainText()
        passport = self.WTextPassportEdit.toPlainText()
        Comment = self.WTextCommentEdit.toPlainText()
        Client = NameSubsistem.GetReferenceByID("UClient",self.LastSaveID)
        Client.Name = Name
        Client.Family = Family
        Client.Second_Name = Second_Name
        Client.passport = passport
        Client.Comment = Comment
        self.GenerateTable()
    def Remove(self):
        Object = NameSubsistem.GetReferenceByID("UClient",self.LastSaveID)
        NameSubsistem.DeleteObject(Object)
        self.GenerateTable()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = UClientWidjet()
    ex.setGeometry(300, 300, 250, 150)
    ex.setWindowTitle('Quit button')
    ex.show()
    sys.exit(app.exec_())
