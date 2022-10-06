from tkinter import *
from tkinter import font

root = Tk()
root.title('Font Families')
fonts=list(font.families())
fonts.sort()

def populate(frame):
    '''Put in the fonts'''
    listnumber = 1
    for item in fonts:
        label = "listlabel" + str(listnumber)
        label = Label(frame,text=item,font=(item, 16)).pack()
        listnumber += 1

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()

# from tkinter import *
# import tkinter.font as tkFont

# root = Tk()

# fonts=list(tkFont.families())
# fonts.sort()

# display = Listbox(root)
# display.pack(fill=BOTH, expand=YES, side=LEFT)

# scroll = Scrollbar(root)
# scroll.pack(side=RIGHT, fill=Y, expand=NO)

# scroll.configure(command=display.yview)
# display.configure(yscrollcommand=scroll.set)

# for item in fonts:
#     display.insert(END, item)

# root.mainloop()