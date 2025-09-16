# funkcja definiujaca dzisiejszy dzien
import datetime

def czas():
    x = datetime.datetime.now()
    print(x)


# funkcja obliczajaca ilosc dni od dziś do wybranej daty

miesiace=['01','02','03','04','05','06','07','08','09','10','11','12']
dniwmiesiacu=[31,28,30,31,30,31,30,31,30,31,30,31]


miesiace = dniwmiesiacu

def obliczanieDni():
    x = datetime.datetime.now()
    dzisiejszyDzien = int(x.strftime('%d'))
    dzisiejszyMiesiac = int(x.strftime('%m'))
    pobranyMiesiac = int(input('do ktorego miesiaca chcesz obliczac losc dni: '))
    pobranyDzien = int(input('do którego dnia chcesz obliczać ilość dni: '))
    liczbaDni = 0

    if pobranyMiesiac > dzisiejszyMiesiac:
        pobranyMiesiac = pobranyMiesiac - dzisiejszyMiesiac

    if pobranyDzien > dzisiejszyDzien:
        pobranyDzien = pobranyDzien - dzisiejszyDzien


    for y in range(dzisiejszyMiesiac-1,pobranyMiesiac):
        liczbaDni = liczbaDni + miesiace[y]

    liczbaDni = liczbaDni + pobranyDzien - dzisiejszyDzien

    print(liczbaDni)

# ilość godzin pomiędzy czasem a i b

def godziny():
    x = datetime.datetime.now()
    dD = int(x.strftime('%d'))
    pD = int(input('podaj dowolny dzień w tym miesiącu: '))
    dR = pD - dD
    print('od',dD,'do',pD,'mineło',(dR*24),'h')

czas()
obliczanieDni()
godziny()