from demos.built_in_functions import fukcje_wbudowane
from demos.data_types import typy_danych
from demos.repeat import repeat

while True:
    print('Menu:')
    print('1-> powtórka')
    print('2-> typy danych')
    print('3 -> funkcje wbudowane ')
    print('k -> funkcje własne')
    odp = input('co robimy szefie')
    if odp == '1':
        repeat()
    elif odp == '2':
        typy_danych()
    elif odp == '3':
        fukcje_wbudowane()
    else:
        import sys #import całej biblioteki
        from sys import exit #import wybranych narzedzi z biblioteki
        print('Dziękuje, do zobaczenia')
            #sys.exit()
        exit()


# match odp:
 #   case '1':
  #      pass


