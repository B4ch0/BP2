#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


import subprocess



class GL_MainWindow(object):

    def openRacuni(self):

        subprocess.call("python" + " unosRacunafinal1.py", shell=True)

    def openArtikli(self):

        subprocess.call("python" + " artikli.py", shell=True)

    def openRadnici(self):

        subprocess.call("python" + " radprijava.py", shell=True)

    def openPregled(self):

        subprocess.call("python" + " pregled.py", shell=True)
    def close(self):
        sys.exit()



    def setupUi1(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1169, 1007)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ikonaframe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 199);")
        MainWindow.setDocumentMode(False)



        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(490, 1000))
        self.groupBox.setStyleSheet("background-color: rgb(255, 253, 171);\n"
"")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.btnUnosRacuna = QtWidgets.QPushButton(self.groupBox)
        self.btnUnosRacuna.setGeometry(QtCore.QRect(20, 260, 450, 120))
        self.btnUnosRacuna.setMaximumSize(QtCore.QSize(450, 120))
        self.btnUnosRacuna.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnUnosRacuna.setAutoFillBackground(False)
        self.btnUnosRacuna.setStyleSheet("QPushButton {\n"
"    font: 24pt \"Franklin Gothic Medium\";\n"
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
        icon1.addPixmap(QtGui.QPixmap("rac.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUnosRacuna.setIcon(icon1)
        self.btnUnosRacuna.setIconSize(QtCore.QSize(55, 55))
        self.btnUnosRacuna.setObjectName("btnUnosRacuna")
        self.btnUnosRacuna.clicked.connect(self.openRacuni)
        self.btnPregledRacuna = QtWidgets.QPushButton(self.groupBox)
        self.btnPregledRacuna.setGeometry(QtCore.QRect(20, 390, 450, 120))
        self.btnPregledRacuna.setMaximumSize(QtCore.QSize(450, 120))
        self.btnPregledRacuna.setStyleSheet("QPushButton {\n"
"    font: 24pt \"Franklin Gothic Medium\";\n"
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
        icon2.addPixmap(QtGui.QPixmap("pracuna.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPregledRacuna.setIcon(icon2)
        self.btnPregledRacuna.setIconSize(QtCore.QSize(55, 50))
        self.btnPregledRacuna.setObjectName("btnPregledRacuna")
        self.btnPregledRacuna.clicked.connect(self.openPregled)
        self.btnArtikli = QtWidgets.QPushButton(self.groupBox)
        self.btnArtikli.setGeometry(QtCore.QRect(20, 520, 450, 120))
        self.btnArtikli.setMaximumSize(QtCore.QSize(450, 120))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnArtikli.setFont(font)
        self.btnArtikli.setWhatsThis("")
        self.btnArtikli.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnArtikli.setAutoFillBackground(False)
        self.btnArtikli.setStyleSheet("QPushButton {\n"
"    font: 24pt \"Franklin Gothic Medium\";\n"
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
        icon3.addPixmap(QtGui.QPixmap("artikli1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnArtikli.setIcon(icon3)
        self.btnArtikli.setIconSize(QtCore.QSize(55, 50))
        self.btnArtikli.setCheckable(False)
        self.btnArtikli.setObjectName("btnArtikli")
        self.btnArtikli.clicked.connect(self.openArtikli)
        self.btnRadnici = QtWidgets.QPushButton(self.groupBox)
        self.btnRadnici.setGeometry(QtCore.QRect(20, 650, 450, 120))
        self.btnRadnici.setMaximumSize(QtCore.QSize(450, 120))
        self.btnRadnici.setStyleSheet("QPushButton {\n"
"    font: 24pt \"Franklin Gothic Medium\";\n"
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
        icon4.addPixmap(QtGui.QPixmap("radnici.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRadnici.setIcon(icon4)
        self.btnRadnici.setIconSize(QtCore.QSize(70, 60))
        self.btnRadnici.setObjectName("btnRadnici")
        self.btnRadnici.clicked.connect(self.openRadnici)

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 401, 61))
        self.label.setStyleSheet("\n"
"font: 20pt \"Franklin Gothic Medium\";")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.btnIzlaz = QtWidgets.QPushButton(self.groupBox)
        self.btnIzlaz.setGeometry(QtCore.QRect(160, 810, 161, 35))
        self.btnIzlaz.setMaximumSize(QtCore.QSize(161, 35))
        self.btnIzlaz.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnIzlaz.setStyleSheet("QPushButton {\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("slOdustani.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIzlaz.setIcon(icon5)
        self.btnIzlaz.setObjectName("btnIzlaz")
        self.btnIzlaz.clicked.connect(self.close)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 321, 121))
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1169, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", '"Van Reda"'))
        self.groupBox.setTitle(_translate("MainWindow", "Glavni Izbornik"))
        self.btnUnosRacuna.setText(_translate("MainWindow", "UNOS RAČUNA"))
        self.btnPregledRacuna.setText(_translate("MainWindow", "PREGLED RAČUNA"))
        self.btnArtikli.setText(_translate("MainWindow", "ARTIKLI"))
        self.btnRadnici.setText(_translate("MainWindow", "RADNICI"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Buffet \"Van Reda\""))
        self.btnIzlaz.setText(_translate("MainWindow", "Izlaz"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GL_MainWindow()
    ui.setupUi1(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
