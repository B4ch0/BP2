import sqlite3
from typing import Any
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
import xlsxwriter

conn = sqlite3.connect('vanreda.db')
c = conn.cursor()




def pice1():

    with conn:
        c.execute("select artikal from artikli where sifra=1")
        a = c.fetchall()
    return a




def pice2():

    with conn:
        c.execute("select artikal from artikli where sifra=2")
        a = c.fetchall()
    return a

def pice3():

    with conn:
        c.execute("select artikal from artikli where sifra=3")
        a = c.fetchall()
    return a


def pice4():

    with conn:
        c.execute("select artikal from artikli where sifra=4")
        a = c.fetchall()
    return a

def pice5():

    with conn:
        c.execute("select artikal from artikli where sifra=5")
        a = c.fetchall()
    return a

def pice6():

    with conn:
        c.execute("select artikal from artikli where sifra=6")
        a = c.fetchall()
    return a

def pice7():

    with conn:
        c.execute("select artikal from artikli where sifra=7")
        a = c.fetchall()
    return a

def pice8():

    with conn:
        c.execute("select artikal from artikli where sifra=8")
        a = c.fetchall()
    return a

def pice9():

    with conn:
        c.execute("select artikal from artikli where sifra=9")
        a = c.fetchall()
    return a

def pice10():

    with conn:
        c.execute("select artikal from artikli where sifra=10")
        a = c.fetchall()
    return a

def pice11():

    with conn:
        c.execute("select artikal from artikli where sifra=11")
        a = c.fetchall()
    return a

def pice12():

    with conn:
        c.execute("select artikal from artikli where sifra=12")
        a = c.fetchall()
    return a

def pice13():

    with conn:
        c.execute("select artikal from artikli where sifra=13")
        a = c.fetchall()
    return a

def pice14():

    with conn:
        c.execute("select artikal from artikli where sifra=14")
        a = c.fetchall()
    return a

def pice15():

    with conn:
        c.execute("select artikal from artikli where sifra=15")
        a = c.fetchall()
    return a

def pice16():

    with conn:
        c.execute("select artikal from artikli where sifra=16")
        a = c.fetchall()
    return a
"""
def id():
    with conn:
        c.execute ("SELECT MAX(racun_id) FROM fiskal")
        rac = c.fetchall()
    return rac

daj = str(id())[3:-4]"""




p1  = str(pice1())[3:-4]
p2  = str(pice2())[3:-4]
p3  = str(pice3())[3:-4]
p4  = str(pice4())[3:-4]
p5  = str(pice5())[3:-4]
p6  = str(pice6())[3:-4]
p7  = str(pice7())[3:-4]
p8  = str(pice8())[3:-4]
p9  = str(pice9())[3:-4]
p10  = str(pice10())[3:-4]
p11  = str(pice11())[3:-4]
p12  = str(pice12())[3:-4]
p13  = str(pice13())[3:-4]
p14  = str(pice14())[3:-4]
p15  = str(pice15())[3:-4]
p16  = str(pice16())[3:-4]


def meso1():

    with conn:
        c.execute("select artikal from artikli where sifra=17")
        a = c.fetchall()
    return a


def meso2():

    with conn:
        c.execute("select artikal from artikli where sifra=18")
        a = c.fetchall()
    return a

def meso3():

    with conn:
        c.execute("select artikal from artikli where sifra=19")
        a = c.fetchall()
    return a


def meso4():

    with conn:
        c.execute("select artikal from artikli where sifra=20")
        a = c.fetchall()
    return a

def meso5():

    with conn:
        c.execute("select artikal from artikli where sifra=21")
        a = c.fetchall()
    return a

def meso6():

    with conn:
        c.execute("select artikal from artikli where sifra=22")
        a = c.fetchall()
    return a

def meso7():

    with conn:
        c.execute("select artikal from artikli where sifra=23")
        a = c.fetchall()
    return a

def meso8():

    with conn:
        c.execute("select artikal from artikli where sifra=24")
        a = c.fetchall()
    return a

def meso9():

    with conn:
        c.execute("select artikal from artikli where sifra=25")
        a = c.fetchall()
    return a

def meso10():

    with conn:
        c.execute("select artikal from artikli where sifra=26")
        a = c.fetchall()
    return a

def meso11():

    with conn:
        c.execute("select artikal from artikli where sifra=27")
        a = c.fetchall()
    return a

def meso12():

    with conn:
        c.execute("select artikal from artikli where sifra=28")
        a = c.fetchall()
    return a

def meso13():

    with conn:
        c.execute("select artikal from artikli where sifra=29")
        a = c.fetchall()
    return a

def meso14():

    with conn:
        c.execute("select artikal from artikli where sifra=30")
        a = c.fetchall()
    return a

def meso15():

    with conn:
        c.execute("select artikal from artikli where sifra=31")
        a = c.fetchall()
    return a

def meso16():

    with conn:
        c.execute("select artikal from artikli where sifra=32")
        a = c.fetchall()
    return a

m1  = str(meso1())[3:-4]
m2  = str(meso2())[3:-4]
m3  = str(meso3())[3:-4]
m4  = str(meso4())[3:-4]
m5  = str(meso5())[3:-4]
m6  = str(meso6())[3:-4]
m7  = str(meso7())[3:-4]
m8  = str(meso8())[3:-4]
m9  = str(meso9())[3:-4]
m10  = str(meso10())[3:-4]
m11  = str(meso11())[3:-4]
m12  = str(meso12())[3:-4]
m13  = str(meso13())[3:-4]
m14  = str(meso14())[3:-4]
m15  = str(meso15())[3:-4]
m16  = str(meso16())[3:-4]

def pizza1():

    with conn:
        c.execute("select artikal from artikli where sifra=33")
        a = c.fetchall()
    return a


def pizza2():

    with conn:
        c.execute("select artikal from artikli where sifra=34")
        a = c.fetchall()
    return a

def pizza3():

    with conn:
        c.execute("select artikal from artikli where sifra=35")
        a = c.fetchall()
    return a


def pizza4():

    with conn:
        c.execute("select artikal from artikli where sifra=36")
        a = c.fetchall()
    return a

def pizza5():

    with conn:
        c.execute("select artikal from artikli where sifra=37")
        a = c.fetchall()
    return a

def pizza6():

    with conn:
        c.execute("select artikal from artikli where sifra=38")
        a = c.fetchall()
    return a

def pizza7():

    with conn:
        c.execute("select artikal from artikli where sifra=39")
        a = c.fetchall()
    return a

def pizza8():

    with conn:
        c.execute("select artikal from artikli where sifra=40")
        a = c.fetchall()
    return a

def pizza9():

    with conn:
        c.execute("select artikal from artikli where sifra=41")
        a = c.fetchall()
    return a

def pizza10():

    with conn:
        c.execute("select artikal from artikli where sifra=42")
        a = c.fetchall()
    return a

def pizza11():

    with conn:
        c.execute("select artikal from artikli where sifra=43")
        a = c.fetchall()
    return a

def pizza12():

    with conn:
        c.execute("select artikal from artikli where sifra=44")
        a = c.fetchall()
    return a

def pizza13():

    with conn:
        c.execute("select artikal from artikli where sifra=45")
        a = c.fetchall()
    return a

def pizza14():

    with conn:
        c.execute("select artikal from artikli where sifra=46")
        a = c.fetchall()
    return a

def pizza15():

    with conn:
        c.execute("select artikal from artikli where sifra=47")
        a = c.fetchall()
    return a

def pizza16():

    with conn:
        c.execute("select artikal from artikli where sifra=48")
        a = c.fetchall()
    return a
pi1  = str(pizza1())[3:-4]
pi2  = str(pizza2())[3:-4]
pi3  = str(pizza3())[3:-4]
pi4  = str(pizza4())[3:-4]
pi5  = str(pizza5())[3:-4]
pi6  = str(pizza6())[3:-4]
pi7  = str(pizza7())[3:-4]
pi8  = str(pizza8())[3:-4]
pi9  = str(pizza9())[3:-4]
pi10  = str(pizza10())[3:-4]
pi11  = str(pizza11())[3:-4]
pi12  = str(pizza12())[3:-4]
pi13  = str(pizza13())[3:-4]
pi14  = str(pizza14())[3:-4]
pi15  = str(pizza15())[3:-4]
pi16  = str(pizza16())[3:-4]



