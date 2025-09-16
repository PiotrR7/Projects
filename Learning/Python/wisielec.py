# program umozliwiajacy gre w wisielca


# tworzenie obrazu

# scena 1
scena1 ="""
-----------
|         |
|
|
|
|
|
|
-----------
"""

# scena 2
scena2 ="""
-----------
|         |
|         O
|
|
|
|
|
-----------
"""

# scena 3
scena3 ="""
-----------
|         |
|         O
|      |--T--|
|
|
|
|
-----------
"""

# scena 4
scena4 ="""
-----------
|         |
|         O
|      |--T--|
|         |
|
|
|
-----------
"""

# scena 5
scena5 ="""
-----------
|         |
|         O
|      |--T--|
|         |
|         M
|        | |
|
-----------
"""

scenywisielca = [scena1,scena2,scena3,scena4,scena5]

# pobranie i przygotowanie hasla
podanehaslo = []
sprawdzonelitery = []
odgadywaniehasla = []
liczbabledow = []

podajhaslo = input('podaj hasło: ')
podajhaslo = podajhaslo.replace(' ','')

for literowaniehasla in range(len(podajhaslo)):
    podanehaslo.append(podajhaslo[literowaniehasla])

print(podanehaslo)

for x in range(len(podanehaslo)):
    odgadywaniehasla.append('_')


# 
def szukanielitery():
    litera = input('podaj litere: ')
    if litera in sprawdzonelitery:
        print('ta litera została już sprawdzona')
        print(sprawdzonelitery)
        print(odgadywaniehasla)
    elif litera in podanehaslo:
        ilejesttakichliter = podanehaslo.count(litera)
        for y in range(ilejesttakichliter):
            miejscelitery = podanehaslo.index(litera)
            odgadywaniehasla[miejscelitery] = podanehaslo[miejscelitery]
            podanehaslo[miejscelitery] = 'litera zostala odgadnieta'
        sprawdzonelitery.append(litera)
        print(sprawdzonelitery)
        print(odgadywaniehasla)
        if ('_') not in odgadywaniehasla:
            print('''
            +----------------+
            |    Wygrałeś    |
            +----------------+
            ''')
    elif litera not in podanehaslo:
        sprawdzonelitery.append(litera)
        if len(liczbabledow) == 5:
            print('''
            +----------------+
            |   Przegrałeś   |
            +----------------+
            ''',quit)
        else:
            print(scenywisielca[len(liczbabledow)])
            liczbabledow.append(1)
    return szukanielitery()





szukanielitery()

print(podanehaslo)
print(sprawdzonelitery)
print(odgadywaniehasla)
