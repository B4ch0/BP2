#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton,QMainWindow,
                             QHBoxLayout, QApplication,QAction,QFileDialog)
import sys
import subprocess



class Ui_prijava(object):


    def setupUi(self,prijava):

        def prijavaok():
            username = self.unosRadlogin.text()
            password = self.unosRadlogin1.text()

            connection = sqlite3.connect("vanreda.db")
            result = connection.execute("SELECT Radnik_ID,Sifra FROM radnici WHERE Radnik_ID = ? AND Sifra = ?", (username, password))
            if (len(result.fetchall()) > 0):
                subprocess.call("python" + " glizbornik.py", shell=True)
                sys.exit(0)

            else:
                print("Neispravan unos!")
            connection.close()



        def close():
            print("POZDRAV")
            self.close()

        prijava.setObjectName("prijava")
        prijava.resize(562, 562)
        prijava.setMinimumSize(QtCore.QSize(562, 562))
        prijava.setMaximumSize(QtCore.QSize(562, 562))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        prijava.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ikonaframe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prijava.setWindowIcon(icon)
        prijava.setStyleSheet("background-color: rgb(255, 255, 207);\n"
"\n"
"\n"
"font: 10pt \"Franklin Gothic Medium\";")



        prijava.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btnprijava = QtWidgets.QPushButton(prijava)
        self.btnprijava.setGeometry(QtCore.QRect(80, 190, 151, 71))
        self.btnprijava.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnprijava.setMouseTracking(True)
        self.btnprijava.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnprijava.setStyleSheet("QPushButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap("slPrijava.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnprijava.setIcon(icon1)
        self.btnprijava.setIconSize(QtCore.QSize(40, 40))
        self.btnprijava.setObjectName("btnprijava")
        self.btnprijava.clicked.connect(prijavaok)

        self.btnodustani = QtWidgets.QPushButton(prijava)
        self.btnodustani.setGeometry(QtCore.QRect(310, 190, 151, 71))
        self.btnodustani.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.btnodustani.setMouseTracking(True)
        self.btnodustani.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btnodustani.setAutoFillBackground(False)
        self.btnodustani.setStyleSheet("QPushButton {\n"
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
        icon2.addPixmap(QtGui.QPixmap("slOdustani.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnodustani.setIcon(icon2)
        self.btnodustani.setIconSize(QtCore.QSize(40, 40))
        self.btnodustani.setShortcut("")
        self.btnodustani.setObjectName("btnodustani")
        self.btnodustani.clicked.connect(close)
        self.unosRadlogin = QtWidgets.QLineEdit(prijava)
        self.unosRadlogin.setGeometry(QtCore.QRect(270, 70, 201, 37))
        self.unosRadlogin.setAutoFillBackground(False)
        self.unosRadlogin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);")
        self.unosRadlogin.setObjectName("unosRadlogin1")
        self.unosRadlogin1 = QtWidgets.QLineEdit(prijava)
        self.unosRadlogin1.setGeometry(QtCore.QRect(270, 130, 201, 37))
        self.unosRadlogin1.setAutoFillBackground(False)
        self.unosRadlogin1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 14pt \"MS Shell Dlg 2\";\n"
                                        "border-color: rgb(0, 0, 0);")
        self.unosRadlogin1.setObjectName("unosRadlogin1")
        self.unosRadlogin1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(prijava)
        self.label.setGeometry(QtCore.QRect(140, 60, 101, 71))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(prijava)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 71, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("radniksl.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(prijava)
        self.label_3.setGeometry(QtCore.QRect(150, 120, 91, 51))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(prijava)
        self.calendarWidget.setGeometry(QtCore.QRect(120, 330, 312, 183))
        self.calendarWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"Franklin Gothic Medium\";")
        self.calendarWidget.setObjectName("calendarWidget")
        self.unosRadlogin.raise_()
        self.unosRadlogin1.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.btnprijava.raise_()
        self.btnodustani.raise_()
        self.calendarWidget.raise_()

        self.retranslateUi(prijava)
        QtCore.QMetaObject.connectSlotsByName(prijava)

    def retranslateUi(self, prijava):
        _translate = QtCore.QCoreApplication.translate
        prijava.setWindowTitle(_translate("prijava", "PRIJAVA"))
        prijava.setToolTip(_translate("prijava", "<html><head/><body><p><img src=\":/ikonaframe/ikonaframe.png\"/></p></body></html>"))
        prijava.setWhatsThis(_translate("prijava", "<html><head/><body><p><img src=\":/ikonaframe/ikonaframe.png\"/></p></body></html>"))
        self.btnprijava.setText(_translate("prijava", "PRIJAVA"))
        self.btnodustani.setText(_translate("prijava", "ODUSTANI"))
        self.label.setText(_translate("prijava", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">RADNIK</span></p></body></html>"))
        self.label_3.setText(_translate("prijava",
                                      "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ŠIFRA</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)


    prijava = QtWidgets.QFrame()
    ui = Ui_prijava()
    ui.setupUi(prijava)
    prijava.show()
    sys.exit(app.exec_())
