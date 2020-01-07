


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def close(self):
        sys.exit()
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 965)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 199);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(920, 520, 171, 331))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 253, 171);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 169, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap("../log/osvjezi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../log/noviunos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        icon3.addPixmap(QtGui.QPixmap("../log/unos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        icon4.addPixmap(QtGui.QPixmap("../log/brisanje.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_izlaz = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_izlaz.setStyleSheet("QPushButton {\n"
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
        icon5.addPixmap(QtGui.QPixmap("../log/slOdustani.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_izlaz.setIcon(icon5)
        self.pushButton_izlaz.setObjectName("pushButton_izlaz")
        self.pushButton_izlaz.clicked.connect(self.close)
        self.verticalLayout.addWidget(self.pushButton_izlaz)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 1121, 481))
        self.frame.setStyleSheet("background-color: rgb(136, 136, 136);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1101, 461))
        self.groupBox.setStyleSheet("background-color: rgb(255, 253, 171);")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 90, 91, 31))
        self.label.setStyleSheet("font: 18pt \"Franklin Gothic Medium\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 100, 231, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(440, 100, 91, 16))
        self.label_2.setStyleSheet("font: 18pt \"Franklin Gothic Medium\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(550, 100, 231, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(440, 220, 101, 21))
        self.label_3.setStyleSheet("font: 18pt \"Franklin Gothic Medium\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(550, 220, 181, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 290, 221, 31))
        self.label_4.setStyleSheet("font: 18pt \"Franklin Gothic Medium\";")
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(300, 290, 161, 31))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Franklin Gothic Medium\";")
        self.dateEdit.setObjectName("dateEdit")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 111, 21))
        self.label_5.setStyleSheet("font: 18pt \"Franklin Gothic Medium\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 160, 221, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(440, 160, 71, 21))
        self.label_6.setStyleSheet("font: 18pt \"Franklin Gothic Medium\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(520, 160, 121, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(40, 40, 71, 21))
        self.label_7.setStyleSheet("font: 18pt \"Franklin Gothic Medium\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 40, 71, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(440, 40, 61, 31))
        self.label_8.setStyleSheet("font: 18pt \"Franklin Gothic Medium\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(540, 45, 113, 20))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(40, 220, 51, 16))
        self.label_9.setStyleSheet("font: 18pt \"Franklin Gothic Medium\";")
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(110, 220, 161, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(610, 330, 77, 23))
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("font: 14pt \"Franklin Gothic Medium\";")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(760, 330, 81, 41))
        self.label_12.setObjectName("label_12")
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setGeometry(QtCore.QRect(909, 20, 171, 121))
        self.frame_2.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 20, 151, 81))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 61, 31))
        self.label_10.setObjectName("label_10")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 520, 891, 411))
        self.frame_3.setStyleSheet("background-color: rgb(136, 136, 136);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tableView = QtWidgets.QTableView(self.frame_3)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 871, 391))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(700, 330, 31, 20))
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_10.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.frame_3.raise_()
        self.frame.raise_()
        self.scrollArea.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "\"Van Reda\""))
        self.pushButton_4.setText(_translate("MainWindow", "OSVJEŽI"))
        self.pushButton.setText(_translate("MainWindow", "UNOS"))
        self.pushButton_2.setText(_translate("MainWindow", "IZMJENA"))
        self.pushButton_3.setText(_translate("MainWindow", "BRISANJE"))
        self.pushButton_izlaz.setText(_translate("MainWindow", "IZLAZ"))
        self.groupBox.setTitle(_translate("MainWindow", "RADNICI"))
        self.label.setText(_translate("MainWindow", "IME"))
        self.label_2.setText(_translate("MainWindow", "PREZIME"))
        self.label_3.setText(_translate("MainWindow", "MOBITEL"))
        self.label_4.setText(_translate("MainWindow", "DATUM ZAPOSLENJA"))
        self.label_5.setText(_translate("MainWindow", "ADRESA"))
        self.label_6.setText(_translate("MainWindow", "GRAD"))
        self.label_7.setText(_translate("MainWindow", "BROJ"))
        self.label_8.setText(_translate("MainWindow", "ŠIFRA"))
        self.label_9.setText(_translate("MainWindow", "OIB"))
        self.label_10.setText(_translate("MainWindow", "Broj radnika:"))
        self.label_11.setText(_translate("MainWindow", "Pozicija:"))
        self.label_12.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:10pt;\">1-Šef </span></p><p><span style=\" font-size:10pt;\">2-Konobar</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
