def demo_bluzy():
    import sqlite3
    con = sqlite3.connect(r'db\bluzy.db')
    cur = con.cursor()

    while True:
        print('\nOPERACJE NA BAZIE BLUZ')
        print('z - zakładanie bazy danych')
        print('c - dodawanie bluz')
        print('r - przeglądanie bluz')
        print('u - modyfikacja (zmiana ceny)')
        print('d - usuwanie bluzy')
        print('k - koniec')

        odp = input('Co robimy? -> ')

        match odp.upper():
            case 'Z':
                cur.execute('drop table if exists bluza')
                cur.execute('drop table if exists marka')

                cur.execute("""
                create table marka(
                    id integer primary key autoincrement,
                    name varchar(50) not null
                )
                """)

                cur.execute("""
                create table bluza(
                    id integer primary key autoincrement,
                    model varchar(100) not null,
                    size varchar(5),
                    price real,
                    marka_id integer,
                    foreign key(marka_id) references marka(id)
                )
                """)

                con.commit()
                print('utworzono bazę bluz')

            case 'C':
                lista_marek(cur)

                odp = input('Czy chcesz dodać markę? (t/n) -> ')
                if odp.upper() == 'T':
                    name = input('Podaj nazwę marki -> ')
                    cur.execute('insert into marka(name) values(?)', (name,))
                    con.commit()

                odp = input('Czy chcesz dodać bluzę? (t/n) -> ')
                if odp.upper() == 'T':
                    lista_marek(cur)
                    marka = input('Wybierz numer marki -> ')
                    model = input('Podaj model bluzy -> ')
                    size = input('Podaj rozmiar (S/M/L/XL) -> ')
                    price = float(input('Podaj cenę -> '))

                    cur.execute(
                        'insert into bluza(model, size, price, marka_id) values(?,?,?,?)',
                        (model, size.upper(), price, marka)
                    )
                    con.commit()
                    print('dodano bluzę')

            case 'R':
                lista_marek(cur)
                marka = input('Podaj numer marki -> ')

                cur.execute("""
                select b.id, model, size, price 
                from bluza b join marka m on b.marka_id = m.id
                where m.id = ?
                """, (marka,))

                wynik = cur.fetchall()

                if wynik:
                    print('lista bluz:')
                    for b in wynik:
                        print(f'{b[0]} -> {b[1]}, rozmiar {b[2]}, {b[3]} zł')
                else:
                    print('brak bluz dla tej marki')

            case 'U':
                cur.execute('select * from bluza')
                for b in cur.fetchall():
                    print(b)

                id_bluzy = input('Podaj ID bluzy -> ')
                nowa_cena = float(input('Podaj nową cenę -> '))

                cur.execute('update bluza set price = ? where id = ?', (nowa_cena, id_bluzy))
                con.commit()

                print('zaktualizowano cenę')

            case 'D':
                cur.execute('select * from bluza')
                for b in cur.fetchall():
                    print(b)

                id_bluzy = input('Podaj ID bluzy do usunięcia -> ')
                cur.execute('delete from bluza where id = ?', (id_bluzy,))
                con.commit()

                print('usunięto bluzę')

                # opcjonalny dźwięk
                try:
                    import gtts
                    from audioplayer import AudioPlayer

                    komunikat = "Bluza została usunięta"
                    tts = gtts.gTTS(text=komunikat, lang='pl')
                    path = 'usunieto.mp3'
                    tts.save(path)
                    AudioPlayer(path).play(block=True)
                except:
                    print('(brak modułów audio)')

            case _:
                import sys
                print('do widzenia')
                sys.exit()


def lista_marek(cur):
    print('\nLISTA MAREK:')
    cur.execute('select * from marka')
    dane = cur.fetchall()

    if dane:
        for m in dane:
            print(f'{m[0]} -> {m[1]}')
    else:
        print('brak marek')