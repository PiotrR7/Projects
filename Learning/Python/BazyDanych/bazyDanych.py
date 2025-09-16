import tkinter as tk
from sql_poloczenie import *
# from funkcje import *

root = tk.Tk()
root.title("Bazy Danych")
root.minsize(1200, 700)

def wyswielanieElementow():
    for record in cur:
        for a in range(0,len(record)):
            x=(record[a])
            print(x)
            liczba = 30
            liczba = int(liczba)
            l1 = tk.Label(text=x).place(x=0, y=(0+liczba*a))


def wyswielanieBazDanych():
    tablica = []
    for record in wbd:
        y=(record[0])
        tablica.append(y)

    l0 = tk.Button(text=tablica[0], bg='gray', fg='white', width=21).place(x=20, y=20)
    l1 = tk.Button(text=tablica[1], bg='gray', fg='white', width=21).place(x=20, y=50)
    l2 = tk.Button(text=tablica[2], bg='gray', fg='white', width=21).place(x=20, y=80)
    l3 = tk.Button(text=tablica[3], bg='gray', fg='white', width=21).place(x=20, y=110)
    l4 = tk.Button(text=tablica[4], bg='gray', fg='white', width=21).place(x=20, y=140)
    l5 = tk.Button(text=tablica[5], bg='gray', fg='white', width=21).place(x=20, y=170)
    l6 = tk.Button(text=tablica[6], bg='gray', fg='white', width=21).place(x=20, y=200)
    l7 = tk.Button(text=tablica[7], bg='gray', fg='white', width=21).place(x=20, y=230)
    l8 = tk.Button(text=tablica[8], bg='gray', fg='white', width=21).place(x=20, y=260)
    l9 = tk.Button(text=tablica[9], bg='gray', fg='white', width=21).place(x=20, y=290)
    l10 = tk.Button(text=tablica[10], bg='gray', fg='white', width=21).place(x=20, y=320)
    l11 = tk.Button(text=tablica[11], bg='gray', fg='white', width=21).place(x=20, y=350)
    l12 = tk.Button(text=tablica[12], bg='gray', fg='white', width=21).place(x=20, y=380)
    l13 = tk.Button(text=tablica[13], bg='gray', fg='white', width=21).place(x=20, y=410)
    l14 = tk.Button(text=tablica[14], bg='gray', fg='white', width=21).place(x=20, y=440)
    l15 = tk.Button(text=tablica[15], bg='gray', fg='white', width=21).place(x=20, y=470)
    l16 = tk.Button(text=tablica[16], bg='gray', fg='white', width=21).place(x=20, y=500)
    l17 = tk.Button(text=tablica[17], bg='gray', fg='white', width=21).place(x=20, y=530)
    l18 = tk.Button(text=tablica[18], bg='gray', fg='white', width=21).place(x=20, y=560)
    l19 = tk.Button(text=tablica[19], bg='gray', fg='white', width=21).place(x=20, y=590)

c1 = tk.Canvas(width=200,height=1000,bg="grey").place(x=0,y=0)

wyswielanieBazDanych()
wyswielanieElementow()

root.mainloop()