#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
import sqlite3

conn = sqlite3.connect('vanreda.db')
c = conn.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 525)
        MainWindow.setMinimumSize(QtCore.QSize(825, 525))
        MainWindow.setMaximumSize(QtCore.QSize(825, 525))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ikonaframe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 199);")

        def rekapArtikla():
            connection = sqlite3.connect("vanreda.db")
            query = "SELECT artikal,count(*) as cnt FROM racuni GROUP BY artikal ORDER BY count(*) DESC"

            rekartikla = connection.execute(query)
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels([ "ARTIKAL","KOLIČINA"])
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(rekartikla):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
            connection.close()



        def potrosnja():
            connection = sqlite3.connect("vanreda.db")
            query = "select sum(cijena) from artikli inner join racuni on artikli.artikal=racuni.artikal;"

            pot = connection.execute(query)
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setHorizontalHeaderLabels(["UKUPAN PROMET"])
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(pot):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data) + " kn"))
            connection.close()

        def potrosnjaPeriod():
            od = self.dateEdit_3.text()
            do = self.dateEdit_4.text()

            c.execute("select sum(cijena) from artikli inner join racuni on artikli.artikal=racuni.artikal WHERE vrijeme BETWEEN ? AND ?;",(od,do))

            pa = c.fetchall()
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setHorizontalHeaderLabels(["PROMET ZA PERIOD"])
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(pa):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data) + " kn"))

        def rekapKon():
            radnik = self.lineEdit_2.text()

            c.execute("SELECT artikal,count(*) as cnt FROM racuni WHERE radnik=? GROUP BY artikal ORDER BY count(*) DESC",(radnik))
            rez = c.fetchall()

            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels([ "ARTIKAL","KOLIČINA"])
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(rez):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

        def pareKonobari():
            rad = self.lineEdit.text()

            c.execute( "select sum(cijena) from artikli inner join racuni on artikli.artikal=racuni.artikal WHERE radnik=?",(rad))
            tot = c.fetchall()

            self.tableWidget.setColumnCount(1)
            self.tableWidget.setHorizontalHeaderLabels(["UKUPAN PROMET"])
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(tot):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data) + " kn"))

        def pareKonobariRaz():
            rad = self.lineEdit.text()
            od = self.dateEdit.text()
            do = self.dateEdit_2.text()

            c.execute(
                "select sum(cijena) from artikli inner join racuni on artikli.artikal=racuni.artikal WHERE radnik=? AND vrijeme BETWEEN ? AND ?",(rad,od,do))
            tota = c.fetchall()

            self.tableWidget.setColumnCount(1)
            self.tableWidget.setHorizontalHeaderLabels(["UKUPAN PROMET"])
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(tota):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data) + " kn"))







        def ponisti():
                while (self.tableWidget.rowCount() > 0):
                        self.tableWidget.removeRow(0)
                        self.tableWidget.setColumnCount(0)
                self.lineEdit_2.setText("")
                self.lineEdit.setText("")

        def close():
            sys.exit()


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(530, 30, 261, 381))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 281, 20))
        self.label.setStyleSheet("font: 14pt \"Franklin Gothic Medium\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 40, 81, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(rekapArtikla)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 290, 231, 16))
        self.label_2.setStyleSheet("font: 14pt \"Franklin Gothic Medium\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 240, 81, 31))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(rekapKon)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 440, 101, 41))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("slOdustani.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(close)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 290, 31, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 290, 81, 31))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
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
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(pareKonobari)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(60, 360, 110, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(210, 360, 110, 22))
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_2.setDate(QtCore.QDate(2020, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 360, 21, 20))
        self.label_3.setStyleSheet("font: 11pt \"Franklin Gothic Medium\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 360, 21, 16))
        self.label_4.setStyleSheet("font: 11pt \"Franklin Gothic Medium\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 350, 81, 31))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
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
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(pareKonobariRaz)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 281, 16))
        self.label_5.setStyleSheet("font: 14pt \"Franklin Gothic Medium\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 240, 31, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 100, 181, 16))
        self.label_6.setStyleSheet("font: 14pt \"Franklin Gothic Medium\";")
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 90, 81, 31))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
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
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(potrosnja)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_3.setGeometry(QtCore.QRect(50, 160, 110, 22))
        self.dateEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_3.setDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_4.setGeometry(QtCore.QRect(210, 160, 110, 22))
        self.dateEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_4.setDate(QtCore.QDate(2020, 1, 1))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 160, 81, 31))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
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
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(potrosnjaPeriod)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 21, 16))
        self.label_7.setStyleSheet("font: 12pt \"Franklin Gothic Medium\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 160, 21, 16))
        self.label_8.setStyleSheet("font: 11pt \"Franklin Gothic Medium\";")
        self.label_8.setObjectName("label_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(520, 20, 281, 401))
        self.frame.setStyleSheet("background-color: rgb(136, 136, 136);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(590, 440, 121, 41))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("change.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(ponisti)
        self.frame.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.lineEdit.raise_()
        self.pushButton_4.raise_()
        self.dateEdit.raise_()
        self.dateEdit_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_5.raise_()
        self.label_5.raise_()
        self.lineEdit_2.raise_()
        self.label_6.raise_()
        self.pushButton_6.raise_()
        self.dateEdit_3.raise_()
        self.dateEdit_4.raise_()
        self.pushButton_7.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "\"Van Reda\""))
        self.tableWidget.setSortingEnabled(True)
        self.label.setText(_translate("MainWindow", "Rekapitulacija artikla po potrošnji"))
        self.pushButton.setText(_translate("MainWindow", "Izlistaj"))
        self.label_2.setText(_translate("MainWindow", "Ukupan promet po konobaru"))
        self.pushButton_2.setText(_translate("MainWindow", "Izlistaj"))
        self.pushButton_3.setText(_translate("MainWindow", "IZLAZ"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "ID.."))
        self.pushButton_4.setText(_translate("MainWindow", "Izlistaj"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy.MM.dd"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "yyyy.MM.dd"))
        self.label_3.setText(_translate("MainWindow", "OD"))
        self.label_4.setText(_translate("MainWindow", "DO"))
        self.pushButton_5.setText(_translate("MainWindow", "Izlistaj"))
        self.label_5.setText(_translate("MainWindow", "Rekapitulacija artikla po konobaru"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "ID..."))
        self.label_6.setText(_translate("MainWindow", "Ukupan promet-TOTAL"))
        self.pushButton_6.setText(_translate("MainWindow", "Izlistaj"))
        self.dateEdit_3.setDisplayFormat(_translate("MainWindow", "yyyy.MM.dd"))
        self.dateEdit_4.setDisplayFormat(_translate("MainWindow", "yyyy.MM.dd"))
        self.pushButton_7.setText(_translate("MainWindow", "Izlistaj"))
        self.label_7.setText(_translate("MainWindow", "OD"))
        self.label_8.setText(_translate("MainWindow", "DO"))
        self.pushButton_8.setText(_translate("MainWindow", "PONIŠTI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
