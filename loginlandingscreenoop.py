from tkinter import *

import math
import sqlite3
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFE3E1"
LIGHTYELLOW = "#FFF5E4"

class Window:  # the main class that will be used to create the windows for every screen
    def __init__(
            self, title: str, width: int, height: int) -> None:
        self.root = Tk()
        self.root.title(title)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.end)
        self.frame = Frame(master=self.root)
        self.dpi = 96
        self.width = width
        self.height = height
        self.root.grid_propagate = False
        self.root.geometry(f"{width}x{height}")
        for x in range(32):
            Grid.columnconfigure(self.root, x, weight=1, uniform='row')
            Label(self.root, width=1, bg='#FFE3E1').grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(18):
            Grid.rowconfigure(self.root, y, weight=1, uniform='row')
            Label(self.root, width=1, bg='#FFE3E1').grid(
                row=y, column=0, sticky=N+S+E+W)
        self.root.configure(background='#FFE3E1')

    def resize():
        pass 

    def start(self):
        self.running = True
        self.root.mainloop()

    def end(self):
        self.running = False
        self.root.destroy()

class SignUpWidgets:
    pass

