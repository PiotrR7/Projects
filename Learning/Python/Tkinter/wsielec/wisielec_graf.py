# zaimportowanie wszystkich potrzebnych bibliotek
import tkinter as tk
import random
from wisielec_hasla import *
from wisielec_sceny import *




# utworzenie okna graficznego
# okno główne
root = tk.Tk()
root.title("Gra — Wisielec")
root.geometry("700x500")
root.config(background="#1A1A1D")
# root.iconbitmap("unnamed.ico")
# zdefiniowanie zmiennych
text_var = tk.StringVar()
pobranaLitera_var = tk.StringVar()
# -----------------------
# pozostałe pola gry
t1 = tk.Text(root,fg="#ffffff",background="#4E4E50", height=15, width=78)
t1.place(x=35,y=40)
l1 = tk.Label(root, textvariable=text_var ,fg="white",background="#6F2232",width=68 ).place(x=110,y=300)
e1 = tk.Entry(root, textvariable=pobranaLitera_var,fg="white",background="#950740", width=80).place(x=110,y=350)
# ustawienie wartości dla pól gry
t1.insert(tk.INSERT,("""
Wisielec!
Twoim zadaniem jest zgadnięcie hasła.
Możesz pomylić się 5 razy.

"""))
text_var.set("Podaj litere")
# ----------------------------


# skrypt gry
# utworzenie tablic
podanehaslo = []
sprawdzonelitery = []
odgadywaniehasla = []
liczbabledow = []

# przygotowanie hasła
for a in range(len(hasla)):
    hasla[a] = (hasla[a].lower())
podajhaslo = hasla[random.randrange(0,29)]
haslo_podglad = podajhaslo
podajhaslo = podajhaslo.replace(' ','')
for literowaniehasla in range(len(podajhaslo)):
    podanehaslo.append(podajhaslo[literowaniehasla])
for x in range(len(podanehaslo)):
    odgadywaniehasla.append('_')

# print(podanehaslo)
# print(sprawdzonelitery)
# print(odgadywaniehasla)
# print(liczbabledow)

# pobranie litery od użytkownika
def pobierz():
    global litera
    litera = pobranaLitera_var.get()
    szukanielitery()

# przycisk wywołujący funkcję pobierz()
Button = tk.Button(root,text="Sprawdź litere",command=pobierz).place(x=310, y=400)

# funkcja spradzająca, czy dana litera jest w haśle 
def szukanielitery():
    running = True

    # czyszczenie pola gry
    t1.delete("1.0", "end")

    # pętla gry
    while running == True:
        # jeżeli podana litera została sprawdzona podaj inną
        if litera in sprawdzonelitery:
            text_var.set('Ta litera została już sprawdzona.')
        # jeżeli podana litera występuje w haśle wypisuje ją
        elif litera in podanehaslo:
            text_var.set("Odgadłeś litere.")
            ilejesttakichliter = podanehaslo.count(litera)
            for y in range(ilejesttakichliter):
                miejscelitery = podanehaslo.index(litera)
                odgadywaniehasla[miejscelitery] = podanehaslo[miejscelitery]
                podanehaslo[miejscelitery] = 'Litera zostala odgadnieta.'
            sprawdzonelitery.append(litera)
        # jeżeli wszystkie litery są odgadnięte użytkownik wygrał
            if ('_') not in odgadywaniehasla:
                t1.insert(tk.INSERT,'''
                +----------------+
                |    Wygrałeś    |
                +----------------+
                ''')
                running = False
        # jeżeli litera nie występuje w haśle kolejny element wisielca
        elif litera not in podanehaslo:
            sprawdzonelitery.append(litera)
        # jeżeli wisielec jest w pelni narysowany użytkownik przegrał
            if len(liczbabledow) == 11:
                t1.insert(tk.INSERT,'''
                +----------------+
                |   Przegrałeś   |
                +----------------+
                ''')
                text_var.set("Prawidłowe hasło to "+ haslo_podglad)
                running = False
        # jeżeli są jeszcze dostępne do wykorzystania sceny wisielca pobierz następna litere
            else:
                text_var.set("Zła litera, podaj inną")
                t1.insert(tk.INSERT, (scenywisielca[len(liczbabledow)]))
                liczbabledow.append(1)
        # update okna
        root.update()
        t1.insert(tk.INSERT,odgadywaniehasla)
        running = False


t1.insert(tk.INSERT,odgadywaniehasla)


root.mainloop()