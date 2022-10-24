from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image, ImageOps
import math
import sqlite3
from ttkthemes import ThemedTk

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
PINK = "#FFE3E1"
OTHERPINK = "#FA9494"
LIGHTYELLOW = "#FFF5E4"
ORANGE = "#FFAA22"
NICEPURPLE = "#B1B2FF"
NICEBLUE = "#AAC4FF"
LAVENDER = "#D2DAFF"
LIGHTPURPLE = "#EEF1FF"
DARKBLUE = "#3e477c"
NAVYBLUE = "#27364d"
dpi = 96
LOGGEDINAS = "Viewer"
LOGINSTATE = False
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN WINDOW ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        ThemedTk.__init__(self, *args, **kwargs)
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
        self.grid_propagate(False)
        self.title("INTI Interactive System")
        self.resizable(0, 0)
        for x in range(32):
            self.columnconfigure(x, weight=1, uniform='row')
            Label(width=1, bg=NICEPURPLE).grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(18):
            self.rowconfigure(y, weight=1, uniform='row')
            Label(width=1, bg=NICEPURPLE, bd=1).grid(
                row=y, column=0, sticky=N+S+E+W,)
        self.configure(background=LAVENDER)

        def setstateofaccount(self, state):
            self.stateofaccount = state
            return self.stateofaccount

        setstateofaccount(self, LOGGEDINAS)
        print(setstateofaccount(self, LOGGEDINAS))
        # Right Container
        container = Frame(self,
                          bg=LAVENDER,
                          width=1, height=1)
        container.grid_propagate(0)
        container.grid(row=2, column=16,
                       rowspan=14, columnspan=14, sticky=N+S+E+W)
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)
        # Left Container
        container2 = Frame(self, bg=LAVENDER)
        container2.grid_propagate(0)
        container2.grid(row=3, column=2, columnspan=13,
                        rowspan=12, sticky=N+S+E+W)
        container2.grid_rowconfigure(0, weight=0)
        container2.grid_columnconfigure(0, weight=0)

        # Top Container
        # functions to enlarge the left and right frames and revert
        def changecontainersizes(rightcontainer, leftcontainer):
            rightcontainer.grid(row=2, column=16, rowspan=14,
                                columnspan=14, sticky=N+S+E+W)
            leftcontainer.grid(row=2, column=2, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

        def makeleftcontainerhuge(leftcontainer):
            leftcontainer.grid(row=2, column=2, rowspan=14,
                               columnspan=28, sticky=N+S+E+W)

        def revertcontainersizes(rightcontainer, leftcontainer):
            rightcontainer.grid(row=3, column=18, columnspan=12,
                                rowspan=12, sticky=N+S+E+W)
            leftcontainer.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
        FONTFORBUTTONS = "Bahnschrift Semibold"

        def keepcontainerlarge(rightcontainer):
            rightcontainer.grid(row=2, column=16, rowspan=14,
                                columnspan=14, sticky=N+S+E+W)
        
        self.container3 = Frame(self, bg=DARKBLUE)
        self.container3.grid(row=0, column=0, rowspan=2,
                            columnspan=32, sticky=N+S+E+W)
        self.container3.grid_propagate(0)
        self.signupbutton = Button(self.container3, text="Sign Up\n Page", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20, "bold"),
                            borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
                            command=lambda: [
                                self.show_frame(RegistrationPage), 
                                self.show_frameleft(RegistrationPage2),
                                revertcontainersizes(container2, container2), 
                                keepcontainerlarge(container)])
        self.signupbutton.grid(row=0, column=0, rowspan=1, sticky=N+S+E+W)
        self.loginbutton = Button(self.container3, text="Login\nPage", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                            borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
                            command=lambda: [
                                self.show_frame(LoginPage), 
                                self.show_frameleft(LoginPage2),
                                revertcontainersizes(container, container2), 
                                keepcontainerlarge(container)])
        self.loginbutton.grid(row=0, column=1, rowspan=1, sticky=N+S+E+W)
 
        
        #Sign out button 
        self.container4 = Frame(self, bg=NAVYBLUE, width=1, height=1, borderwidth=2, relief="flat", padx=0, pady=0)
        self.container4.grid(row=16, column=0, rowspan=2, columnspan=24,
                            sticky=N+S+E+W)
        self.container4.grid_propagate(0)
        self.signoutbutton = Button(self.container4, text="Sign Out", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                 borderwidth=1, relief="solid", height=3, width=10,
                                 command=lambda: [self.show_frame(LoginPage), self.show_frameleft(LoginPage2), keepcontainerlarge(container), self.signout()]) 
        self.signoutbutton.grid(row=0, column=2, rowspan=1, sticky=N+S+E+W)
        self.studentbutton = Button(self.container4, text="Student\nButton", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                 borderwidth=1, relief="solid", height=3, width=10,
                                 command=lambda: [self.show_loggedin()])
        self.studentbutton.grid(row=0, column=3, rowspan=1, sticky=N+S+E+W)

        self.adminbutton = Button(self.container4, text="Admin\nButton", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                borderwidth=1, relief="solid", height=3, width=10,
                                command=lambda:[self.show_admin(), self.show_loggedin()])
        self.adminbutton.grid(row=0, column=4, rowspan=1, sticky=N+S+E+W)
        self.container5 = Frame(self, bg=NAVYBLUE, width=1, height=1, borderwidth=4, relief="flat",  padx=10, pady=10)
        self.container5.grid(row=2, column=0, rowspan=14, columnspan=2, 
                            sticky=N+S+E+W)
        self.container5.grid_propagate(0)
 
        self.signoutbutton.grid_propagate(0)
        self.studentbutton.grid_propagate(0)
        self.adminbutton.grid_propagate(0)

        self.frames = {}

        for F in (RegistrationPage, LoginPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(RegistrationPage)

        for F in (RegistrationPage2, LoginPage2):
            frame = F(container2, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frameleft(RegistrationPage2)
    def show_container3(self):
        self.container3.grid(row=0, column=0, rowspan=2,
                            columnspan=20, sticky=N+S+E+W)
    def signout(self):
        self.mainpagebutton.grid_forget()
        self.eventlistbutton.grid_forget()
        self.eventregistrationbutton.grid_forget()
        self.eventcreationbutton.grid_forget()
        self.viewparticipantsbutton.grid_forget()
        global LOGGEDINAS
        global LOGINSTATE 
        LOGGEDINAS = "Viewer"
        LOGINSTATE = False
        
        

    def show_loggedin(self):
        self.mainpagebutton.grid(row=0, column=2, rowspan=1, sticky=N+S+E+W)
        self.eventlistbutton.grid(row=0, column=3, rowspan=1, sticky=N+S+E+W)
        self.eventregistrationbutton.grid(row=0, column=4, rowspan=1, sticky=N+S+E+W)
        self.calendarbutton.grid(row=0, column=7, rowspan=1, sticky=N+S+E+W)

    def show_admin(self):
        self.eventcreationbutton.grid(row=0, column=5, rowspan=1, sticky=N+S+E+W)
        self.viewparticipantsbutton.grid(row=0, column=6, rowspan=1, sticky=N+S+E+W)
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
        Frame.__init__(self, parent, bg=LIGHTPURPLE,
                       borderwidth=1, relief="solid")
        for x in range(50):
            Grid.columnconfigure(self, x, weight=1, uniform='row')
            Label(self, height=2, bg=LIGHTPURPLE, borderwidth=1, relief="solid").grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(30):
            Grid.rowconfigure(self, y, weight=1, uniform='row')
            Label(self, width=5, bg=LIGHTPURPLE, borderwidth=1, relief="solid").grid(
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
            password text NOT NULL,
            role text NOT NULL
        )""")
        # c.execute ("DROP TABLE registration")
        # possibly, we could make two functions, one to validate input and another to actually send the data to the database, instead of checking validity itself in checkfields()

        def checkfields():
            # c.execute("DROP TABLE registration")
            firstnametext = firstnamefield.get()
            lastnametext = lastnamefield.get()
            emailtext = emailfield.get()
            passwordtext = passwordfield.get()
            confirmpasstext = confirmpasswordfield.get()
            try:
                emailending = emailfield.get().split("@")[1]
                if emailending == "student.newinti.edu.my":
                    role = "student"
                    validemail = True
                elif emailending == "newinti.edu.my":
                    role = "admin"
                    validemail = True
                else:
                    validemail = False
                    role = "invalid"
                if (FIRSTNAME in firstnametext) or (LASTNAME in lastnametext) or (EMAILTEXT in emailtext) or (PASSWORDTEXT in passwordtext) or (CONFPASSTEXT in confirmpasstext):
                    messagebox.showerror("Error", "Please fill in all fields.")
                elif passwordtext != confirmpasstext:
                    messagebox.showerror("Error", "Passwords do not match.")
                elif validemail == False:
                    messagebox.showerror(
                        "Error", "Please enter a valid email.")
                else:
                    with conn:
                        information = (firstnametext, lastnametext,
                           emailtext, passwordtext, role)
                        c.execute(
                            """INSERT INTO registration VALUES(?, ?, ?, ?, ?)""", information)
                        messagebox.showinfo(
                            "Success", "You have successfully registered.")
                        controller.show_frame(LoginPage)
                        controller.show_frameleft(LoginPage2)
                        cleareveryentry()
                        _.changecontainersize(self, parent)
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Email already in use.")
            except IndexError:
                emailwarning.configure(text="You have not entered an email")
                messagebox.showerror("Error", "Please enter a valid email.")            

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=16, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=17, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)
        # sizebutton = Button(
        #     self, text="Big", command=lambda: _.changecontainersize(self, parent))
        # sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        # unsizebutton = Button(
        #     self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        # unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

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
        emailwarning = Label(self, text="Please enter a valid email address.", font=(
            'Arial', 10), width=1, height=1, fg='#000000', bg='#FFF5E4')

        def clearemailfield():
            emailfield.configure(fg="black")
            if emailfield.get() == EMAILTEXT:
                emailfield.delete(0, END)
            try:
                emailending = emailfield.get().split("@")[1]
                if emailending in ["student.newinti.edu.my", "newinti.edu.my"]:
                    emailwarning.configure(fg="black")
                else:
                    emailwarning.configure(
                        text="Email entered is not with INTI or incomplete")
            except IndexError:
                emailwarning.configure(text="You have not entered an email")

        def showwarninglabelaboveentry():
            # configure emailwarning to show and become red when invalid email
            emailwarning.grid(row=6, column=12, columnspan=8,
                              rowspan=2, sticky=N+S+E+W, padx=5, pady=10)
            emailwarning.configure(
                text="Please enter a valid email.", fg="red")

        def repopulateemailfield():
            try:
                emailending = emailfield.get().split("@")[1]
                if emailending not in ["student.newinti.edu.my", "newinti.edu.my"]:
                    if emailfield == "":
                        emailfield.insert(0, EMAILTEXT)
                    emailfield.configure(fg="red")
                    showwarninglabelaboveentry()
                else:
                    emailfield.configure(fg="black")
                    emailwarning.grid_forget()
            except IndexError:
                if emailfield.get() == EMAILTEXT or emailfield.get() == "":
                    emailfield.delete(0, END)
                    emailfield.insert(0, EMAILTEXT)
                emailfield.configure(fg="red")
                showwarninglabelaboveentry()
        passwordwarning = Label(self, text="Please enter a valid password.", font=(
            'Arial', 10), width=1, height=1, fg='#000000', bg='#FFF5E4')

        def clearpasswordfield():
            passwordfield.configure(fg="black")
            passwordfield.configure(show="*")
            if passwordfield.get() == PASSWORDTEXT:
                passwordfield.delete(0, END)
            try:
                passwordcontents = passwordfield.get()
            except:
                pass

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

        def cleareveryentry():
            firstnamefield.delete(0, END)
            lastnamefield.delete(0, END)
            emailfield.delete(0, END)
            passwordfield.delete(0, END)
            confirmpasswordfield.delete(0, END)
            firstnamefield.insert(0, FIRSTNAME)
            lastnamefield.insert(0, LASTNAME)
            emailfield.insert(0, EMAILTEXT)
            passwordfield.insert(0, PASSWORDTEXT)
            confirmpasswordfield.insert(0, CONFPASSTEXT)
            passwordfield.configure(show="")
            confirmpasswordfield.configure(show="")
            passwordfield.configure(fg="black")
            confirmpasswordfield.configure(fg="black")

        # Labels
        enterdetailslabel = Label(self, text="Please enter your details as shown in the entries.", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        enterdetailslabel.grid(row=0, column=1,
                               rowspan=3, columnspan=20, sticky=N+S+E+W)

        # Entries
        firstnamefield = Entry(self, width=1, bg='#FFFFFF',
                               font=(FONTNAME, 18), justify='center')
        firstnamefield.grid(row=4, column=2,
                            rowspan=2, columnspan=8, sticky=N+S+E+W)
        firstnamefield.insert(0, FIRSTNAME)

        lastnamefield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        lastnamefield.grid(row=4, column=12,
                           rowspan=2, columnspan=8, sticky=N+S+E+W)
        lastnamefield.insert(0, LASTNAME)

        emailfield = Entry(self, width=1, bg='#FFFFFF',
                           font=(FONTNAME, 18), justify='center')
        emailfield.grid(row=8, column=2,
                        rowspan=2, columnspan=18, sticky=N+S+E+W)
        emailfield.insert(0, EMAILTEXT)

        passwordfield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        passwordfield.grid(row=12, column=2,
                           rowspan=2, columnspan=18, sticky=N+S+E+W)
        passwordfield.insert(0, PASSWORDTEXT)

        confirmpasswordfield = Entry(
            self, width=1, bg='#FFFFFF', font=(FONTNAME, 18), justify='center')
        confirmpasswordfield.grid(row=16, column=2,
                                  rowspan=2, columnspan=18, sticky=N+S+E+W)
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
        signupbutton = Button(self, text="SIGN UP", takefocus=1,font=(
            'Arial', 18), width=1, height=1, fg='#000000', command=lambda: checkfields(), bg=LIGHTYELLOW)
        signupbutton.grid(row=19, column=6, columnspan=10,
                          rowspan=2, sticky=N+S+E+W)

        loginbutton = Button(self, text="Already have an account?\nClick here to sign in.", font=('Atkinson Hyperlegible', 18), width=1,
                             height=1, fg='#000000', command=lambda: [controller.show_frame(LoginPage),
                                                                      controller.show_frameleft(
                                                                          LoginPage2),
                                                                      _.changecontainersize(
                                                                          self, parent),
                                                                      cleareveryentry()], bg=OTHERPINK)
        loginbutton.grid(row=22, column=6, columnspan=10,
                         rowspan=2, sticky=N+S+E+W)


class RegistrationPage2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER, borderwidth=1,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=LAVENDER, borderwidth=0, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(30):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=LAVENDER, bd=1, borderwidth=0, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=2, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)

        # sizebutton = Button(
        #     self, text="Big", command=lambda: _.changecontainersize(self, parent))
        # sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        # unsizebutton = Button(
        #     self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        # unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        label = ttk.Label(self, text="This is the registration page on left frame\nCome back later, still under construction!", font=(
            'Avenir Next', 20),justify='center', background=ORANGE,)
        label.grid(row=1, column=2, columnspan=17,
                   rowspan=2, sticky=N+S+E+W)
        label.grid_propagate(0)
        self.s = ttk.Style()
        self.entry = ttk.Entry(self, width=1, font=("Comic Sans Ms", 18), justify='center')
        self.entry.grid(row=3, column=2, columnspan=17,
                        rowspan=2, sticky=N+S+E+W)
        self.s.configure('TButton', font=('Comic Sans MS', 25), foreground= "RED")
        self.button = ttk.Button(self, text="Go to the start page", style='my.TButton',
                            command=lambda: print('test'))
        self.button.grid(row=6, column=2, columnspan=17,
                    rowspan=2, sticky=N+S+E+W)
        self.radiobuttons = ttk.Radiobutton(self, text="Option 1", value=1)
        self.radiobuttons.grid(row=9, column=2, columnspan=17,
                    rowspan=2, sticky=N+S+E+W)
    

        # Buttons
class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER, borderwidth=0,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=LAVENDER, borderwidth=0, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(30):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=LAVENDER, bd=1, borderwidth=0, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
            def changecontainersize(self, container):
                container.grid(row=2, column=16, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=18, columnspan=12,
                               rowspan=12, sticky=N+S+E+W)
        
        # Database Functions for Logging in and setting loginstate to student or teacher
        # Sqlite3 commands to fetch registered emails from database and assigning roles based on email ending.
        # If email is not found in database, it will return an error message.
        # If email is found in database, it will return a success message.

        conn = sqlite3.connect('registration.db')
        c = conn.cursor()

        def checkcredentials():
            global LOGGEDINAS
            global LOGINSTATE
            if LOGGEDINAS != "Admin" and LOGGEDINAS != "Student" and LOGINSTATE != True:
                with conn:
                    c.execute("SELECT * FROM registration WHERE email = ? AND password = ?",
                              (emailfield.get(), passwordfield.get()))
                    for row in c.fetchall():
                        name = row[0]
                        email = row[2]
                        password = row[3]
                        role = row[4]
                        print("Your name is: ", name)
                        print("Email is: ", email)
                        print("Password is :", password)
                        print("Your role is : ", role)
                        print(row)
                    try:
                        if role == "student":
                            messagebox.showinfo(
                                "Login Successful", "Welcome Student!")
                            LOGGEDINAS = "Student"
                            LOGINSTATE = True
                            _.show_loggedin(controller)
                        elif role == "admin":
                            messagebox.showinfo(
                                "Login Successful", "Welcome Admin!")
                            LOGGEDINAS = "Admin"
                            LOGINSTATE = True
                            _.show_loggedin(controller)
                            _.show_admin(controller)
                        else:
                            messagebox.showerror(
                                "Login Failed", "Invalid Email or Password")
                    except UnboundLocalError:
                        messagebox.showerror(
                            "Login Failed", "Invalid Email or Password")
            else:
                roles = LOGGEDINAS
                messagebox.showerror(
                    "Login Failed", f"You are already logged in as {roles}!")

        emailwarning = Label(self, text="Please enter a valid email address.", font=(
            'Arial', 10), width=1, height=1, fg='#000000', bg='#FFF5E4')

        def signinbuttonpressed():
            checkcredentials()

        def clearemailfield():
            emailfield.configure(fg="black")
            if emailfield.get() == EMAILTEXT:
                emailfield.delete(0, END)
            try:
                emailending = emailfield.get().split("@")[1]
                if emailending in ["student.newinti.edu.my", "newinti.edu.my"]:
                    emailwarning.configure(fg="black")
                else:
                    emailwarning.configure(
                        text="Email entered is not with INTI or incomplete")
            except IndexError:
                emailwarning.configure(text="You have not entered an email")

        def showwarninglabelaboveentry():
            # configure emailwarning to show and become red when invalid email
            emailwarning.grid(row=6, column=12, columnspan=8,
                              rowspan=2, sticky=N+S+E+W)
            emailwarning.configure(
                text="Please enter a valid email.", fg="red")

        def repopulateemailfield():
            try:
                emailending = emailfield.get().split("@")[1]
                if emailending not in ["student.newinti.edu.my", "newinti.edu.my"]:
                    if emailfield == "":
                        emailfield.insert(0, EMAILTEXT)
                    emailfield.configure(fg="red")
                    showwarninglabelaboveentry()
                else:
                    emailfield.configure(fg="black")
                    emailwarning.grid_forget()
            except IndexError:
                if emailfield.get() == EMAILTEXT or emailfield.get() == "":
                    emailfield.delete(0, END)
                    emailfield.insert(0, EMAILTEXT)
                emailfield.configure(fg="red")
                showwarninglabelaboveentry()

        def clearpasswordfield():
            passwordfield.configure(fg="black")
            passwordfield.configure(show="*")
            if passwordfield.get() == PASSWORDTEXT:
                passwordfield.delete(0, END)
            try:
                passwordcontents = passwordfield.get()
            except:
                pass

        def repopulatepasswordfield():
            if passwordfield.get() == "":
                passwordfield.insert(0, PASSWORDTEXT)
                passwordfield.configure(show="")
                passwordfield.configure(fg="red")
            else:
                passwordfield.configure(show="*")

        # Widgets
        # label = Label(self, text="This is the primary login page", font=(
        #     'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        # label.grid(row=1, column=2, columnspan=18,
        #            rowspan=2, sticky=N+S+E+W)
        EMAILTEXT = "Please enter your registered email address"
        PASSWORDTEXT = "Please enter your password"
        FONTNAME = "Avenir Next"
        # Buttons
        emailfield = Entry(self, width=1, bg='#FFFFFF',
                           font=(FONTNAME, 18), justify='center')
        emailfield.grid(row=8, column=2, columnspan=18,
                        rowspan=2, sticky=N+S+E+W)
        emailfield.insert(0, EMAILTEXT)
        passwordfield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        passwordfield.grid(row=11, column=2, columnspan=18,
                           rowspan=2, sticky=N+S+E+W)
        passwordfield.insert(0, PASSWORDTEXT)
        emailfield.bind("<FocusIn>", lambda a: clearemailfield())
        emailfield.bind("<FocusOut>", lambda a: repopulateemailfield())
        passwordfield.bind("<FocusIn>", lambda a: clearpasswordfield())
        passwordfield.bind("<FocusOut>", lambda a: repopulatepasswordfield())

        self.intibanner = Image.open("Home-Banner-INTI.png")
        self.intibanner = ImageTk.PhotoImage(self.intibanner.resize(
            (math.ceil(720 * dpi / 96), math.ceil(240 * dpi / 96)), Image.Resampling.LANCZOS))
        logolabel = Button(self, image=self.intibanner,
                           anchor=CENTER, width=1, height=1)
        logolabel.grid(row=1, column=2, columnspan=18,
                       rowspan=5, sticky=N+S+E+W)

        signinbutton = Button(self, text="SIGN IN", font=(
            'Arial', 18), width=1, height=1, bg=LIGHTYELLOW, fg='#000000', command=lambda: signinbuttonpressed())
        signinbutton.grid(row=16, column=6, columnspan=9,
                          rowspan=2, sticky=N+S+E+W)
        ortext = Label(self, text="------OR------", font=('Arial', 18), width=1,
                       height=1, fg='#000000', bg='#FFF5E4')
        ortext.grid(row=18, column=6, columnspan=9,
                    rowspan=2, sticky=N+S+E+W)

        signupbutton = Button(self, text="Not a member yet?\n Click here to sign up", font=(
            'Arial', 18), width=1, height=1, fg='#000000', command=lambda: [
            controller.show_frame(RegistrationPage), controller.show_frameleft(RegistrationPage2), _.changecontainersize(self, parent)], bg=OTHERPINK)
        signupbutton.grid(row=20, column=6, columnspan=9,
                          rowspan=2, sticky=N+S+E+W)


        def changedtologout():
            global LOGGEDINAS
            global LOGINSTATE
            LOGGEDINAS = "Viewer"
            LOGINSTATE = False

        def checkstate():
            global LOGGEDINAS
            print(LOGGEDINAS)
        signoutbutton = Button(self, text="SIGN OUT", font=(
            'Arial', 18), width=1, height=1, bg=LIGHTYELLOW, fg='#000000', command=lambda: changedtologout())
        signoutbutton.grid(row=24, column=6, columnspan=9,
                           rowspan=2, sticky=N+S+E+W)
        checkstatebutton = Button(
            self, text="Check state", command=lambda: checkstate())
        checkstatebutton.grid(row=22, column=6, columnspan=9,
                              rowspan=2, sticky=N+S+E+W)


class LoginPage2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER, borderwidth=1,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=LAVENDER, borderwidth=0, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(30):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=LAVENDER, bd=1, borderwidth=0, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        class _(Window):
            def changecontainersize(self, container):
                container.grid(row=2, column=2, rowspan=14,
                               columnspan=14, sticky=N+S+E+W)

            def revertcontainersize(self, container):
                container.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)

        # sizebutton = Button(
        #     self, text="Big", command=lambda: _.changecontainersize(self, parent))
        # sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        # unsizebutton = Button(
        #     self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        # unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        self.label = Label(self, text="This is the secondary login page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        self.label.grid(row=1, column=2, columnspan=16,
                        rowspan=2, sticky=N+S+E+W)
        


if __name__ == "__main__":
    window = Window(theme='Ubuntu')
    print(window.get_themes())

    window.mainloop()