
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
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
DARKBLUE = "#3e477c"
NAVYBLUE = "#27364d"
dpi = 96
LOGGEDINAS = "Viewer"
LOGINSTATE = False
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN WINDOW ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


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

        self.mainpagebutton = Button(self.container3, text="Main\nPage", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                     borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
                                     command=lambda: [self.show_frame(MainPage), self.show_frameleft(MainPage2), makeleftcontainerhuge(container2)])
        self.eventlistbutton = Button(self.container3, text="Event\nList", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                      borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
                                      command=lambda: [
            self.show_frame(EventView),
            self.show_frameleft(EventView2),
            revertcontainersizes(container, container2),
            changecontainersizes(container, container2)])
        self.eventregistrationbutton = Button(self.container3, text="Event\nRegistration", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                              borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
                                              command=lambda: [
            self.show_frame(EventRegistration),
            self.show_frameleft(EventRegistration2),
            revertcontainersizes(container, container2),
            changecontainersizes(container, container2)])
        self.eventcreationbutton = Button(self.container3, text="Event\nCreation\n(ADMIN)", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                          borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
                                          command=lambda: [
            self.show_frame(EventCreation),
            self.show_frameleft(EmptyRFrame),
            makeleftcontainerhuge(container2)])
        self.viewparticipantsbutton = Button(self.container3, text="View\nParticipants\n(ADMIN)", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                             borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
                                             command=lambda: [
            self.show_frame(ViewParticipants),
            self.show_frameleft(EmptyRFrame),
            makeleftcontainerhuge(container2)])
        self.feedbackbutton = Button(self.container3, text="Feedback\nForm", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                            borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
                            command=lambda: [
                                self.show_frame(FeedbackForm), 
                                self.show_frameleft(EmptyRFrame),
                                makeleftcontainerhuge(container2)])
        self.calendarbutton = Button(self.container3, text="Calendar", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                     borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
                                     command=lambda: [
            self.show_frame(Calendar),
            self.show_frameleft(EmptyRFrame),
            makeleftcontainerhuge(container2)])

        # Sign out button
        self.container4 = Frame(
            self, bg=NAVYBLUE, width=1, height=1, borderwidth=2, relief="flat", padx=0, pady=0)
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
                                  command=lambda: [self.show_admin(), self.show_loggedin()])
        self.adminbutton.grid(row=0, column=4, rowspan=1, sticky=N+S+E+W)
        self.container5 = Frame(self, bg=NAVYBLUE, width=1, height=1,
                                borderwidth=4, relief="flat",  padx=10, pady=10)
        self.container5.grid(row=2, column=0, rowspan=14, columnspan=2,
                             sticky=N+S+E+W)
        self.container5.grid_propagate(0)

        self.signoutbutton.grid_propagate(0)
        self.studentbutton.grid_propagate(0)
        self.adminbutton.grid_propagate(0)

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

        for F in (RegistrationPage, LoginPage, MainPage, EmptyRFrame, EventView, EventRegistration):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(RegistrationPage)

        for F in (RegistrationPage2, LoginPage2, MainPage2, EventView2, EventRegistration2, EventCreation, ViewParticipants, Calendar, FeedbackForm):
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
        self.feedbackbutton.grid_forget()
        self.calendarbutton.grid_forget()
        global LOGGEDINAS
        global LOGINSTATE
        LOGGEDINAS = "Viewer"
        LOGINSTATE = False

    def show_loggedin(self):
        self.mainpagebutton.grid(row=0, column=2, rowspan=1, sticky=N+S+E+W)
        self.eventlistbutton.grid(row=0, column=3, rowspan=1, sticky=N+S+E+W)
        self.eventregistrationbutton.grid(row=0, column=4, rowspan=1, sticky=N+S+E+W)
        self.calendarbutton.grid(row=0, column=7, rowspan=1, sticky=N+S+E+W)
        self.feedbackbutton.grid(row=0, column=8, rowspan=1, sticky=N+S+E+W)

    def show_admin(self):
        self.eventcreationbutton.grid(
            row=0, column=5, rowspan=1, sticky=N+S+E+W)
        self.viewparticipantsbutton.grid(
            row=0, column=6, rowspan=1, sticky=N+S+E+W)

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
        signupbutton = Button(self, text="SIGN UP", takefocus=1, font=(
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
        label = Label(self, text="This is the registration page on left frame\nCome back later, still under construction!", font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=17,
                   rowspan=2, sticky=N+S+E+W)

        self.intibanner = Image.open("assets\Home-Banner-INTI.png")
        self.intibanner = ImageTk.PhotoImage(self.intibanner.resize(
            (math.ceil(359 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        logolabel = Button(self, image=self.intibanner,
                           anchor=CENTER, width=1, height=1)
        logolabel.grid(row=4, column=5, columnspan=11,
                       rowspan=5, sticky=N+S+E+W)
        self.titleart = Image.open("assets\DR7j7r0.png")
        self.titleart = ImageTk.PhotoImage(self.titleart.resize(
            (math.ceil(720 * dpi / 96), math.ceil(240 * dpi / 96)), Image.Resampling.LANCZOS))
        titleartlabel = Button(self, image=self.titleart,
                               anchor=CENTER, width=1, height=1)
        titleartlabel.grid(row=9, column=0, columnspan=21,
                           rowspan=8, sticky=N+S+E+W)

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

        self.intibanner = Image.open("assets\Home-Banner-INTI.png")
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


class MainPage(Frame):
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

        # Widgets
        label = Label(self, text="This is the main page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=17,
                   rowspan=2, sticky=N+S+E+W)

        # Buttons


class EmptyRFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LIGHTYELLOW)
        #  bg=LIGHTYELLOW, borderwidth=0, relief="solid")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # for x in range(30):
        #     self.columnconfigure(x, weight=1, uniform='x')
        #     Label(self, height=2, bg="red", borderwidth=0, relief="solid").grid(
        #         row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        # for y in range(30):
        #     self.rowconfigure(y, weight=0, uniform='x')
        #     Label(self, width=5, bg=LAVENDER, bd=1, borderwidth=0, relief="solid").grid(
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
                                    columnspan=28, sticky=N+S+E+W)

        # sizebutton = Button(
        #     self, text="Big", command=lambda: _.changecontainersize(self, parent))
        # sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        # unsizebutton = Button(
        #     self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        # unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Picture
        self.originalimage = Image.open("assets\Home-Banner-INTI.png")
        self.resultingimage = ImageTk.PhotoImage(self.originalimage.resize(
            (math.ceil(600 * dpi / 96), math.ceil(200 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.resultingimage,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=1, column=2, columnspan=16,
                        rowspan=4, sticky=N+S+E+W)

        self.notificationimage = Image.open(r"assets\Notification.png")
        self.resultimage = ImageTk.PhotoImage(self.notificationimage.resize(
            (math.ceil(120 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.resultimage,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=11, column=20, columnspan=5,
                        rowspan=4, sticky=N+S+E+W)

        self.registrationimage = Image.open(r"assets\registration form.png")
        self.outcomeimage = ImageTk.PhotoImage(self.registrationimage.resize(
            (math.ceil(120 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.outcomeimage,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=11, column=28, columnspan=5,
                        rowspan=4, sticky=N+S+E+W)

        self.calendarimage = Image.open("assets\Calendar.png")
        self.outcomingimage = ImageTk.PhotoImage(self.calendarimage.resize(
            (math.ceil(120 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.outcomingimage,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=11, column=36, columnspan=5,
                        rowspan=4, sticky=N+S+E+W)

        # Label
        todotext = """Feedback"""
        todolabel = Label(self, text=todotext, font=(
            'Lucida Calligraphy', 20), justify=('left'), width=1, height=1, fg='#000000', bg='#FFF5E4')
        todolabel.grid(row=6, column=2, columnspan=16,
                       rowspan=1, sticky=N+S+E+W)

        todotext = """Upcoming Events"""
        todolabel = Label(self, text=todotext, font=(
            'Lucida Calligraphy', 20), justify=('left'), width=1, height=1, fg='#000000', bg='#FFF5E4')
        todolabel.grid(row=13, column=2, columnspan=16,
                       rowspan=1, sticky=N+S+E+W)

        # TODO label
        todotext = """If you want to get more enquiries,you can ask INTI IT management through\nphone number: + 04-6355793 or email: iicpitmanagement@newinti.edu.my"""
        todolabel = Label(self, text=todotext, font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        todolabel.grid(row=1, column=20, columnspan=21,
                       rowspan=2, sticky=N+S+E+W)

        # Widgets
        placeholderlabel = Label(self, text="Welcome To INTI Announcement website.\nAs a member of IT staffs, we hear a lot of complaints\nand dissatisfaction from our students that the announcements\nmiss out or overlooked the date and duration of event.\nTo prevent this situation happen again\nINTI decided to create\na special announcement website for students.\n This will be a golden opportunity\n for you all to enjoy this welfare.", font=(
            'Arial', 16), justify=('center'), width=1, height=1, fg='#000000', bg='#FFF5E4')
        placeholderlabel.grid(row=4, column=20, columnspan=21,
                              rowspan=6, sticky=N+S+E+W)

        # Buttons
        self.feedbackimage = Image.open(r"assets\feedbackimage.png")
        self.feedbackimage = ImageTk.PhotoImage(self.feedbackimage.resize(
            (math.ceil(258 * dpi / 96), math.ceil(172 * dpi / 96)), Image.Resampling.LANCZOS)),
        feedbackbutton = Button(self, image=self.feedbackimage, width=1, height=1, fg='#000000', bg='#FFF5E4', command=lambda: [
                                controller.show_frame(EmptyRFrame), controller.show_frameleft(FeedbackForm), _.keepcontainerlarge(parent)])
        feedbackbutton.grid(row=8, column=2, columnspan=16,
                            rowspan=4, sticky=N+S+E+W)
        imagelabel = Label(self, image=self.feedbackimage,
                           anchor=CENTER, width=1, height=1)

        eventnamebutton = Button(self, text="Event Name", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [controller.show_frame(EventView), controller.show_frameleft(EventView2),
        _.keepcontainerlarge(parent)])
        eventnamebutton.grid(row=15, column=2, columnspan=16,
                             rowspan=1, sticky=N+S+E+W)

        eventsnamebutton = Button(self, text="Event Name", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4', command=lambda: [controller.show_frame(EventView), controller.show_frameleft(EventView2),
        _.keepcontainerlarge(parent)])
        eventsnamebutton.grid(row=16, column=2, columnspan=16,
                              rowspan=1, sticky=N+S+E+W)

        aneventnamebutton = Button(self, text="Event Name", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4', command=lambda: [controller.show_frame(EventView), controller.show_frameleft(EventView2),
        _.keepcontainerlarge(parent)])
        aneventnamebutton.grid(row=17, column=2, columnspan=16,
                               rowspan=1, sticky=N+S+E+W)

        theeventnamebutton = Button(self, text="Event Name", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4', command=lambda: [controller.show_frame(EventView), controller.show_frameleft(EventView2),
        _.keepcontainerlarge(parent)])
        theeventnamebutton.grid(row=18, column=2, columnspan=16,
                                rowspan=1, sticky=N+S+E+W)

        eventlistbutton = Button(self, text="Event List", font=(
        'Lucida Calligraphy', 16), width=1, height=1, fg='#000000', bg='#FFF5E4', command=lambda: [controller.show_frame(EventView), controller.show_frameleft(EventView2),
        _.keepcontainerlarge(parent)])
        eventlistbutton.grid(row=16, column=20, columnspan=5,
                             rowspan=3, sticky=N+S+E+W)

        eventregistrationbutton = Button(self, text="Event\nRegistration", font=(
        'Lucida Calligraphy', 16), width=1, height=1, fg='#000000', bg='#FFF5E4',  command=lambda:
        [controller.show_frame(EventRegistration), controller.show_frameleft(EventRegistration2),
            _.keepcontainerlarge(parent)])
        eventregistrationbutton.grid(row=16, column=28, columnspan=5,
                                     rowspan=3, sticky=N+S+E+W)

        calendarbutton = Button(self, text="Calendar", font=(
            'Lucida Calligraphy', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        calendarbutton.grid(row=16, column=36, columnspan=5,
                            rowspan=3, sticky=N+S+E+W)

        self.logoutimage = Image.open("assets\logoutbutton.png")
        self.logoutimage = ImageTk.PhotoImage(self.logoutimage.resize(
            (math.ceil(38 * dpi / 96), math.ceil(38 * dpi / 96)), Image.Resampling.LANCZOS)),
        logoutbutton = Button(self,image=self.logoutimage , width=1, height=1, fg='#000000', bg='#FFF5E4',command=lambda:
            [controller.show_frame(LoginPage), controller.show_frameleft(LoginPage2),
            _.revertcontainersizes(self, parent)])
        logoutbutton.grid(row=0, column=42, columnspan=1, rowspan=1, sticky=N+S+E+W)
        imagelabel = Label(self, image=self.logoutimage, anchor=CENTER, width=1, height=1)


class EventView(Frame):
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

        # Widgets
        label = Label(self, text="This is the event view page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=17,
                   rowspan=2, sticky=N+S+E+W)


class EventView2(Frame):
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
        label = Label(self, text="This is the secondary event view page\n Still under construction :)", font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=3, columnspan=16,
                   rowspan=2, sticky=N+S+E+W)
        # TODO label
        todotext = "Here's what we need to do here, \n create widgets that allow participants to view events\n by category, or/and by date, by location, etc.\n We also need to create a widget that \nsends participants to register for events page."
        todolabel = Label(self, text=todotext, font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        todolabel.grid(row=3, column=3, columnspan=16,
                       rowspan=10, sticky=N+S+E+W)


class EventRegistration(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER, borderwidth=1,
                       relief="solid", cursor="hand2")
        FONTNAME = "Avenir Next"
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
        # Database functions

        # Connect to database
        conn = sqlite3.connect('registration.db')
        # Create cursor
        c = conn.cursor()
        # Create a table
        c.execute("""CREATE TABLE IF NOT EXISTS eventregistration (
            full_name text NOT NULL,
            icpass_number text NOT NULL, 
            phone_number text,
            email text PRIMARY KEY NOT NULL,
            address text
            )""")
        # Send entries to database

        def submit():
            full_nametext = fullnamefield.get()
            icpass_number = icnumberfield.get()
            phone_number = phonenumentry.get()
            email = emailentry.get()
            address = addressentry.get()
            information = (full_nametext, icpass_number,
                           phone_number, email, address)
            try:
                if full_nametext == "" or icpass_number == "" or phone_number == "" or email == "" or address == "":
                    messagebox.showerror(
                        "Error", "Please fill in all the fields")
                else:
                    with conn:
                        c.execute(
                            "INSERT INTO eventregistration VALUES (?,?,?,?,?)", information)
                        messagebox.showinfo(
                            "Success", "Registration Successful!")
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
        label.grid(row=1, column=2, columnspan=18,
                   rowspan=2, sticky=N+S+E+W)

        event_list = ["Lorem", "Ipsum", "Dolor"]
        eventdropdown = ttk.Combobox(
            self, values=event_list, width=1, state='readonly')
        eventdropdown.set("Please select the event you want to register for:",)
        eventdropdown.grid(row=3, column=2, columnspan=18,
                           rowspan=2, sticky=N+S+E+W)
        eventdropdown.bind('<FocusIn>', defocus)
        separator = ttk.Separator(self, orient=HORIZONTAL)
        separator.grid(row=5, column=3, columnspan=16, pady=5, sticky=EW)
        icpasslabel = Label(self, text="NRIC/\nPassport No.",
                            font=(FONTNAME, 10), bg='#FFF5E4')
        icpasslabel.grid(row=9, column=3, columnspan=2,
                         rowspan=2, sticky=N+S+E+W)
        phonenumberlabel = Label(
            self, text="Phone\nNumber", font=(FONTNAME, 14), bg='#FFF5E4')
        phonenumberlabel.grid(
            row=12, column=3, columnspan=2, rowspan=2, sticky=N+S+E+W)
        emaillabel = Label(self, text="Email", font=(
            FONTNAME, 14), bg='#FFF5E4')
        emaillabel.grid(row=15, column=3, columnspan=2,
                        rowspan=2, sticky=N+S+E+W)
        addresslabel = Label(self, text="Address",
                             font=(FONTNAME, 14), bg='#FFF5E4')
        addresslabel.grid(row=18, column=3, columnspan=2,
                          rowspan=2, sticky=N+S+E+W)

        # radio_1 = ttk.Radiobutton(self, text="Male  ", variable=var, value=0)
        # radio_1.grid(row=9, column=5,rowspan=2, columnspan=2, pady=(0, 10), sticky=NS)

        # radio_1 = ttk.Radiobutton(self, text="Female", variable=var, value=1, command=lambda:print(var.get()))
        # radio_1.grid(row=9, column=7,rowspan=2, columnspan=2, pady=(0, 10), sticky=NS)

        fullnamefield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        fullnamefield.grid(row=6, column=3, columnspan=16,
                           rowspan=2, sticky=N+S+E+W)
        fullnamefield.insert(0, "Full Name")

        icnumberfield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        icnumberfield.grid(row=9, column=5, columnspan=14,
                           rowspan=2, sticky=N+S+E+W)
        phonenumentry = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        phonenumentry.grid(row=12, column=5, columnspan=14,
                           rowspan=2, sticky=N+S+E+W)
        emailentry = Entry(self, width=1, bg='#FFFFFF',
                           font=(FONTNAME, 18), justify='center')
        emailentry.grid(row=15, column=5, columnspan=14,
                        rowspan=2, sticky=N+S+E+W)
        addressentry = Entry(self, width=1, bg='#FFFFFF',
                             font=(FONTNAME, 18), justify='center')
        addressentry.grid(row=18, column=5, columnspan=14,
                          rowspan=2, sticky=N+S+E+W)
        # Buttons
        cancelbutton = Button(self, text="Cancel", font=(FONTNAME, 14), bg='White', command=lambda: [
                              controller.show_frame(EventView), controller.show_frameleft(EventView2)])
        cancelbutton.grid(row=21, column=3, columnspan=6,
                          rowspan=2, sticky=N+S+E+W)
        confirmbutton = Button(self, text="Confirm", font=(
            FONTNAME, 14), bg='White', command=lambda: submit())
        confirmbutton.grid(row=21, column=13, columnspan=6,
                           rowspan=2, sticky=N+S+E+W)


class EventRegistration2(Frame):
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
        label = Label(self, text="This is the secondary event registration page\n Still under construction :)", font=(
            'Segoe Ui Semibold', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=3, columnspan=16,
                   rowspan=2, sticky=N+S+E+W)

        def defocus(event):
            event.widget.master.focus_set()

        event_list = [
            "Please select the event you want to register for:", "Lorem", "Ipsum", "Dolor"]
        eventdropdown = ttk.Combobox(
            self, values=event_list, width=1, state='readonly')
        eventdropdown.current(0)
        eventdropdown.grid(row=6, column=3, columnspan=16,
                           rowspan=2, sticky=NSEW)
        eventdropdown.bind('<FocusIn>', defocus)


class EventCreation(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER, borderwidth=1,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
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
        label = Label(self, text="This is the event creation page for admins\n Still under construction :)", font=(
            'Segoe Ui Semibold', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=12, columnspan=18,
                   rowspan=2, sticky=N+S+E+W)


class ViewParticipants(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER, borderwidth=1,
                       relief="solid", cursor="hand2")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(50):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(28):
            self.rowconfigure(y, weight=0, uniform='x')
            Label(self, width=5, bg=LAVENDER, bd=1, borderwidth=0, relief="solid").grid(
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
        # Combobox example
        firstquestionanswers = ["good", "bad", "ugly"]
        secondquestionanswers = ["big", "small", "brave"]
        combobox = ttk.Combobox(
            self, values=firstquestionanswers, width=1, state='readonly')
        combobox.current(0)
        combobox.grid(row=8, column=12, columnspan=18, rowspan=2, sticky=NSEW)
        combobox2 = ttk.Combobox(
            self, values=secondquestionanswers, width=1, state='readonly')
        combobox2.current(0)
        combobox2.grid(row=12, column=12, columnspan=18,
                       rowspan=2, sticky=NSEW)

        textentry = Entry(self, width=1, bg="white", fg='#000000', font=(
            "Helvetica", 18), justify="center", bd=1, borderwidth=1, relief="solid")
        textentry.grid(row=16, column=12, columnspan=18,
                       rowspan=2, sticky=NSEW)

        def getcomboboxanswers():
            cmb1answer = combobox.get()
            cmb2answer = combobox2.get()
            textentryanswer = textentry.get()
            messagebox.showinfo(
                "Answers", f"First question answer: {cmb1answer}\nSecond question answer: {cmb2answer}\nText entry answer: {textentryanswer}")
        # random button to click
        button = Button(self, text="Click me", bg=LIGHTYELLOW, font=(
            "Helvetica", 18), command=lambda: getcomboboxanswers())
        button.grid(row=1, column=1, columnspan=5, rowspan=5, sticky=N+S+E+W)

        # sizebutton = Button(
        #     self, text="Big", command=lambda: _.changecontainersize(self, parent))
        # sizebutton.grid(row=1, column=1, sticky=N+S+E+W)
        # unsizebutton = Button(
        #     self, text="Small", command=lambda: _.revertcontainersize(self, parent))
        # unsizebutton.grid(row=2, column=1, sticky=N+S+E+W)

        # Widgets
        label = Label(self, text="This is the view participants page for admins\n Still under construction :)", font=(
            'Segoe Ui Semibold', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=12, columnspan=18,
                   rowspan=2, sticky=N+S+E+W)


class FeedbackForm(Frame):
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

        # Widgets
        label = Label(self, text="This is a feedback form to help us improve our app.\nPlease answer the questions below to the best of your ability.\nThank you for your time!", font=(
            'Segoe Ui Semibold', 14), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=10, columnspan=22,
                   rowspan=2, sticky=N+S+E+W)
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS feedback(
            satisfactionquestion1 text NOT NULL,
            satisfactionquestion2 text NOT NULL,
            likelihoodquestion text NOT NULL,
            easinessquestion text NOT NULL,
            yesnoquestion text NOT NULL,
            entryquestion text NOT NULL
            )""")

        # Radiobutton example
        def ShowChoice():
            messagebox.showinfo(
                "The answers are:", f"First question answer: {question1answer.get()}\nSecond question answer: {question2answer.get()}\nLikelihood answer: {question3answer.get()}\nEasinessQ answer: {question4answer.get()}\nYes no answer: {yesnoquestionanswer.get()}\nText entry answer: {openendedentry.get()}")

        def dosomedatabasemagic():
            satisfactionans = question1answer.get()
            helpfulans = question2answer.get()
            likelihoodans = question3answer.get()
            easinessans = question4answer.get()
            ynans = yesnoquestionanswer.get()
            entryanswer = openendedentry.get()
            print(entryanswer)
            information = (satisfactionans, helpfulans,
                           likelihoodans, easinessans, ynans, entryanswer)

            with conn:
                c.execute(
                    "INSERT INTO feedback VALUES (?,?,?,?,?,?)", information)
                messagebox.showinfo(
                    "Success", "Your answers have been recorded!")

        scaleofsatisfaction = [("1", "Very Unsatisfied"), ("2", "Unsatisfied"), (
            "3", "Neutral"), ("4", "Satisfied"), ("5", "Very Satisfied")]  # Scale for satisfaction
        scaleofhelpful = [("1", "Very Unhelpful"), ("2", "Unhelpful"), ("3", "Plain"),
                          ("4", "Helpful"), ("5", "Very Helpful")]  # Scale for helpful
        scaleoflikelihood = [("1", "Very Unlikely"), ("2", "Unlikely"), ("3", "Neutral"), (
            "4", "Likely"), ("5", "Very Likely")]  # Example if want to create a scale for likelihood
        scaleofeasiness = [("1", "Very Difficult"), ("2", "Difficult"), ("3", "Neutral"), (
            "4", "Easy"), ("5", "Very Easy")]  # If want to create an easiness scale question
        # messagebox.showinfo("Welcome to the survey!", "This is a survey to help us improve our app. Please answer the questions below to the best of your ability. Thank you for your time!")
        yesnooptions = ["No", "Yes"]

        # Label
        question1label = Label(self, text="How would you rate our announcement system for your overall experience? ", font=(
            "Helvetica", 14), bg=LIGHTYELLOW)
        question1label.grid(row=4, column=10, columnspan=22,
                            rowspan=1, sticky=NSEW)
        question1answer = StringVar()
        question1answer.set("Neutral")  # Satisfaction Q

        question2label = Label(self, text="Is this system very helpful to you that you are not miss or neglect any event? ", font=(
            "Helvetica", 14), bg=LIGHTYELLOW)
        question2label.grid(row=6, column=10, columnspan=22,
                            rowspan=1, sticky=NSEW)
        question2answer = StringVar()
        question2answer.set("Neutral")  # Satisfaction Q

        question3label = Label(self, text="How likely are you to recommend our app to your friends?", font=(
            "Helvetica", 14), bg=LIGHTYELLOW)
        question3label.grid(row=8, column=10, columnspan=22,
                            rowspan=1, sticky=NSEW)
        question3answer = StringVar()
        question3answer.set("Neutral")  # Likelihood Q

        question4label = Label(
            self, text="How difficult / easy was it to find the event on this app? ", font=("Helvetica", 14), bg=LIGHTYELLOW)
        question4label.grid(row=10, column=10, columnspan=22,
                            rowspan=1, sticky=NSEW)
        question4answer = StringVar()
        question4answer.set("Neutral")  # Easiness Q

        yesnoquestionlabel = Label(self, text="Were you able to find information you needed about the events?", font=(
            "Helvetica", 14), bg=LIGHTYELLOW)
        yesnoquestionlabel.grid(
            row=12, column=10, columnspan=22, rowspan=1, sticky=NSEW)
        yesnoquestionanswer = StringVar()
        yesnoquestionanswer.set("Yes")

        count = 12  # starting on column 12
        count2 = 12
        count3 = 12  # Change this to customize the column layout if needed, in this case since different loops, it's easier to just create the count2 variable
        count4 = 12
        count5 = 14  # Changing for yes no to make it centered
        # Creating Satisfaction Scale(because using satisfaction options)
        for text, rating in scaleofsatisfaction:
            self.firstrow = Radiobutton(self,
                                        text=text,  # text of the radiobutton becomes 1, 2, 3, 4, 5
                                        # for a row(horizontal), each radiobutton needs to share same variable
                                        variable=question1answer,
                                        # value is going to be the rating in ("Number", "Rating") that will be stored as the value for the radiobutton
                                        value=rating,
                                        justify=CENTER,
                                        bg=ORANGE, font=("Helvetica", 18))
            # count becomes the column number, 12, 16, 20, 24, 28
            self.firstrow.grid(row=5, column=count, rowspan=1,
                               columnspan=2, sticky=N+S+E+W)
            self.firstrow.grid_propagate(0)
            count += 4

        # Creating Helpful Scale
        for text, rating in scaleofhelpful:
            self.secondrow = Radiobutton(self,
                                         text=text,  # text of the radiobutton becomes 1, 2, 3, 4, 5
                                         # for a row(horizontal), each radiobutton needs to share same variable
                                         variable=question2answer,
                                         # value is going to be the rating in ("Number", "Rating") that will be stored as the value for the radiobutton
                                         value=rating,
                                         justify=CENTER,
                                         bg=ORANGE, font=("Helvetica", 18))
            # count becomes the column number, 12, 16, 20, 24, 28
            self.secondrow.grid(row=7, column=count2,
                                rowspan=1, columnspan=2, sticky=N+S+E+W)
            self.secondrow.grid_propagate(0)
            count2 += 4

        # Creating Likelihood Scale
        for text, rating in scaleoflikelihood:
            self.thirdrow = Radiobutton(self, text=text, variable=question3answer, value=rating, bg=ORANGE, font=("Helvetica", 18),
                                        justify=CENTER)
            self.thirdrow.grid(row=9, column=count3, rowspan=1,
                               columnspan=2, sticky=N+S+E+W)
            self.thirdrow.grid_propagate(0)
            count3 += 4  # have to set column=count2,because different type of answers
            # in options means different count needs to be used, basically, count is for satisfaction questions,
            # count2 is for likelihood questions, count3 for yes no questions
            # notice gap value is still 4

        # Creating Easiness Scale(because using easiness question)
        for text, rating in scaleofeasiness:
            self.fourthrow = Radiobutton(self, text=text, variable=question4answer, value=rating, bg=ORANGE, font=("Helvetica", 18),
                                         justify=CENTER)
            self.fourthrow.grid(row=11, column=count4,
                                rowspan=1, columnspan=2, sticky=N+S+E+W)
            self.fourthrow.grid_propagate(0)
            count4 += 4

        # Creating Yes No
        for text in yesnooptions:
            self.fifthrow = Radiobutton(self, text=text, variable=yesnoquestionanswer, value=text, bg=ORANGE, font=("Helvetica", 18),
                                        justify=CENTER)
            self.fifthrow.grid(row=13, column=count5,
                               rowspan=2, columnspan=3, sticky=N+S+E+W)
            self.fifthrow.grid_propagate(0)
            count5 += 11

        # Open Question
        openendquestionlabel = Label(self, text="Please leave any comments or suggestions below:", font=(
            "Helvetica", 14), bg=LIGHTYELLOW)
        openendquestionlabel.grid(
            row=15, column=10, columnspan=22, rowspan=1, sticky=NSEW)
        openendedentry = Entry(self, width=1, bg="white",
                               font=("Helvetica", 18), justify=CENTER)
        openendedentry.grid(row=16, column=10, columnspan=22,
                            rowspan=2, sticky=NSEW)

        # labels for scale
        satisfactionlabel = Label(self, text="More Unsatisfied", font=(
            "Helvetica", 11), bg=NICEPURPLE, justify="left")
        satisfactionlabel.grid(
            row=4, column=10, columnspan=2, rowspan=1, sticky=NSEW)
        dissatisfactionlabel = Label(self, text="More satisfied", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right")
        dissatisfactionlabel.grid(
            row=4, column=30, columnspan=2, rowspan=1, sticky=NSEW)
        unhelpfullabel = Label(self, text="Very Unhelpful", font=(
            "Helvetica", 11), bg=NICEPURPLE, justify="left")
        unhelpfullabel.grid(row=6, column=10, columnspan=2,
                            rowspan=1, sticky=NSEW)
        helpfullabel = Label(self, text="Very Helpful", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right")
        helpfullabel.grid(row=6, column=30, columnspan=2,
                          rowspan=1, sticky=NSEW)
        unlikelihoodlabel = Label(self, text="Less likelihood", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="left")
        unlikelihoodlabel.grid(
            row=8, column=10, columnspan=2, rowspan=1, sticky=NSEW)
        likelihoodlabel = Label(self, text="More likelihood", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right")
        likelihoodlabel.grid(row=8, column=30, columnspan=2,
                             rowspan=1, sticky=NSEW)
        difficultlabel = Label(self, text="More difficult", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="left")
        difficultlabel.grid(row=10, column=10, columnspan=2,
                            rowspan=1, sticky=NSEW)
        easierlabel = Label(self, text="Easier", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right")
        easierlabel.grid(row=10, column=30, columnspan=2,
                         rowspan=1, sticky=NSEW)

        # Button
        self.getanswers = Button(self, text="Cancel", command=lambda: [controller.show_frame(
            MainPage), controller.show_frameleft(MainPage2)], bg=ORANGE, font=("Helvetica", 18))
        self.getanswers.grid(row=18, column=10, rowspan=2,
                             columnspan=6, sticky=N+S+E+W)
        self.getanswers.grid_propagate(0)

        self.getanswers = Button(self, text="Confirm", command=lambda: [
                                 ShowChoice(), dosomedatabasemagic()], bg=ORANGE, font=("Helvetica", 18))
        self.getanswers.grid(row=18, column=26, rowspan=2,
                             columnspan=6, sticky=N+S+E+W)
        self.getanswers.grid_propagate(0)

        # Picture
        self.decorateimage = Image.open(r"assets\decoration.jpg")
        self.decoratingimage = ImageTk.PhotoImage(self.decorateimage.resize(
            (math.ceil(200 * dpi / 96), math.ceil(800 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.decoratingimage,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=1, column=3, columnspan=5,
                        rowspan=19, sticky=N+S+E+W)

        self.decorate2image = Image.open(r"assets\decoration.jpg")
        self.decorating2image = ImageTk.PhotoImage(self.decorate2image.resize(
            (math.ceil(200 * dpi / 96), math.ceil(800 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.decorating2image,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=1, column=34, columnspan=5,
                        rowspan=19, sticky=N+S+E+W)


class Calendar(Frame):
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
        # Widgets
        label = Label(self, text="This is a feedback form to help us improve our app.\nPlease answer the questions below to the best of your ability.\nThank you for your time!", font=(
            'Segoe Ui Semibold', 14), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=12, columnspan=18,
                   rowspan=2, sticky=N+S+E+W)
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS feedback(
            satisfactionquestion1 text NOT NULL,
            satisfactionquestion2 text NOT NULL,
            likelihoodquestion text NOT NULL,
            easinessquestion text NOT NULL,
            yesnoquestion text NOT NULL,
            entryquestion text NOT NULL
            )""")

        # Radiobutton example
        def ShowChoice():
            messagebox.showinfo(
                "The answers are:", f"First question answer: {question1answer.get()}\nSecond question answer: {question2answer.get()}\nLikelihood answer: {question3answer.get()}\nEasinessQ answer: {question4answer.get()}\nYes no answer: {yesnoquestionanswer.get()}\nText entry answer: {openendedentry.get()}")

        def dosomedatabasemagic():
            satisfaction1ans = question1answer.get()
            satisfaction2ans = question2answer.get()
            likelihoodans = question3answer.get()
            easinessans = question4answer.get()
            ynans = yesnoquestionanswer.get()
            entryanswer = openendedentry.get()
            print(entryanswer)
            information = (satisfaction1ans, satisfaction2ans,
                           likelihoodans, easinessans, ynans, entryanswer)

            with conn:
                c.execute(
                    "INSERT INTO feedback VALUES (?,?,?,?,?,?)", information)
                messagebox.showinfo(
                    "Success", "Your answers have been recorded!")

        scaleofsatisfaction = [("1", "Very Unsatisfied"), ("2", "Unsatisfied"), (
            "3", "Neutral"), ("4", "Satisfied"), ("5", "Very Satisfied")]  # Scale for satisfaction
        scaleoflikelihood = [("1", "Very Unlikely"), ("2", "Unlikely"), ("3", "Neutral"), (
            "4", "Likely"), ("5", "Very Likely")]  # Example if want to create a scale for likelihood
        scaleofeasiness = [("1", "Very Difficult"), ("2", "Difficult"), ("3", "Neutral"), (
            "4", "Easy"), ("5", "Very Easy")]  # If want to create an easiness scale question
        # messagebox.showinfo("Welcome to the survey!", "This is a survey to help us improve our app. Please answer the questions below to the best of your ability. Thank you for your time!")
        yesnooptions = ["No", "Yes"]

        question1label = Label(self, text="How satisfied are you with ...so and so...?", font=(
            "Helvetica", 14), bg=LIGHTYELLOW)
        question1label.grid(row=4, column=12, columnspan=18,
                            rowspan=1, sticky=NSEW)
        question1answer = StringVar()
        question1answer.set("Neutral")  # Satisfaction Q

        question2label = Label(self, text="How satisfied are you with ...so and so...?", font=(
            "Helvetica", 14), bg=LIGHTYELLOW)
        question2label.grid(row=6, column=12, columnspan=18,
                            rowspan=1, sticky=NSEW)
        question2answer = StringVar()
        question2answer.set("Neutral")  # Satisfaction Q

        question3label = Label(self, text="How likely are you to recommend ...so and so... to a friend?", font=(
            "Helvetica", 14), bg=LIGHTYELLOW)
        question3label.grid(row=8, column=12, columnspan=18,
                            rowspan=1, sticky=NSEW)
        question3answer = StringVar()
        question3answer.set("Neutral")  # Likelihood Q

        question4label = Label(
            self, text="How difficult/easy was it to ...so and so...?", font=("Helvetica", 14), bg=LIGHTYELLOW)
        question4label.grid(row=10, column=12, columnspan=18,
                            rowspan=1, sticky=NSEW)
        question4answer = StringVar()
        question4answer.set("Neutral")  # Easiness Q

        yesnoquestionlabel = Label(self, text="Were you able to find information you needed about the events?", font=(
            "Helvetica", 14), bg=LIGHTYELLOW)
        yesnoquestionlabel.grid(
            row=12, column=12, columnspan=18, rowspan=1, sticky=NSEW)
        yesnoquestionanswer = StringVar()
        yesnoquestionanswer.set("Yes")

        count = 12  # starting on column 12
        count2 = 12  # Change this to customize the column layout if needed, in this case since different loops, it's easier to just create the count2 variable
        count3 = 12
        count4 = 16  # Changing for yes no to make it centered
        # Creating Satisfaction Scale(because using satisfaction options)
        for text, rating in scaleofsatisfaction:
            # Creating row of radiobuttons for Q1
            self.firstrow = Radiobutton(self,
                                        text=text,  # text of the radiobutton becomes 1, 2, 3, 4, 5
                                        # for a row(horizontal), each radiobutton needs to share same variable
                                        variable=question1answer,
                                        # value is going to be the rating in ("Number", "Rating") that will be stored as the value for the radiobutton
                                        value=rating,
                                        justify=CENTER,
                                        bg=ORANGE, font=("Helvetica", 18))
            # count becomes the column number, 12, 16, 20, 24, 28
            self.firstrow.grid(row=5, column=count, rowspan=1,
                               columnspan=2, sticky=N+S+E+W)
            self.firstrow.grid_propagate(0)

            # Creating 2nd row of radiobuttons for Question 2 Satisfaction Scale
            self.secondrow = Radiobutton(self, text=text, variable=question2answer, value=rating, bg=ORANGE, font=("Helvetica", 18),
                                         justify=CENTER)
            self.secondrow.grid(row=7,
                                column=count,  # follows same pattern as above
                                rowspan=1, columnspan=2, sticky=N+S+E+W)
            self.secondrow.grid_propagate(0)
            # column=count2, #can dowan follow the same pattern as above
            # count2 += 4
            count += 4  # increase/decrease to make gap larger/smaller

        # Creating Likelihood Scale(because using likelihood question)
        for text, rating in scaleoflikelihood:
            self.thirdrow = Radiobutton(self, text=text, variable=question3answer, value=rating, bg=ORANGE, font=("Helvetica", 18),
                                        justify=CENTER)
            self.thirdrow.grid(row=9, column=count2, rowspan=1,
                               columnspan=2, sticky=N+S+E+W)
            self.thirdrow.grid_propagate(0)
            count2 += 4  # have to set column=count2,because different type of answers
            # in options means different count needs to be used, basically, count is for satisfaction questions,
            # count2 is for likelihood questions, count3 for yes no questions
            # notice gap value is still 4

        # Creating Easiness Scale(because using easiness question)
        for text, rating in scaleofeasiness:
            self.fourthrow = Radiobutton(self, text=text, variable=question4answer, value=rating, bg=ORANGE, font=("Helvetica", 18),
                                         justify=CENTER)
            self.fourthrow.grid(row=11, column=count3,
                                rowspan=1, columnspan=2, sticky=N+S+E+W)
            self.fourthrow.grid_propagate(0)
            count3 += 4

        # Creating Yes No
        for text in yesnooptions:
            self.fifthrow = Radiobutton(self, text=text, variable=yesnoquestionanswer, value=text, bg=ORANGE, font=("Helvetica", 18),
                                        justify=CENTER)
            self.fifthrow.grid(row=13, column=count4,
                               rowspan=2, columnspan=3, sticky=N+S+E+W)
            self.fifthrow.grid_propagate(0)
            count4 += 7  # notice gap value is 8, leading to a different gap between radiobuttons
        openendquestionlabel = Label(self, text="Please leave any comments or suggestions below:", font=(
            "Helvetica", 14), bg=LIGHTYELLOW)
        openendquestionlabel.grid(
            row=15, column=12, columnspan=18, rowspan=1, sticky=NSEW)
        openendedentry = Entry(self, width=1, bg="white",
                               font=("Helvetica", 18), justify=CENTER)
        openendedentry.grid(row=16, column=12, columnspan=18,
                            rowspan=2, sticky=NSEW)

        # labels for scale
        satisfactionlabel = Label(self, text="More Unsatisfied", font=(
            "Helvetica", 11), bg=NICEPURPLE, justify="left")
        satisfactionlabel.grid(
            row=4, column=12, columnspan=2, rowspan=1, sticky=NSEW)
        dissatisfactionlabel = Label(self, text="More satisfied", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right")
        dissatisfactionlabel.grid(
            row=4, column=28, columnspan=2, rowspan=1, sticky=NSEW)
        unlikelihoodlabel = Label(self, text="Less likelihood", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="left")
        unlikelihoodlabel.grid(
            row=8, column=12, columnspan=2, rowspan=1, sticky=NSEW)
        likelihoodlabel = Label(self, text="More likelihood", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right")
        likelihoodlabel.grid(row=8, column=28, columnspan=2,
                             rowspan=1, sticky=NSEW)
        difficultlabel = Label(self, text="More difficult", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="left")
        difficultlabel.grid(row=10, column=12, columnspan=2,
                            rowspan=1, sticky=NSEW)
        easierlabel = Label(self, text="Easier", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right")
        easierlabel.grid(row=10, column=28, columnspan=2,
                         rowspan=1, sticky=NSEW)

        # get answers button
        self.getanswers = Button(self, text="Get Answers", command=lambda: [
                                 ShowChoice(), dosomedatabasemagic()], bg=ORANGE, font=("Helvetica", 18))
        self.getanswers.grid(row=18, column=24, rowspan=2,
                             columnspan=6, sticky=N+S+E+W)
        self.getanswers.grid_propagate(0)

        self.randombutton = ttk.Button(
            self, text="Random", command=lambda: print("hello"))
        self.randombutton.grid(row=18, column=12, rowspan=2,
                               columnspan=6, sticky=N+S+E+W)
        self.randombutton.grid_propagate(0)
        radiobuttonstyle = ttk.Style()
        radiobuttonstyle.configure(
            "a.TRadiobutton", background=ORANGE, font=("Helvetica", 18))
        self.radiobuttonexample = ttk.Radiobutton(
            self, text="Example", style="a.TRadiobutton", command=lambda: print("hello"))
        self.radiobuttonexample.grid(
            row=18, column=18, rowspan=1, columnspan=6, sticky=N+S+E+W)
        self.radiobuttonexample.grid_propagate(0)


if __name__ == "__main__":
    window = Window()
    window.mainloop()
