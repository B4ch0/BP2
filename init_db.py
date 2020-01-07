import sqlite3


if __name__ == '__main__':

    conn = sqlite3.connect('vanreda.db')

    c = conn.cursor()


    c.execute("""CREATE TABLE artikli (
                artikal text NOT NULL,
                kolicina integer,
                cijena integer,
                sifra integer unique,
                artikal_id integer primary key autoincrement
                ) """)

    conn.commit()
