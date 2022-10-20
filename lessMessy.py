from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from typing import Protocol
from PIL import ImageTk, Image, ImageOps
import math
import sqlite3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
PINK = "#FFE3E1"
OTHERPINK = "#FA9494"
LIGHTYELLOW = "#FFF5E4"
ORANGE = "#FFAA22"
NICEPURPLE = "#B1B2FF"
NICEBLUE = "#AAC4FF"
LAVENDER = "#D2DAFF"
LIGHTPURPLE = "#EEF1FF"
dpi = 96
LOGGEDIN = "Neither student or admin"
LOGINSTATE = "Not logged in"

class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        dpiError = False
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            print('ERROR. Could not set DPI awareness.')
        dpiError = True
        if dpiError:
            dpi = 96
        else:
            dpi = self.winfo_fpixels('1i')
        self.geometry(
            f'{math.ceil(1920 * dpi / 96)}x{math.ceil(1080 * dpi / 96)}')
        for x in range(32):
            self.columnconfigure(x, weight=1, uniform='row')
            Label(width=10, height=10, bg=LIGHTYELLOW, borderwidth=1, relief="solid").grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(18):
            self.rowconfigure(y, weight=1, uniform='row')
            Label(width=10, height = 10, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, sticky=N+S+E+W)
        self.title("INTI Interactive System")
        self.container = Frame(self, bg=LIGHTPURPLE, borderwidth=1, relief="solid")
        self.container.grid(row=0, column=0, columnspan=30, rowspan=16, sticky=N+S+E+W)
        self.frames = {}
        
        for F in {RegistrationPage, RegistrationPage2}:
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(RegistrationPage)

    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def edit_containersize(self, cont):
        self.container.grid(row=9, column=16, columnspan=30, rowspan=16, sticky=N+S+E+W)
    
        

class RegistrationPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="yellow",
                       borderwidth=1, relief="solid")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # for x in range(30):
        #     Grid.columnconfigure(self, x, weight=1, uniform='row')
        #     Label(width=10, height=10, bg="grey", borderwidth=1, relief="solid").grid(
        #         row=0, column=x, sticky=N+S+E+W)
        # for y in range(18):
        #     Grid.rowconfigure(self, y, weight=1, uniform='row')
        #     Label(width=10, height=10, bg="Pink", borderwidth=1, relief="solid").grid(
        #         row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W,)
        

class RegistrationPage2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER, borderwidth=1,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(32):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=LAVENDER, borderwidth=0, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(18):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=LAVENDER, bd=1, borderwidth=0, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        # sizebutton = Button(
        #     self, text="Big", command=lambda: _.changecontainersize(self, parent))
        # sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        # unsizebutton = Button(
        #     self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        # unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        label = Label(self, text="This is the registration page on left frame\nCome back later, still under construction!", font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=17,
                   rowspan=2, sticky=N+S+E+W)

        self.intibanner = Image.open("Home-Banner-INTI.png")
        self.intibanner = ImageTk.PhotoImage(self.intibanner.resize(
            (math.ceil(359 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        logolabel = Button(self, image=self.intibanner, anchor=CENTER, width=1, height=1)
        logolabel.grid(row=4, column=5, columnspan=11,
                        rowspan=5, sticky=N+S+E+W)
        self.titleart = Image.open("DR7j7r0.png")
        self.titleart = ImageTk.PhotoImage(self.titleart.resize(
            (math.ceil(720 * dpi / 96), math.ceil(240 * dpi / 96)), Image.Resampling.LANCZOS))
        titleartlabel = Button(self, image=self.titleart, anchor=CENTER, width=1, height=1)
        titleartlabel.grid(row=9, column=0, columnspan=21,
                        rowspan=8, sticky=N+S+E+W)

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()