import tkinter as tk
from easy_mode import EasyMode
from medium_mode import MediumMode
from hard_mode import *

class Memory:
    root = ""
    chosen_level = ""

class Apk:
    def root_open():
        EasyMode.Memory.window.withdraw()
        MediumMode.Memory.window.withdraw()

        Memory.root = tk.Tk()
        Memory.root.resizable(False,False)
        Memory.root.title("")
        Memory.root.geometry("900x300")

        btn_ey = tk.Button(Memory.root, text="Easy", width=20, height=3, command=lambda: Apk.Level("easy")).place(x=70, y=100)
        btn_mm = tk.Button(Memory.root, text="Medium", width=20, height=3, command=lambda: Apk.Level("medium")).place(x=270, y=100)
        btn_mh = tk.Button(Memory.root, text="Medium Hard", width=20, height=3, command=lambda: Apk.Level("medium_hard")).place(x=470, y=100)
        btn_hd = tk.Button(Memory.root, text="Hard", width=20, height=3, command=lambda: Apk.Level("hard")).place(x=670, y=100)

        Memory.root.mainloop()
    
    def Level(arg):
        Memory.chosen_level = arg
        Memory.root.destroy()
        if (Memory.chosen_level == "easy"):
            EasyMode.Memory.window.iconify()
            EasyMode.RandomWord()
            EasyMode.Play()
        if (Memory.chosen_level == "medium"):
            MediumMode.Memory.window.iconify()
            MediumMode.RandomWord()
            MediumMode.Play()
        if (Memory.chosen_level == "hard"):
            print("hard")
        if (Memory.chosen_level == "medium_hard"):
            print("hard")

Apk.root_open()