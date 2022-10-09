from tkinter import *
from PIL import ImageTk, Image

import tkinter

class Test:
    def __init__(self, master):
        canvas = tkinter.Canvas(master)
        canvas.grid(row = 0, column = 0)
        self.photo = tkinter.PhotoImage(file = 'caption-23.gif') # Changes here
        canvas.create_image(0, 0, image=self.photo) # Changes here

root = tkinter.Tk()
test = Test(root)
root.mainloop()