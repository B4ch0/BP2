#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui
import sqlite3
import subprocess

from PyQt5.QtPrintSupport import QPrintDialog, QPrinter


import sys,os

conn = sqlite3.connect('vanreda.db')
c = conn.cursor()

class Ui_MainWindow(QtWidgets.QWidget):




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 880)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ikonaframe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 199);")

        def pregledRacuna():

            connection = sqlite3.connect("vanreda.db")
            query = "SELECT racun,artikal,radnik,vrijeme FROM racuni ORDER BY racun DESC"

            prikaz = connection.execute(query)


            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["RAČUN", "ARTIKAL", "KONOBAR", "VRIJEME"])
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(prikaz):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
            connection.close()






        def pregledKonobara():
            connection = sqlite3.connect("vanreda.db")
            query = "SELECT racun,artikal,radnik,vrijeme FROM racuni ORDER BY radnik ASC"
            prikaz = connection.execute(query)
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["RAČUN", "ARTIKAL", "KONOBAR", "VRIJEME"])
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(prikaz):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
            connection.close()

        def pregledDatum():
            connection = sqlite3.connect("vanreda.db")
            query = "SELECT racun,artikal,radnik,vrijeme FROM racuni ORDER BY vrijeme ASC"
            prikaz = connection.execute(query)
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["RAČUN", "ARTIKAL","KONOBAR", "VRIJEME"])
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(prikaz):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
            connection.close()

        def pretragaRacun():
            racuna = self.lineEditRacun.text()


            c.execute ("SELECT artikal,radnik,vrijeme FROM racuni WHERE racun = ?",(racuna))

            pa = c.fetchall()

            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels([ "ARTIKAL", "KONOBAR","VRIJEME"])
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(pa):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))


        def pretragaRadnika():
            radni = self.lineEditKonobar.text()

            c.execute ("SELECT racun,artikal,vrijeme FROM racuni WHERE radnik = ?",(radni))
            da = c.fetchall()
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["RAČUN", "ARTIKAL", "VRIJEME"])
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(da):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))


        def pretragaRazdoblje():
            od = self.dateEdit.text()

            do = self.dateEdit_2.text()

            c.execute("SELECT racun,artikal,radnik,vrijeme FROM racuni WHERE vrijeme  BETWEEN ? AND ?",(od,do))
            pa = c.fetchall()
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["RAČUN", "ARTIKAL", "KONOBAR", "VRIJEME"])
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(pa):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))



        def ponisti():
                while (self.tableWidget.rowCount() > 0):
                        self.tableWidget.removeRow(0)
                        self.tableWidget.setColumnCount(0)








        def handlePrint():
            printer = QPrinter(QPrinter.HighResolution)
            dialog = QPrintDialog(printer, self)
            if dialog.exec_() == QPrintDialog.Accepted:
                self.handlePaintRequest.print_(printer)
        def detalji():
            subprocess.call("python" + " rekapitulacija.py", shell=True)



        def close():
            sys.exit()


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 230, 561, 541))
        self.frame.setStyleSheet("background-color: rgb(136, 136, 136);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 541, 521))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.lineEditRacun = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRacun.setGeometry(QtCore.QRect(190, 40, 91, 20))
        self.lineEditRacun.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditRacun.setObjectName("lineEditRacun")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 121, 21))
        self.label.setStyleSheet("font: 14pt \"Franklin Gothic Medium\";")
        self.label.setObjectName("label")
        self.pushButtonRacun = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRacun.setGeometry(QtCore.QRect(320, 30, 115, 31))
        self.pushButtonRacun.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRacun.setIcon(icon1)
        self.pushButtonRacun.setObjectName("pushButtonRacun")
        self.pushButtonRacun.clicked.connect(pretragaRacun)

        self.pushButtonKonobar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonKonobar.setGeometry(QtCore.QRect(320, 80, 115, 31))
        self.pushButtonKonobar.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButtonKonobar.setIcon(icon1)
        self.pushButtonKonobar.setObjectName("pushButtonKonobar")
        self.pushButtonKonobar.clicked.connect(pretragaRadnika)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 151, 21))
        self.label_2.setStyleSheet("font: 14pt \"Franklin Gothic Medium\";")
        self.label_2.setObjectName("label_2")
        self.lineEditKonobar = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditKonobar.setGeometry(QtCore.QRect(190, 90, 91, 21))
        self.lineEditKonobar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditKonobar.setObjectName("lineEditKonobar")
        self.pushButtonDatum = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDatum.setGeometry(QtCore.QRect(720, 310, 281, 81))
        self.pushButtonDatum.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("rac.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDatum.setIcon(icon2)
        self.pushButtonDatum.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonDatum.setObjectName("pushButtonDatum")
        self.pushButtonDatum.clicked.connect(pregledDatum)
        self.pushButtonSkonobar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSkonobar.setGeometry(QtCore.QRect(720, 540, 281, 81))
        self.pushButtonSkonobar.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButtonSkonobar.setIcon(icon2)
        self.pushButtonSkonobar.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonSkonobar.setObjectName("pushButtonSkonobar")
        self.pushButtonSkonobar.clicked.connect(pregledKonobara)
        self.pushButtonSracun = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSracun.setGeometry(QtCore.QRect(720, 420, 281, 81))
        self.pushButtonSracun.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButtonSracun.setIcon(icon2)
        self.pushButtonSracun.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonSracun.setObjectName("pushButtonSracun")
        self.pushButtonSracun.clicked.connect(pregledRacuna)
        self.pushButtonPrintaj = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPrintaj.setGeometry(QtCore.QRect(330, 790, 140, 41))
        self.pushButtonPrintaj.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonPrintaj.setIcon(icon3)
        self.pushButtonPrintaj.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonPrintaj.setObjectName("pushButtonPrintaj")
        self.pushButtonPrintaj.clicked.connect(handlePrint)
        self.pushButtonIzlaz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonIzlaz.setGeometry(QtCore.QRect(780, 730, 150, 50))
        self.pushButtonIzlaz.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("slOdustani.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonIzlaz.setIcon(icon4)
        self.pushButtonIzlaz.setObjectName("pushButtonIzlaz")
        self.pushButtonIzlaz.clicked.connect(close)
        self.pushButtonRazdoblje = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRazdoblje.setGeometry(QtCore.QRect(390, 160, 115, 31))
        self.pushButtonRazdoblje.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButtonRazdoblje.setIcon(icon1)
        self.pushButtonRazdoblje.setObjectName("pushButtonRazdoblje")
        self.pushButtonRazdoblje.clicked.connect(pretragaRazdoblje)
        self.pushButtonOsvjezi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOsvjezi.setGeometry(QtCore.QRect(790, 650, 131, 41))
        self.pushButtonOsvjezi.setStyleSheet("QPushButton {\n"
                                             "    font: 14pt \"Franklin Gothic Medium\";\n"
                                             "    color: #333;\n"
                                             "    border: 2px solid #555;\n"
                                             "    border-radius: 20px;\n"
                                             "    border-style: outset;\n"
                                             "    background: qradialgradient(\n"
                                             "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                             "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                             "        );\n"
                                             "    padding: 5px;\n"
                                             "    }\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "    background: qradialgradient(\n"
                                             "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                             "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                             "        );\n"
                                             "    }\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    border-style: inset;\n"
                                             "    background: qradialgradient(\n"
                                             "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                             "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                             "        );\n"
                                             "    }")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("change.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOsvjezi.setIcon(icon31)
        self.pushButtonOsvjezi.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonOsvjezi.setObjectName("pushButtonOsvjezi")
        self.pushButtonOsvjezi.clicked.connect(ponisti)
        self.pushButtonDet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDet.setGeometry(QtCore.QRect(500, 40, 161, 51))
        self.pushButtonDet.setStyleSheet("QPushButton {\n"
                                              "    font: 11pt \"Franklin Gothic Medium\";\n"
                                              "    color: #333;\n"
                                              "    border: 2px solid #555;\n"
                                              "    border-radius: 20px;\n"
                                              "    border-style: outset;\n"
                                              "    background: qradialgradient(\n"
                                              "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                              "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                              "        );\n"
                                              "    padding: 5px;\n"
                                              "    }\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    background: qradialgradient(\n"
                                              "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                              "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                              "        );\n"
                                              "    }\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    border-style: inset;\n"
                                              "    background: qradialgradient(\n"
                                              "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                              "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                              "        );\n"
                                              "    }")
        self.pushButtonDet.setIcon(icon2)
        self.pushButtonDet.setIconSize(QtCore.QSize(25, 25))
        self.pushButtonDet.setObjectName("pushButtonDet")
        self.pushButtonDet.clicked.connect(detalji)
        self.pushButtonSkonobar.clicked.connect(pregledKonobara)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 90, 291, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(770, 30, 171, 41))
        self.label_7.setStyleSheet("font: 20pt \"Franklin Gothic Heavy\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 800, 71, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 800, 91, 21))
        self.label_4.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 31, 16))
        self.label_5.setStyleSheet("font: 14pt \"Franklin Gothic Medium\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 170, 31, 16))
        self.label_6.setStyleSheet("font: 14pt \"Franklin Gothic Medium\";")
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(60, 168, 110, 22))
        self.dateEdit.setDisplayFormat("yyyy.MM.dd")

        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 12pt \"MS Shell Dlg 2\";")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(250, 168, 110, 22))
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setDisplayFormat("yyyy.MM.dd")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "\"Van Reda\""))
        self.tableWidget.setSortingEnabled(True)
        self.label.setText(_translate("MainWindow", "BROJ RAČUNA"))
        self.pushButtonRacun.setText(_translate("MainWindow", "PRETRAŽI"))
        self.pushButtonKonobar.setText(_translate("MainWindow", "PRETRAŽI"))
        self.label_2.setText(_translate("MainWindow", "BROJ KONOBARA"))
        self.pushButtonDatum.setText(_translate("MainWindow", "SORTIRAJ PO DATUMU"))
        self.pushButtonSkonobar.setText(_translate("MainWindow", "SORTIRAJ PO KONOBARU"))
        self.pushButtonSracun.setText(_translate("MainWindow", "SORTIRAJ PO BROJU RAČUNA"))
        self.pushButtonPrintaj.setText(_translate("MainWindow", "PRINTAJ"))
        self.pushButtonOsvjezi.setText(_translate("MainWindow", "PONIŠTI"))
        self.pushButtonIzlaz.setText(_translate("MainWindow", "IZLAZ"))
        self.pushButtonDet.setText(_translate("MainWindow", "Rekapitulacija"))
        self.label_7.setText(_translate("MainWindow", "\"Van Reda\""))
        self.label_4.setText(_translate("MainWindow", "Broj računa"))
        self.label_5.setText(_translate("MainWindow", "OD"))
        self.label_6.setText(_translate("MainWindow", "DO"))
        self.pushButtonRazdoblje.setText(_translate("MainWindow", "PRETRAŽI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())








