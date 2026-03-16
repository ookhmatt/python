def repeat():
    osoba ='Dariusz Pieter'
    print('Dariusz Pieter')
    print(id(osoba))
    teacher ='Dariusz Pieter'
    print(id(teacher))
    osoba ='Dariusz Pieter'
    osoba ='Dariusz Mc/Pieter'
    Piotr_Żyła ='Powiedział cyt:"hehehe"'
    """
    Babcia ma gdzieś w dokumentac
    zapisany pon do karty 1234,
    i trzeba go znalść
    """
    print('-*-'* 10)
    print('Witaj' + osoba)
    #print(12+ osoba) # błąd
    print(str(12)+ osoba) #błąd
    osoby = ['Oleksii','Kacper', 'Wiktor','Oliwia', 'Michał']
    [print(o) for o in osoby]
    for o in osoby:
        print(o)
    print(osoby)
    print(*osoby) #dekompozycja
    print(*osoby, sep=',')
    #plik
    with open (r'files/osoby.csv', 'a', encoding='utf-8') as f:
        [print(o, file=f) for o in osoby]
    print('Witaj' + osoba)
    print('Witaj{0} ma lat {1}'.format(osoba, 12))
    print('Witaj {osoba} ma lat {12}')

    #Zapytaj użytkowniak i imię,nazwisko,wage, wzrost i pesel.
    #Dane zapisać do pliku: dane_osobowe.csv
    def ex01():
        imie =input('Podaj imie ->')
        nazwisko =input('Podaj nazwisko->')
        waga =input('Podaj swoją wage->')
        wzrost =input('Podaj swój wzrost->')
        pesel =input('Podaj swój pesel')
        with open(r'files/dane_osobowe.csv', 'b', encoding='utf-8') as f:
            print( imie, nazwisko , waga, wzrost, pesel, sep=';' , file=f)


    ex01()
