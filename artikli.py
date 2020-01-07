
from artui import *
import os
import datetime
import artiklidb as ad
import init_db

from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import (QWidget, QPushButton,QMainWindow,
                             QHBoxLayout, QApplication,QAction,QFileDialog)

import sqlite3



try:
    conn = sqlite3.connect('vanreda.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE artikli (
                artikal text NOT NULL,
                kolicina integer,
                cijena integer,
                sifra integer unique,
                kategorija integer,
                artikal_id integer primary key autoincrement,
                kategorija integer
                ) """)
    conn.commit()
except Exception:
    print('DB postoji')


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textName.setPlaceholderText("Radnik...")
        self.textName.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textPass.setPlaceholderText("Šifra...")
        self.textPass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buttonLogin = QtWidgets.QPushButton('Prijava', self)

        self.buttonLogin.setStyleSheet("QPushButton {\n"
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
        self.buttonLogin.clicked.connect(self.artLogin)

        layout = QtWidgets.QVBoxLayout(self)
        self.setStyleSheet("background-color: rgb(255, 255, 199);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../log/ikonaframe.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)

        self.setWindowIcon(icon)


        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        self.setWindowTitle('"Van Reda"')

    def artLogin(self):
        username = self.textName.text()
        password = self.textPass.text()

        connection = sqlite3.connect("vanreda.db")
        result = connection.execute("SELECT * FROM radnici WHERE Radnik_ID = ? AND Sifra = ? AND Pozicija =1", (username, password))
        if (len(result.fetchall()) > 0):

            self.accept()
        else: QtWidgets.QMessageBox.warning(
                self, 'Greška', 'Neispravni podaci')

class Glavni(QMainWindow):


    def __init__(self):
        super().__init__()
        self.artui = Ui_MainWindow()
        self.artui.setupUi(self)
        self.setWindowTitle('Artikli "Van Reda"')

        self.initUI()

    def initUI(self):
        self.st = stackedGlavni()
        exitAct = QAction(QIcon('slOdustani.png'), 'IZLAZ', self)
        exitAct.setStatusTip('IZLAZ')
        exitAct.triggered.connect(self.close)


        self.statusBar()

        toolbar = self.addToolBar('Izlaz')
        toolbar.addAction(exitAct)

        self.setCentralWidget(self.st)

        self.show()

class stackedGlavni(QWidget):
    def __init__(self):

        super(stackedGlavni, self).__init__()
        self.leftlist = QListWidget()
        self.leftlist.setStyleSheet("background-color: rgb(255, 255, 255); border: 2px solid #555; border-radius: 2px;")


        self.leftlist.setFixedWidth(200)
        self.leftlist.setFixedHeight(300)

        self.leftlist.insertItem(0, 'DODAJ ARTIKAL')
        self.leftlist.insertItem(1, 'IZMJENA ARTIKLA')
        self.leftlist.insertItem(2, 'PREGLED ARTIKLA')
        self.leftlist.insertItem(3, 'EVIDENCIJA UPISA U BAZU')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()

        self.dodajUI()
        self.stack2UI()
        self.stack3UI()
        self.stack4UI()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        self.Stack.addWidget(self.stack4)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300,350, 200, 200)

        self.show()


    def dodajUI(self):
        layout = QFormLayout()


        self.ok = QPushButton('DODAJ', self)
        cancel = QPushButton('PONIŠTI', self)

        self.art_name = QLineEdit()

        layout.addRow("NAZIV ARTIKLA", self.art_name)

        self.art_count = QLineEdit()
        layout.addRow("KOLIČINA", self.art_count)

        self.art_cost = QLineEdit()
        layout.addRow("CIJENA", self.art_cost)

        self.art_code =QLineEdit()
        layout.addRow("ŠIFRA", self.art_code)
        self.artKat = QLineEdit()
        layout.addRow("KATEGORIJA", self.artKat)


        #self.artInfo.setText("Proba")
        #self.artInfo.setGeometry(420,420,47,13)


        layout.addWidget(self.ok)
        layout.addWidget(cancel)

       # self.artInfo.setGeometry(420,420,47,13)
        self.art_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_name.setFixedWidth(300)
        self.art_count.setFixedWidth(200)
        self.art_cost.setFixedWidth(200)
        self.art_code.setFixedWidth(200)
        self.artKat.setFixedWidth(50)
        self.art_cost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_name.setContentsMargins(0,0,0,10)
        self.art_count.setContentsMargins(0, 0, 0, 10)
        self.art_cost.setContentsMargins(0, 0, 0, 10)
        self.art_code.setContentsMargins(0, 0, 0, 10)
        self.artKat.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_count.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_code.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ok.setFixedWidth(200)
        self.ok.setStyleSheet("QPushButton {\n"
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
                              "    }; "
                              "")
        self.ok.setIcon(QtGui.QIcon('slPrijava.png'))
        cancel.setStyleSheet("QPushButton {\n"
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

        cancel.setFixedWidth(200)
        cancel.setIcon(QtGui.QIcon('slOdustani.png'))

        self.ok.clicked.connect(self.on_click)
        cancel.clicked.connect(self.art_name.clear)
        cancel.clicked.connect(self.art_cost.clear)
        cancel.clicked.connect(self.art_count.clear)
        cancel.clicked.connect(self.art_code.clear)
        cancel.clicked.connect(self.artKat.clear)
        self.stack1.setLayout(layout)
        self.artInfo = QLabel()
        layout.addRow("KATEGORIJA: 1- Piće 2- Meso 3- Pizza",self.artInfo)
        self.artSifra = QLabel()
        layout.addRow("ŠIFRE: 1-16= Piće 17-32=Meso 33-48=Pizza",self.artSifra)

#dodaj
    def on_click(self):
        now = datetime.datetime.now()
        art_name_inp = self.art_name.text().replace(' ','_').lower()
        art_count_inp = int(self.art_count.text())
        art_cost_inp = int(self.art_cost.text())
        art_code_inp = int(self.art_code.text())
        art_kat_inp = int(self.artKat.text())

        art_add_date_time = now.strftime("%Y-%m-%d %H:%M")
        d = ad.insert_prod(art_name_inp,art_count_inp,art_cost_inp,art_code_inp,art_kat_inp,art_add_date_time)
        print(d)




    def stack2UI(self):

        layout = QHBoxLayout()

        tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        tabs.addTab(self.tab1, 'DODAJ KOLIČINU')
        tabs.addTab(self.tab2, 'SMANJI KOLIČINU')
        tabs.addTab(self.tab4, 'IZMIJENI CIJENU')
        tabs.addTab(self.tab5, 'IZMIJENI ŠIFRU')
        tabs.addTab(self.tab3, 'IZBRIŠI ARTIKAL')
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()

        layout.addWidget(tabs)
        self.stack2.setLayout(layout)

    def tab1UI(self):
        layout = QFormLayout()
        self.ok_add = QPushButton('DODAJ', self)
        cancel = QPushButton('PONIŠTI', self)

        self.art_name_add = QLineEdit()
        layout.addRow("ARTIKAL", self.art_name_add)

        self.art_count_add = QLineEdit()
        layout.addRow("KOLIČINA ZA DODAT", self.art_count_add)

        layout.addWidget(self.ok_add)
        layout.addWidget(cancel)
        self.tab1.setLayout(layout)
        self.art_name_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_count_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_name_add.setFixedWidth(350)
        self.art_count_add.setFixedWidth(200)


        self.ok_add.clicked.connect(self.call_add)
        cancel.clicked.connect(self.art_name_add.clear)
        cancel.clicked.connect(self.art_count_add.clear)
        self.ok_add.setStyleSheet("QPushButton {\n"
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
                              "    }; "
                              "")
        self.ok_add.setFixedWidth(230)
        self.ok_add.setIcon(QtGui.QIcon('noviunos.png'))
        cancel.setFixedWidth(230)
        cancel.setIcon(QtGui.QIcon('slOdustani.png'))

        cancel.setStyleSheet("QPushButton {\n"
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

    def tab2UI(self):
        layout = QFormLayout()
        self.ok_red = QPushButton('ODUZMI', self)
        cancel = QPushButton('PONIŠTI', self)

        self.art_name_red = QLineEdit()
        layout.addRow("ARTIKAL", self.art_name_red)

        self.art_count_red = QLineEdit()
        layout.addRow("KOLIČINA ZA SMANJIT", self.art_count_red)


        layout.addWidget(self.ok_red)
        layout.addWidget(cancel)
        self.tab2.setLayout(layout)
        self.art_name_red.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_count_red.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_name_red.setFixedWidth(350)
        self.art_count_red.setFixedWidth(200)


        self.ok_red.clicked.connect(self.call_red)
        cancel.clicked.connect(self.art_name_red.clear)
        cancel.clicked.connect(self.art_count_red.clear)
        self.ok_red.setStyleSheet("QPushButton {\n"
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
                                  "    }; "
                                  "")
        self.ok_red.setFixedWidth(230)
        self.ok_red.setIcon(QtGui.QIcon('minus.png'))
        cancel.setFixedWidth(230)
        cancel.setIcon(QtGui.QIcon('slOdustani.png'))
        cancel.setStyleSheet("QPushButton {\n"
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

    def tab3UI(self):
        layout = QFormLayout()
        self.ok_del = QPushButton('IZBRIŠI', self)
        cancel = QPushButton('PONIŠTI', self)

        self.art_name_del = QLineEdit()
        layout.addRow("ARTIKAL", self.art_name_del)
        self.art_code_del = QLineEdit()
        layout.addRow("ili ŠIFRA", self.art_code_del)
        layout.addWidget(self.ok_del)
        layout.addWidget(cancel)
        self.tab3.setLayout(layout)
        self.art_name_del.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_code_del.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_name_del.setFixedWidth(350)
        self.art_code_del.setFixedWidth(200)

        self.ok_del.clicked.connect(self.call_del)
        cancel.clicked.connect(self.art_name_del.clear)
        cancel.clicked.connect(self.art_code_del.clear)

        self.ok_del.setStyleSheet("QPushButton {\n"
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
                                  "    }; "
                                  "")
        self.ok_del.setFixedWidth(230)
        self.ok_del.setIcon(QtGui.QIcon('brisanje.png'))
        cancel.setFixedWidth(230)
        cancel.setIcon(QtGui.QIcon('slOdustani.png'))
        cancel.setStyleSheet("QPushButton {\n"
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

    def tab4UI(self):
        layout = QFormLayout()
        self.btn_izmj = QPushButton('IZMJENI', self)
        cancel = QPushButton('PONIŠTI', self)

        self.art_name_izmj = QLineEdit()
        layout.addRow("ARTIKAL", self.art_name_izmj)

        self.art_count_izmj = QLineEdit()
        layout.addRow("NOVA CIJENA", self.art_count_izmj)

        layout.addWidget(self.btn_izmj)
        layout.addWidget(cancel)
        self.tab4.setLayout(layout)
        self.art_name_izmj.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_count_izmj.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_name_izmj.setFixedWidth(350)
        self.art_count_izmj.setFixedWidth(200)

        self.btn_izmj.clicked.connect(self.call_izmj)
        cancel.clicked.connect(self.art_name_izmj.clear)
        cancel.clicked.connect(self.art_count_izmj.clear)

        self.btn_izmj.setStyleSheet("QPushButton {\n"
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
                                  "    }; "
                                  "")
        self.btn_izmj.setFixedWidth(230)
        self.btn_izmj.setIcon(QtGui.QIcon('change.png'))
        cancel.setFixedWidth(230)
        cancel.setIcon(QtGui.QIcon('slOdustani.png'))
        cancel.setStyleSheet("QPushButton {\n"
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

    def tab5UI(self):
        layout = QFormLayout()
        self.btn_izmj_code = QPushButton('IZMJENI', self)
        cancel = QPushButton('PONIŠTI', self)

        self.art_code_name = QLineEdit()
        layout.addRow("ARTIKAL", self.art_code_name)

        self.art_code_izmj = QLineEdit()
        layout.addRow("NOVA ŠIFRA", self.art_code_izmj)

        layout.addWidget(self.btn_izmj_code)
        layout.addWidget(cancel)
        self.tab5.setLayout(layout)
        self.art_code_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_code_izmj.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.art_code_name.setFixedWidth(350)
        self.art_code_izmj.setFixedWidth(200)

        self.btn_izmj_code.clicked.connect(self.call_izmj_code)
        cancel.clicked.connect(self.art_code_name.clear)
        cancel.clicked.connect(self.art_code_izmj.clear)

        self.btn_izmj_code.setStyleSheet("QPushButton {\n"
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
                                  "    }; "
                                  "")
        self.btn_izmj_code.setFixedWidth(230)
        self.btn_izmj_code.setIcon(QtGui.QIcon('change.png'))
        cancel.setFixedWidth(230)
        cancel.setIcon(QtGui.QIcon('slOdustani.png'))
        cancel.setStyleSheet("QPushButton {\n"
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


#IZBRISI
    def call_del(self):
        now = datetime.datetime.now()
        art_del_date_time = now.strftime("%Y-%m-%d %H:%M")
        art_name = self.art_name_del.text().replace(' ','_').lower()
        art_code = self.art_code_del.text().replace(' ', '_').lower()
        ad.remove_art(art_name,art_code,art_del_date_time)
#kolicina
    def call_red(self):
        now = datetime.datetime.now()
        art_red_date_time = now.strftime("%Y-%m-%d %H:%M")
        art_name = self.art_name_red.text().replace(' ','_').lower()
        try:
            art_val = -(int(self.art_count_red.text()))
            print(art_val)
            print(type(art_val))
            ad.update_quantity(art_name, art_val, art_red_date_time)
        except Exception:
            print('Krivi podatak!')
#izmj. cijene
    def call_izmj(self):
        now = datetime.datetime.now()
        art_red_date_time = now.strftime("%Y-%m-%d %H:%M")
        art_name = self.art_name_izmj.text().replace(' ', '_').lower()
        try:
           art_cost = (int(self.art_count_izmj.text()))
           print(art_cost)
           print(type(art_cost))
           ad.update_cost(art_name, art_cost, art_red_date_time)
        except Exception:
           print('Krivi podatak!')

    def call_izmj_code(self):


        art_name = self.art_code_name.text().replace(' ', '_').lower()
        try:
            art_code = (int(self.art_code_izmj.text()))
            print(art_code)
            print(type(art_code))
            ad.update_code(art_name, art_code)
        except Exception:
            print('Krivi podatak!')



#DODAJ
    def call_add(self):
        now = datetime.datetime.now()
        art_call_add_date_time = now.strftime("%Y-%m-%d %H:%M")
        art_name = self.art_name_add.text().replace(' ','_').lower()
        art_val = int(self.art_count_add.text())
        ad.update_quantity(art_name, art_val, art_call_add_date_time)



    def stack3UI(self):

        table = ad.show_art()
        print('prikaz')
        print(table)
        layout = QVBoxLayout(self)




        self.srb = QPushButton()
        self.srb1 = QPushButton()
        self.srb.setText("PRETRAŽI")

        self.srb1.setText("DOHVATI ARTIKLE")
        self.View = QTableWidget()
        self.lbl3 = QLabel()
        self.lbl_conf_text = QLabel()
        self.lbl_conf_text.setText("PRETRAŽI:")
        self.lbl_conf_text.setContentsMargins(20,10,0,0)


        self.conf_text = QLineEdit()
        self.conf_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.conf_text.setPlaceholderText("Unesi naziv artikla ili početno slovo...")
        self.conf_text.setFixedWidth(320)
        self.conf_text.setContentsMargins(0,10,0,10)

        self.View.setColumnCount(4)
        self.View.setColumnWidth(0, 250)
        self.View.setColumnWidth(1, 200)
        self.View.setColumnWidth(2, 200)
        self.View.setColumnWidth(3, 200)
        self.View.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.View.horizontalScrollBar().setStyleSheet("background-color: rbg(136, 136 , 136);")
        self.View.verticalScrollBar().setStyleSheet("background-color: rbg(136, 136 , 136);")
        self.View.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.View.setHorizontalHeaderLabels(["ARTIKAL", "KOLIČINA", "CIJENA", "ŠIFRA"])
        self.View.setSortingEnabled(True)

        self.View.insertRow(0)


        layout.addWidget(self.View)
        layout.addWidget(self.lbl_conf_text)
        layout.addWidget(self.conf_text)
        layout.addWidget(self.srb)
        layout.addWidget(self.srb1)
        layout.addWidget(self.lbl3)
        self.srb.clicked.connect(self.show_search)
        self.srb1.clicked.connect(self.show_search)
        self.stack3.setLayout(layout)

        self.srb.setStyleSheet("QPushButton {\n"
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
                                  "    }; "
                                  "")
        self.srb.setFixedWidth(230)
        self.srb.setIcon(QtGui.QIcon('search.png'))

        self.srb1.setStyleSheet("QPushButton {\n"
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
                                  "    }; "
                                  "")
        self.srb1.setFixedWidth(230)
        self.srb1.setIcon(QtGui.QIcon('grab.png'))


    def stack4UI(self):
            layout = QVBoxLayout()
            self.srt = QPushButton()
            self.srt.setText("DOHVATI LOGOVE")
            self.Trans = QTableWidget()
            self.lbl4 = QLabel()
            self.trans_text = QLineEdit()
            self.trans_text.setDisabled(True)

            self.Trans.setColumnCount(6)
            self.Trans.setColumnWidth(0, 150)
            self.Trans.setColumnWidth(1, 150)
            self.Trans.setColumnWidth(2, 150)
            self.Trans.setColumnWidth(3, 100)
            self.Trans.setColumnWidth(4, 100)
            self.Trans.setColumnWidth(5, 500)
            self.Trans.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.Trans.horizontalScrollBar().setStyleSheet("background-color: rbg(136, 136 , 136);")
            self.Trans.verticalScrollBar().setStyleSheet("background-color: rbg(136, 136 , 136);")
            self.Trans.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.Trans.setSortingEnabled(True)
            self.Trans.setHorizontalHeaderLabels(["LOG ID", "ARTIKAL ili ŠIFRA", "NAREDBA", "DATUM","VRIJEME","DETALJI"])

            self.Trans.insertRow(0)

            self.Trans.setRowHeight(0, 50)

            layout.addWidget(self.Trans)
            layout.addWidget(self.trans_text)
            layout.addWidget(self.srt)
            layout.addWidget(self.lbl4)
            self.srt.clicked.connect(self.show_trans_history)
            self.stack4.setLayout(layout)

            self.srt.setStyleSheet("QPushButton {\n"
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
                            "    }; "
                            "")
            self.srt.setFixedWidth(230)

            self.srt.setIcon(QtGui.QIcon('grab.png'))

#PRETRAGA
    def show_search(self):
        if self.View.rowCount()>1:
            for i in range(1,self.View.rowCount()):
                self.View.removeRow(1)


        x_act = ad.show_art()
        x = []
        if self.conf_text.text() != '':
            for i in range(0,len(x_act)):
                a = list(x_act[i])
                if self.conf_text.text().lower() in a[0].lower():
                    x.append(a)
        else:
            x = ad.show_art()

        if len(x)!=0:
            for i in range(1,len(x)+1):
                self.View.insertRow(i)
                a = list(x[i-1])
                self.View.setItem(i, 0, QTableWidgetItem(a[0].replace('_',' ').upper()))
                self.View.setItem(i, 1, QTableWidgetItem(str(a[1])))
                self.View.setItem(i, 2, QTableWidgetItem(str(a[2])))
                self.View.setItem(i, 3, QTableWidgetItem(str(a[3])))
                self.View.setRowHeight(i, 50)
            self.lbl3.setText('Trenutno stanje artikla.')
        else:
            self.lbl3.setText('Nema podatka u bazi.')


#upis logova
    def show_trans_history(self):
        if self.Trans.rowCount()>1:
            for i in range(1,self.Trans.rowCount()):
                self.Trans.removeRow(1)

        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'logovi.txt')
        if os.path.exists(path):
            tsearch = open(path, 'r')
            x_c = tsearch.readlines()
            tsearch.close()
            x = []
            if self.trans_text.text() != '':
                key = self.trans_text.text()
                for i in range(0,len(x_c)):
                    a = x_c[i].split(" ")
                    name = a[0]
                    action = a[-2]
                    if (key.lower() in name.lower()) or (key.lower() in action.lower()) :
                        x.append(a)
            else:
                x = x_c.copy()

            for i in range(0,len(x)):
                x.sort(key=lambda a: a[4])
            print(x)
            tid = 1
            for i in range(1,len(x)+1):
                self.Trans.insertRow(i)

                a = x[i-1].split(" ")
                if a[-2] == 'UPDATE':
                    p = 'Izmjenjena početna količina :'+a[1]+' nova količina: '+a[2]
                elif a[-2] == 'INSERT':
                    p = 'Artikal dodan sa količinom : '+a[1]+' i cijenom : '+a[2]
                elif a[-2] == 'REMOVE':
                    p = 'Izbrisan artikal'
                else:
                    p = 'Ništa'


                self.Trans.setItem(i, 0, QTableWidgetItem(str(tid)))
                self.Trans.setItem(i, 1, QTableWidgetItem(a[0].replace('_',' ')))
                self.Trans.setItem(i, 2, QTableWidgetItem(a[-2]))
                self.Trans.setItem(i, 3, QTableWidgetItem(a[3]))
                self.Trans.setItem(i, 4, QTableWidgetItem(a[4]))
                self.Trans.setItem(i, 5, QTableWidgetItem(p))
                self.Trans.setRowHeight(i, 50)
                tid += 1


            self.lbl4.setText('Logovi izmjena.')
        else:
            self.lbl4.setText('Nije pronađen podatak.')



    def display(self, i):
        self.Stack.setCurrentIndex(i)




if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Glavni()
        sys.exit(app.exec_())
