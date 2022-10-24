from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk, Image, ImageOps
import math
import sqlite3
import datetime as dt
from tkcalendar import Calendar as tkCalendar


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
LOGINID = "Viewer"
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
        global LOGINID
        print(setstateofaccount(self, LOGGEDINAS))
        print(setstateofaccount(self, LOGINID))
        # Right Container
        self.container = Frame(self,
                          bg=LAVENDER,
                          width=1, height=1, borderwidth=1, relief="solid")
        self.container.grid_propagate(0)
        self.container.grid(row=2, column=2,
                       rowspan=14, columnspan=14, sticky=N+S+E+W)
        self.container.grid_rowconfigure(0, weight=0)
        self.container.grid_columnconfigure(0, weight=0)
        # Left Container
        self.container2 = Frame(self, bg=LAVENDER, width=1, height=1, borderwidth=1, relief="solid")
        self.container2.grid_propagate(0)
        self.container2.grid(row=3, column=2, columnspan=13,
                        rowspan=12, sticky=N+S+E+W)
        self.container2.grid_rowconfigure(0, weight=0)
        self.container2.grid_columnconfigure(0, weight=0)

        # Top Container
        # functions to change container sizes has been moved to the class

        FONTFORBUTTONS = "Bahnschrift Semibold"
        self.container3 = Frame(self, bg=DARKBLUE)
        self.container3.grid(row=0, column=0, rowspan=2,
                             columnspan=32, sticky=N+S+E+W)
        self.container3.grid_propagate(0)
        # self.signupbutton = Button(self.container3, text="Sign Up\n Page", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20, "bold"),
        #                            borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
        #                            command=lambda: [
        #     self.show_frame(RegistrationPage),
        #     self.show_frameleft(RegistrationPage2),
        #     self.onelargeonesmallcont()])
        # self.signupbutton.grid(row=0, column=0, rowspan=1, sticky=N+S+E+W)
        # self.loginbutton = Button(self.container3, text="Login\nPage", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
        #                           borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
        #                           command=lambda: [
        #     self.show_frame(LoginPage),
        #     self.show_frameleft(LoginPage2),
        #     self.onelargeonesmallcont()])
        # self.loginbutton.grid(row=0, column=1, rowspan=1, sticky=N+S+E+W)
        # self.mainpagebutton = Button(self.container3, text="Main\nPage", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
        #                              borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
        #                              command=lambda: [
        #     self.show_frame(MainPage),
        #     self.show_frameleft(MainPage2), 
        #     self.singlecontainer()])
        # self.eventlistbutton = Button(self.container3, text="Event\nList", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
        #                               borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
        #                               command=lambda: [
        #     self.show_frame(EventView),
        #     self.show_frameleft(EventView2),
        #     self.doublelargecontainers()])
        # self.eventregistrationbutton = Button(self.container3, text="Event\nRegistration", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
        #                                       borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
        #                                       command=lambda: [
        #     self.show_frame(EventRegistration),
        #     self.show_frameleft(EventRegistration2),
        #     self.doublelargecontainers()])
        # self.eventcreationbutton = Button(self.container3, text="Event\nCreation\n(ADMIN)", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
        #                                   borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
        #                                   command=lambda: [
        #     self.show_frame(EventCreation),
        #     self.singlecontainer()])
        # self.viewparticipantsbutton = Button(self.container3, text="View\nParticipants\n(ADMIN)", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
        #                                      borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
        #                                      command=lambda: [
        #     self.show_frame(ViewParticipants),
        #     self.singlecontainer()])
        # self.feedbackbutton = Button(self.container3, text="Feedback\nForm", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
        #                     borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
        #                     command=lambda: [
        #     self.show_frame(FeedbackForm), 
        #     self.singlecontainer()])
        self.calendarbutton = Button(self.container3, text="Calendar", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                     borderwidth=1, relief="sunken", height=3, width=10, padx=15, pady=0, highlightthickness=0,
                                     command=lambda: [
            self.show_frame(Calendar),
            self.singlecontainer()])

        # # Sign out button
        self.container4 = Frame(
            self, bg=NAVYBLUE, width=1, height=1, borderwidth=2, relief="flat", padx=0, pady=0)
        self.container4.grid(row=16, column=0, rowspan=2, columnspan=24,
                             sticky=N+S+E+W)
        self.container4.grid_propagate(0)
        self.signoutbutton = Button(self.container4, text="Sign Out", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                    borderwidth=1, relief="solid", height=3, width=10,
                                    command=lambda: [
            self.show_frame(Calendar),
            self.show_frameleft(Calendar),
            self.onelargeonesmallcont(),
            self.signout()])
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
                                borderwidth=0, relief="flat")
        self.container5.grid(row=2, column=0, rowspan=14, columnspan=2,
                             sticky=N+S+E+W)
        self.container5.grid_propagate(0)
        for x in range(2):
                Grid.columnconfigure(self.container5, x, weight=1, uniform='row')
                Label(self.container5, height=1, bg=NAVYBLUE).grid(
                  row=0, column=x,rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(14):
                Grid.rowconfigure(self.container5, y, weight=1, uniform='row')
                Label(self.container5, width=2, bg=NAVYBLUE).grid(
                    row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)
        self.bellimage = Image.open(r"assets\bell.png")
        self.bellimage = ImageTk.PhotoImage(self.bellimage.resize(
            (math.ceil(120 * dpi/96), math.ceil(120 * dpi/96)), Image.Resampling.LANCZOS))
        self.bellbutton = Button(self.container5, image=self.bellimage, bg=NAVYBLUE,
                                    borderwidth=1, relief="flat", height=1, width=1,
                                    command=lambda: print('yes'))

        self.calendarimage = Image.open(r"assets\calenderr.png")
        self.calendarimage = ImageTk.PhotoImage(self.calendarimage.resize(
            (math.ceil(120 * dpi/96), math.ceil(120 * dpi/96)), Image.Resampling.LANCZOS))
        self.sidecalendar = Button(self.container5, image=self.calendarimage, bg=NAVYBLUE,
                                    borderwidth=1, relief="flat", height=1, width=1,
                                    command=lambda:[
            self.make_a_container()])

        #Clickable Calendar Frame
        self.randomframe = Frame(self, bg=PINK, width=1, height=1,
                                    borderwidth=1, relief="flat")
        self.randomframe.grid_propagate(0)
        for x in range(12):
            Grid.columnconfigure(self.randomframe, x, weight=1, uniform='row')
            Label(self.randomframe, height=1, bg=LIGHTPURPLE, borderwidth=1, relief="solid").grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(12):
            Grid.rowconfigure(self.randomframe, y, weight=1, uniform='row')
            Label(self.randomframe, width=1, bg=LIGHTPURPLE, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W,)
        self.randomlabel = Label(self.randomframe, text="What would you\nlike to do?",
                            font=("Atkinson Hyperlegible", 14), width=1, height=1,
                            bg=LAVENDER, fg="black")
        self.randomlabel.grid(row=0, column=2, rowspan=2, columnspan=8, sticky=N+S+E+W)
        self.randomlabel.grid_propagate(0)
        self.viewbutton = Button(self.randomframe, text="View Calendar", bg=DARKBLUE, fg="WHITE",width=1,height=1,
        command=lambda:[
            # self.show_frame(EventView),
            # self.show_frameleft(RegistrationPage2),
            # self.doublelargecontainers(),
            self.randomframe.grid_remove()
        ])
        self.loggedinaslabel = Label(self.randomframe, text="Logged in as: " + LOGINID,
                            font=("Atkinson Hyperlegible", 14), width=1, height=1,
                            bg=LAVENDER, fg="black")
        self.loggedinaslabel.grid(row=3, column=1, rowspan=2, columnspan=6, sticky=N+S+E+W)
        self.loggedinaslabel.grid_propagate(0)
        self.viewbutton.grid(row=5, column=1, rowspan=2, columnspan=4, sticky=N+S+E+W,pady=5)
        self.viewbutton.grid_propagate(0)
        self.editbutton = Button(self.randomframe, text="Edit Calendar", bg=DARKBLUE, fg="WHITE", width=1,height=1,
        command=lambda:[
        ])
        self.editbutton.grid(row=5, column=5, rowspan=2, columnspan=4, sticky=N+S+E+W,pady=5)
        self.editbutton.grid_propagate(0)





        # self.signoutbutton.grid_propagate(0)
        self.studentbutton.grid_propagate(0)
        self.adminbutton.grid_propagate(0)

        self.welcomelabel("Stranger", "Viewer")

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
        self.singlecontainer()
        self.show_loggedin()
        self.frames = {}

        for F in (Calendar,):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Calendar)

        for F in (Calendar,):
            frame = F(self.container2, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frameleft(Calendar)

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
        self.sidecalendar.grid_forget()
        self.bellbutton.grid_forget()
        self.welcomelabel("Stranger", "Viewer")
        global LOGGEDINAS
        global LOGINSTATE
        global LOGINID
        LOGGEDINAS = "Viewer"
        LOGINSTATE = False
        LOGINID = "Viewer"


    def show_loggedin(self):
        # self.mainpagebutton.grid(row=0, column=2, rowspan=1, sticky=N+S+E+W)
        # self.eventlistbutton.grid(row=0, column=3, rowspan=1, sticky=N+S+E+W)
        # self.eventregistrationbutton.grid(row=0, column=4, rowspan=1, sticky=N+S+E+W)
        self.calendarbutton.grid(row=0, column=7, rowspan=1, sticky=N+S+E+W)
        # self.feedbackbutton.grid(row=0, column=8, rowspan=1, sticky=N+S+E+W)
        self.sidecalendar.grid(row=7, column=0, rowspan=2, columnspan=2, sticky=NSEW)
        self.bellbutton.grid(row=10, column=0, rowspan=2, columnspan=2, sticky=NSEW)

    def show_admin(self):
        self.eventcreationbutton.grid(
            row=0, column=5, rowspan=1, sticky=N+S+E+W)
        self.viewparticipantsbutton.grid(
            row=0, column=6, rowspan=1, sticky=N+S+E+W)

    def onelargeonesmallcont(self): #used in sign up page, login page, event list, event registration
        self.container.grid(row=2, column=16, rowspan=14,
                            columnspan=14, sticky=N+S+E+W)
        self.container2.grid(row=3, column=2, columnspan=13,
                               rowspan=12, sticky=N+S+E+W)

    def doublelargecontainers(self): #used in event list, event registration
        self.container.grid(row=2, column=16, rowspan=14,
                                columnspan=14, sticky=N+S+E+W)
        self.container2.grid(row=2, column=2, columnspan=14,
                               rowspan=14, sticky=N+S+E+W)

    def singlecontainer(self): # used for container on the left, on main page, event creation, view participants, calendar, feedbackform 
        self.container2.grid(row=2, column=2, rowspan=14,
                            columnspan=26, sticky=N+S+E+W)
        self.container.grid_remove()
    
    def revertcontainer3(self):
        self.container3.grid(row=0, column=0, rowspan=2,
                             columnspan=32, sticky=N+S+E+W)
    
    def shiftcontainer3over(self):
        self.container3.grid(row=0, column=5, rowspan=2,
                             columnspan=32, sticky=N+S+E+W)
    def make_a_container(self):
        self.randomframe.grid_remove()
        self.randomframe.grid(row=7, column=2, rowspan=6, columnspan=6,
                            sticky=N+S+E+W)


    def makecontainer(self):
        randomframe = Frame(self, bg=PINK, width=1, height=1,
                                borderwidth=1, relief="flat")
        randomframe.grid(row=2, column=2, rowspan=14, columnspan=14,
                             sticky=N+S+E+W)
        randomframe.grid_propagate(0)
        self.randomframe = randomframe
        for x in range(14):
            Grid.columnconfigure(self.randomframe, x, weight=1, uniform='row')
            Label(randomframe, height=1, bg=LIGHTPURPLE, borderwidth=1, relief="solid").grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(14):
            Grid.rowconfigure(self.randomframe, y, weight=1, uniform='row')
            Label(randomframe, width=1, bg=LIGHTPURPLE, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W,)
        randomlabel = Label(self.randomframe, text="random", bg=DARKBLUE)
        randomlabel.grid(row=0, column=0, rowspan=1, columnspan=14, sticky=N+S+E+W,pady=5)
        randomlabel.grid_propagate(0)
        randombutton = Button(self.randomframe, text="random", bg=DARKBLUE, fg="WHITE", command=lambda:[
            self.show_frame(Calendar),
            self.show_frameleft(Calendar),
            self.doublelargecontainers(),
            self.randomframe.grid_remove()
        ])
        randombutton.grid(row=13, column=0, rowspan=1, columnspan=14, sticky=N+S+E+W,pady=5)
    def removethecontainer(self):
        self.randomframe.grid_remove()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_frameleft(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def welcomelabel(self, name, role):
        welcomeframe = Frame(self, bg=NICEBLUE, width=1, height=1,
                            borderwidth=1, relief="flat")
        welcomeframe.grid(row=16, column=24, rowspan=2, columnspan=8,
                            sticky=N+S+E+W)
        welcomeframe.grid_propagate(0)
        # self.welcomeframe = welcomeframe
        for x in range(8):
            Grid.columnconfigure(welcomeframe, x, weight=1, uniform='row')
            Label(welcomeframe, height=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(2):
            Grid.rowconfigure(welcomeframe, y, weight=1, uniform='row')
            Label(welcomeframe, width=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W,)
        namelabel = Label(welcomeframe, text="", font=("Avenir Next", 18), fg="white",bg=DARKBLUE)
        namelabel.grid(row=0, column=0, rowspan=2, columnspan=8, sticky=N+S+E+W)
        namelabel.configure(text=f"Welcome {name.capitalize()} as {role.capitalize()}!")
        namelabel.grid_propagate(0)

class Calendar(Frame):
    def __init__(self, parent, controller):
        a = Frame
        a.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(40):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, width=1, bg=LAVENDER, borderwidth=1, relief="solid").grid(
                row=0, column=x, rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(24):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, height=1, width=5, bg=LAVENDER, bd=1, borderwidth=1, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)
        # b = Frame(self, bg=LAVENDER, width=1, height=1,borderwidth=1, relief="solid")
        # b.grid(row=15, column=9, rowspan=6, columnspan=12, sticky=N+S+E+W)
        xbuttonlabel = Button(self, text="X", font=("Avenir Next", 18),height=1,width=1, bg=DARKBLUE, fg="white")
        xbuttonlabel.grid(row=0, column=38, rowspan=2, columnspan=2, sticky=N+S+E+W)
        
        # Widgets
        label = Label(self, text="This is the Calendar", font=(
            'Segoe Ui Semibold', 14), width=1, height=1, fg='#000000', bg='#FFF5E4', justify="left")
        label.grid(row=0, column=2, columnspan=6,
                   rowspan=2, sticky=N+S+E+W)
        conn = sqlite3.connect('registration.db')
        #Creating Squares for a calendar
        cal = tkCalendar(self, 
        selectmode="day", year=2022, month=10, day=24, font=("Avenir Next", 14),
        date_pattern="yy-mm-dd")
        cal.grid(row=2, column=2, columnspan=24, rowspan=20, sticky=N+S+E+W)

if __name__ == "__main__":
    window = Window()
    window.mainloop()