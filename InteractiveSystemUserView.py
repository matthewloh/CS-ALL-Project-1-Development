import subprocess
import os
from ctypes.wintypes import BOOL, HWND, LONG
import ctypes
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import io 

try:
    import pyglet
except:
    print('Installing pyglet.')
    subprocess.check_call(['pip', 'install', 'pyglet'])
    print('Done.')
    import pyglet
try:
  from PIL import ImageTk, Image, ImageOps
except:
  print('Installing PIL.')
  subprocess.check_call(['pip', 'install', 'pillow'])
  print('Done.')
  from PIL import ImageTk, Image, ImageOps
try:
    from tkcalendar import Calendar as tkCalendar 
    from tkcalendar import DateEntry
except:
    print('Installing tkcalendar.')
    subprocess.check_call(['pip', 'install', 'tkcalendar'])
    print('Done.')
    from tkcalendar import Calendar as tkCalendar
    from tkcalendar import DateEntry



pyglet.font.add_file(r'fonts\AtkinsonHyperlegible.ttf')
pyglet.font.add_file(r'fonts\AvenirNext-Medium.otf')
pyglet.font.add_file(r'fonts\Helvetica.ttf')
import math
import sqlite3
import datetime
from ctypes import windll
# windll.shcore.SetProcessDpiAwareness(1)

GetWindowLongPtrW = ctypes.windll.user32.GetWindowLongPtrW
SetWindowLongPtrW = ctypes.windll.user32.SetWindowLongPtrW

def get_handle(root) -> int:
    root.update_idletasks()
    # This gets the window's parent same as `ctypes.windll.user32.GetParent`
    return GetWindowLongPtrW(root.winfo_id(), GWLP_HWNDPARENT)
# Constants
GWL_STYLE = -16
GWLP_HWNDPARENT = -8
WS_CAPTION = 0x00C00000
WS_THICKFRAME = 0x00040000
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
LOGGEDINAS = "Viewer"
LOGINSTATE = False
LOGINID = "Viewer"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN WINDOW ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        global dpi 
        global dpiError
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
            f'{math.ceil(1920 * dpi / 96)}x{math.ceil(1049 * dpi / 96)}')
        self.title("INTI Interactive System")
        self.resizable(0, 0)
        for x in range(32):
            self.columnconfigure(x, weight=1, uniform='row')
            Label(width=1, bg=NICEPURPLE).grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(18):
            self.rowconfigure(y, weight=1, uniform='row')
            Label(width=1, bg=NICEPURPLE).grid(
                row=y, column=0, sticky=N+S+E+W)
        self.configure(background=LAVENDER)

        print(LOGINID)
        print(LOGGEDINAS)       
        #frame to contain  the entire container why didnt i think of this earlier looll
        self.centercontainer = Frame(self, bg=LAVENDER)
        self.centercontainer.grid(row=2, column=2, rowspan=14,
                             columnspan=28, sticky=N+S+E+W) 
        self.centercontainer.grid_propagate(0)
        for x in range(28):
            Grid.columnconfigure(self.centercontainer, x, weight=1, uniform='row')
            Label(self.centercontainer, height=1, bg=LAVENDER).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(16):
            Grid.rowconfigure(self.centercontainer, y, weight=1, uniform='row')
            Label(self.centercontainer, width=1, bg=LAVENDER).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)
                        
        self.container2 = Frame(self.centercontainer, bg=LAVENDER)



        FONTFORBUTTONS = "Bahnschrift Semibold"
        self.container3 = Frame(self, bg=DARKBLUE)
        self.container3.grid(row=0, column=0, rowspan=2,
                             columnspan=30, sticky=N+S+E+W)
        for x in range(30):
            Grid.columnconfigure(self.container3, x, weight=1, uniform='row')
            Label(self.container3, height=1, bg=DARKBLUE).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(2):
            Grid.rowconfigure(self.container3, y, weight=1, uniform='row')
            Label(self.container3, height=1, width=1, bg=DARKBLUE).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)

        self.container3.grid_propagate(0)
        self.signupbutton = Button(self.container3, text="Sign Up\n Page", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20, "bold"),
                                   borderwidth=2, relief="raised", height=1,width=1, highlightthickness=2,
                                   command=lambda: [
            self.show_frame(RegistrationPage),
            self.togglebuttonrelief(self.signupbutton)
            ])
        self.signupbutton.grid(row=0, column=0, rowspan=2, columnspan=3, sticky=N+S+E+W)
        self.loginbutton = Button(self.container3, text="Login\nPage", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                  borderwidth=2, relief="raised", height=1, width=1, padx=15, pady=0, highlightthickness=0,
                                  command=lambda: [
            self.show_frame(LoginPage),
            self.togglebuttonrelief(self.loginbutton)
            ])
        self.loginbutton.grid(row=0, column=3, rowspan=2, columnspan=3, sticky=N+S+E+W)
        self.mainpagebutton = Button(self.container3, text="Main\nPage", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                     borderwidth=2, relief="raised", height=1, width=1, padx=15, pady=0, highlightthickness=0,
                                     command=lambda: [
            self.show_frame(MainPage),
            self.togglebuttonrelief(self.mainpagebutton)
            ])
        self.eventlistbutton = Button(self.container3, text="Event\nList", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                      borderwidth=2, relief="raised", height=1, width=1, padx=15, pady=0, highlightthickness=0,
                                      command=lambda: [
            self.show_frame(EventView),
            self.togglebuttonrelief(self.eventlistbutton)
            ])
        self.eventregistrationbutton = Button(self.container3, text="Event\nRegistration", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                              borderwidth=2, relief="raised",
                                              height=1, width=1, padx=15, pady=0, highlightthickness=0,
                                              command=lambda: [
            self.show_frame(EventRegistration),
            self.togglebuttonrelief(self.eventregistrationbutton)
            ])
        self.eventcreationbutton = Button(self.container3, text="Event\nCreation\n(ADMIN)", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                          borderwidth=2, relief="raised", height=1,width=1, padx=15, pady=0, highlightthickness=0,
                                          command=lambda: [
            self.show_frame(EventCreation),
            self.togglebuttonrelief(self.eventcreationbutton)
            ])
        self.viewparticipantsbutton = Button(self.container3, text="View\nParticipants\n(ADMIN)", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                             borderwidth=2, relief="raised", height=1,width=1, padx=15, pady=0, highlightthickness=0,
                                             command=lambda: [
            self.show_frame(ViewParticipants),
            self.togglebuttonrelief(self.viewparticipantsbutton)
            ])
        self.feedbackbutton = Button(self.container3, text="Feedback\nForm", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                            borderwidth=2, relief="raised", height=1,width=1, padx=15, pady=0, highlightthickness=0,
                            command=lambda: [
            self.show_frame(FeedbackForm),
            self.togglebuttonrelief(self.feedbackbutton)
            ])
        self.calendarbutton = Button(self.container3, text="Calendar", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                     borderwidth=2, relief="raised", height=1,width=1, padx=15, pady=0, highlightthickness=0,
                                     command=lambda: [
            self.show_frame(CalendarPage),
            self.togglebuttonrelief(self.calendarbutton)
            ])

        # Sign out button
        self.bottomleftbuttons = Frame(
            self, bg=NAVYBLUE, width=1, height=1, borderwidth=2, relief="flat", padx=0, pady=0)
        self.bottomleftbuttons.grid(row=16, column=0, rowspan=2, columnspan=16,
                             sticky=N+S+E+W)
        self.bottomleftbuttons.grid_propagate(0)
        for x in range(16):
                Grid.columnconfigure(self.bottomleftbuttons, x, weight=1, uniform='row')
                Label(self.bottomleftbuttons, height=2, bg=NAVYBLUE).grid(
                  row=0, column=x,rowspan=1, columnspan=2, sticky=N+S+E+W)
        for y in range(2):
                Grid.rowconfigure(self.bottomleftbuttons, y, weight=1, uniform='row')
                Label(self.bottomleftbuttons, width=5, bg=NAVYBLUE).grid(
                    row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        self.signoutbutton = Button(self.bottomleftbuttons, text="Sign Out", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                    borderwidth=2, relief="solid", height=1,width=1,
                                    command=lambda: [
            self.show_frame(LoginPage),
            self.signout()])
        self.signoutbutton.grid(row=0, column=0, rowspan=2,columnspan=3, sticky=N+S+E+W)
        self.studentbutton = Button(self.bottomleftbuttons, text="Student\nButton", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                    borderwidth=2, relief="solid", height=3, width=10,
                                    command=lambda: [self.show_loggedin()])
        self.studentbutton.grid(row=0, column=3, rowspan=2,columnspan=3, sticky=N+S+E+W)

        self.adminbutton = Button(self.bottomleftbuttons, text="Admin\nButton", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                  borderwidth=2, relief="solid", height=3, width=10,
                                  command=lambda: [self.show_admin()])
        self.adminbutton.grid(row=0, column=6, rowspan=2, columnspan=3, sticky=N+S+E+W)
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
        #bind escape to close the window
        self.bind("<Escape>", lambda e: self.destroy())
        self.welcomelabel("Stranger", "Viewer")
        self.createcalendarframe()
        self.createwindowmanagementframe()
        self.frames = {}

        for F in (RegistrationPage, LoginPage, MainPage, 
                EventView, EventRegistration, EventCreation,
                ViewParticipants, CalendarPage, FeedbackForm):
            frame = F(self.centercontainer, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, rowspan=16, columnspan=28, sticky="nsew")
        #Shows the loading frame
        self.show_frame(LoginPage)
        self.togglebuttonrelief(self.loginbutton)

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
        self.mainpagebutton.grid(row=0, column=6, rowspan=2, columnspan=3,sticky=N+S+E+W)
        self.eventlistbutton.grid(row=0, column=9, rowspan=2, columnspan=3, sticky=N+S+E+W)
        self.eventregistrationbutton.grid(row=0, column=12, rowspan=2,columnspan=3,sticky=N+S+E+W)
        self.calendarbutton.grid(row=0, column=15, rowspan=2,columnspan=3, sticky=N+S+E+W)
        self.feedbackbutton.grid(row=0, column=18, rowspan=2,columnspan=3, sticky=N+S+E+W)
        self.sidecalendar.grid(row=7, column=0, rowspan=2, columnspan=2, sticky=NSEW)
        self.bellbutton.grid(row=10, column=0, rowspan=2, columnspan=2, sticky=NSEW)

    def show_admin(self):
        self.mainpagebutton.grid(row=0, column=6, rowspan=2, columnspan=3,sticky=N+S+E+W)
        self.eventlistbutton.grid(row=0, column=9, rowspan=2, columnspan=3, sticky=N+S+E+W)
        self.eventregistrationbutton.grid(row=0, column=12, rowspan=2,columnspan=3,  sticky=N+S+E+W)
        self.eventcreationbutton.grid(row=0, column=15, rowspan=2,columnspan=3, sticky=N+S+E+W)
        self.viewparticipantsbutton.grid(row=0, column=18, rowspan=2,columnspan=3, sticky=N+S+E+W)
        self.calendarbutton.grid(row=0, column=21, rowspan=2,columnspan=3, sticky=N+S+E+W)
        self.feedbackbutton.grid(row=0, column=24, rowspan=2,columnspan=3, sticky=N+S+E+W)
        self.sidecalendar.grid(row=7, column=0, rowspan=2, columnspan=2, sticky=NSEW)
        self.bellbutton.grid(row=10, column=0, rowspan=2, columnspan=2, sticky=NSEW)

    def welcomelabel(self, name, role):
        welcomeframe = Frame(self, bg=NICEBLUE, width=1, height=1,
                            borderwidth=1, relief="flat")
        welcomeframe.grid(row=16, column=20, rowspan=2, columnspan=12,
                            sticky=N+S+E+W)
        welcomeframe.grid_propagate(0)
        for x in range(8):
            Grid.columnconfigure(welcomeframe, x, weight=1, uniform='row')
            Label(welcomeframe, height=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(2):
            Grid.rowconfigure(welcomeframe, y, weight=1, uniform='row')
            Label(welcomeframe, width=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W,)
        namelabel = Button(welcomeframe, text="", font=("Atkinson Hyperlegible", 18), fg="white",bg=DARKBLUE)
        namelabel.grid(row=0, column=0, rowspan=2, columnspan=8, sticky=N+S+E+W)
        namelabel.configure(text=f"Welcome {name.capitalize()} as {role.capitalize()}!\nWe are glad to have you here!")
        namelabel.grid_propagate(0)

    def deletethewindowbar(self):
        hwnd:int = get_handle(self)
        style:int = GetWindowLongPtrW(hwnd, GWL_STYLE)
        style &= ~(WS_CAPTION | WS_THICKFRAME)
        SetWindowLongPtrW(hwnd, GWL_STYLE, style)
    
    def showthewindowbar(self):
        hwnd:int = get_handle(self)
        style:int = GetWindowLongPtrW(hwnd, GWL_STYLE)
        style |= (WS_CAPTION | WS_THICKFRAME)
        SetWindowLongPtrW(hwnd, GWL_STYLE, style)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]

    def make_a_container(self):
        self.randomframe.grid_remove()
        self.randomframe.grid(row=7, column=2, rowspan=6, columnspan=6,
                            sticky=N+S+E+W)
    #Window management button frame
    def createwindowmanagementframe(self):
        self.windowmanagementframe = Frame(self, bg=NAVYBLUE, width=1, height=1,
                                    borderwidth=0, relief="flat")
        self.windowmanagementframe.grid(row=0, column=30, rowspan=2, columnspan=2,
                                    sticky=N+S+E+W)
        self.windowmanagementframe.grid_propagate(0)
        for x in range(2):
            Grid.columnconfigure(self.windowmanagementframe, x, weight=1, uniform='row')
            Label(self.windowmanagementframe, height=1, bg=NAVYBLUE).grid(
                row=0, column=x, rowspan=2, columnspan=1, sticky=N+S+E+W)
        for y in range(2):
            Grid.rowconfigure(self.windowmanagementframe, y, weight=1, uniform='row')
            Label(self.windowmanagementframe, width=1, bg=NAVYBLUE).grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W)

        self.minimizebutton = Button(self.windowmanagementframe, text="Show", font=("Atkinson Hyperlegible", 14),
                                    bg="#fdbc40", fg="WHITE", width=1, height=1,
                                    command=lambda:[
            self.state('normal'),
            self.showthewindowbar()
        ])
        self.minimizebutton.grid(row=0, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)
        self.minimizebutton.grid_propagate(0)
        self.maximizebutton = Button(self.windowmanagementframe, text="Hide", font=("Atkinson Hyperlegible", 14),
                                    bg="#33c748", fg="WHITE", width=1, height=1,
                                    command=lambda:[
            self.deletethewindowbar(),
            self.state('zoomed')
        ])
        self.maximizebutton.grid(row=1, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)
        self.maximizebutton.grid_propagate(0)
        self.closewindowbutton = Button(self.windowmanagementframe, text="Close", font=("Atkinson Hyperlegible", 14),
                                    bg="#fc5753", fg="WHITE", width=1, height=1,
                                    command=lambda:[
            self.destroy()
        ])
        self.closewindowbutton.grid(row=0, column=1, rowspan=2, columnspan=1, sticky=N+S+E+W)
        self.closewindowbutton.grid_propagate(0)
    #this function toggles the relief to sunken every time the mouse clicks the button
    def togglebuttonrelief(self, button):
        self.buttonlist = [self.signupbutton, self.loginbutton, self.mainpagebutton,
        self.calendarbutton, self.eventlistbutton, self.eventregistrationbutton,
        self.eventcreationbutton, self.viewparticipantsbutton, self.feedbackbutton, self.calendarbutton]
        #sets every button to raised by default on click
        for b in self.buttonlist:
            b.configure(relief="raised")
        if button['relief'] == 'raised':
            button['relief'] = 'sunken'
        else:
            button['relief'] = 'raised'
    def createcalendarframe(self):
        self.randomframe = Frame(self, bg=PINK, width=1, height=1,
                                    borderwidth=1, relief="flat")
        self.randomframe.grid_propagate(0)
        for x in range(12):
            Grid.columnconfigure(self.randomframe, x, weight=1, uniform='row')
            Label(self.randomframe, height=1, bg=LIGHTPURPLE).grid(
                row=0, column=x, sticky=N+S+E+W)
        for y in range(12):
            Grid.rowconfigure(self.randomframe, y, weight=1, uniform='row')
            Label(self.randomframe, width=1, bg=LIGHTPURPLE).grid(
                row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W,)
        self.introlabel = Label(self.randomframe, text="What would you\nlike to do?",
                            font=("Atkinson Hyperlegible", 14), width=1, height=1,
                            bg=LAVENDER, fg="black")
        self.introlabel.grid(row=0, column=2, rowspan=2, columnspan=8, sticky=N+S+E+W)
        self.introlabel.grid_propagate(0)
        self.viewbutton = Button(self.randomframe,
            text="View Calendar", font=("Atkinson Hyperlegible", 14),
            bg=DARKBLUE, fg="WHITE", width=1, height=1,
            command=lambda:[
                self.show_frame(CalendarPage),
                self.togglebuttonrelief(self.calendarbutton),
                self.randomframe.grid_remove()
            ])
        self.loggedinaslabel = Label(self.randomframe, 
            text="Logged in as:\n" + LOGINID, font=("Atkinson Hyperlegible", 14),
            bg=LAVENDER, fg="black", width=1, height=1)
        self.loggedinaslabel.grid(row=10, column=1, rowspan=2, columnspan=10, sticky=N+S+E+W)
        self.loggedinaslabel.grid_propagate(0)
        self.viewbutton.grid(row=5, column=1, rowspan=2, columnspan=5, sticky=N+S+E+W,padx=2)
        self.viewbutton.grid_propagate(0)
        self.editbutton = Button(self.randomframe,
            text="Edit Calendar", font=("Atkinson Hyperlegible", 14),
            bg=DARKBLUE, fg="WHITE", width=1, height=1,
            command=lambda:[print('yes')])
        self.editbutton.grid(row=5, column=6, rowspan=2, columnspan=5, sticky=N+S+E+W,padx=2)
        self.editbutton.grid_propagate(0)
        self.closebutton = Button(self.randomframe, 
            text="Close", font=("Atkinson Hyperlegible", 14),
            bg=DARKBLUE, fg="WHITE", width=1, height=1,
            command=lambda:[
                self.randomframe.grid_remove()
            ])
        self.closebutton.grid(row=8, column=1, rowspan=2, columnspan=10, sticky=N+S+E+W,padx=2)
        self.closebutton.grid_propagate(0)


        self.signoutbutton.grid_propagate(0)
        self.studentbutton.grid_propagate(0)
        self.adminbutton.grid_propagate(0)
        

class RegistrationPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LIGHTPURPLE)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #list comprehension to create lay out for the grid
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=2, bg=LIGHTPURPLE, relief="flat").grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=5, bg=LIGHTPURPLE, relief="flat").grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)
        # constants
        FONTNAME = "Avenir Next Medium"
        FIRSTNAME = "First Name"
        LASTNAME = "Last Name"
        EMAILTEXT = "Please enter your student email."
        PASSWORDTEXT = "Please enter your password."
        CONFPASSTEXT = "Please confirm your password."
        # database functions
        conn = sqlite3.connect('interactivesystem.db')
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
            #Raise an error if more than two @'s in the email
            if emailtext.count("@") > 1:
                messagebox.showerror("Invalid Email", "Please enter a valid email.")
            if emailtext.count("@") == 0:
                messagebox.showerror("Invalid Email", "Please enter a valid email.")
            try:
                emailending = emailfield.get().split("@")[1]
                namefield = emailfield.get().split("@")[0]
                if namefield == "":
                    messagebox.showerror("Invalid Email", "Please enter a valid email.")
                    return
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
                        controller.togglebuttonrelief(controller.loginbutton)
                        cleareveryentry()
                        
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Email already in use.")
            except IndexError:
                emailwarning.configure(text="You have not entered an email")
                messagebox.showerror("Error", "Please enter a valid email.")

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
            emailwarning.grid(row=5, column=34, columnspan=8, sticky=N+S+E+W)
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

        SCAMTEXT = "Please confirm your password "
        def clearconfpasswordfield():
            confirmpasswordfield.configure(fg="black")
            confirmpasswordfield.configure(show="*")
            if confirmpasswordfield.get() == CONFPASSTEXT or confirmpasswordfield.get() == SCAMTEXT:
                confirmpasswordfield.delete(0, END)
        def repopulateconfpasswordfield():    
            if confirmpasswordfield.get() != SCAMTEXT:    
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
            confirmpasswordfield.insert(0, SCAMTEXT)
            passwordfield.configure(show="")
            confirmpasswordfield.configure(show="")
  
            

        # Labels
        enterdetailslabel = Label(self, text="Please enter your details as shown in the entries.", font=(
            'Atkinson Hyperlegible', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        enterdetailslabel.grid(row=0, column=24,
                               rowspan=2, columnspan=17, sticky=N+S+E+W)

        # Entries
        firstnamefield = Entry(self, width=1, bg='#FFFFFF',
                               font=(FONTNAME, 18), justify='center')
        firstnamefield.grid(row=3, column=24,
                            rowspan=2, columnspan=7, sticky=N+S+E+W)
        firstnamefield.insert(0, FIRSTNAME)
        firstnamefield.grid_propagate(0)

        lastnamefield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        lastnamefield.grid(row=3, column=34,
                           rowspan=2, columnspan=7, sticky=N+S+E+W)
        lastnamefield.insert(0, LASTNAME)
        lastnamefield.grid_propagate(0)

        emailfield = Entry(self, width=1, bg='#FFFFFF',
                           font=(FONTNAME, 18), justify='center')
        emailfield.grid(row=6, column=24,
                        rowspan=2, columnspan=17, sticky=N+S+E+W)
        emailfield.insert(0, EMAILTEXT)
        emailfield.grid_propagate(0)

        passwordfield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        passwordfield.grid(row=9, column=24,
                           rowspan=2, columnspan=17, sticky=N+S+E+W)
        passwordfield.insert(0, PASSWORDTEXT)
        passwordfield.grid_propagate(0)

        confirmpasswordfield = Entry(
            self, width=1, bg='#FFFFFF', font=(FONTNAME, 18), justify='center')
        confirmpasswordfield.grid(row=12, column=24,
                                  rowspan=2, columnspan=17, sticky=N+S+E+W)
        confirmpasswordfield.insert(0, CONFPASSTEXT)
        confirmpasswordfield.grid_propagate(0)

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

        

        self.intibanner = Image.open(r"assets\Home-Banner-INTI.png")
        self.intibanner = ImageTk.PhotoImage(self.intibanner.resize(
            (math.ceil(420 * dpi / 96), math.ceil(160 * dpi / 96)), Image.Resampling.LANCZOS))
        self.logolabel = Button(self, image=self.intibanner,
                           anchor=CENTER, width=1, height=1,
                           background= NICEBLUE, 
                           command = lambda:aboutINTIcontainer())
        self.logolabel.grid(row=4, column=5, columnspan=11,
                       rowspan=5, sticky=N+S+E+W)
        self.logolabel.grid_propagate(0)
        self.titleart = Image.open(r"assets\DR7j7r0.png")
        self.titleart = ImageTk.PhotoImage(self.titleart.resize(
            (math.ceil(680 * dpi / 96), math.ceil(320 * dpi / 96)), Image.Resampling.LANCZOS))
        titleartlabel = Button(self, image=self.titleart,
                               background= NICEBLUE, 
                               anchor=CENTER, width=1, height=1)
        titleartlabel.grid(row=10, column=2, columnspan=17,
                           rowspan=8, sticky=N+S+E+W)
        titleartlabel.grid_propagate(0)
        # Buttons
        signupbutton = Button(self, text="SIGN UP", width=1, height=1, font=(
            'Atkinson Hyperlegible', 14), fg='#000000', command=lambda: checkfields(), bg=LIGHTYELLOW)
        signupbutton.grid(row=15, column=28, columnspan=9,
                          rowspan=2, sticky=N+S+E+W)
        signupbutton.grid_propagate(0)

        loginbutton = Button(self, text="Click here to sign in.",
        font=('Atkinson Hyperlegible', 14), width=1, height=1,
        fg='#000000', command=lambda: [
        controller.show_frame(LoginPage),
        controller.togglebuttonrelief(controller.loginbutton),
        cleareveryentry()],
        bg=OTHERPINK)
        loginbutton.grid(row=18, column=28, columnspan=9,
                         rowspan=2, sticky=N+S+E+W)
        loginbutton.grid_propagate(0)

        label = Label(self, text="This is the registration page on left frame\nCome back later, still under construction!", font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=17,
                   rowspan=2, sticky=N+S+E+W)
        label.grid_propagate(0)
        def aboutINTIcontainer():
            randomframe = Frame(controller, bg=NICEBLUE, width=1, height=1,
                                borderwidth=1, relief="flat")
            randomframe.grid(row=6, column=4, rowspan=10, columnspan=10,
                             sticky=N+S+E+W)
            randomframe.grid_propagate(0)
            # self.randomframe = randomframe
            for x in range(10):
                Grid.columnconfigure(randomframe, x, weight=1, uniform='row')
                Label(randomframe, height=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                  row=0, column=x, sticky=N+S+E+W)
            for y in range(10):
                Grid.rowconfigure(randomframe, y, weight=1, uniform='row')
                Label(randomframe, width=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                    row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W,)
            randomlabel = Label(randomframe, text="INTI COLLEGE LOL", font=("Comic Sans Ms", 18), width=1,height=1, fg="white",bg=DARKBLUE)
            randomlabel.grid(row=0, column=0, rowspan=1, columnspan=14, sticky=N+S+E+W)
            randomlabel.grid_propagate(0)
            randombutton = Button(randomframe, text="click me to close ", font=("Comic Sans Ms", 18), bg=DARKBLUE, fg="WHITE", command=lambda:[
            randomframe.grid_forget()])
            randombutton.grid(row=6, column=0, rowspan=1, columnspan=14, sticky=N+S+E+W)


class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LIGHTPURPLE)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=LIGHTPURPLE).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=5, bg=LIGHTPURPLE).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)
        # Database Functions for Logging in and setting loginstate to student or teacher
        # Sqlite3 commands to fetch registered emails from database and assigning roles based on email ending.
        # If email is not found in database, it will return an error message.
        # If email is found in database, it will return a success message.
        global dpi 
        conn = sqlite3.connect('interactivesystem.db')
        c = conn.cursor()

        def checkcredentials():
            global LOGGEDINAS
            global LOGINSTATE
            global LOGINID
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
                            LOGINID = email
                            controller.show_loggedin()
                            controller.welcomelabel(name, role)
                            controller.loggedinaslabel.configure(text=("Logged in as: ", email))
                        elif role == "admin":
                            messagebox.showinfo(
                                "Login Successful", "Welcome Admin!")
                            LOGGEDINAS = "Admin"
                            LOGINSTATE = True
                            LOGINID = email
                            controller.show_loggedin()
                            controller.show_admin()
                            controller.welcomelabel(name, role)
                            controller.loggedinaslabel.configure(text=(f"Logged in as:\n{email}"))


                            
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
            emailwarning.grid(row=6, column=34, columnspan=8,
                              rowspan=1, sticky=N+S+E+W)
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
        FONTNAME = "Avenir Next Medium"
        # Buttons
        # self.intibanner = Image.open(r"assets\Home-Banner-INTI.png")
        # self.intibanner = ImageTk.PhotoImage(self.intibanner.resize(
        #     (math.ceil(720 * dpi / 96), math.ceil(240 * dpi / 96)), Image.Resampling.LANCZOS))
        # logolabel = Button(self, image=self.intibanner,
        #                    anchor=CENTER, width=1, height=1)
        # logolabel.grid(row=1, column=24, columnspan=18,
        #                rowspan=5, sticky=N+S+E+W)
        self.backgroundimageoriginal = Image.open(r"Assets\backgroundimage.png")
        self.backgroundimage = ImageTk.PhotoImage(self.backgroundimageoriginal.resize(
            (math.ceil(1680 * dpi / 96), math.ceil(817 * dpi / 96)), Image.Resampling.LANCZOS))
        self.backgroundimagelabel = Label(self, image=self.backgroundimage, width=1, height=1, bg=LIGHTPURPLE)
        self.backgroundimagelabel.grid(row=0, column=0, rowspan=21, columnspan=43, sticky=N+S+E+W)
        self.backgroundimagelabel.grid_propagate(0)
        self.signinbuttonimage = Image.open(r"Assets\signinbutton.png")
        self.signinbuttonimage = ImageTk.PhotoImage(self.signinbuttonimage.resize(
            (math.ceil(444 * dpi / 96), math.ceil(81 * dpi / 96)), Image.Resampling.LANCZOS))
        self.signinbutton = Button(self, image=self.signinbuttonimage, width=1, height=1,
        bg=LIGHTPURPLE, relief="flat",command=lambda:signinbuttonpressed())
        self.signinbutton.grid(row=15, column=26, rowspan=2, columnspan=11, sticky=N+S+E+W)
        self.signinbutton.grid_propagate(0)
        self.signupbuttonimage = Image.open(r"Assets\signupbutton.png")
        self.signupbuttonimage = ImageTk.PhotoImage(self.signupbuttonimage.resize(
            (math.ceil(605 * dpi / 96), math.ceil(81 * dpi / 96)), Image.Resampling.LANCZOS))
        self.signupbutton = Button(self, image=self.signupbuttonimage, width=1, height=1,
        bg=LIGHTPURPLE, borderwidth=1, relief="flat", command=lambda:[controller.show_frame(RegistrationPage),
        controller.togglebuttonrelief(controller.signupbutton)])
        self.signupbutton.grid(row=18, column=24, rowspan=2, columnspan=15,sticky=N+S+E+W)
        self.signupbutton.grid_propagate(0)
        emailwarning = Label(self, text="Please enter a valid email address.", font=(
            'Arial', 10), width=1, height=1, fg='#000000', bg='#FFF5E4')
        emailfield = Entry(self, width=1, bg='#FFFFFF', highlightthickness=1,
                           font=(FONTNAME, 14), justify='center')
        emailfield.grid(row=7, column=25, columnspan=13,
                        rowspan=2, sticky=N+S+E+W)
        emailfield.insert(0, EMAILTEXT)
        emailfield.grid_propagate(0)
        passwordfield = Entry(self, width=1, bg='#FFFFFF', highlightthickness=1,
                              font=(FONTNAME, 14), justify='center')
        passwordfield.grid(row=12, column=25, columnspan=13,
                           rowspan=2, sticky=N+S+E+W)
        passwordfield.insert(0, PASSWORDTEXT)
        passwordfield.grid_propagate(0)
        emailfield.bind("<FocusIn>", lambda a: clearemailfield())
        emailfield.bind("<FocusOut>", lambda a: repopulateemailfield())
        passwordfield.bind("<FocusIn>", lambda a: clearpasswordfield())
        passwordfield.bind("<FocusOut>", lambda a: repopulatepasswordfield())

        # signinbutton = Button(self, text="SIGN IN", font=(
        #     'Arial', 18), width=1, height=1, bg=LIGHTYELLOW, fg='#000000', command=lambda: signinbuttonpressed())
        # signinbutton.grid(row=13, column=28, columnspan=9,
        #                   rowspan=2, sticky=N+S+E+W)
        # ortext = Label(self, text="------OR------", font=('Arial', 18), width=1,
        #                height=1, fg='#000000', bg='#FFF5E4')
        # ortext.grid(row=15, column=28, columnspan=9,
        #             rowspan=1, sticky=N+S+E+W)

        # signupbutton = Button(self, text="Not a member yet?\n Click here to sign up", font=(
        #     'Arial', 18), width=1, height=1, fg='#000000', command=lambda: [
        #     controller.show_frame(RegistrationPage)], bg=OTHERPINK)
        # signupbutton.grid(row=16, column=28, columnspan=9,
        #                   rowspan=2, sticky=N+S+E+W)

        def checkstate():
            global LOGGEDINAS
            print(LOGGEDINAS)
        # signoutbutton = Button(self, text="SIGN OUT", font=(
        #     'Arial', 18), width=1, height=1, bg=LIGHTYELLOW, fg='#000000', command=lambda: changedtologout())
        # signoutbutton.grid(row=18, column=28, columnspan=9,
                        #    rowspan=2, sticky=N+S+E+W)
        checkstatebutton = Button(
            self, text="Check state", command=lambda: checkstate())
        checkstatebutton.grid(row=17, column=40, columnspan=4,
                              rowspan=2, sticky=N+S+E+W)
        checkstatebutton.grid_propagate(0)

        # self.titleart = Image.open(r"assets\DR7j7r0.png")
        # self.titleart = ImageTk.PhotoImage(self.titleart.resize(
        #     (math.ceil(780 * dpi / 96), math.ceil(320 * dpi / 96)), Image.Resampling.LANCZOS))
        # titleartlabel = Button(self, image=self.titleart,
        #                        background= NICEBLUE, 
        #                        anchor=CENTER, width=1, height=1)
        # titleartlabel.grid(row=8, column=2, columnspan=20,
        #                    rowspan=8, sticky=N+S+E+W)
        #random label attributed to self
        def resize():
            dimensions = [controller.winfo_width(), controller.winfo_height()]
            if controller.winfo_width() != dimensions[0] or controller.winfo_width != dimensions[1]:
                self.backgroundimageoriginal = Image.open(r"Assets\backgroundimage.png")
                self.backgroundimage = ImageTk.PhotoImage(self.backgroundimageoriginal.resize(
            (math.ceil(1680 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
                self.backgroundimagelabel.config(image=self.backgroundimage)
        global eventID
        eventID = None
        controller.resizeDelay = 100
        def resizeEvent(event):
            global eventID
            if eventID:
                controller.after_cancel(eventID)
            if controller.state() == "zoomed":
                eventID = controller.after(controller.resizeDelay, resize)
        controller.bind('<Configure>', resizeEvent)
        def aboutINTIcontainer():
            randomframe = Frame(controller, bg=NICEBLUE, width=1, height=1,
                                borderwidth=1, relief="flat")
            randomframe.grid(row=6, column=4, rowspan=10, columnspan=10,
                             sticky=N+S+E+W)
            randomframe.grid_propagate(0)
            # self.randomframe = randomframe
            for x in range(10):
                Grid.columnconfigure(randomframe, x, weight=1, uniform='row')
                Label(randomframe, height=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                  row=0, column=x, sticky=N+S+E+W)
            for y in range(10):
                Grid.rowconfigure(randomframe, y, weight=1, uniform='row')
                Label(randomframe, width=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                    row=y, column=0, rowspan=2, columnspan=1, sticky=N+S+E+W,)
            randomlabel = Label(randomframe, text="INTI SUCKS LOL", font=("Comic Sans Ms", 18), fg="white",bg=DARKBLUE)
            randomlabel.grid(row=0, column=0, rowspan=1, columnspan=14, sticky=N+S+E+W)
            randomlabel.grid_propagate(0)
            randombutton = Button(randomframe, text="click me to close ", font=("Comic Sans Ms", 18), bg=DARKBLUE, fg="WHITE", command=lambda:[
            randomframe.grid_forget()])
            randombutton.grid(row=6, column=0, rowspan=1, columnspan=14, sticky=N+S+E+W,pady=5)

    def hidealabel(self):
        self.label.grid_remove()
    def showalabel(self):
        self.label.grid()

class MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=LAVENDER).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=5, bg=LAVENDER).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)

        # Picture
        self.originalimage = Image.open(r"assets\Home-Banner-INTI.png")
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

        self.calendarimage = Image.open(r"assets\Calendar.png")
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
        feedbackbutton = Button(self, image=self.feedbackimage, width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [
        controller.show_frame(FeedbackForm),
        controller.togglebuttonrelief(controller.feedbackbutton)
        ])
        feedbackbutton.grid(row=8, column=2, columnspan=16,
                            rowspan=4, sticky=N+S+E+W)
        imagelabel = Label(self, image=self.feedbackimage,
                           anchor=CENTER, width=1, height=1)

        eventnamebutton = Button(self, text="Event 1", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])

        eventnamebutton.grid(row=15, column=2, columnspan=16,
                             rowspan=1, sticky=N+S+E+W)
        eventsnamebutton = Button(self, text="Event 2", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        eventsnamebutton.grid(row=16, column=2, columnspan=16,
                              rowspan=1, sticky=N+S+E+W)

        aneventnamebutton = Button(self, text="Event 3", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        aneventnamebutton.grid(row=17, column=2, columnspan=16,
                               rowspan=1, sticky=N+S+E+W)

        theeventnamebutton = Button(self, text="Event 4", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        theeventnamebutton.grid(row=18, column=2, columnspan=16,
                                rowspan=1, sticky=N+S+E+W)

        eventlistbutton = Button(self, text="Event List", font=(
        'Lucida Calligraphy', 16), width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        eventlistbutton.grid(row=16, column=20, columnspan=5,
                             rowspan=3, sticky=N+S+E+W)

        eventregistrationbutton = Button(self, text="Event\nRegistration", font=(
        'Lucida Calligraphy', 16), width=1, height=1, fg='#000000', bg='#FFF5E4',  command=lambda:
        [controller.show_frame(EventRegistration),
        controller.togglebuttonrelief(controller.eventregistrationbutton)])
        eventregistrationbutton.grid(row=16, column=28, columnspan=5,
                                     rowspan=3, sticky=N+S+E+W)

        calendarbutton = Button(self, text="Calendar", font=(
            'Lucida Calligraphy', 16), width=1, height=1, fg='#000000', bg='#FFF5E4', command=
            lambda: [
            controller.show_frame(CalendarPage),
            controller.togglebuttonrelief(controller.calendarbutton)])
        calendarbutton.grid(row=16, column=36, columnspan=5,
                            rowspan=3, sticky=N+S+E+W)

        self.logoutimage = Image.open(r"assets\logoutbutton.png")
        self.logoutimage = ImageTk.PhotoImage(self.logoutimage.resize(
            (math.ceil(38 * dpi / 96), math.ceil(38 * dpi / 96)), Image.Resampling.LANCZOS)),
        logoutbutton = Button(self,image=self.logoutimage , width=1, height=1, fg='#000000', bg='#FFF5E4',command=lambda:
            [controller.show_frame(LoginPage), controller.togglebuttonrelief(controller.loginbutton),
            controller.signout()])
        logoutbutton.grid(row=0, column=41, columnspan=1, rowspan=1, sticky=N+S+E+W)
        imagelabel = Label(self, image=self.logoutimage, anchor=CENTER, width=1, height=1)


class EventView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=LAVENDER).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=5, bg=LAVENDER).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)

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

class EventRegistration(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=PINK)
        FONTNAME = "Avenir Next"
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=PINK).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=5, bg=PINK).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)

        # Connect to database
        conn = sqlite3.connect('interactivesystem.db')
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
                        controller.togglebuttonrelief(controller.eventlistbutton)
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Email already registered")

        def defocus(event):
            event.widget.master.focus_set()
            refresh()
        def focusout(event):
            self.read_blob(self.eventdropdown.get())

        #Event Registration page background image)
        self.bgwallpaper = Image.open(r"Assets\EventRegistration\EventRegistration.jpg")
        self.bgwall = ImageTk.PhotoImage(self.bgwallpaper.resize(
             (math.ceil(1680 * dpi / 96), math.ceil(817 * dpi / 96)), Image.Resampling.LANCZOS))
        self.bgwalllabel = Label(self, image=self.bgwall, width=1, height=1, bg=LIGHTPURPLE)
        self.bgwalllabel.grid(row=0, column=0, rowspan=21, columnspan=43, sticky=N+S+E+W)
        self.bgwalllabel.grid_propagate(0)

        # Widgets
        label = Label(self, text="This is the event registration page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=18,
                   rowspan=1, sticky=N+S+E+W)
        label.grid_propagate(0)
        #dropdown for events
        conn = sqlite3.connect('interactivesystem.db')
        # Create cursor
        c = conn.cursor()
        event_list = ["Select an event"]
        #refresh the event_list everytime the combobox is selected
        def refresh():
            c.execute("SELECT event_name FROM eventcreation")
            event_list.clear()
            event_list.append("")
            for row in c.fetchall():
                event_list.append(row[0])
            self.eventdropdown['values'] = event_list
        
        try:
            with conn:
                c.execute("""SELECT event_name FROM eventcreation""")
                for eventname in c.fetchall():
                    event_list.append(eventname)
        except sqlite3.OperationalError:
            c.execute("""CREATE TABLE IF NOT EXISTS eventcreation (
            event_name text NOT NULL,
            eventkey_number text PRIMARY KEY NOT NULL, 
            venue_name text,
            hostname text NOT NULL
            )""")

        self.eventdropdown = ttk.Combobox(
            self, values=event_list, width=1, state='readonly')
        self.eventdropdown.current(0)
        self.eventdropdown.grid(row=1, column=2, columnspan=18,
                           rowspan=2, sticky=NSEW)
        self.eventdropdown.bind('<FocusIn>', defocus)
        self.eventdropdown.bind('<<ComboboxSelected>>', focusout)
        self.eventdropdown.grid_propagate(0)
        
        separator = ttk.Separator(self, orient=HORIZONTAL)
        separator.grid(row=3, column=3, columnspan=16, pady=5, sticky=EW)
        icpasslabel = Label(self, text="IC No.",
                            font=(FONTNAME, 10), bg='#FFF5E4')
        icpasslabel.grid(row=7, column=3, columnspan=2,
                         rowspan=2, sticky=N+S+E+W)
        icpasslabel.grid_propagate(0)
        phonenumberlabel = Label(
            self, text="Phone\nNo", font=(FONTNAME, 10), bg='#FFF5E4')
        phonenumberlabel.grid(
            row=10, column=3, columnspan=2, rowspan=2, sticky=N+S+E+W)
        emaillabel = Label(self, text="Email", font=(
            FONTNAME, 14), bg='#FFF5E4')
        emaillabel.grid(row=13, column=3, columnspan=2,
                        rowspan=2, sticky=N+S+E+W)
        emaillabel.grid_propagate(0)
        addresslabel = Label(self, text="Address",
                             font=(FONTNAME, 10), bg='#FFF5E4')
        addresslabel.grid(row=16, column=3, columnspan=2,
                          rowspan=2, sticky=N+S+E+W)
        addresslabel.grid_propagate(0)

        # radio_1 = ttk.Radiobutton(self, text="Male  ", variable=var, value=0)
        # radio_1.grid(row=9, column=5,rowspan=2, columnspan=2, pady=(0, 10), sticky=NS)

        # radio_1 = ttk.Radiobutton(self, text="Female", variable=var, value=1, command=lambda:print(var.get()))
        # radio_1.grid(row=9, column=7,rowspan=2, columnspan=2, pady=(0, 10), sticky=NS)

        fullnamefield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        fullnamefield.grid(row=4, column=3, columnspan=16,
                           rowspan=2, sticky=N+S+E+W)
        fullnamefield.insert(0, "Full Name")

        icnumberfield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        icnumberfield.grid(row=7, column=5, columnspan=14,
                           rowspan=2, sticky=N+S+E+W)
        phonenumentry = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        phonenumentry.grid(row=10, column=5, columnspan=14,
                           rowspan=2, sticky=N+S+E+W)
        emailentry = Entry(self, width=1, bg='#FFFFFF',
                           font=(FONTNAME, 18), justify='center')
        emailentry.grid(row=13, column=5, columnspan=14,
                        rowspan=2, sticky=N+S+E+W)
        addressentry = Entry(self, width=1, bg='#FFFFFF',
                             font=(FONTNAME, 18), justify='center')
        addressentry.grid(row=16, column=5, columnspan=14,
                          rowspan=2, sticky=N+S+E+W)
        # Buttons
        cancelbutton = Button(self, text="Cancel", font=(FONTNAME, 14), bg='White', command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        cancelbutton.grid(row=18, column=3, columnspan=6,
                          rowspan=2, sticky=N+S+E+W)
        confirmbutton = Button(self, text="Confirm", font=(
            FONTNAME, 14), bg='White', command=lambda: submit())
        confirmbutton.grid(row=18, column=13, columnspan=6,
                           rowspan=2, sticky=N+S+E+W)
        self.panel = Label(self, image="",width=1,height=1, bg=ORANGE)
        self.panel.grid(row=4, column=22, columnspan=16,
                    rowspan=10, sticky=N+S+E+W)
        self.panel.grid_propagate(0)
    def read_blob(self, event_name):
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("SELECT event_image FROM eventcreation WHERE event_name=?", (event_name,))
            self.blobData = io.BytesIO(self.c.fetchone()[0])
            self.img = Image.open(self.blobData)
            self.img = ImageTk.PhotoImage(self.img.resize(
                 (math.ceil(605 * dpi / 96), math.ceil(400 * dpi / 96)), Image.Resampling.LANCZOS))
            self.panel.config(image=self.img)
            self.panel.grid_propagate(0)

class EventCreation(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=PINK)
        FONTNAME = "Arial"
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=1, bg=PINK).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=5, bg=PINK).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)
        # Connect to database
        self.conn = sqlite3.connect('interactivesystem.db')
        # Create cursor
        self.c = self.conn.cursor()
        # Create a table
        # self.c.execute("""DROP TABLE eventcreation""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS eventcreation (
            eventkey_number TEXT PRIMARY KEY NOT NULL, 
            event_name TEXT NOT NULL,
            event_description TEXT NOT NULL,
            event_startdate TEXT NOT NULL,
            event_enddate TEXT NOT NULL,
            event_starttime TEXT NOT NULL,
            event_endtime TEXT NOT NULL,
            event_organizer TEXT NOT NULL,
            venue_name TEXT,
            host_name TEXT NOT NULL,
            event_image BLOB NULL
            )""")
        # Send entries to database

        global dpi
       #Event Creation page background image)
        self.bgimageoriginal = Image.open(r"Assets\EventCreation\Aesthetic anime pc wallpaper _3.jpg")
        self.bgimage = ImageTk.PhotoImage(self.bgimageoriginal.resize(
             (math.ceil(1680 * dpi / 96), math.ceil(817 * dpi / 96)), Image.Resampling.LANCZOS))
        self.bgimagelabel = Label(self, image=self.bgimage, width=1, height=1, bg=LIGHTPURPLE)
        self.bgimagelabel.grid(row=0, column=0, rowspan=21, columnspan=43, sticky=N+S+E+W)
        self.bgimagelabel.grid_propagate(0)

        # Widgets
        label = Label(self, text="This is the event creation page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=18,
                   rowspan=2, sticky=N+S+E+W)
        label.grid_propagate(0)

       
        separator = ttk.Separator(self, orient=HORIZONTAL)
        separator.grid(row=5, column=3, columnspan=17, pady=5, sticky=EW)
        separator.grid_propagate(0)
        eventkeylabel = Label(self, text="Event\nNo.",
                            font=(FONTNAME, 14), bg='#FFF5E4')
        eventkeylabel.grid(row=12, column=3, columnspan=2,
                            rowspan=2, sticky=N+S+E+W)
        eventkeylabel.grid_propagate(0)
        venuenamelabel = Label(
            self, text="Venue\nName",
            width=1,height=1,
            font=(FONTNAME, 14), bg='#FFF5E4')
        venuenamelabel.grid(
            row=15, column=3, columnspan=2, rowspan=2, sticky=N+S+E+W)
        venuenamelabel.grid_propagate(0)
        hostnamelabel = Label(self, text="Host\nName", 
        font=(FONTNAME, 14),
        width=1,height=1,
        bg='#FFF5E4')
        hostnamelabel.grid(row=15, column=12, columnspan=2,
                        rowspan=2, sticky=N+S+E+W)
        hostnamelabel.grid_propagate(0)
        organizinglabel = Label(self, text="Organized\nBy", font=(
            FONTNAME, 14), bg='#FFF5E4', width=1, height=1)
        organizinglabel.grid(row=12, column=12, columnspan=2,
                            rowspan=2, sticky=N+S+E+W)
        organizinglabel.grid_propagate(0)

        self.eventnamefield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        self.eventnamefield.grid(row=6, column=3, columnspan=17,
                           rowspan=2, sticky=N+S+E+W)
        self.eventnamefield.insert(0, "Event Name")
        self.eventnamefield.grid_propagate(0)
        self.eventkeyfield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        self.eventkeyfield.grid(row=12, column=5, columnspan=6,
                           rowspan=2, sticky=N+S+E+W)
        self.eventkeyfield.grid_propagate(0)
        self.organizerfield = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 18), justify='center')
        self.organizerfield.grid(row=12, column=14, columnspan=6,
                                    rowspan=2, sticky=N+S+E+W)
        self.organizerfield.grid_propagate(0)
        self.organizerfield.insert(0, "Organizing School")
        self.venuenameentry = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        self.venuenameentry.grid(row=15, column=5, columnspan=6,
                           rowspan=2, sticky=N+S+E+W)
        self.venuenameentry.grid_propagate(0)
        self.hostnameentry = Entry(self, width=1, bg='#FFFFFF',
                           font=(FONTNAME, 18), justify='center')
        self.hostnameentry.grid(row=15, column=14, columnspan=6,
                        rowspan=2, sticky=N+S+E+W)
        self.hostnameentry.grid_propagate(0)
        self.eventdescription = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        self.eventdescription.grid(row=9, column=3, columnspan=17,
                            rowspan=2, sticky=N+S+E+W)
        self.eventdescription.insert(0, "Event Description")
        self.eventdescription.grid_propagate(0)
        # Upload image functionality
        self.readblobentry = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 12), justify='center')
        self.readblobentry.grid(row=16, column=38, columnspan=4,
                            rowspan=2, sticky=N+S+E+W)
        self.readblobentry.insert(0, "Enter a event key\n to find image")
        uploadimagebutton = Button(self, text="Upload Image", width=1,height=1,
        font=(FONTNAME, 14), bg='#FFF5E4', command=lambda:self.upload_image())
        uploadimagebutton.grid(row=15, column=22, columnspan=8,
                                 rowspan=2, sticky=N+S+E+W)
        uploadimagebutton.grid_propagate(0)
        submitbutton = Button(self, text="Submit", width=1,height=1, font=(
            FONTNAME, 14), bg='#FFF5E4', command=lambda:self.submit())
        submitbutton.grid(row=18, column=22, columnspan=8,
                            rowspan=2, sticky=N+S+E+W)
        submitbutton.grid_propagate(0)
        deleteimagebutton = Button(self, text="Delete Image", width=1,height=1,
        font=(FONTNAME, 14), bg='#FFF5E4', command=lambda:self.delete_image())
        deleteimagebutton.grid(row=15, column=30, columnspan=8,
                                    rowspan=2, sticky=N+S+E+W)
                                    
        readblobbutton = Button(self, text="Read Blob", font=(
            FONTNAME, 14), bg='#FFF5E4', command=lambda:self.read_blob(self.readblobentry.get()))
        readblobbutton.grid(row=18, column=30, columnspan=8,
                                    rowspan=2, sticky=N+S+E+W)
        readblobbutton.grid_propagate(0)
        #Store image into the eventcreation table 
        # self.c.execute("ALTER TABLE eventcreation ADD COLUMN image BLOB")
        # conn.commit()
        # c.execute("SELECT * FROM eventcreation")
        # print(c.fetchall())
        # Buttons
        
        cancelbutton = Button(self, text="Cancel", 
        width=1,height=1,
        font=(FONTNAME, 10), bg='White', 
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        cancelbutton.grid(row=18, column=3, columnspan=6,
                          rowspan=2, sticky=N+S+E+W)
        cancelbutton.grid_propagate(0)
        confirmbutton = Button(self, text="Confirm",
        width=1,height=1,
        font=(FONTNAME, 14), bg='White', command=lambda: self.insert_blob())
        confirmbutton.grid(row=18, column=13, columnspan=6,
                           rowspan=2, sticky=N+S+E+W)
        confirmbutton.grid_propagate(0)
        self.panel = Label(self, image="",width=1,height=1, bg=ORANGE)
        self.panel.grid(row=1, column=22, columnspan=18,
                    rowspan=12, sticky=N+S+E+W)
        self.panel.grid_propagate(0)
        self.filename = ""
        #start date
        self.fromlabel = Label(self, text="Start Date", font=(FONTNAME, 10), bg=NICEBLUE)
        self.fromlabel.grid(row=3, column=2, columnspan=2,  
                          rowspan=1, sticky=N+S+E+W)    
        self.date_entrywidget = DateEntry(self, height=1, width=1, background=NAVYBLUE, 
        headersbackground = ORANGE,
        font=("Avenir Next Medium",20), justify='center',
        date_pattern='dd/mm/yyyy') 
        self.date_entrywidget.grid(row=3, column=4, columnspan=5,
                            rowspan=1, sticky=N+S+E+W)
        self.date_entrywidget.grid_propagate(0)
        #end date

        self.tolabel = Label(self, text="End Date", font=(FONTNAME, 10), bg=NICEBLUE)
        self.tolabel.grid(row=4, column=2, columnspan=2,
                            rowspan=1, sticky=N+S+E+W)
    
        self.date_entrywidget2 = DateEntry(self, height=1, width=1, background=NAVYBLUE,
        headersbackground = ORANGE,
        font=("Avenir Next Medium",20), justify='center',
        date_pattern='dd/mm/yyyy')
        self.date_entrywidget2.grid(row=4, column=4, columnspan=5,
                            rowspan=1, sticky=N+S+E+W)
        self.date_entrywidget2.grid_propagate(0)
        
        #time entry widget using two entries for hour and minutes and then am pm 
        #start time label
        starttimelabel = Label(self, text="Start Time", font=(FONTNAME, 10), bg=NICEBLUE)
        starttimelabel.grid(row=3, column=9, columnspan=2,
                            rowspan=1, sticky=N+S+E+W)
        self.hourentry = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 18), justify='center')
        self.hourentry.grid(row=3, column=11, columnspan=3,
                            rowspan=1, sticky=N+S+E+W)
        self.hourentry.insert(0, "Hour")
        self.minentry = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 18), justify='center')
        self.minentry.grid(row=3, column=15, columnspan=3,
                            rowspan=1, sticky=N+S+E+W)
        self.minentry.insert(0, "Min")
        #Am pm menu 
        self.am_pm = StringVar(self)
        self.am_pm.set("AM") # default value
        self.am_pm_menu = OptionMenu(self, self.am_pm, "AM", "PM")
        self.am_pm_menu.config(width=1, font=(FONTNAME, 18), bg='White')
        self.am_pm_menu.grid(row=3, column=18, columnspan=2,
                            rowspan=1, sticky=N+S+E+W)
        #: label for start time
        colonlabel = Label(self, text=":", font=(FONTNAME, 12), bg=NICEBLUE)
        colonlabel.grid(row=3, column=14, columnspan=1,
                            rowspan=1, sticky=N+S+E+W) 
        #: label for end time
        colonlabel2 = Label(self, text=":", font=(FONTNAME, 12), bg=NICEBLUE)
        colonlabel2.grid(row=4, column=14, columnspan=1,
                            rowspan=1, sticky=N+S+E+W)  
        #End time entry widget
        endtimelabel = Label(self, text="End Time", font=(FONTNAME, 12), bg=NICEBLUE)
        endtimelabel.grid(row=4, column=9, columnspan=2,
                            rowspan=1, sticky=N+S+E+W)  
        self.endhourentry = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 18), justify='center')
        self.endhourentry.grid(row=4, column=11, columnspan=3,
                            rowspan=1, sticky=N+S+E+W)
        self.endhourentry.insert(0, "Hour")
        self.endminentry = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 18), justify='center')
        self.endminentry.grid(row=4, column=15, columnspan=3,
                            rowspan=1, sticky=N+S+E+W)
        self.endminentry.insert(0, "Min")
        #Am pm menu
        self.endam_pm = StringVar(self)
        self.endam_pm.set("AM") # default value
        self.endam_pm_menu = OptionMenu(self, self.endam_pm, "AM", "PM")
        self.endam_pm_menu.config(width=1, font=(FONTNAME, 12), bg='White')
        self.endam_pm_menu.grid(row=4, column=18, columnspan=2,
                            rowspan=1, sticky=N+S+E+W)
        

        self.date_entrywidget.grid_propagate(0)
        self.date_entrywidget.set_date(datetime.date.today())
        self.date_entrywidget.bind("<<DateEntrySelected>>", self.onDateSelected)
    def onDateSelected(self, event):
        self.date = self.date_entrywidget.get_date()
        print(self.date)


        # Widgets
    def upload_image(self):
        global dpi
        self.filename = filedialog.askopenfilename(initialdir="/",
                                                title="Select A File",
                                                filetypes=(("png files", "*.png"),("jpeg files", "*.jpg"), ("all files", "*.*")))
        #This is the file we need to make as a blob
        self.img = Image.open(self.filename)
        self.img = ImageTk.PhotoImage(self.img.resize(
            (math.ceil(706 * dpi / 96), math.ceil(468 * dpi / 96)), Image.Resampling.LANCZOS))
        # Presents the images for future editing purposes or to just submit right away
        #store self.filename in the global name space
        self.panel.configure(image=self.img)

    def convert_to_binary_data(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData
    def insert_blob(self):
            eventkey_number = self.eventkeyfield.get()
            event_nametext = self.eventnamefield.get()
            event_descriptiontext = self.eventdescription.get()
            event_startdate = self.date_entrywidget.get_date()
            event_enddate = self.date_entrywidget2.get_date()
            event_starttime = self.hourentry.get() + ":" + self.minentry.get() + " " + self.am_pm.get()
            event_endtime = self.endhourentry.get() + ":" + self.endminentry.get() + " " + self.endam_pm.get()
            event_organizer = self.organizerfield.get()
            venue_name = self.venuenameentry.get()
            hostname = self.hostnameentry.get()
            self.filename = self.filename
            self.blobData = self.convert_to_binary_data(self.filename)
            information = (eventkey_number, event_nametext, event_descriptiontext, event_startdate, event_enddate, event_starttime, event_endtime, event_organizer, venue_name, hostname, self.blobData)
            # Insert BLOB into table
            self.conn = sqlite3.connect('interactivesystem.db')
            self.c = self.conn.cursor()
            try:
                with self.conn:
                    #alter the table to add event description, event key, event date, event start time, 
                    # event end time, event organizer, venue name, host name
                    self.c.execute("""INSERT INTO eventcreation
                    (eventkey_number, event_name, event_description, event_startdate, event_enddate, event_starttime, event_endtime, event_organizer, venue_name, host_name, event_image) VALUES(?,?,?,?,?,?,?,?,?,?,?)""",
                    (information))
                    messagebox.showinfo("Success", "Event Created")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Event Key already exists")

    def read_blob(self, eventkey_number):
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("SELECT event_image FROM eventcreation WHERE eventkey_number = ?", (eventkey_number,))
            self.blobData = io.BytesIO(self.c.fetchone()[0])
            self.img = Image.open(self.blobData)
            self.img = ImageTk.PhotoImage(self.img.resize(
                 (math.ceil(706 * dpi / 96), math.ceil(468 * dpi / 96)), Image.Resampling.LANCZOS))
            self.panel.config(image=self.img)
            self.panel.grid_propagate(0)

    def submit_image(self):
        global dpi
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        with self.conn:
            with open(self.filename, 'rb') as f:
                self.blob = f.read()
            self.c.execute("UPDATE eventcreation SET image = ? WHERE eventkey = ?", (self.blob,
            self.eventkeyfield.get()))
            self.c.execute("SELECT * FROM eventcreation")
            print(self.c.fetchall())
    def delete_image(self):
        self.panel.configure(image="")


            


class ViewParticipants(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=PINK)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=PINK).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=5, bg=PINK).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)

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
            "Helvetica", 18), justify="center", bd=1)
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

        # Widgets
        label = Label(self, text="This is the view participants page for admins\n Still under construction :)", font=(
            'Segoe Ui Semibold', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=12, columnspan=18,
                   rowspan=2, sticky=N+S+E+W)


class FeedbackForm(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=PINK)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=PINK, relief="flat").grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=5, bg=PINK, relief="flat").grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)

        # Widgets
        label = Label(self, text="This is a feedback form to help us improve our app.\nPlease answer the questions below to the best of your ability.\nThank you for your time!", font=(
            'Segoe Ui Semibold', 14), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=10, columnspan=22,
                   rowspan=2, sticky=N+S+E+W)
        conn = sqlite3.connect('interactivesystem.db')
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

        scaleofsatisfaction = [("1", "Very Unsatisfied"), ("2", "Unsatisfied"),
                               ("3", "Neutral"), ("4", "Satisfied"), ("5", "Very Satisfied")]  # Scale for satisfaction
        scaleofhelpful = [("1", "Very Unhelpful"), ("2", "Unhelpful"), ("3", "Plain"),
                          ("4", "Helpful"), ("5", "Very Helpful")]  # Scale for helpful
        scaleoflikelihood = [("1", "Very Unlikely"), ("2", "Unlikely"), ("3", "Neutral"), (
            "4", "Likely"), ("5", "Very Likely")]  # Example if want to create a scale for likelihood
        scaleofeasiness = [("1", "Very Difficult"), ("2", "Difficult"), ("3", "Neutral"), (
            "4", "Easy"), ("5", "Very Easy")]  # If want to create an easiness scale question
        # messagebox.showinfo("Welcome to the survey!", "This is a survey to help us improve our app. Please answer the questions below to the best of your ability. Thank you for your time!")
        yesnooptions = ["No", "Yes"]

        # Label
        question1label = Label(self, text="How would you rate our announcement system for your overall experience? ",
        font=("Helvetica", 14), width=1, height=1,
        bg=LIGHTYELLOW)
        question1label.grid(row=4, column=10, columnspan=22,
                            rowspan=1, sticky=NSEW)
        question1answer = StringVar()
        question1answer.set("Neutral")  # Satisfaction Q
        question2label = Label(self, text="Is this system very helpful to you that you are not miss or neglect any event? ", 
        font=("Helvetica", 14), width=1, height=1,
        bg=LIGHTYELLOW)
        question2label.grid(row=6, column=10, columnspan=22,
                            rowspan=1, sticky=NSEW)
        question2answer = StringVar()
        question2answer.set("Neutral")  # Satisfaction Q
        question3label = Label(self, text="How likely are you to recommend our app to your friends?",
        font=("Helvetica", 14), bg=LIGHTYELLOW)
        question3label.grid(row=8, column=10, columnspan=22,
                            rowspan=1, sticky=NSEW)
        question3answer = StringVar()
        question3answer.set("Neutral")  # Likelihood Q

        question4label = Label(self, text="How difficult / easy was it to find the event on this app?",
        font=("Helvetica", 14), width=1, height=1,
        bg=LIGHTYELLOW)
        question4label.grid(row=10, column=10, columnspan=22,
                            rowspan=1, sticky=NSEW)
        question4answer = StringVar()
        question4answer.set("Neutral")  # Easiness Q
        yesnoquestionlabel = Label(self, text="Were you able to find information you needed about the events?",
        font=("Helvetica", 14), width=1, height=1,
        bg=LIGHTYELLOW)
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
                bg=ORANGE, font=("Helvetica", 18), height=1, width=1)
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
                    bg=ORANGE, font=("Helvetica", 18), width=1, height=1)
            # count becomes the column number, 12, 16, 20, 24, 28
            self.secondrow.grid(row=7, column=count2,
                                rowspan=1, columnspan=2, sticky=N+S+E+W)
            self.secondrow.grid_propagate(0)
            count2 += 4

        # Creating Likelihood Scale
        for text, rating in scaleoflikelihood:
            self.thirdrow = Radiobutton(self, text=text, variable=question3answer, value=rating, bg=ORANGE, font=("Helvetica", 18),
                                        justify=CENTER, width=1, height=1)
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
                                         justify=CENTER, width=1, height=1)
            self.fourthrow.grid(row=11, column=count4,
                                rowspan=1, columnspan=2, sticky=N+S+E+W)
            self.fourthrow.grid_propagate(0)
            count4 += 4

        # Creating Yes No
        for text in yesnooptions:
            self.fifthrow = Radiobutton(self, text=text, variable=yesnoquestionanswer, value=text, bg=ORANGE, font=("Helvetica", 18),
                                        justify=CENTER, width=1, height=1)
            self.fifthrow.grid(row=13, column=count5,
                               rowspan=2, columnspan=3, sticky=N+S+E+W)
            self.fifthrow.grid_propagate(0)
            count5 += 11

        # Open Question
        openendquestionlabel = Label(self, text="Please leave any comments or suggestions below:", font=(
            "Helvetica", 14), width=1, height=1, bg=LIGHTYELLOW)
        openendquestionlabel.grid(
            row=15, column=10, columnspan=22, rowspan=1, sticky=NSEW)
        openendedentry = Entry(self, width=1, bg="white",
                               font=("Helvetica", 18), justify=CENTER)
        openendedentry.grid(row=16, column=10, columnspan=22,
                            rowspan=2, sticky=NSEW)

        # labels for scale
        satisfactionlabel = Label(self, text="More Unsatisfied", font=(
            "Helvetica", 11), bg=NICEPURPLE, justify="left", width=1, height=1)
        satisfactionlabel.grid(
            row=4, column=10, columnspan=2, rowspan=1, sticky=NSEW)
        dissatisfactionlabel = Label(self, text="More satisfied", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right", width=1, height=1)
        dissatisfactionlabel.grid(
            row=4, column=30, columnspan=2, rowspan=1, sticky=NSEW)
        unhelpfullabel = Label(self, text="Very Unhelpful", font=(
            "Helvetica", 11), bg=NICEPURPLE, justify="left", width=1, height=1)
        unhelpfullabel.grid(row=6, column=10, columnspan=2,
                            rowspan=1, sticky=NSEW)
        helpfullabel = Label(self, text="Very Helpful", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right", width=1, height=1)
        helpfullabel.grid(row=6, column=30, columnspan=2,
                          rowspan=1, sticky=NSEW)
        unlikelihoodlabel = Label(self, text="Less likelihood", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="left", width=1, height=1)
        unlikelihoodlabel.grid(
            row=8, column=10, columnspan=2, rowspan=1, sticky=NSEW)
        likelihoodlabel = Label(self, text="More likelihood", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right", width=1, height=1)
        likelihoodlabel.grid(row=8, column=30, columnspan=2,
                             rowspan=1, sticky=NSEW)
        difficultlabel = Label(self, text="More difficult", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="left", width=1, height=1)
        difficultlabel.grid(row=10, column=10, columnspan=2,
                            rowspan=1, sticky=NSEW)
        easierlabel = Label(self, text="Easier", font=(
            "Helvetica", 12), bg=NICEPURPLE, justify="right", width=1, height=1)
        easierlabel.grid(row=10, column=30, columnspan=2,
                         rowspan=1, sticky=NSEW)

        # Button
        self.getanswers = Button(self, text="Cancel", command=lambda: [controller.show_frame(MainPage), 
        controller.togglebuttonrelief(controller.mainpagebutton)],
        bg=ORANGE, font=("Helvetica", 18), width=1, height=1)
        self.getanswers.grid(row=18, column=10, rowspan=2,
                             columnspan=6, sticky=N+S+E+W)
        self.getanswers.grid_propagate(0)

        self.getanswers = Button(self, text="Confirm", command=lambda: [
                                 ShowChoice(), dosomedatabasemagic()], bg=ORANGE, font=("Helvetica", 18), width=1, height=1)
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
                        rowspan=18, sticky=N+S+E+W)

        self.decorate2image = Image.open(r"assets\decoration.jpg")
        self.decorating2image = ImageTk.PhotoImage(self.decorate2image.resize(
            (math.ceil(200 * dpi / 96), math.ceil(800 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.decorating2image,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=1, column=34, columnspan=5,
                        rowspan=18, sticky=N+S+E+W)


class CalendarPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=PINK)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, height=2, bg=NICEPURPLE).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=5, bg=NICEPURPLE).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)
        def hidetheentireframe():
            self.grid_remove()
        xbuttonlabel = Button(self, text="X", font=("Avenir Next Medium", 18), height=1,width=1,
        bg=DARKBLUE, fg="white",
        command= lambda:hidetheentireframe())
        xbuttonlabel.grid(row=0, column=40, rowspan=2, columnspan=2, sticky=N+S+E+W)
        # Widgets
        label = Label(self, text="This is the Calendar", font=(
            'Segoe Ui Semibold', 14), width=1, height=1, fg='#000000', bg='#FFF5E4', justify="left")
        label.grid(row=0, column=2, columnspan=6,
                   rowspan=2, sticky=N+S+E+W)
        self.cal = tkCalendar(self, width=1, height=1,
            background = DARKBLUE, foreground = 'white', 
            bordercolor = ORANGE, 
            headersbackground = NAVYBLUE, headersforeground = 'white', 
            selectbackground = NICEBLUE, selectforeground = 'black',
            showothermonthdays = False,
            selectmode="day",
            font=("Avenir Next Medium", 18),
            date_pattern="dd-mm-yyyy")
        self.cal.grid(row=2, column=2, columnspan=21, rowspan=17, sticky=N+S+E+W)
        self.cal.bind("<<CalendarSelected>>", self.generate_buttons)

        #Go back to current date button
        self.gobackbutton = Button(self, text="Change view to current date", width=1, height=1,
        bg=ORANGE, font=("Atkinson Hyperlegible", 18), command=lambda: [self.go_to_today()])
        self.gobackbutton.grid(row=19, column=3, rowspan=2,
                             columnspan=6, sticky=N+S+E+W)
        self.gobackbutton.grid_propagate(0)
        self.refreshbutton = Button(self, text="Refresh",
        bg=ORANGE, font=("Atkinson Hyperlegible", 18), width=1, height=1,
        command=lambda: [self.add_events()] )
        self.refreshbutton.grid(row=19, column=10, rowspan=2,
                                columnspan=6, sticky=N+S+E+W)
        self.refreshbutton.grid_propagate(0)
        self.buttonframe=Frame(self, bg = ORANGE, relief=RAISED, width=1, height=1,)
        self.buttonframe.grid(row=4, column=24, rowspan=15, columnspan=17, sticky=N+S+E+W)
        self.buttonframe.grid_propagate(0)
        self.detailslabel = Label(self, text="Click on an event to view the details.", width=1, height=1,
        font = ("Avenir Next Medium", 18), background=LIGHTYELLOW)
        self.detailslabel.grid(row=2, column=24, rowspan=2, columnspan=17, sticky=N+S+E+W)
        self.add_events()
    def generate_buttons(self, event):
        detailslabel = self.detailslabel 
        for widgets in self.buttonframe.winfo_children():
            widgets.destroy()
        for x in range(15):
            self.buttonframe.columnconfigure(x, weight=1, uniform='x')
            Label(self.buttonframe, width=1, bg=ORANGE).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(15):
            self.buttonframe.rowconfigure(y, weight=1, uniform='x')
            Label(self.buttonframe, width=1, bg=ORANGE).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        date = self.cal.selection_get()
        self.c.execute("""SELECT count(*) FROM eventcreation WHERE event_startdate = ?""", (date,))
        self.eventnumber = self.c.fetchall()
        for row in self.eventnumber:
            detailslabel.configure(text=f"Event details: There is/are {row[0]} event(s)\noccurring on {date}")
        self.c.execute("""SELECT event_name FROM eventcreation WHERE event_startdate = ?""", (date,))
        self.eventnames = self.c.fetchall()
        startingrowno = 0
        for index, name in list(enumerate(self.eventnames)):
            #Unpacking the tuple (name) to get the string
            name = name[0]
            Label(self.buttonframe, text=f"Event name: {name}", width=1, height=1, 
            bg = LIGHTYELLOW, fg = "black", relief="groove",
            font = ("Avenir Next Medium", 18)).grid(row=0+startingrowno, column=0, rowspan=2, columnspan=11, sticky=N+S+E+W)
            Button(self.buttonframe, text="View details", width=1, height=1,
            bg = PINK, fg = "black", relief="groove",
            font = ("Avenir Next Medium", 18),
            # lambda command fix thanks to https://stackoverflow.com/questions/17677649/tkinter-assign-button-command-in-a-for-loop-with-lambda
            command=lambda name=name:self.createdetails(name)).grid(row=0+startingrowno, column=11, rowspan=2, columnspan=4, sticky=N+S+E+W)
            startingrowno += 2

    def createdetails(self, name):
        #A frame to display the details of the event
        self.subframe = Frame(self.buttonframe, bg = NICEBLUE, relief=RAISED, height=1, width=1)
        self.subframe.grid(row=0, column=0, rowspan=15, columnspan=15, sticky=N+S+E+W)
        for x in range(15):
            self.subframe.columnconfigure(x, weight=1, uniform='x')
            Label(self.subframe, width=1, bg=LIGHTYELLOW).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=N+S+E+W)
        for y in range(15):
            self.subframe.rowconfigure(y, weight=1, uniform='x')
            Label(self.subframe, width=1, bg=LIGHTYELLOW).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=N+S+E+W)
        self.subframe.grid_propagate(0)
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        self.c.execute("""SELECT 
        event_name, event_startdate, event_enddate, event_starttime, event_endtime, event_organizer, venue_name, host_name FROM eventcreation WHERE event_name = ?""", (name,))
        self.eventdetails = self.c.fetchall()
        for row in self.eventdetails:
            Label(self.subframe, text="Event details", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=0, column=0, rowspan=2, columnspan=15, sticky=N+S+E+W)
            Label(self.subframe, text=f"Event name: {row[0]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=2, column=0, rowspan=2, columnspan=15, sticky=N+S+E+W)
            Label(self.subframe, text=f"Event Date: From {row[1]} to {row[2]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=4, column=0, rowspan=2, columnspan=15, sticky=N+S+E+W)
            Label(self.subframe, text=f"Event time: {row[3]} - {row[4]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=6, column=0, rowspan=2, columnspan=15, sticky=N+S+E+W)
            Label(self.subframe, text=f"Event organizer: {row[5]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=8, column=0, rowspan=2, columnspan=15, sticky=N+S+E+W)
            Label(self.subframe, text=f"Host name: {row[7]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=10, column=0, rowspan=2, columnspan=15, sticky=N+S+E+W)
            Label(self.subframe, text=f"Venue: {row[6]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=12, column=0, rowspan=2, columnspan=15, sticky=N+S+E+W)
            Button(self.subframe, text="Back", width=1, height=1,
            bg = PINK, fg = "black", relief="groove",
            font = ("Avenir Next Medium", 18),
            command=lambda: self.subframe.grid_remove()).grid(row=14, column=0, rowspan=2, columnspan=15, sticky=N+S+E+W)

    
    def go_to_today(self):
        self.cal.selection_set(datetime.date.today())
        self.cal.see(datetime.date.today())
    #read from the eventcreation table and add the events to the calendar
    def add_events(self):
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT event_startdate, event_name FROM eventcreation")
        self.rows = self.c.fetchall()
        for row in self.rows:
            #convert to datetime 
            self.date = datetime.datetime.strptime(row[0], r'%Y-%m-%d').date()
            self.cal.calevent_create(self.date, row[1], 'all')

            

    



def main():
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    main()