import datetime


def gender_from_pesel(pesel:str) -> str:
    return 'f' if int(pesel[9]) % 2 == 0 else 'm'



def data_ur_from_pesel(pesel:str) -> datetime.date:
    pass


def gender_from():
    return


def data_ur_from_pesel(pesel:str) -> datetime.date:
        rok = int(pesel[:2])
        mc = int(pesel[2:4])
        dzien =int(pesel[4:6])
        if mc > 12:
            mc-=20
            rok +=2000
        else: rok += 1900
        return datetime.date(rok, mc, dzien)