def demo_db():
    import sqlite3
    con = sqlite3.connect(r'db\dane_school.db')
    cur = con.cursor()

    while True:
        print('operacje na bazie danych')
        print('z - zakładanie bazy danych (kasuje istniejąca strukturę i dane)')
        print('c - tworzenie rekordów')
        print('r - odczyt rekordów')
        print('u - modyfikacja rekordów')
        print('d - usuwanie rekordów')
        print('k - koniec')
        odp = input('Co robimy? -> ')
        match odp.upper():
            case 'Z':
                cur.execute('drop table if exists student')
                cur.execute('drop table if exists class')
                sql = """
                create table class(
                    id integer primary key autoincrement,
                    name varchar(10) not null,
                    profile varchar(100) default ''
                )
                """
                cur.execute(sql)
                sql = """
                create table student(
                    id integer primary key autoincrement,
                    fname varchar(30) not null,
                    lname varchar(60) not null,
                    class_id integer,
                    foreign key(class_id) references class(id)
                )
                """
                cur.execute(sql)
                con.commit()
                print('założono nowe tabele')
            case 'C':
                lista_klas(cur)

                #dodawanie klas
                odp = input('Czy chcesz zdefiniowac nową klasę? (t-tak, n-nie) -> ')
                if odp.upper() == 'T':
                    name = input('Podaj symbol klasy, np 1A -> ')
                    profile = input('Podaj profil klasy, np. biologiczno-chemiczna -> ')
                    cur.execute('insert into class(name, profile) values(?,?)', (name.upper(), profile))
                    con.commit() # zapis danych do bazy danych
                odp = input('Czy chcesz dodac ucznia? (t-tak, n-nie) -> ')
                if odp.upper() == 'T':
                    lista_klas(cur)
                    klasa = input('Wybierz numer klasy do której chcesz dodać ucznia, np 1 dla 1A -> ')
                    imie = input('Podaj imię -> ')
                    nazwisko = input('Podaj nazwisko -> ')
                    cur.execute('insert into student(fname, lname, class_id) values(?,?,?)', (imie, nazwisko, klasa))
                    con.commit()
                    print('dodano ucznia do klasy')
            case 'R':
                lista_klas(cur)
                klasa = input('Wybierz numer klasy z której chcesz odczytać uczniów, np 1 dla 1A -> ')
                try:
                    cur.execute('select s.id, fname, lname from student as s join class as c on s.class_id = c.id where c.id = ?', (klasa,))
                    k = cur.fetchall()
                    if k:
                        print('lista uczniów:')
                        for u in k:
                            print(f'{u[0]} -> {u[1]} {u[2]}')
                    else: print('w tej klasie nie ma uczniów')
                except: print('nie ma takiej klasy')
            case 'U':
                lista_klas(cur)
                klasa = input('Wybierz numer klasy z której chcesz odczytać uczniów, np 1 dla 1A -> ')
                try:
                    cur.execute(
                        'select s.id, fname, lname from student as s join class as c on s.class_id = c.id where c.id = ?',
                        (klasa,))
                    k = cur.fetchall()
                    if k:
                        print('lista uczniów:')
                        for u in k: print(f'{u[0]} -> {u[1]} {u[2]}')
                        st = input('Podaj numer ucznia do przeniesienia -> ')
                        kl = input('Podaj numer klasy, do której ucznia przenosimy -> ')
                        cur.execute('update student set class_id = ? where id = ?', (kl, st))
                        con.commit()
                        print('dokonano przeniesienia')
                    else:
                        print('w tej klasie nie ma uczniów')
                except:
                    print('nie ma takiej klasy')
            case 'D':
                lista_klas(cur)
                klasa = input('Wybierz numer klasy z której chcesz odczytać uczniów, np 1 dla 1A -> ')
                try:
                    cur.execute(
                        'select s.id, fname, lname from student as s join class as c on s.class_id = c.id where c.id = ?',
                        (klasa,))
                    k = cur.fetchall()
                    if k:
                        print('lista uczniów:')
                        for u in k: print(f'{u[0]} -> {u[1]} {u[2]}')
                        st = input('Podaj numer ucznia do usunięcia -> ')
                        cur.execute('delete from student where id = ?', (st,))
                        con.commit()
                        komunikat = 'uczen został usunięty z klasy'
                        print('komunikat')

                        language ="PL"
                        do_czytania = gtts.gTT(text = komunikat, lang=language, slow= True)
                        path = r'files/do_czytania.mp3'
                        do_czytania.save(path)
                        #import os
                       # os.system(rf'start {path}')
                        from audioplayer import AudioPlayer
                        AudioPlayer(path).play(block=True)
                except: print('w tej klasie nie ma uczniów')
            case _:
                import sys
                print('do widzenia')
                sys.exit()


def lista_klas(cur):
    print('lista klas')
    cur.execute('select * from class')
    c = cur.fetchall()
    if c:
        for kl in c:
            print(f'{kl[0]} -> {kl[1]}, profil {kl[2]}')
    else:
        print('jeszcze nie założono żadnej klasy')