
from tkinter import *
from typing import Protocol
from PIL import ImageTk, Image, ImageOps
import math

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
PINK = "#FFE3E1"
LIGHTYELLOW = "#FFF5E4"
ORANGE = "#FFAA22"
dpi = 96

class ContainerFactory(Protocol):
    def __call__(self, master: Tk, *args, **kwargs) -> Frame:
        Frame.__init__(self, master, *args, **kwargs)
        
class IntiInteractiveSystem():
    def __init__(self, root) -> None:
        self.root = root
        self.button_dict = {}
        self.frame_dict = {}
        self.container_dict = {}
        self.root.geometry('1920x1080')
        self.create_buttons()
        self.start_page_frame()

        for classname, lit in [(RegistrationPage, "RegistrationPage"),(RegistrationPage2, "RegistrationPage2")]:
            instance = classname(root)
            self.frame_dict[lit] = instance.page_frame

    def button_press(self, button_id):
        """
            deselect current frame's button, and activate all others
        """
        print(button_id)
        for key in self.button_dict:
            if key == button_id:
                self.button_dict[key].config(state="disabled")
            else:
                self.button_dict[key].config(state="normal")

        # raise the frame corresponding to the button clicked
        self.frame_dict[button_id].lift()

    
    
        
class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('1920x1080')
        self.title("INTI Interactive System")
        self.resizable(0, 0)
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
        container.grid(row=3, column=18, columnspan=12,
                       rowspan=12, sticky=N+S+E+W)
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)
        #Left Container
        container2 = Frame(self, bg=PINK, borderwidth=1, relief="solid")
        container2.grid_propagate(0)
        container2.grid(row=3, column=2, columnspan=15, rowspan=12, sticky=N+S+E+W)
        container2.grid_rowconfigure(0, weight=0)
        container2.grid_columnconfigure(0, weight=0)
        #Bottom Container
        container3 = Containers(self, bg="orange", borderwidth=1, relief="solid", row=16, column=0, rowspan=2, columnspan=16, sticky=N+S+E+W)
        #Top Container
        # container4 = Containers(self, bg="magenta", borderwidth=1, relief="solid", row=0, column=0, rowspan=2, columnspan=32, sticky=N+S+E+W)

        

        
        self.frames = {}
        
        for F in (RegistrationPage,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(RegistrationPage)
        for F in (RegistrationPage2,):
            frame = F(container2, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(RegistrationPage2)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Containers(Frame):
    def __init__(self, parent, row, column, rowspan, columnspan, sticky, *args, **kwargs):
        self.row = row
        self.column = column
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.sticky = sticky
        Frame.__init__(self, parent, *args, **kwargs)
        self.grid(row=self.row, column=self.column, rowspan=self.rowspan, columnspan=self.columnspan, sticky=self.sticky)

class LabelFactory(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)

class RegistrationPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="dark green", borderwidth=1, relief="solid")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="nsew")
        for x in range(20):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=2, bg="red", borderwidth=1, relief="solid").grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W,)

class RegistrationPage2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1, relief="solid", cursor="hand2")
        self.grid(row=0, column=0,sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        for x in range(20):
            self.columnconfigure(x, weight=0, uniform='x')
            Label(self, height=2, bg="red", borderwidth=1, relief="solid").grid(
                row=0, column=x,rowspan=1,columnspan=2, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(row=y, column=0,rowspan=2, columnspan=1, sticky=N+S+E+W)
        haveanaccountlabel = Label(self, text="Already have an account?", font=(
        'Arial', 16), width=1, height=1, fg='#000000', bg='red')
        haveanaccountlabel.grid_propagate(0)
        haveanaccountlabel.grid(row=0, column=4, rowspan=2, columnspan=12, sticky=N+S+E+W)
        
    

        
        


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
