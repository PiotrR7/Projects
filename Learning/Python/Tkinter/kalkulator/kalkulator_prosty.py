import tkinter as tk


global number1
global number2

root = tk.Tk()
root.title("kalkulator")
root.geometry('400x480')
root.maxsize(400,480)
root.minsize(400,480)


number1_var = tk.StringVar()
number2_var = tk.StringVar()
wynik_var = tk.StringVar()


# funkcje
def dodawanie():
    number1 = number1_var.get()
    number2 = number2_var.get()
    wynik_var.set(int(number1)+int(number2))

def odejmowanie():
    number1 = number1_var.get()
    number2 = number2_var.get()
    wynik_var.set(int(number1)-int(number2))

def mnozenie():
    number1 = number1_var.get()
    number2 = number2_var.get()
    wynik_var.set(int(number1)*int(number2))

def potegowanie():
    number1 = number1_var.get()
    number2 = number2_var.get()
    wynik_var.set(int(number1)**int(number2))

def dzielenie():
    number1 = number1_var.get()
    number2 = number2_var.get()
    wynik_var.set(int(number1)/int(number2))

def dziel_calk():
    number1 = number1_var.get()
    number2 = number2_var.get()
    wynik_var.set(int(number1)//int(number2))

def modulo():
    number1 = number1_var.get()
    number2 = number2_var.get()
    wynik_var.set(int(number1)%int(number2))



c1 = tk.Canvas(height=100, width=400, bg="gray").place(x=0, y=0)

wynik = tk.Label(textvariable=wynik_var,width=50, height=4).place(x=22, y=19)

liczba1 = tk.Entry(width=27, bg="gray", fg="white", textvariable = number1_var).place(x=20 ,y=120)
liczba2 = tk.Entry(width=27, bg="gray", fg="white", textvariable = number2_var).place(x=210 ,y=120)

c2 = tk.Canvas(height=323, width=400, bg="gray").place(x=0, y=155)


b_dod = tk.Button(text="+", width=10, command=dodawanie).place(x=20, y=170)
b_ode = tk.Button(text="-", width=10, command=odejmowanie).place(x=20, y=200)
b_mno = tk.Button(text="*", width=10, command=mnozenie).place(x=20, y=230)
b_pot = tk.Button(text="**", width=10, command=potegowanie).place(x=20, y=260)
b_dzi = tk.Button(text="/", width=10, command=dzielenie).place(x=20, y=290)
b_dzc = tk.Button(text="//", width=10, command=dziel_calk).place(x=20, y=320)
b_mod = tk.Button(text="%", width=10, command=modulo).place(x=20, y=350)


root.mainloop()