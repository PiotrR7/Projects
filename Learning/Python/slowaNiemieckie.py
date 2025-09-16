slowaNiemieckie = {
    "być":"sein",
    "interesować":"interessieren",
    "dawać":'geben',
    "kosztować":"kosten",
    "kochać":"lieben",
    "słyszeć":"hören",
    "szukać":"suchen",
    "znajdować":"finden",
    "prowadzić":"fahren",
    "pisać" : "schreiben",
    "widzieć" : "sehen",
    "uczyć się" : "lernen",
    "czytać" : 'lesen',
    "potrzebować" : "brauchen",
    "handlować" : "handeln",
}

def sprawdz(x):
    print(slowaNiemieckie[x])

running = True
while running == True:
    sprawdzSlowo = input(": ")
    if sprawdzSlowo == 0:
        break
    if sprawdzSlowo not in slowaNiemieckie:
        print("Nie ma takiego słowa")
    else:
        sprawdzSlowoNiemieckie = input("podaj tłumaczenie: ")
        czyDobrze = slowaNiemieckie[sprawdzSlowo]
        if sprawdzSlowoNiemieckie == czyDobrze:
            print("Dobrze!")
            czyKontynuowac = input("[TAK lub NIE] Czy chcesz kontynuować?")
        else:
            print("źle!","Powinno być ",czyDobrze)
            czyKontynuowac = input("[TAK lub NIE] Czy chcesz kontynuować? ")
        while czyKontynuowac == 'TAK':
            running = True
        while czyKontynuowac == 'NIE':
            running = False