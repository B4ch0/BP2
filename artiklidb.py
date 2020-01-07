
import sqlite3

conn = sqlite3.connect('vanreda.db')

c = conn.cursor()

def insert_prod(name,q,cost,code,kat,date):
    with conn:
        c.execute("SELECT kolicina FROM artikli WHERE artikal = :name",{'name':name})
        check = c.fetchone()

    print(check)
    if check is None:
        with conn:
            print('da')
            c.execute("INSERT INTO artikli (artikal,kolicina,cijena,sifra,kategorija) VALUES (:artikal, :kolicina, :cijena, :sifra, :kategorija)", {'artikal': name, 'kolicina': q, 'cijena': cost, 'sifra': code,'kategorija' : kat})
            a = name.upper() +' ' +str(q)+' '+str(cost)+' '+str(date) + ' ' + 'INSERT '+"\n"
            with open("logovi.txt", "a") as myfile:
                myfile.write(a)
        return 'Artikal ubačen'
    else:
        return 'Artikal već postoji sa istim imenom'

def show_art():
    with conn:
        c.execute("SELECT * FROM artikli")

    return c.fetchall()


def update_cost(name, cost, date):
    with conn:
        c.execute("""UPDATE artikli SET cijena = :cijena
                    WHERE artikal = :artikal""",
                  {'artikal': name, 'cijena': cost})

def update_code(name, code):
    with conn:
        c.execute("""UPDATE artikli SET sifra = :sifra
                    WHERE artikal = :artikal""",
                  {'artikal': name, 'sifra': code})


def update_quantity(name, val,date):
    with conn:
        c.execute("SELECT kolicina FROM artikli WHERE artikal = :artikal",{'artikal': name})
        z = c.fetchone()
        cost = z[0]+val
        if cost < 0:
            return
        c.execute("""UPDATE artikli SET kolicina = :kolicina
                    WHERE artikal = :artikal""",
                  {'artikal': name, 'kolicina': cost})
        a = name.upper() + ' ' + str(z[0]) + ' ' + str(cost) + ' ' + str(date) +' UPDATE '+"\n"
        with open("logovi.txt", "a") as myfile:
            myfile.write(a)


def remove_art(name,code,date):
    with conn:
        c.execute("DELETE from artikli WHERE artikal = :artikal OR sifra = :sifra" ,
                  {'artikal': name, 'sifra': code})
        a = name.upper() or code +' ' + 'None' + ' ' + 'None'+' ' + str(date) + ' REMOVE '+"\n"

        with open("logovi.txt", "a") as myfile:
            myfile.write(a)

        conn.commit()

