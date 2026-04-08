import locale

from lib.kalkulatory import kalkulator_walut


def demo_collections():
    osoby = ['Oleksii', 'Kacper', 'Wiktor', 'Oliwia', 'Michał']
    print(*osoby, sep=',')
    osoby.append('Natalia')
    print(*osoby, sep=",")
    ptencjalne_kandydatki('Magda' , "Zuzanna")
    osoby.extend( ptenjalne_kandydatki )
    print(*osoby, sep=',')
    osoby.inset(  2,  'Patrycja' )
    print(*osoby , sep=',')

    #sortowanie
    osoby.append('tomek')
    print(*osoby, sep=',')
    osoby.sort()
    print(*osoby, sep=',')
    import locale
    locale.setlocale(locale.LC_ALL, 'pl-PL')
    osoby.sort(key=locale.strxfm) #sortowanien z uwzględnieniem ustawień lokalnych
    print(*osoby, sep=',')

    #usuwanie z listy
    #osoby.remove('Marcin') #błąd
    if 'Marcin' in osoby: osoby.remove('Marcin') #bezpieczne usuwanie


    #usuniecie elisty
    #del osoby
    #print(*osoby, sep=',') #bład bo nie ma listy

    osoba = osoby[6]
    print(osoba)

    osoba_mnoga =osoby[1:5]
    print(*osoba_mnoga, sep=",")

    osoba_mnoga = osoby[:7]
    print(*osoba_mnoga, sep=",")

    osoba_mnoga = osoby[7:]
    print(*osoba_mnoga, sep=",")

    print(len(osoby))

    #ćw napisać apkę która pyta o imię osoby, i dopóki ktoś nie wybierz, wpisze N(nie), to pyta o kolejne imię
    #imiona są składane na liście
    #po zakończeniu skłąsania, imiona są wypisywane z numeram na początku

    #apka_lista_osob()
    def apka_lista_osob():
        while True:
            odp = input('Czy chcesz podac osobę? t-tak, n-nie ->')
            if odp.upper() == 'T':
                imie = input('podaj imię ->')
                lista_osob.append(imie)
            else:
                [print(f'{i} -> {o}') for i, o in enumerate(lista_osoby, start=1)]
                break #przerwanie pętli


    #użytkownik podaje kwoty dopóki nie wybierze N, wtedy wyświetli się suma

        def apka_lista_kwot():
            lista_kwoty = []
            while True:
                odp = input('Czy chcesz podac kwotę? t-tak, n-nie ->')
                if odp.upper() == 'T':
                    kwota = input('podaj kwotę ->')
                    kwota = kwota.replace("," , ",")
                    lista_kwota.append(float(kwota))
                else:
                    print(f'suma wynsoi: {sum(lista_kwoty)}')
                    break  # przerwanie pętli


def demo_tuple():
    osoby = ['Oleksii', 'Kacper', 'Wiktor', 'Oliwia', 'Michał']
    print(type(osoby))


    print(osoby.index('Wiktor'))
    print(osoby.count('Wiktor'))
    (pierwsza, druga, *pozostali) = osoby
    print(pierwsza)
    print(druga)
    print(pozostali)


def apka_set_osoby():
    pass


def demo_sets():
    osoby = ['Oleksii', 'Kacper', 'Wiktor', 'Oliwia', 'Michał']
    print(*osoby, sep=",")
    osoby.add('Marcelina')
    osoby.add('Grażyna')
    osoby.add('Andrzej')
    print(*osoby, sep=",")
    inne_osoby = set(['Kacper' , 'Anna' , 'Oliwia', "Adrianna"])

    print(osoby.intersection(inne_osoby)) #częsć wspólna
    print(osoby.difference(inne_osoby)) # cześć różna od drugiego zbioru
    print(inne_osoby.difference(osoby))
    all = osoby.union(inne_osoby)
    print(*all , sep=',')

    osoby.remove('Wiktor')
    print(*osoby,sep=',')
    osoby.add('Wiktor')
    inni = {'Kacper' , 'Wiktor'}
    print(osoby.issuperset(inni))
    print(inni.issubset(osoby))


    zimne_osoby=frozenset(osoby)
    #zimne_osoby. #brak metod pozwalających na zmiany, tylko operacje weryfikacji

    #ćw. zieramy imiona od użytkownika do zbioru,
    #gdy użytkownik wybierze n, wyświetlamy posortowaną liste osób

    apka_set_osoby()

    def apka_set_osoby():
        while True:
            odp = input('Czy chcesz podac osobę? t-tak, n-nie ->')
            if odp.upper() == 'T':
                imie = input('podaj imię ->')
                lista_osob.append(imie)
            else:
                locale.setlocale(locale.LC_ALL, 'pl-PL')
                osoby.sort(key=locale.strxfm)  # sortowanien z uwzględnieniem ustawień lokalnych
                [print(f'{i} -> {o}') for i, o in enumerate(set_osoby, start=1)]
                break  # przerwanie pętli


def demo_collections():
    #demo_lista()
    #demo_tuple()
    #demo_sets()
    kalkulator_walut()


def demo_dict():
    bluza={
        "cena": 100,
        "kolor":"czarny",
        "rozmiar":"L",
        "zapiecie":"zamek",
        "kaptur":True
    }

    #ćw opisać  samodzielnie swój własny objekt notacją json
    print(bluza)

    import pprint

    pprint.pprint(bluza)

    [print(f'{k} -> {v}') for k, v in bluze.items()]





    def demo_dicte():
        gry= {
            "cena": 50,
            "rodzaj": "ekszyn",
            "rozmiar gry": "25Gb",
            "waluta w grze": "gold",
            "Ekipirowaie": True
        }
