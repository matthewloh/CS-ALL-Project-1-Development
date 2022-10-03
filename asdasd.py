import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_459=tk.Entry(root)
        GLineEdit_459["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_459["font"] = ft
        GLineEdit_459["fg"] = "#333333"
        GLineEdit_459["justify"] = "center"
        GLineEdit_459["text"] = "Entry"
        GLineEdit_459.place(x=370,y=130,width=128,height=30)
        GLineEdit_459["show"] = "yhehe"
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
