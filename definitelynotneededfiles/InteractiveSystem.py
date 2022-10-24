
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
dpi = 96


class ContainerFactory(Protocol):
    def __call__(self, master: Tk, *args, **kwargs) -> Frame:
        Frame.__init__(self, master, *args, **kwargs)


class Window(Tk):
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
        self.geometry(f'{math.ceil(1920 * dpi / 96)}x{math.ceil(1080 * dpi / 96)}')
        self.grid_propagate(False)
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
        # Right Container
        container = Frame(self, 
                         bg="brown", borderwidth=1,relief="solid", 
                         width=1, height=1)
        container.grid_propagate(0)
        container.grid(row=3, column=17, columnspan=13,
                       rowspan=12, sticky=N+S+E+W)
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)
        # Left Container
        container2 = Frame(self, bg=PINK, borderwidth=1, relief="solid")
        container2.grid_propagate(0)
        container2.grid(row=3, column=2, columnspan=13,
                        rowspan=12, sticky=N+S+E+W)
        container2.grid_rowconfigure(0, weight=0)
        container2.grid_columnconfigure(0, weight=0)


        # Top Container
        #functions to enlarge the left and right frames and revert
        def changecontainersizes(rightcontainer, leftcontainer): 
            rightcontainer.grid(row=2, column=16, rowspan=14,
                            columnspan=14, sticky=N+S+E+W)
            leftcontainer.grid(row=2, column=2, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)
        def makeleftcontainerhuge(leftcontainer):
             leftcontainer.grid(row=2, column=2, rowspan=14,
                               columnspan=28, sticky=N+S+E+W)

        def revertcontainersizes(rightcontainer, leftcontainer):
            rightcontainer.grid(row=3, column=17, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
            leftcontainer.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
        def keepcontainerlarge(rightcontainer):
            rightcontainer.grid(row=2, column=16, rowspan=14,
                            columnspan=14, sticky=N+S+E+W)
        container3 = Frame(self, bg="orange", borderwidth=1, relief="solid")
        container3.grid(row=0, column=0, rowspan=2, columnspan=20, sticky=N+S+E+W)
        container3.grid_propagate(0)
        signupbutton = Button(container3, text="Sign Up\n Page", bg=OTHERPINK, fg="white", font=(
            "Arial", 20), borderwidth=1, relief="solid", command=lambda: [self.show_frame(RegistrationPage), self.show_frameleft(RegistrationPage2), revertcontainersizes(container, container2)])
        signupbutton.grid(row=0, column=0, rowspan=1, sticky=N+S+E+W)
        loginbutton = Button(container3, text="Login\nPage", bg=OTHERPINK, fg="white", font=(
            "Arial", 20), borderwidth=1, relief="solid", command=lambda: [self.show_frame(LoginPage), self.show_frameleft(LoginPage2), revertcontainersizes(container, container2), keepcontainerlarge(container)])
        loginbutton.grid(row=0, column=1, rowspan=1, sticky=N+S+E+W)
        mainpagebutton = Button(container3, text="Main\nPage", bg=OTHERPINK, fg="white", font=(
            "Arial", 20), borderwidth=1, relief="solid", command=lambda: [self.show_frame(EmptyRFrame),self.show_frameleft(MainPage2), makeleftcontainerhuge(container2)])
        mainpagebutton.grid(row=0, column=2, rowspan=1, sticky=N+S+E+W)
        eventlistbutton = Button(container3, text="Event\nList", bg=OTHERPINK, fg="white", font=(
            "Arial", 20), borderwidth=1, relief="solid", command=lambda: [self.show_frame(EventView), self.show_frameleft(EventView2), revertcontainersizes(container, container2),changecontainersizes(container,container2)])
        eventlistbutton.grid(row=0, column=3, rowspan=1, sticky=N+S+E+W)
        eventregistrationbutton = Button(container3, text="Event\nRegistration", bg=OTHERPINK, fg="white", font=(
            "Arial", 20), borderwidth=1, relief="solid", command=lambda: [self.show_frame(EventRegistration), self.show_frameleft(EventRegistration2), revertcontainersizes(container, container2),changecontainersizes(container,container2)])
        eventregistrationbutton.grid(row=0, column=4, rowspan=1, sticky=N+S+E+W)
        eventcreationbutton = Button(container3, text="Event\nCreation\n(ADMIN)", bg=OTHERPINK, fg="white", font=(
            "Arial", 20), borderwidth=1, relief="solid", command=lambda: [self.show_frame(EventCreation), self.show_frameleft(EmptyRFrame), makeleftcontainerhuge(container2)])
        eventcreationbutton.grid(row=0, column=5, rowspan=1, sticky=N+S+E+W)
        viewparticipantsbutton = Button(container3, text="View\nParticipants\n(ADMIN)", bg=OTHERPINK, fg="white", font=("Arial", 20), borderwidth=1, relief="solid", command=lambda: [self.show_frame(ViewParticipants), self.show_frameleft(EmptyRFrame), makeleftcontainerhuge(container2)])
        viewparticipantsbutton.grid(row=0, column=6, rowspan=1, sticky=N+S+E+W)
            
        # container3.grid_rowconfigure(0, weight=1)
        # container3.grid_columnconfigure(0, weight=1)
        # container3.grid_rowconfigure(1, weight=1)
        # container3.grid_columnconfigure(1, weight=1)
        # container3.grid_rowconfigure(2, weight=1)
        # container3.grid_columnconfigure(2, weight=1)
        # container3.grid_rowconfigure(3, weight=1)
        # container3.grid_columnconfigure(3, weight=1)
        # container3.grid_rowconfigure(4, weight=1)
        # container3.grid_columnconfigure(4, weight=1)
        # Top Container
        # container4 = Containers(self, bg="magenta", borderwidth=1, relief="solid", row=0, column=0, rowspan=2, columnspan=32, sticky=N+S+E+W)

        self.frames = {}

        for F in (RegistrationPage, LoginPage, MainPage,EmptyRFrame, EventView, EventRegistration):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(RegistrationPage)

        for F in (RegistrationPage2, LoginPage2, MainPage2, EventView2, EventRegistration2, EventCreation, ViewParticipants):
            frame = F(container2, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frameleft(RegistrationPage2)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_frameleft(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# this is totally unnecessary and I was just messing around to learn how classes worked
class Containers(Frame):
    def __init__(self, parent, row, column, rowspan, columnspan, sticky, *args, **kwargs):
        self.row = row
        self.column = column
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.sticky = sticky
        Frame.__init__(self, parent, *args, **kwargs)
        self.grid(row=self.row, column=self.column, rowspan=self.rowspan,
                  columnspan=self.columnspan, sticky=self.sticky)


class LabelFactory(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)


class RegistrationPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="dark green",
                       borderwidth=1, relief="solid")
        for x in range(25):
            Grid.columnconfigure(self, x, weight=1, uniform='row')
            Label(self, height=2, bg="red", borderwidth=1, relief="solid").grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(25):
            Grid.rowconfigure(self, y, weight=1, uniform='row')
            Label(self, width=5, bg=ORANGE, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W,)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # constants
        FONTNAME = "Avenir Next Medium"
        FIRSTNAME = "First Name"
        LASTNAME = "Last Name"
        EMAILTEXT = "Please enter your student email."
        PASSWORDTEXT = "Please enter your password."
        CONFPASSTEXT = "Please confirm your password."
        # database functions
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS registration(
            first_name text NOT NULL,
            last_name text NOT NULL,
            email text NOT NULL PRIMARY KEY,
            role text NOT NULL,
            password text NOT NULL
        )""")
        c.execute("DROP Table registration")

        # possibly, we could make two functions, one to validate input and another to actually send the data to the database, instead of checking validity itself in checkfields()
        # a function to designate a role depending on ending of email registration

        def role():
            try:
                emailending = emailfield.get().split("@")[1]
                if emailending==("student.newinti.edu.my"):
                    messagebox.showinfo("Role", "You are a student.")
                    return "student"

                elif emailending==("newinti.edu.my"):
                    messagebox.showinfo("Role", "You are an.")
                    return "admin"
                else:
                    emailwarning = Label(self, text="Please enter a valid email address.", font=(
                    'Arial', 10), width=1, height=1, fg='#000000', bg='#FFF5E4')
                    emailwarning.grid(row=6, column=11, columnspan=7,
                                rowspan=1, sticky=N+S+E+W)
                    emailwarning.configure(text ="Please enter a valid email.", fg="red")
                    return "invalid"
            except IndexError:
                messagebox.showerror("Error", "Please enter an email")
            
 
        def checkfields():
            # c.execute("DROP TABLE registration")
            firstnametext = firstnamefield.get()
            lastnametext = lastnamefield.get()
            emailtext = emailfield.get()
            passwordtext = passwordfield.get()
            confirmpasstext = confirmpasswordfield.get()
            
            information = (firstnametext, lastnametext,
                           emailtext, passwordtext)

            try:
                if (FIRSTNAME in firstnametext) or (LASTNAME in lastnametext) or (EMAILTEXT in emailtext) or (PASSWORDTEXT in passwordtext) or (CONFPASSTEXT in confirmpasstext):
                    messagebox.showerror("Error", "Please fill in all fields.")
                elif passwordtext != confirmpasstext:
                    messagebox.showerror("Error", "Passwords do not match.")
                else:
                    with conn:
                        c.execute(
                            """INSERT INTO registration VALUES(?, ?, ?, ?)""", information)
                        messagebox.showinfo(
                            "Success", "You have successfully registered.")
                        controller.show_frame(LoginPage)
                        controller.show_frameleft(LoginPage2)

            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Email already in use.")

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=16, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=17, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # functions to clear the entry boxes

        def clearnamefields():
            if firstnamefield.get() == FIRSTNAME:
                firstnamefield.delete(0, END)
            if lastnamefield.get() == LASTNAME:
                lastnamefield.delete(0, END)

        def repopulatenamefields():
            if firstnamefield.get() == "":
                firstnamefield.insert(0, FIRSTNAME)
            if lastnamefield.get() == "":
                lastnamefield.insert(0, LASTNAME)

        def clearemailfield():
            emailfield.configure(fg="black")
            if emailfield.get() == EMAILTEXT:
                emailfield.delete(0, END)

        def repopulateemailfield():
            if emailfield.get() == "":
                emailfield.insert(0, EMAILTEXT)
                emailfield.configure(fg="red")

        def clearpasswordfield():
            passwordfield.configure(fg="black")
            passwordfield.configure(show="*")
            if passwordfield.get() == PASSWORDTEXT:
                passwordfield.delete(0, END)

        def repopulatepasswordfield():
            if passwordfield.get() == "":
                passwordfield.insert(0, PASSWORDTEXT)
                passwordfield.configure(show="")
                passwordfield.configure(fg="red")
            else:
                passwordfield.configure(show="*")

        def clearconfpasswordfield():
            confirmpasswordfield.configure(fg="black")
            confirmpasswordfield.configure(show="*")
            if confirmpasswordfield.get() == CONFPASSTEXT:
                confirmpasswordfield.delete(0, END)

        def repopulateconfpasswordfield():
            confirmpasswordfield.configure(show="*")
            if confirmpasswordfield.get() == "":
                confirmpasswordfield.insert(0, CONFPASSTEXT)
                confirmpasswordfield.configure(show="")
                confirmpasswordfield.configure(fg="red")

        # Labels
        enterdetailslabel = Label(self, text="Please enter your details as shown in the entries.", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        enterdetailslabel.grid(
            row=1, column=2, columnspan=16, rowspan=2, sticky=N+S+E+W)

        # Entries
        firstnamefield = Entry(self, width=1, bg='#FFFFFF',
                               font=(FONTNAME, 18), justify='center')
        firstnamefield.grid(row=4, column=2, columnspan=7,
                            rowspan=2, sticky=N+S+E+W)
        firstnamefield.insert(0, FIRSTNAME)

        lastnamefield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        lastnamefield.grid(row=4, column=11, columnspan=7,
                           rowspan=2, sticky=N+S+E+W)
        lastnamefield.insert(0, LASTNAME)

        emailfield = Entry(self, width=1, bg='#FFFFFF',
                           font=(FONTNAME, 18), justify='center')
        emailfield.grid(row=7, column=2, columnspan=16,
                        rowspan=2, sticky=N+S+E+W)
        emailfield.insert(0, EMAILTEXT)

        passwordfield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        passwordfield.grid(row=10, column=2, columnspan=16,
                           rowspan=2, sticky=N+S+E+W)
        passwordfield.insert(0, PASSWORDTEXT)

        confirmpasswordfield = Entry(
            self, width=1, bg='#FFFFFF', font=(FONTNAME, 18), justify='center')
        confirmpasswordfield.grid(
            row=13, column=2, columnspan=16, rowspan=2, sticky=N+S+E+W)
        confirmpasswordfield.insert(0, CONFPASSTEXT)

        # Entry Binding
        firstnamefield.bind("<FocusIn>", lambda event: clearnamefields())
        lastnamefield.bind("<FocusIn>", lambda event: clearnamefields())
        firstnamefield.bind("<FocusOut>", lambda event: repopulatenamefields())
        lastnamefield.bind("<FocusOut>", lambda event: repopulatenamefields())
        emailfield.bind("<FocusIn>", lambda event: clearemailfield())
        emailfield.bind("<FocusOut>", lambda event: repopulateemailfield())
        passwordfield.bind("<FocusIn>", lambda event: clearpasswordfield())
        passwordfield.bind(
            "<FocusOut>", lambda event: repopulatepasswordfield())
        confirmpasswordfield.bind(
            "<FocusIn>", lambda event: clearconfpasswordfield())
        confirmpasswordfield.bind(
            "<FocusOut>", lambda event: repopulateconfpasswordfield())

        # Buttons
        signupbutton = Button(self, text="SIGN UP", font=(
            'Arial', 18), width=1, height=1, fg='#000000', command=lambda: checkfields(), bg=LIGHTYELLOW)
        signupbutton.grid(row=16, column=6, columnspan=8,
                          rowspan=2, sticky=N+S+E+W)

        loginbutton = Button(self, text="Already have an account?\nClick here to sign in.", font=('Atkinson Hyperlegible', 18), width=1,
                             height=1, fg='#000000', command=lambda: [controller.show_frame(LoginPage), controller.show_frameleft(LoginPage2), _.changecontainersize(self, parent)], bg=OTHERPINK)
        loginbutton.grid(row=19, column=6, columnspan=8,
                         rowspan=2, sticky=N+S+E+W)

        checkrolebutton = Button(self, text="Check your role", font=(
            'Arial', 18), width=1, height=1, fg='#000000', command=lambda: role(), bg=LIGHTYELLOW)
        checkrolebutton.grid(row=15, column=2, columnspan=4,
                                rowspan=2, sticky=N+S+E+W)


class RegistrationPage2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="red", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=2, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        label = Label(self, text="This is the registration page on left frame\nCome back later, still under construction!", font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=16,
                   rowspan=2, sticky=N+S+E+W)
        # imageframe = Frame(self, borderwidth=1,
        #                     relief="solid", cursor="hand2")
        # imageframe.grid(row=3, column=2, columnspan=13,
        #                 rowspan=12, sticky=N+S+E+W) 
        # self.INTI_BannerImage = Image.open('Assets\Home-Banner-INTI.png')
        # self.INTI_BannerImage = ImageOps.exif_transpose(self.INTI_BannerImage)
        # self.INTI_BannerImage = ImageTk.PhotoImage(self.INTI_BannerImage.resize(
        #     (math.ceil(359 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        # INTI_Banner = Label(self, image=self.INTI_BannerImage, anchor=S)
        # INTI_Banner.grid(row=3, column=2, columnspan=4,
        #                     rowspan=3, sticky=N+S+E+W) 
        # INTI_Banner.grid_propagate(False)
        # self.bannerphoto = Image.open("Assets\Home-Banner-INTI.png")
        # self.bannerphoto = ImageTk.PhotoImage(self.bannerphoto.resize(
        #     (math.ceil(359 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))

        # bannerlabel = Label(self, image=self.bannerphoto, anchor=NW, width=1, height=1)
        # bannerlabel.grid(row=6, column=5, columnspan=9, rowspan=4, sticky=N+S+E+W)
        # bannerlabel.grid_propagate(False)
        self.intibanner = Image.open("Home-Banner-INTI.png")
        self.intibanner = ImageTk.PhotoImage(self.intibanner.resize(
            (math.ceil(380 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        ballslabel = Button(self, image=self.intibanner, anchor=NW, width=1, height=1)
        ballslabel.grid(row=7, column=5, columnspan=10,
                        rowspan=12, sticky=N+S+E+W)


        
        

     
        # Buttons


class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(25):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="red", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=16, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=17, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        label = Label(self, text="This is the primary login page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=17,
                   rowspan=2, sticky=N+S+E+W)

        # Buttons
        signinbutton = Button(self, text="SIGN IN", font=(
            'Arial', 18), width=1, height=1, fg='#000000', command=lambda: [messagebox.showinfo("Successful Login", "You can now click on the main page function!")], bg=LIGHTYELLOW)
        signinbutton.grid(row=16, column=6, columnspan=9,
                          rowspan=2, sticky=N+S+E+W)
        ortext = Label(self, text="------OR------", font=('Arial', 18), width=1,
                       height=1, fg='#000000', bg='#FFF5E4')
        ortext.grid(row=18, column=6, columnspan=9,
                    rowspan=2, sticky=N+S+E+W)
        signupbutton = Button(self, text="Not a member yet?\n Click here to sign up",font=(
            'Arial', 18), width=1, height=1, fg='#000000', command=lambda: [
            controller.show_frame(RegistrationPage), controller.show_frameleft(RegistrationPage2), _.revertcontainersize(self, parent)], bg=OTHERPINK)
        signupbutton.grid(row=20, column=6, columnspan=9,
                          rowspan=2, sticky=N+S+E+W)


class LoginPage2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="orange", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)
        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=2, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        self.label = Label(self, text="This is the secondary login page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        self.label.grid(row=1, column=2, columnspan=16,
                        rowspan=2, sticky=N+S+E+W)

class MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(25):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="red", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=16, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=17, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        label = Label(self, text="This is the main page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=17,
                   rowspan=2, sticky=N+S+E+W)
        

        # Buttons
class EmptyRFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LIGHTYELLOW)
        #  bg=LIGHTYELLOW, borderwidth=1, relief="solid")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # for x in range(25):
        #     self.columnconfigure(x, weight=1, uniform='x')
        #     Label(self, height=2, bg="red", borderwidth=1, relief="solid").grid(
        #         row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        # for y in range(25):
        #     self.rowconfigure(y, weight=0, uniform='x')
        #     Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
        #         row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        # class _(Window):
        #     def changecontainersize(self, container):
        #         container.grid(row=2, column=16, rowspan=14,
        #                        columnspan=14, sticky=N+S+E+W)

        #     def revertcontainersize(self, container):
        #         container.grid(row=3, column=17, columnspan=13,
        #                        rowspan=12, sticky=N+S+E+W)

        # sizebutton = Button(
        #     self, text="Big", command=lambda: _.changecontainersize(self, parent))
        # sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        # unsizebutton = Button(
        #     self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        # unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # # Widgets
        # label = Label(self, text="This is an empty page", font=(
        #     'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        # label.grid(row=1, column=2, columnspan=17,
        #            rowspan=2, sticky=N+S+E+W)

# Should only be one main page, but this is just for testing :)
class MainPage2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="light yellow", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def revertcontainersize(self, container):
                container.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
            def changecontainersize(self, container): 
                container.grid(row=2, column=2, rowspan=14,
                               columnspan=28, sticky=N+S+E+W)
            def makeleftcontainerhuge(leftcontainer):
             leftcontainer.grid(row=2, column=2, rowspan=14,
                               columnspan=28, sticky=N+S+E+W)

            def revertcontainersizes(rightcontainer, leftcontainer):
                 rightcontainer.grid(row=3, column=17, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
                 leftcontainer.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
            def keepcontainerlarge(rightcontainer):
                    rightcontainer.grid(row=2, column=2, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)


        # Widgets
        placeholderlabel = Label(self, text="This is the main page\n Still under construction :)", font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        placeholderlabel.grid(row=1, column=12, columnspan=18,
                        rowspan=2, sticky=N+S+E+W)

        # Buttons
        eventlistbutton = Button(self, text="Event List", font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4', command=lambda:[controller.show_frame(EventView), controller.show_frameleft(EventView2),
            _.keepcontainerlarge(parent)])
        eventlistbutton.grid(row=10, column=2, columnspan=4,
                        rowspan=4, sticky=N+S+E+W)
        eventregistrationbutton = Button(self, text="Event\nRegistration", font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        eventregistrationbutton.grid(row=10, column=8, columnspan=4,
                        rowspan=4, sticky=N+S+E+W)
        # TODO label
        todotext = """Here's what we need to do here, in the main page, \n we need to allow participants to access view eventlist \nor go directly to registration. 
        On the other hand, \nfor admins, their main page will have special \nfunctionality like going into the event creation \nor view participants page."""
        todolabel = Label(self, text=todotext, font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        todolabel.grid(row=5, column=14, columnspan=16,
                rowspan=10, sticky=N+S+E+W)


class EventView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                    relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(25):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="red", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=16, rowspan=14,
                            columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=17, columnspan=13,
                            rowspan=12, sticky=N+S+E+W)

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        label = Label(self, text="This is the event view page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=17,
                rowspan=2, sticky=N+S+E+W)

class EventView2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                    relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="light green", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=2, rowspan=14,
                            columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=2, columnspan=13,
                            rowspan=12, sticky=N+S+E+W)

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        label = Label(self, text="This is the secondary event view page\n Still under construction :)", font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=16,
                rowspan=2, sticky=N+S+E+W)
        # TODO label
        todotext = "Here's what we need to do here, \n create widgets that allow participants to view events\n by category, or/and by date, by location, etc.\n We also need to create a widget that \nsends participants to register for events page."
        todolabel = Label(self, text=todotext, font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        todolabel.grid(row=3, column=2, columnspan=16,
                rowspan=10, sticky=N+S+E+W)
        
        

class EventRegistration(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                    relief="solid", cursor="hand2")
        FONTNAME = "Avenir Next"
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(25):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="red", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=16, rowspan=14,
                            columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=17, columnspan=13,
                            rowspan=12, sticky=N+S+E+W)

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)
        #Database functions
       
        #Connect to database
        conn = sqlite3.connect('registration.db')
        #Create cursor
        c = conn.cursor()
        #Create a table
        c.execute("""CREATE TABLE IF NOT EXISTS eventregistration (
            full_name text NOT NULL,
            icpass_number text NOT NULL, 
            phone_number text,
            email text PRIMARY KEY NOT NULL,
            address text
            )""")
        #Send entries to database
        def submit():
            full_nametext = fullnamefield.get()
            icpass_number = icnumberfield.get()
            phone_number = phonenumentry.get()
            email = emailentry.get()
            address = addressentry.get()
            information = (full_nametext, icpass_number, phone_number, email, address)
            try:
                if full_nametext == "" or icpass_number == "" or phone_number == "" or email == "" or address == "":
                    messagebox.showerror("Error", "Please fill in all the fields")
                else:    
                    with conn:
                        c.execute("INSERT INTO eventregistration VALUES (?,?,?,?,?)", information)
                        messagebox.showinfo("Success", "Registration Successful!")
                        fullnamefield.delete(0, END)
                        icnumberfield.delete(0, END)
                        phonenumentry.delete(0, END)
                        emailentry.delete(0, END)
                        addressentry.delete(0, END)
                        controller.show_frame(EventView)
                        controller.show_frameleft(EventView2)
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Email already registered")
    

        def defocus(event):
            event.widget.master.focus_set()

        # Widgets
        label = Label(self, text="This is the event registration page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=17,
                rowspan=2, sticky=N+S+E+W)

        event_list = ["Lorem", "Ipsum", "Dolor"]
        eventdropdown = ttk.Combobox(self, values = event_list, width = 1, state = 'readonly')
        eventdropdown.set("Please select the event you want to register for:",)
        eventdropdown.grid(row = 3, column = 2, columnspan = 17, rowspan = 2, sticky = N+S+E+W)
        eventdropdown.bind('<FocusIn>', defocus)
        separator = ttk.Separator(self, orient=HORIZONTAL)
        separator.grid(row=5, column=3,columnspan=15, pady=5, sticky=EW)
        icpasslabel = Label(self, text="NRIC/\nPassport No.", font=(FONTNAME, 10), bg='#FFF5E4')
        icpasslabel.grid(row=9, column=3, columnspan=2, rowspan=2, sticky=N+S+E+W)
        phonenumberlabel = Label(self, text="Phone\nNumber", font=(FONTNAME, 14), bg='#FFF5E4')
        phonenumberlabel.grid(row=12, column=3, columnspan=2, rowspan=2, sticky=N+S+E+W) 
        emaillabel = Label(self, text="Email", font=(FONTNAME, 14), bg='#FFF5E4')
        emaillabel.grid(row=15, column=3, columnspan=2, rowspan=2, sticky=N+S+E+W) 
        addresslabel = Label(self, text="Address", font=(FONTNAME, 14), bg='#FFF5E4')
        addresslabel.grid(row=18, column=3, columnspan=2, rowspan=2, sticky=N+S+E+W) 

        # radio_1 = ttk.Radiobutton(self, text="Male  ", variable=var, value=0)
        # radio_1.grid(row=9, column=5,rowspan=2, columnspan=2, pady=(0, 10), sticky=NS)

        # radio_1 = ttk.Radiobutton(self, text="Female", variable=var, value=1, command=lambda:print(var.get()))
        # radio_1.grid(row=9, column=7,rowspan=2, columnspan=2, pady=(0, 10), sticky=NS)

        fullnamefield = Entry(self, width=1, bg='#FFFFFF',
                               font=(FONTNAME, 18), justify='center')
        fullnamefield.grid(row=6, column=3, columnspan=15,
                            rowspan=2, sticky=N+S+E+W)
        fullnamefield.insert(0, "Full Name")

        icnumberfield = Entry(self, width=1, bg='#FFFFFF',
                               font=(FONTNAME, 18), justify='center')
        icnumberfield.grid(row=9, column=5, columnspan=13,
                            rowspan=2, sticky=N+S+E+W)
        phonenumentry = Entry(self, width=1, bg='#FFFFFF',
                               font=(FONTNAME, 18), justify='center')
        phonenumentry.grid(row=12, column=5, columnspan=13,
                            rowspan=2, sticky=N+S+E+W)
        emailentry = Entry(self, width=1, bg='#FFFFFF',
                               font=(FONTNAME, 18), justify='center')
        emailentry.grid(row=15, column=5, columnspan=13,
                            rowspan=2, sticky=N+S+E+W)
        addressentry = Entry(self, width=1, bg='#FFFFFF',
                               font=(FONTNAME, 18), justify='center')
        addressentry.grid(row=18, column=5, columnspan=13,
                            rowspan=2, sticky=N+S+E+W)
        #Buttons
        cancelbutton = Button(self, text="Cancel", font=(FONTNAME, 14), bg='White', command=lambda:[controller.show_frame(EventView), controller.show_frameleft(EventView2)])
        cancelbutton.grid(row=21, column=3, columnspan=5, rowspan=2, sticky=N+S+E+W)
        confirmbutton = Button(self, text="Confirm", font=(FONTNAME, 14), bg='White', command=lambda:submit())
        confirmbutton.grid(row=21, column=13, columnspan=5, rowspan=2, sticky=N+S+E+W)





  

class EventRegistration2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                    relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="light blue", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=2, rowspan=14,
                            columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=2, columnspan=13,
                            rowspan=12, sticky=N+S+E+W)

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        label = Label(self, text="This is the secondary event registration page\n Still under construction :)", font=(
            'Segoe Ui Semibold', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=16,
                rowspan=2, sticky=N+S+E+W)
        
        def defocus(event):
            event.widget.master.focus_set()
        
        event_list = ["Please select the event you want to register for:","Lorem", "Ipsum", "Dolor"]
        eventdropdown = ttk.Combobox(self, values = event_list, width = 1, state = 'readonly')
        eventdropdown.current(0)
        eventdropdown.grid(row = 6, column = 2, columnspan = 16, rowspan = 2, sticky = NSEW)
        eventdropdown.bind('<FocusIn>', defocus)
class EventCreation(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                    relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="light blue", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=2, rowspan=14,
                            columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=2, columnspan=13,
                            rowspan=12, sticky=N+S+E+W)

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        label = Label(self, text="This is the event creation page for admins\n Still under construction :)", font=(
            'Segoe Ui Semibold', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=12, columnspan=16,
                rowspan=2, sticky=N+S+E+W)

class ViewParticipants(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="gold", borderwidth=1,
                    relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg="light blue", borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(25):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=ORANGE, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def revertcontainersize(self, container):
                container.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
            def changecontainersize(self, container): 
                container.grid(row=2, column=2, rowspan=14,
                               columnspan=28, sticky=N+S+E+W)
            def makeleftcontainerhuge(leftcontainer):
             leftcontainer.grid(row=2, column=2, rowspan=14,
                               columnspan=28, sticky=N+S+E+W)

            def revertcontainersizes(rightcontainer, leftcontainer):
                 rightcontainer.grid(row=3, column=17, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
                 leftcontainer.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
            def keepcontainerlarge(rightcontainer):
                    rightcontainer.grid(row=2, column=2, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            

        sizebutton = Button(
            self, text="Big", command=lambda: _.changecontainersize(self, parent))
        sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        unsizebutton = Button(
            self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)


        # Widgets
        label = Label(self, text="This is the view participants page for admins\n Still under construction :)", font=(
            'Segoe Ui Semibold', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=12, columnspan=16,
                rowspan=2, sticky=N+S+E+W)

if __name__ == "__main__":
    window = Window()
    window.mainloop()
