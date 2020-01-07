#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5 import QtGui

class form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('vanreda.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('radnici')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal,"Radnik_ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal,"Ime")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Prezime")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "OIB")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Adresa")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Grad")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Mobitel")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Datum Zaposlenja")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Sifra")
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(8, True)

        self.ui.pushButton.clicked.connect(self.addToDb)
        self.ui.pushButton_4.clicked.connect(self.reset)
        self.show()
        self.ui.pushButton_2.clicked.connect(self.updaterow)
        self.ui.pushButton_3.clicked.connect(self.delrow)
        self.i = self.model.rowCount()
        self.ui.lcdNumber.display(self.i)
        print(self.ui.tableView.currentIndex().row())




    def addToDb(self):

        print(self.i)
        self.model.insertRows(self.i,1)
        self.model.setData(self.model.index(self.i, 0), self.ui.lineEdit_6.text())
        self.model.setData(self.model.index(self.i, 1),self.ui.lineEdit.text())
        self.model.setData(self.model.index(self.i, 2), self.ui.lineEdit_2.text())
        self.model.setData(self.model.index(self.i, 3), self.ui.lineEdit_8.text())
        self.model.setData(self.model.index(self.i, 4), self.ui.lineEdit_4.text())
        self.model.setData(self.model.index(self.i, 5), self.ui.lineEdit_5.text())
        self.model.setData(self.model.index(self.i, 6), self.ui.lineEdit_3.text())
        self.model.setData(self.model.index(self.i, 7), self.ui.dateEdit.text())
        self.model.setData(self.model.index(self.i, 8), self.ui.lineEdit_7.text())
        self.model.setData(self.model.index(self.i, 9), self.ui.lineEdit_10.text())
        self.model.submitAll()
        self.i += 1
        self.ui.lcdNumber.display(self.i)

    def delrow(self):
        if self.ui.tableView.currentIndex().row() > -1:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
            self.i -= 1
            self.model.select()
            self.ui.lcdNumber.display(self.i)
        else:
            QMessageBox.question(self,'Greška!', "Izaberite radnika!", QMessageBox.Ok)
            self.show()

    def updaterow(self):
        if self.ui.tableView.currentIndex().row() > 0:
            record = self.model.record(self.ui.tableView.currentIndex().row())
            record.setValue("Radnik_ID", self.ui.lineEdit_6.text())
            record.setValue("Ime",self.ui.lineEdit.text())
            record.setValue("Prezime",self.ui.lineEdit_2.text())
            record.setValue("OIB", self.ui.lineEdit_8.text())
            record.setValue("Adresa", self.ui.lineEdit_4.text())
            record.setValue("Grad", self.ui.lineEdit_5.text())
            record.setValue("Mobitel", self.ui.lineEdit_3.text())
            record.setValue("Datum Zaposlenja", self.ui.dateEdit.text())
            record.setValue("Sifra", self.ui.lineEdit_7.text())
            self.model.setRecord(self.ui.tableView.currentIndex().row(), record)
        else:
            QMessageBox.question(self,'Greška!', "Izaberite radnika!", QMessageBox.Ok)
            self.show()

    def reset(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")
        self.ui.lineEdit_5.setText("")
        self.ui.lineEdit_6.setText("")
        self.ui.lineEdit_7.setText("")
        self.ui.lineEdit_8.setText("")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = form()
    sys.exit(app.exec_())
