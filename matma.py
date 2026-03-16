import math
def obwod_kola(promien:float) -> float:
    return 2 * math.pi * promien
def pole_kola(promien:float) -> float:
    return math.pi * math.pow(promien, 2)
def pole_prostokata(podstawa:float, wysokosc:float) -> float:
    return podstawa * wysokosc
def obwod_prostokata(podstawa:float, wysokosc:float) -> float:
    return 2 * podstawa + 2 * wysokosc
def pole_walca(promien:float, wysokosc:float) -> float:
    return 2 * pole_kola(promien) + pole_prostokata(obwod_kola(promien), wysokosc)
def obwod_walca(promien:float, wysokosc:float) -> float:
    return pole_kola(promien) * wysokosc
def rownanie_kwadratowe(a:float, b:float, c:float):
    """..."""
     delta = b ** 2 -4 * a * c
        if delta < 0: return None
        elif delta == 0: return -b/(2 * a)
        else:return(
                    (-b-math.sqrt(delta))/(2 * a),
                    (-b+math.sqrt(delta))/(2 * a))


def uklad_2_rownan_2_niewiadome(a:float, b:float, c: float, d:float, e:float, f:float):
    '''
    ax+by=c
    dx=ey=f
    w = a*e -b * d
    if w! =0
    wx = c * e - b * f
    wy = a * f - c * d
    x=wx/w
    y =wy/w
    :param a:
    :param b:
    :param c:
    :param d:
    :param e:
    :param f:
    :return:
    '''
    w =a * e - b * d
    if w !=0:
        wx =c * e - b *f
        wy =a * f - c * d
        x = wx /w
        y = wy /w
        return (x,y)
    else:
        return None







