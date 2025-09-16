import tkinter as tk

root = tk.Tk()
root.title("Kalkulator")
root.minsize(352,380)
root.maxsize(352,380)

# zmienne i definicje


    

# -------------------


# wygląd
c1 = tk.Canvas(root, bg="gray",height=290, width=352).place(x=0, y=90)

pole_wyniku = tk.Entry(text="" ,width=17, font=('Arial 24')).place(x=20, y=20)

b_dzielCałk = tk.Button(text="//", height=2, width=9, command="").place(x=20, y=110)
b_dziel = tk.Button(text="/", height=2, width=9, command="").place(x=100, y=110)
b_mnoz = tk.Button(text="*", height=2, width=9, command="").place(x=180, y=110)
b_dod = tk.Button(text="+", height=2, width=9, command="").place(x=260, y=110)
b_7 = tk.Button(text="7", height=2, width=9, command="").place(x=20, y=157)
b_8 = tk.Button(text="8", height=2, width=9, command="").place(x=100, y=157)
b_9 = tk.Button(text="9", height=2, width=9, command="").place(x=180, y=157)
b_odej = tk.Button(text="-", height=2, width=9, command="").place(x=260, y=157)
b_4 = tk.Button(text="4", height=2, width=9, command="").place(x=20, y=204)
b_5 = tk.Button(text="5", height=2, width=9, command="").place(x=100, y=204)
b_6 = tk.Button(text="6", height=2, width=9, command="").place(x=180, y=204)
b_modulo = tk.Button(text="%", height=2, width=9, command="").place(x=260, y=204)
b_1 = tk.Button(text="1", height=2, width=9, command="").place(x=20, y=251)
b_2 = tk.Button(text="2", height=2, width=9, command="").place(x=100, y=251)
b_3 = tk.Button(text="3", height=2, width=9, command="").place(x=180, y=251)
b_oblicz = tk.Button(text="=", height=5, width=9, command="").place(x=260, y=252)
b_0 = tk.Button(text="0", height=2, width=20, command="").place(x=21, y=298)
b_kropka = tk.Button(text=".", height=2, width=9, command="").place(x=180, y=298)






root.mainloop()