
from tkinter import *
from PIL import ImageTk, Image, ImageOps
import math

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
PINK = "#FFE3E1"
LIGHTYELLOW = "#FFF5E4"
ORANGE = "#FFAA22"
dpi = 96


class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('1920x1080')
        self.title("INTI Interactive System")
        for x in range(32):
            self.columnconfigure(x, weight=1, uniform='row')
            Label(width=1, bg=LIGHTYELLOW, borderwidth=1, relief="solid").grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(18):
            self.rowconfigure(y, weight=1, uniform='row')
            Label(width=1, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, sticky=N+S+E+W,)
        self.configure(background=LIGHTYELLOW)
        #Right Container
        container = Frame(self, bg="brown", borderwidth=1,
                          relief="solid", width=1, height=1)
        container.grid_propagate(0)
        container.grid(row=3, column=18, columnspan=10,
                       rowspan=12, sticky=N+S+E+W)
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)
        #Left Container
        container2 = Frame(self, bg=PINK, borderwidth=1, relief="solid")
        container2.grid_propagate(0)
        container2.grid(row=2, column=4, columnspan=12, rowspan=14, sticky=N+S+E+W)
        container2.grid_rowconfigure(0, weight=0)
        container2.grid_columnconfigure(0, weight=0)

        self.frames = {}

        for EACHFRAME in (RegistrationPage,):
            frame = EACHFRAME(container, self)
            self.frames[EACHFRAME] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(RegistrationPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class RegistrationPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="light green")
        
        


# haveanaccountlabel = Label(self, text="Already have an account?", font=(
#     'Arial', 16), width=1, height=1, fg='#000000', bg='red')
# haveanaccountlabel.grid()
# SignUpLabel = Label(self, text="Please enter your details as shown.", font=(
#     'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
# SignUpLabel.grid(row=5, column=20, columnspan=8,
#                     rowspan=1, sticky=N+S+E+W)
# SignUpEmailEntry = Entry(self, width=50, bg='#FFFFFF',
#                             font=('Arial', 16), justify='center')
# SignUpEmailEntry.insert(0, "Please enter your student email")
# SignUpEmailEntry.grid(row=9, column=21, columnspan=6,
#                         rowspan=1, sticky=N+S+E+W)
# signupregister = Button(self, text="SIGN UP", font=(
#     'Arial', 16), width=1, height=1, fg='#000000', command=lambda: print("hello world"), bg='#FFF5E4')
# signupregister.grid(row=9, column=21, columnspan=6,
#                     rowspan=1, sticky=N+S+E+W)
# gotosigninbutton = Button(self, text="Click here for sign in page", font=(
#     'Arial', 14), width=1, height=1, fg='#000000', command=print("hello"), bg='#00FFFF')
# gotosigninbutton.grid(
#     row=15, column=26, columnspan=2, rowspan=1, sticky=N+S+E+W)
window = Window()
window.mainloop()
