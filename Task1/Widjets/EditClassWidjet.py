import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QTabWidget,QLabel,QLineEdit)
from PyQt5.QtCore import pyqtSlot
from Subsistems.ResiterSubsistem import NameSubsistem

class UEditClassWidjet(QWidget):
    def __init__(self):
        super().__init__()
        self.MainLayout = None
        self.InitUI()
        self.LastSaveID = 0

    def handle_cell_clicked(self, row, col):
        pass
    def InitUI(self):
        self.MainLayout = QVBoxLayout()
        self.setLayout(self.MainLayout)
    def AddNew(self):
        pass
    def Save(self):
        pass
    def Remove(self):
        pass



