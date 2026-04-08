from lib.matma import rownanie_kwadratowe
from lib.person import data_ur_from_pesel


def fukcje_wbudowane():
    osoby = ['Oleksii', 'Kacper', 'Wiktor', 'Oliwia', 'Michał']
    print('zaproszeni na imprezę:')
    for i, o in enumerate(osoby, start=1):
        print(f"{i} -> {o}")

    nazwiska = ['Okhmat' , 'Karpała' , 'Grabarz' , 'Zatorska' , ' Komenda']
    for i, (imie, nazwisko) in enumerate(zip(osoby, nazwiska), start=1):
        print(f"{1} -> {imie} {nazwisko}")

    liczba = 0.5
    print(format(liczba, "%"))
    liczba = 123
    print(format(liczba, "x")) #heksadycemalnym
    print(format(liczba, "o")) #actagonalny(osiemkowy)

    #optylizacja działania kodu
    #demo_compile
    method_name()


def method_name(lamba=None):
    n = 123.5
    kod_eval = "67 * 34 * 100 * n"
    kod_exec = '''
v =123 * 345
v += 234.7
v += n
    '''
    import time
    start = time.time()
    for i in range(1000000):
        eval(kod_eval)
        exec(kod_exec)

    print(f"czas wykonania bez kompilacji {time.time() - start}")

    start = time.time()
    kod_comp_eval = compile(kod_eval, 'komentarz', 'eval')
    kod_comp_exec = compile(kod_exec, 'komentarz', 'exec')
    for i in range(1000000):
        eval(kod_comp_eval)
        exec(kod_comp_exec)
    print(f"czas wykonania z kompilacją {time.time() - start}")

    liczby = [123, 54, -123, 45 ,65 , 78 , 32]
    from lib.validators import isEven
    liczby_parz =filter(isEven , liczby)
    print(*liczby_parz)
    liczby_nieparz = filter(lambda x: x % 2 == 1, liczby)
    print(*liczby_nieparz)

    #ćw zaprojetuj funcję podwajająca liczby i użyjcie z funkcją map

    from lib.validators import podwojenie
    liczby_podwojone =map(podwojenie, liczby)
    print(*liczby_podwojone)

    #spróbować napisać lamba dla liczb potrojonych

    triple = lambda x: x * 3
    print(triple(3))
    print(triple(10))
    print(triple(2.5))
    numbers = [1, 2, 3, 4, 5]
    liczby_potrojone = list(map(lambda x: x * 3, numbers))
    print(*liczby_potrojone)

    #czelendż (zadanie)
    temperatury_stopnie_celcjusza = [2,4,7,12,15,17,16,14,11,9,5]
    temperatury_fahrenheit = ''
    # *F =(C *9/5) =32

    from lib.validators import celcjusz_to_fahrenheit
    temperatury_fahrenheit =map(celcjusz_to_fahrenheit, temperatury_stopnie_celcjusza)
    print(*temperatury_fahrenheit)

    pesele=["60060867926","87070148937","06292682997","08301055578","97051318433","10280976447","78020744938","01282586776","54060236633","73012159158"]

     #dla pesel : xx płec to :xxx

    from lib.person import  gender_from_pesel
    gendery = map(gender_from_pesel, pesele)

    for i, (p,g) in enumerate(zip(pesele, gendery), start =1):
        print(f"{1}-> dla pesela {p} płeć {'żeńska' if g == 'f' else 'męska'}")



    rok, mięsiąc, dzień = 2008, 3 ,7
    import datetime
    data_ur = datetime.date(rok, mięsiąc, dzień)
    print(data_ur)

    #dla peseli obliczyć daty urodzenia i je podać jak w przykładzie dla gender
    from lib.person import data_ur_from_pesel
    daty_ur = map(data_ur_from_pesel, pesele)
    for i, (p,d) in enumerate(zip(pesele, daty_ur), start=1):
        print(f"{1} -> data urodzin dla pesel {p} to {d}")



    #przetestować funkcje w lib matma dla wybranych przez siebie wartości
    promien = [12.4,43.6,31,33]
    podstawa =[11,22.3,41.2]
    wysokosci =[21,32.2,51.2]

    #test równanie kwadratowe
    a,b,c = 1,1,1 #wynik None
    print(rownanie_kwadratowe(a,b,c))
    a,b,c = 1,2,1 #wynik -1
    print(rownanie_kwadratowe(a,b,c))
    a,b,c =1,3,1 #wynik tupla 2-ch liczb
    print(rownanie_kwadratowe(a,b,c))


