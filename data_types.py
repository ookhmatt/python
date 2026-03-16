from operator import truediv


def typy_danych():
    x = 'Dariusz'
    print(x, type(x))
    x = 12
    print(x, type(x))
    x = 12.3
    print(x, type(x))
    x = True
    print(x, type(x))
    x = None
    print(x, type(x))
    x = 12 + 34.5
    print(x.real, x.imag, type(x))
    import datetime
    x = datetime.date.today()
    print(x, type(x))

    #typy kolekcyjne
    x = ['Oleksii','Kacper', 'Wiktor','Oliwia', 'Michał' 'Wiktor']
    print(x, type(x))
    x =tuple(x)
    print(x, type(x))
    x = set(x)
    print(x, type(x))
    x = frozenset(x)
    print(x, type(x))

    #typ mapujący
    x={
    'imie':'Dariusz',
    'nazwiko':'Pieter',
    'certyfikaty': ['Python dev', 'C# dev']
    }
    print(x, type(x))

    #ćw - opisac typem słownikowym pojazd, cechy, itd
    # zapisać te dane do pliku pojazd.json
    pojazd = {
        'marka':'Audi',
        'model':'A4',
        'wersja':'B7',
        'paliwo':'ON',
        'moc':'150'
        }

    with open(r'files/pojazd.json', 'w' , encoding='utf-8') as f:
        print(pojazd, file=f)

    