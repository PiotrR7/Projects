import random


karty = ['As','1','2','3','4','5','6','7','8','9','10','walet','dama','król']
typKarty = ['pik','kier','trefl','karo']


class Gracz1():
    kartyGracza = {}
    porownywaneKarty = []
    iloscKart = len(kartyGracza)

class Gracz2():
    kartyGracza = {}
    porownywaneKarty = []
    iloscKart = len(kartyGracza)

class Game():
    runda = 0



# funkcja losowania kart
def losowanieKart(nazwa_gracza,ilosc_kart):
    while nazwa_gracza.iloscKart <= ilosc_kart:

        losowaKarta = random.randrange(0,13)
        losowyTypKarty = random.randrange(0,4)

        nazwa_gracza.kartyGracza[losowaKarta] = losowyTypKarty
        
        nazwa_gracza.iloscKart += 1
    


# funkcja porównywania kart



losowanieKart(Gracz1,10)
losowanieKart(Gracz2,10)

print('gracz 1',Gracz1.kartyGracza)
print('gracz 2',Gracz2.kartyGracza)

print('gracz 1',Gracz1.kartyGracza.keys())
print('gracz 2',Gracz2.kartyGracza.keys())

print('karty po przemianie' % Gracz1.porownywaneKarty)
