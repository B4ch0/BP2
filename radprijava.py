#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import sqlite3


class Ui_MainWindow(object):







    def setupUi(self, MainWindow):

        def ok():
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()

            connection = sqlite3.connect("vanreda.db")
            result = connection.execute(
                "SELECT Radnik_ID,Sifra FROM radnici WHERE Radnik_ID = ? AND Sifra = ? AND Pozicija=1",
                (username, password))
            if (len(result.fetchall()) > 0):
                subprocess.call("python" + " unosRadnika.py", shell=True)
                sys.exit(0)

            else:
                print("Neispravan unos!")
            connection.close()
        def close():

            self.close()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(304, 246)
        MainWindow.setMinimumSize(QtCore.QSize(304, 246))
        MainWindow.setMaximumSize(QtCore.QSize(304, 246))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ikonaframe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 199);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 61, 16))
        self.label.setStyleSheet("font: 12pt \"Franklin Gothic Medium\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 61, 20))
        self.label_2.setStyleSheet("font: 12pt \"Franklin Gothic Medium\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 60, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 110, 113, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(113, 16777215))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 170, 111, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(ok)
        self.pushButton.clicked.connect(close)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "\"Van Reda\""))
        self.label.setText(_translate("MainWindow", "RADNIK"))
        self.label_2.setText(_translate("MainWindow", "ŠIFRA"))
        self.pushButton.setText(_translate("MainWindow", "Prijava"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
