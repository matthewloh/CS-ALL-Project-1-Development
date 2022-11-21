import ctypes
import io
import os
import subprocess
from ctypes.wintypes import BOOL, HWND, LONG
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from tkinter.filedialog import askopenfilename

try:
    import pyglet
except:
    print('Installing pyglet.')
    subprocess.check_call(['pip', 'install', 'pyglet'])
    print('Done.')
    import pyglet
try:
  from PIL import Image, ImageOps, ImageTk
except:
  print('Installing PIL.')
  subprocess.check_call(['pip', 'install', 'pillow'])
  print('Done.')
  from PIL import Image, ImageOps, ImageTk
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
import datetime
import math
import sqlite3
from ctypes import windll

# Ctypes method that allows us to interact with windows and get the system resolution
# https://stackoverflow.com/a/3129524

user32 = windll.user32
  
# https://stackoverflow.com/a/68621773
# This bit of code allows us to remove the title bar from the window
# in case of a fullscreen application
GetWindowLongPtrW = ctypes.windll.user32.GetWindowLongPtrW
SetWindowLongPtrW = ctypes.windll.user32.SetWindowLongPtrW

def get_handle(root) -> int:
    root.update_idletasks()
    # This gets the window's parent same as `ctypes.windll.user32.GetParent`
    return GetWindowLongPtrW(root.winfo_id(), GWLP_HWNDPARENT)

# Constants for the ctypes functions above 
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
WHITE = "#FFFFFF"
BLACK = "#000000"

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
        # This bit of code allows us to perform dpi awareness and allows us to
        # maintain the same size of the window on different resolutions and scalings 
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
        # The line below lets us get the primary display's resolution
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        print(self.screensize)
        #TODO - Make the window automatically hide the title bar and maximize if resolution is 1920x1080

        if self.screensize == (1920, 1080):
            self.geometry(
                f'{math.ceil(1920 * dpi / 96)}x{math.ceil(1049 * dpi / 96)}')            
        elif self.screensize > (1920, 1080):
            self.geometry(
                f'{math.ceil(1920 * dpi / 96)}x{math.ceil(1080 * dpi / 96)}')
        self.title("INTI Interactive System")
        self.resizable(False, False)
        self.configure(background=LAVENDER)

        for x in range(32):
            self.columnconfigure(x, weight=1, uniform='row')
            Label(self, width=1, bg=NICEPURPLE).grid(
                row=0, column=x, sticky=NSEW)
        for y in range(18):
            self.rowconfigure(y, weight=1, uniform='row')
            Label(self, width=1, bg=NICEPURPLE).grid(
                row=y, column=0, sticky=NSEW)

        FONTFORBUTTONS = "Bahnschrift Semibold"
        print(LOGINID)
        print(LOGGEDINAS)       
        #Frame that has everything stacked on top of it
        self.centercontainer = Frame(self, bg=LAVENDER)
        self.centercontainer.grid(row=2, column=2, rowspan=14,
                             columnspan=28, sticky=NSEW) 
        self.centercontainer.grid_propagate(False)
        
        for x in range(28):
            self.centercontainer.columnconfigure(x, weight=1, uniform='row')
            Label(self.centercontainer, width=1, bg=LAVENDER).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(16):
            self.centercontainer.rowconfigure(y, weight=1, uniform='row')
            Label(self.centercontainer, width=1, bg=LAVENDER).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)
                        
        self.buttoncontainer = Frame(self, bg=DARKBLUE, highlightbackground=ORANGE, highlightthickness=2)
        self.buttoncontainer.grid(row=0, column=0, rowspan=2,
                             columnspan=30, sticky=NSEW)
        self.buttoncontainer.grid_propagate(False)

        for x in range(30):
            self.buttoncontainer.columnconfigure(x, weight=1, uniform='row')
            Label(self.buttoncontainer, width=1, bg=DARKBLUE).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(2):
            self.buttoncontainer.rowconfigure(y, weight=1, uniform='row')
            Label(self.buttoncontainer, width=1, bg=DARKBLUE).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)

        self.signupbutton = Button(self.buttoncontainer, text="Sign Up\n Page", bg=NICEBLUE,
                            fg="white",font=(FONTFORBUTTONS, 20),
                            borderwidth=2, relief="raised", height=1, width=1, highlightthickness=2,
                            command=lambda: [
                    self.show_frame(RegistrationPage),
                    self.togglebuttonrelief(self.signupbutton)
                    ])
        self.loginbutton = Button(self.buttoncontainer, text="Login\nPage", bg=NICEBLUE,
                            fg="white", font=(FONTFORBUTTONS, 20),
                            borderwidth=2, relief="raised", height=1, width=1, highlightthickness=2,
                            command=lambda: [
                    self.show_frame(LoginPage),
                    self.togglebuttonrelief(self.loginbutton)
                    ])

        self.signupbutton.grid(row=0, column=0, rowspan=2, columnspan=3, sticky=NSEW)
        self.loginbutton.grid(row=0, column=3, rowspan=2, columnspan=3, sticky=NSEW)

        self.mainpagebutton = Button(self.buttoncontainer, text="Main\nPage", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                     borderwidth=2, relief="raised", height=1, width=1, highlightthickness=0,
                                     command=lambda: [
                    self.show_frame(MainPage),
                    self.togglebuttonrelief(self.mainpagebutton)
                    ])
        self.eventlistbutton = Button(self.buttoncontainer, text="Event\nList", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                      borderwidth=2, relief="raised", height=1, width=1, highlightthickness=0,
                                      command=lambda: [
                    self.show_frame(EventView),
                    self.togglebuttonrelief(self.eventlistbutton)
                    ])
        self.eventregistrationbutton = Button(self.buttoncontainer, text="Event\nRegistration", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                              borderwidth=2, relief="raised",
                                              height=1, width=1, highlightthickness=0,
                                              command=lambda: [
                    self.show_frame(EventRegistration),
                    self.togglebuttonrelief(self.eventregistrationbutton)
                    ])
        self.eventcreationbutton = Button(self.buttoncontainer, text="Event\nCreation\n(ADMIN)", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                          borderwidth=2, relief="raised", height=1,width=1, highlightthickness=0,
                                          command=lambda: [
                    self.show_frame(EventCreation),
                    self.togglebuttonrelief(self.eventcreationbutton)
                    ])
        self.viewparticipantsbutton = Button(self.buttoncontainer, text="Management\nSuite\n(ADMIN)", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                             borderwidth=2, relief="raised", height=1,width=1, highlightthickness=0,
                                             command=lambda: [
                    self.show_frame(ViewParticipants),
                    self.togglebuttonrelief(self.viewparticipantsbutton)
                    ])
        self.feedbackbutton = Button(self.buttoncontainer, text="Feedback\nForm", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                            borderwidth=2, relief="raised", height=1,width=1, highlightthickness=0,
                            command=lambda: [
                    self.show_frame(FeedbackForm),
                    self.togglebuttonrelief(self.feedbackbutton)
                    ])
        self.calendarbutton = Button(self.buttoncontainer, text="Calendar", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                                     borderwidth=2, relief="raised", height=1,width=1, highlightthickness=0,
                                     command=lambda: [
                    self.show_frame(CalendarPage),
                    self.togglebuttonrelief(self.calendarbutton)
                    ])

        # Sign out buttons + reminder frame

        self.bottomleftbuttons = Frame(self, bg=NAVYBLUE, width=1, height=1)
        self.bottomleftbuttons.grid(row=16, column=0, rowspan=2, columnspan=20, sticky=NSEW)
        self.bottomleftbuttons.grid_propagate(False)

        for x in range(20):
            self.bottomleftbuttons.columnconfigure(x, weight=1, uniform='row')
            Label(self.bottomleftbuttons, width=1, bg=NAVYBLUE).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(2):
            self.bottomleftbuttons.rowconfigure(y, weight=1, uniform='row')
            Label(self.bottomleftbuttons, width=1, bg=NAVYBLUE).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)

        self.signoutbutton = Button(self.bottomleftbuttons,
                            text="Sign Out", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                            relief="solid", height=1, width=1,
                            command=lambda: [
                                self.show_frame(LoginPage),
                                self.togglebuttonrelief(self.loginbutton),
                                self.signout()])
                                
        self.studentbutton = Button(self.bottomleftbuttons,
                            text="Student\nButton", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                            relief="solid", height=1, width=1,
                            command=lambda: [
                                self.show_loggedin()])

        self.adminbutton = Button(self.bottomleftbuttons,
                            text="Admin\nButton", bg=NICEBLUE, fg="white", font=(FONTFORBUTTONS, 20),
                            relief="solid", height=1, width=1,
                            command=lambda: [
                                self.show_admin()])

        self.signoutbutton.grid(row=0, column=0, rowspan=2, columnspan=3, sticky=NSEW)
        self.studentbutton.grid(row=0, column=3, rowspan=2, columnspan=3, sticky=NSEW)
        self.adminbutton.grid(row=0, column=6, rowspan=2, columnspan=3, sticky=NSEW)

        self.remindercontainer = Frame(self.bottomleftbuttons, bg=LIGHTYELLOW, width=1, height=1)
        # self.remindercontainer.grid(row=0, column=9, rowspan=2, columnspan=11, sticky=NSEW)
        self.remindercontainer.grid_propagate(False)
        self.sidebarframe = Frame(self, bg=NAVYBLUE, width=1, height=1)
        self.sidebarframe.grid(row=2, column=0, rowspan=14, columnspan=2,
                             sticky=NSEW)
        self.sidebarframe.grid_propagate(False)

        for x in range(2):
                self.sidebarframe.columnconfigure(x, weight=1, uniform='row')
                Label(self.sidebarframe, width=1, bg=NAVYBLUE).grid(
                row=0, column=x, sticky=NSEW)
        for y in range(14):
                self.sidebarframe.rowconfigure(y, weight=1, uniform='row')
                Label(self.sidebarframe, width=1, bg=NAVYBLUE).grid(
                row=y, column=0, sticky=NSEW)
        
        self.bellimage = Image.open(r"assets\bell.png")
        self.bellimage = ImageTk.PhotoImage(self.bellimage.resize(
            (math.ceil(120 * dpi/96), math.ceil(120 * dpi/96)), Image.Resampling.LANCZOS))
        self.bellbutton = Button(self.sidebarframe, image=self.bellimage, bg=NAVYBLUE,
                                borderwidth=1, relief="flat", height=1, width=1,
                                command=lambda: print(dpi))

        self.calendarimage = Image.open(r"assets\calenderr.png")
        self.calendarimage = ImageTk.PhotoImage(self.calendarimage.resize(
            (math.ceil(120 * dpi/96), math.ceil(120 * dpi/96)), Image.Resampling.LANCZOS))
        self.sidecalendar = Button(self.sidebarframe, image=self.calendarimage, bg=NAVYBLUE,
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
            frame = F(parent=self.centercontainer, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, rowspan=16, columnspan=28, sticky=NSEW)

        #Shows the loading frame
        self.show_frame(ViewParticipants)
        self.togglebuttonrelief(self.viewparticipantsbutton)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.grid()
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]

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
        self.mainpagebutton.grid(row=0, column=6, rowspan=2, columnspan=3,sticky=NSEW)
        self.eventlistbutton.grid(row=0, column=9, rowspan=2, columnspan=3, sticky=NSEW)
        self.eventregistrationbutton.grid(row=0, column=12, rowspan=2,columnspan=3,sticky=NSEW)
        self.calendarbutton.grid(row=0, column=15, rowspan=2,columnspan=3, sticky=NSEW)
        self.feedbackbutton.grid(row=0, column=18, rowspan=2,columnspan=3, sticky=NSEW)
        self.sidecalendar.grid(row=7, column=0, rowspan=2, columnspan=2, sticky=NSEW)
        self.bellbutton.grid(row=10, column=0, rowspan=2, columnspan=2, sticky=NSEW)

    def show_admin(self):
        self.mainpagebutton.grid(row=0, column=6, rowspan=2, columnspan=3,sticky=NSEW)
        self.eventlistbutton.grid(row=0, column=9, rowspan=2, columnspan=3, sticky=NSEW)
        self.eventregistrationbutton.grid(row=0, column=12, rowspan=2,columnspan=3,  sticky=NSEW)
        self.eventcreationbutton.grid(row=0, column=15, rowspan=2,columnspan=3, sticky=NSEW)
        self.eventcreationbutton.grid_propagate(False)
        self.viewparticipantsbutton.grid(row=0, column=18, rowspan=2,columnspan=3, sticky=NSEW)
        self.viewparticipantsbutton.grid_propagate(False)
        self.calendarbutton.grid(row=0, column=21, rowspan=2,columnspan=3, sticky=NSEW)
        self.feedbackbutton.grid(row=0, column=24, rowspan=2,columnspan=3, sticky=NSEW)
        self.sidecalendar.grid(row=7, column=0, rowspan=2, columnspan=2, sticky=NSEW)
        self.bellbutton.grid(row=10, column=0, rowspan=2, columnspan=2, sticky=NSEW)

    def welcomelabel(self, name, role):
        self.welcomeframe = Frame(self, bg=NICEBLUE, width=1, height=1)
        self.welcomeframe.grid(row=16, column=20, rowspan=2, columnspan=12, sticky=NSEW)
        self.welcomeframe.grid_propagate(False)

        for x in range(8):
            self.welcomeframe.columnconfigure(x, weight=1, uniform='row')
            Label(self.welcomeframe, width=1, bg=NICEBLUE).grid(
                row=0, column=x, sticky=NSEW)
        for y in range(2):
            self.welcomeframe.rowconfigure(y, weight=1, uniform='row')
            Label(self.welcomeframe, width=1, bg=NICEBLUE).grid(
                row=y, column=0, sticky=NSEW)
                
        self.namelabel = Button(self.welcomeframe, width=1, height=1,
                text="",font=("Atkinson Hyperlegible", 30), fg="white",bg=DARKBLUE)
        self.namelabel.grid(row=0, column=0, rowspan=2, columnspan=8, sticky=NSEW)
        self.namelabel.configure(text=f"Welcome {name.capitalize()} as {role.capitalize()}!\nWe are glad to have you here!")
        self.namelabel.grid_propagate(False)

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

    def make_a_container(self):
        self.randomframe.grid_remove()
        self.randomframe.grid(row=10, column=9, rowspan=6, columnspan=11,
                            sticky=NSEW)

    #Window management button frame
    def createwindowmanagementframe(self):
        self.windowmanagementframe = Frame(self, bg=NAVYBLUE, width=1, height=1)
        self.windowmanagementframe.grid(row=0, column=30, rowspan=2, columnspan=2,
                                    sticky=NSEW)
        self.windowmanagementframe.grid_propagate(False)

        for x in range(2):
            self.windowmanagementframe.columnconfigure(x, weight=1, uniform='row')
            Label(self.windowmanagementframe, width=1, bg=NAVYBLUE).grid(
                row=0, column=x, sticky=NSEW)
        for y in range(2):
            self.windowmanagementframe.rowconfigure(y, weight=1, uniform='row')
            Label(self.windowmanagementframe, width=1, bg=NAVYBLUE).grid(
                row=y, column=0, sticky=NSEW)

        self.minimizebutton = Button(self.windowmanagementframe, width=1, height=1,
                            text="Show", font=("Atkinson Hyperlegible", 12),
                            bg="#fdbc40", fg="WHITE", relief=RAISED,
                            command=lambda:[
                                self.state('normal'),
                                self.showthewindowbar()
                                ])
        self.minimizebutton.grid(row=0, column=0, sticky=NSEW)
        self.minimizebutton.grid_propagate(False)
        self.maximizebutton = Button(self.windowmanagementframe,
                            text="Hide", font=("Atkinson Hyperlegible", 12),
                            bg="#33c748", fg="WHITE", width=1, height=1, relief=RAISED,
                            command=lambda:[
                                self.deletethewindowbar(),
                                print(self.get_display_size())
                                ])
        self.maximizebutton.grid(row=1, column=0, sticky=NSEW)
        self.maximizebutton.grid_propagate(False)
        self.closewindowbutton = Button(self.windowmanagementframe, text="Close", font=("Atkinson Hyperlegible", 12),
                                    bg="#fc5753", fg="WHITE", width=1, height=1, relief=RAISED,
                                    command=lambda:[
            self.destroy()
        ])
        self.closewindowbutton.grid(row=0, column=1, rowspan=2, columnspan=1, sticky=NSEW)
        self.closewindowbutton.grid_propagate(False)
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
        self.randomframe.grid_propagate(False)
        for x in range(12):
            self.randomframe.columnconfigure(x, weight=1, uniform='row')
            Label(self.randomframe, width=1, bg=LIGHTPURPLE).grid(
                row=0, column=x, sticky=NSEW)
        for y in range(12):
            self.randomframe.rowconfigure(y, weight=1, uniform='row')
            Label(self.randomframe, width=1, bg=LIGHTPURPLE).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW,)
        self.introlabel = Label(self.randomframe, text="What would you\nlike to do?",
                            font=("Atkinson Hyperlegible", 14), width=1, height=1,
                            bg=LAVENDER, fg="black")
        self.introlabel.grid(row=0, column=2, rowspan=2, columnspan=8, sticky=NSEW)
        self.introlabel.grid_propagate(False)
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
        self.loggedinaslabel.grid(row=10, column=1, rowspan=2, columnspan=10, sticky=NSEW)
        self.loggedinaslabel.grid_propagate(False)
        self.viewbutton.grid(row=5, column=1, rowspan=2, columnspan=5, sticky=NSEW,padx=2)
        self.viewbutton.grid_propagate(False)
        self.editbutton = Button(self.randomframe,
            text="Edit Calendar", font=("Atkinson Hyperlegible", 14),
            bg=DARKBLUE, fg="WHITE", width=1, height=1,
            command=lambda:[print('yes')])
        self.editbutton.grid(row=5, column=6, rowspan=2, columnspan=5, sticky=NSEW,padx=2)
        self.editbutton.grid_propagate(False)
        self.closebutton = Button(self.randomframe, 
            text="Close", font=("Atkinson Hyperlegible", 14),
            bg=DARKBLUE, fg="WHITE", width=1, height=1,
            command=lambda:[
                self.randomframe.grid_remove()
            ])
        self.closebutton.grid(row=8, column=1, rowspan=2, columnspan=10, sticky=NSEW,padx=2)
        self.closebutton.grid_propagate(False)
        self.signoutbutton.grid_propagate(False)
        self.studentbutton.grid_propagate(False)
        self.adminbutton.grid_propagate(False)
    def get_display_size(self):
        if self.screensize <= (1920, 1080):
            self.state('zoomed')

class RegistrationPage(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent, bg=LIGHTPURPLE)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=1, bg=LIGHTPURPLE, relief="flat").grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=1, bg=LIGHTPURPLE, relief="flat").grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)
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
            emailwarning.grid(row=5, column=34, columnspan=8, sticky=NSEW)
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
                               rowspan=2, columnspan=17, sticky=NSEW)

        # Entries
        firstnamefield = Entry(self, width=1, bg='#FFFFFF',
                               font=(FONTNAME, 18), justify='center')
        firstnamefield.grid(row=3, column=24,
                            rowspan=2, columnspan=7, sticky=NSEW)
        firstnamefield.insert(0, FIRSTNAME)
        firstnamefield.grid_propagate(False)

        lastnamefield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        lastnamefield.grid(row=3, column=34,
                           rowspan=2, columnspan=7, sticky=NSEW)
        lastnamefield.insert(0, LASTNAME)
        lastnamefield.grid_propagate(False)

        emailfield = Entry(self, width=1, bg='#FFFFFF',
                           font=(FONTNAME, 18), justify='center')
        emailfield.grid(row=6, column=24,
                        rowspan=2, columnspan=17, sticky=NSEW)
        emailfield.insert(0, EMAILTEXT)
        emailfield.grid_propagate(False)

        passwordfield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        passwordfield.grid(row=9, column=24,
                           rowspan=2, columnspan=17, sticky=NSEW)
        passwordfield.insert(0, PASSWORDTEXT)
        passwordfield.grid_propagate(False)

        confirmpasswordfield = Entry(
            self, width=1, bg='#FFFFFF', font=(FONTNAME, 18), justify='center')
        confirmpasswordfield.grid(row=12, column=24,
                                  rowspan=2, columnspan=17, sticky=NSEW)
        confirmpasswordfield.insert(0, CONFPASSTEXT)
        confirmpasswordfield.grid_propagate(False)

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
                       rowspan=5, sticky=NSEW)
        self.logolabel.grid_propagate(False)
        self.titleart = Image.open(r"assets\DR7j7r0.png")
        self.titleart = ImageTk.PhotoImage(self.titleart.resize(
            (math.ceil(680 * dpi / 96), math.ceil(320 * dpi / 96)), Image.Resampling.LANCZOS))
        titleartlabel = Button(self, image=self.titleart,
                               background= NICEBLUE, 
                               anchor=CENTER, width=1, height=1)
        titleartlabel.grid(row=10, column=2, columnspan=17,
                           rowspan=8, sticky=NSEW)
        titleartlabel.grid_propagate(False)
        # Buttons
        signupbutton = Button(self, text="SIGN UP", width=1, height=1, font=(
            'Atkinson Hyperlegible', 14), fg='#000000', command=lambda: checkfields(), bg=LIGHTYELLOW)
        signupbutton.grid(row=15, column=28, columnspan=9,
                          rowspan=2, sticky=NSEW)
        signupbutton.grid_propagate(False)

        loginbutton = Button(self, text="Click here to sign in.",
        font=('Atkinson Hyperlegible', 14), width=1, height=1,
        fg='#000000', command=lambda: [
        controller.show_frame(LoginPage),
        controller.togglebuttonrelief(controller.loginbutton),
        cleareveryentry()],
        bg=OTHERPINK)
        loginbutton.grid(row=18, column=28, columnspan=9,
                         rowspan=2, sticky=NSEW)
        loginbutton.grid_propagate(False)

        label = Label(self, text="This is the registration page on left frame\nCome back later, still under construction!", font=(
            'Avenir Next', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=17,
                   rowspan=2, sticky=NSEW)
        label.grid_propagate(False)
        def aboutINTIcontainer():
            randomframe = Frame(controller, bg=NICEBLUE, width=1, height=1,
                                borderwidth=1, relief="flat")
            randomframe.grid(row=6, column=4, rowspan=10, columnspan=10,
                             sticky=NSEW)
            randomframe.grid_propagate(False)
            # self.randomframe = randomframe
            for x in range(10):
                randomframe.columnconfigure(x, weight=1, uniform='row')
                Label(randomframe, width=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                  row=0, column=x, sticky=NSEW)
            for y in range(10):
                randomframe.rowconfigure(y, weight=1, uniform='row')
                Label(randomframe, width=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
                    row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW,)
            randomlabel = Label(randomframe, text="INTI COLLEGE LOL", font=("Comic Sans Ms", 18), width=1,height=1, fg="white",bg=DARKBLUE)
            randomlabel.grid(row=0, column=0, rowspan=1, columnspan=14, sticky=NSEW)
            randomlabel.grid_propagate(False)
            randombutton = Button(randomframe, text="click me to close ", font=("Comic Sans Ms", 18), bg=DARKBLUE, fg="WHITE", command=lambda:[
            randomframe.grid_forget()])
            randombutton.grid(row=6, column=0, rowspan=1, columnspan=14, sticky=NSEW)


class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LIGHTPURPLE)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.controller = controller
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=1, bg=LIGHTPURPLE).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=1, bg=LIGHTPURPLE).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)
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
                              rowspan=1, sticky=NSEW)
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
        #            rowspan=2, sticky=NSEW)
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
        #                rowspan=5, sticky=NSEW)
        self.backgroundimageoriginal = Image.open(r"Assets\backgroundimage.png")
        self.backgroundimage = ImageTk.PhotoImage(self.backgroundimageoriginal.resize(
            (math.ceil(1680 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
        
        self.backgroundimagelabel = Label(self, image=self.backgroundimage, width=1, height=1, bg=LIGHTPURPLE)
        self.backgroundimagelabel.grid(row=0, column=0, rowspan=21, columnspan=43, sticky=NSEW)
        self.backgroundimagelabel.grid_propagate(False)
        self.signinbuttonimage = Image.open(r"Assets\signinbutton.png")
        self.signinbuttonimage = ImageTk.PhotoImage(self.signinbuttonimage.resize(
            (math.ceil(444 * dpi / 96), math.ceil(81 * dpi / 96)), Image.Resampling.LANCZOS))
        self.signinbutton = Button(self, image=self.signinbuttonimage, width=1, height=1,
        bg=LIGHTPURPLE, relief="flat",command=lambda:signinbuttonpressed())
        self.signinbutton.grid(row=15, column=26, rowspan=2, columnspan=11, sticky=NSEW)
        self.signinbutton.grid_propagate(False)
        self.signupbuttonimage = Image.open(r"Assets\signupbutton.png")
        self.signupbuttonimage = ImageTk.PhotoImage(self.signupbuttonimage.resize(
            (math.ceil(605 * dpi / 96), math.ceil(81 * dpi / 96)), Image.Resampling.LANCZOS))
        self.signupbutton = Button(self, image=self.signupbuttonimage, width=1, height=1,
        bg=LIGHTPURPLE, borderwidth=1, relief="flat", command=lambda:[controller.show_frame(RegistrationPage),
        controller.togglebuttonrelief(controller.signupbutton)])
        self.signupbutton.grid(row=18, column=24, rowspan=2, columnspan=15,sticky=NSEW)
        self.signupbutton.grid_propagate(False)
        emailwarning = Label(self, text="Please enter a valid email address.", font=(
            'Arial', 10), width=1, height=1, fg='#000000', bg='#FFF5E4')
        emailfield = Entry(self, width=1, bg='#FFFFFF', highlightthickness=1,
                           font=(FONTNAME, 14), justify='center')
        emailfield.grid(row=7, column=25, columnspan=13,    
                        rowspan=2, sticky=NSEW)
        emailfield.insert(0, EMAILTEXT)
        emailfield.grid_propagate(False)
        passwordfield = Entry(self, width=1, bg='#FFFFFF', highlightthickness=1,
                              font=(FONTNAME, 14), justify='center')
        passwordfield.grid(row=12, column=25, columnspan=13,
                           rowspan=2, sticky=NSEW)
        passwordfield.insert(0, PASSWORDTEXT)
        passwordfield.grid_propagate(False)
        emailfield.bind("<FocusIn>", lambda a: clearemailfield())
        emailfield.bind("<FocusOut>", lambda a: repopulateemailfield())
        passwordfield.bind("<FocusIn>", lambda a: clearpasswordfield())
        passwordfield.bind("<FocusOut>", lambda a: repopulatepasswordfield()) 

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
        # def aboutINTIcontainer():
        #     randomframe = Frame(controller, bg=NICEBLUE, width=1, height=1,
        #                         borderwidth=1, relief="flat")
        #     randomframe.grid(row=6, column=4, rowspan=10, columnspan=10,
        #                      sticky=NSEW)
        #     randomframe.grid_propagate(False)
        #     # self.randomframe = randomframe
        #     for x in range(10):
        #         Grid.columnconfigure(randomframe, x, weight=1, uniform='row')
        #         Label(randomframe, height=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
        #           row=0, column=x, sticky=NSEW)
        #     for y in range(10):
        #         Grid.rowconfigure(randomframe, y, weight=1, uniform='row')
        #         Label(randomframe, width=1, bg=NICEBLUE, borderwidth=0, relief="solid").grid(
        #             row=y, column=0, rowspan=2, columnspan=1, sticky=NSEW,)
        #     randomlabel = Label(randomframe, text="INTI SUCKS LOL", font=("Comic Sans Ms", 18), fg="white",bg=DARKBLUE)
        #     randomlabel.grid(row=0, column=0, rowspan=1, columnspan=14, sticky=NSEW)
        #     randomlabel.grid_propagate(False)
        #     randombutton = Button(randomframe, text="click me to close ", font=("Comic Sans Ms", 18), bg=DARKBLUE, fg="WHITE", command=lambda:[
        #     randomframe.grid_forget()])
        #     randombutton.grid(row=6, column=0, rowspan=1, columnspan=14, sticky=NSEW,pady=5)
        


class MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=1, bg=LAVENDER).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=1, bg=LAVENDER).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)

        # Picture
        self.backgroundimageoriginal = Image.open(r"Assets\Main Page.png")
        self.backgroundimage = ImageTk.PhotoImage(self.backgroundimageoriginal.resize(
            (math.ceil(1680 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
        
        self.backgroundimagelabel = Label(self, image=self.backgroundimage, width=1, height=1, bg=LIGHTPURPLE)
        self.backgroundimagelabel.grid(row=0, column=0, rowspan=21, columnspan=43, sticky=NSEW)
        self.backgroundimagelabel.grid_propagate(False)
        # self.originalimage = Image.open(r"assets\Home-Banner-INTI.png")
        # self.resultingimage = ImageTk.PhotoImage(self.originalimage.resize(
        #     (math.ceil(600 * dpi / 96), math.ceil(200 * dpi / 96)), Image.Resampling.LANCZOS))
        # imagelabel = Label(self, image=self.resultingimage,
        #                    anchor=CENTER, width=1, height=1)
        # imagelabel.grid(row=1, column=2, columnspan=16,
        #                 rowspan=4, sticky=NSEW)

        # self.notificationimage = Image.open(r"assets\Notification.png")
        # self.resultimage = ImageTk.PhotoImage(self.notificationimage.resize(
        #     (math.ceil(120 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        # imagelabel = Label(self, image=self.resultimage,
        #                    anchor=CENTER, width=1, height=1)
        # imagelabel.grid(row=11, column=20, columnspan=5,
        #                 rowspan=4, sticky=NSEW)

        self.registrationimage = Image.open(r"assets\registration form.png")
        self.outcomeimage = ImageTk.PhotoImage(self.registrationimage.resize(
            (math.ceil(120 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.outcomeimage,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=11, column=28, columnspan=5,
                        rowspan=4, sticky=NSEW)

        self.calendarimage = Image.open(r"assets\Calendar.png")
        self.outcomingimage = ImageTk.PhotoImage(self.calendarimage.resize(
            (math.ceil(120 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.outcomingimage,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=11, column=36, columnspan=5,
                        rowspan=4, sticky=NSEW)

        # # Label
        # todotext = """Feedback"""
        # todolabel = Label(self, text=todotext, font=(
        #     'Lucida Calligraphy', 20), justify=('left'), width=1, height=1, fg='#000000', bg='#FFF5E4')
        # todolabel.grid(row=6, column=2, columnspan=16,
        #                rowspan=1, sticky=NSEW)

        # todotext = """Upcoming Events"""
        # todolabel = Label(self, text=todotext, font=(
        #     'Lucida Calligraphy', 20), justify=('left'), width=1, height=1, fg='#000000', bg='#FFF5E4')
        # todolabel.grid(row=13, column=2, columnspan=16,
        #                rowspan=1, sticky=NSEW)

        # # TODO label
        # todotext = """If you want to get more enquiries,you can ask INTI IT management through\nphone number: + 04-6355793 or email: iicpitmanagement@newinti.edu.my"""
        # todolabel = Label(self, text=todotext, font=(
        #     'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        # todolabel.grid(row=1, column=20, columnspan=21,
        #                rowspan=2, sticky=NSEW)

        # Widgets
        # placeholderlabel = Label(self, text="Welcome To INTI Announcement website.\nAs a member of IT staffs, we hear a lot of complaints\nand dissatisfaction from our students that the announcements\nmiss out or overlooked the date and duration of event.\nTo prevent this situation happen again\nINTI decided to create\na special announcement website for students.\n This will be a golden opportunity\n for you all to enjoy this welfare.", font=(
        #     'Arial', 16), justify=('center'), width=1, height=1, fg='#000000', bg='#FFF5E4')
        # placeholderlabel.grid(row=4, column=20, columnspan=21,
        #                       rowspan=6, sticky=NSEW)

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
                            rowspan=4, sticky=NSEW)
        imagelabel = Label(self, image=self.feedbackimage,
                           anchor=CENTER, width=1, height=1)

        eventnamebutton = Button(self, text="Event 1", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])

        eventnamebutton.grid(row=15, column=2, columnspan=16,
                             rowspan=1, sticky=NSEW)
        eventsnamebutton = Button(self, text="Event 2", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        eventsnamebutton.grid(row=16, column=2, columnspan=16,
                              rowspan=1, sticky=NSEW)

        aneventnamebutton = Button(self, text="Event 3", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        aneventnamebutton.grid(row=17, column=2, columnspan=16,
                               rowspan=1, sticky=NSEW)

        theeventnamebutton = Button(self, text="Event 4", font=(
        'Arial', 12), width=1, height=1, fg='#000000', bg='#FFF5E4',
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        theeventnamebutton.grid(row=18, column=2, columnspan=16,
                                rowspan=1, sticky=NSEW)
        self.eventlistbuttonimage = Image.open(r"Assets\Event List Button.png")
        self.eventlistbuttonimage = ImageTk.PhotoImage(self.eventlistbuttonimage.resize(
            (math.ceil(200 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        eventlistbutton = Button(self, image=self.eventlistbuttonimage, width=1, height=1, 
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        eventlistbutton.grid(row=16, column=20, columnspan=5,
                             rowspan=3, sticky=NSEW)

        eventregistrationbutton = Button(self, text="Event\nRegistration", font=(
        'Lucida Calligraphy', 16), width=1, height=1, fg='#000000', bg='#FFF5E4',  command=lambda:
        [controller.show_frame(EventRegistration),
        controller.togglebuttonrelief(controller.eventregistrationbutton)])
        eventregistrationbutton.grid(row=16, column=28, columnspan=5,
                                     rowspan=3, sticky=NSEW)

        calendarbutton = Button(self, text="Calendar", font=(
            'Lucida Calligraphy', 16), width=1, height=1, fg='#000000', bg='#FFF5E4', command=
            lambda: [
            controller.show_frame(CalendarPage),
            controller.togglebuttonrelief(controller.calendarbutton)])
        calendarbutton.grid(row=16, column=36, columnspan=5,
                            rowspan=3, sticky=NSEW)

        self.logoutimage = Image.open(r"assets\logoutbutton.png")
        self.logoutimage = ImageTk.PhotoImage(self.logoutimage.resize(
            (math.ceil(38 * dpi / 96), math.ceil(38 * dpi / 96)), Image.Resampling.LANCZOS)),
        logoutbutton = Button(self,image=self.logoutimage , width=1, height=1, fg='#000000', bg='#FFF5E4',command=lambda:
            [controller.show_frame(LoginPage), controller.togglebuttonrelief(controller.loginbutton),
            controller.signout()])
        logoutbutton.grid(row=0, column=41, columnspan=1, rowspan=1, sticky=NSEW)
        imagelabel = Label(self, image=self.logoutimage, anchor=CENTER, width=1, height=1)


class EventView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=LAVENDER)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=1, bg=LAVENDER).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=1, bg=LAVENDER).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)

        self.backgroundimageoriginal = Image.open(r"Assets\eventviewpage\backgroundimage.png")
        if controller.screensize == (1920, 1080):
            self.backgroundimage = ImageTk.PhotoImage(self.backgroundimageoriginal.resize(
                (math.ceil(1680 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
        elif controller.screensize > (1920, 1080):
            self.backgroundimage = ImageTk.PhotoImage(self.backgroundimageoriginal.resize(
                (math.ceil(1680 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
        
        self.backgroundimagelabel = Label(self, image=self.backgroundimage, width=1, height=1, bg=LIGHTPURPLE)
        self.backgroundimagelabel.grid(row=0, column=0, rowspan=21, columnspan=43, sticky=NSEW)
        self.backgroundimagelabel.grid_propagate(False)

        self.showcaseimage = Label(self, image="", width=1, height=1, bg=LIGHTPURPLE)
        self.showcaseimage.grid(row=1, column=23, columnspan=17,
                     rowspan=17, sticky=NSEW)
        
        self.happeninglabelimage = Image.open(r"Assets\eventviewpage\whatshappening.png")
        self.happeninglabelimage = ImageTk.PhotoImage(self.happeninglabelimage.resize(
            (math.ceil(360 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        self.happeninglabel = Label(self, image=self.happeninglabelimage, width=1, height=1, bg=LIGHTPURPLE)
        self.happeninglabel.grid(row=0, column=21, columnspan=9,
                        rowspan=3, sticky=NSEW)

        self.eventdetailsimage = Image.open(r"Assets\eventviewpage\eventdetails.png")
        self.eventdetailsimage = ImageTk.PhotoImage(self.eventdetailsimage.resize(
            (math.ceil(480 * dpi / 96), math.ceil(360 * dpi / 96)), Image.Resampling.LANCZOS))
        self.eventdetails = Label(self, image=self.eventdetailsimage, width=1, height=1, relief="flat")
        self.eventdetails.grid(row=10, column=29, columnspan=12,
                        rowspan=9, sticky=NSEW)
        self.titleart = Image.open(r"Assets\eventviewpage\titleart.png")
        self.titleart = ImageTk.PhotoImage(self.titleart.resize(
            (math.ceil(320 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.titleartlabel = Label(self,
        text="", font=("Avenir Next Medium", 18), fg = "black",
        image=self.titleart, compound=CENTER, width=1, height=1, bg=LIGHTPURPLE)
        self.titleartlabel.grid(row=11, column=31, columnspan=8, rowspan=2, sticky=NSEW)
        self.dateart = Image.open(r"Assets\eventviewpage\datepicture.png")
        self.dateart = ImageTk.PhotoImage(self.dateart.resize(
            (math.ceil(240 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.dateartlabel = Label(self,
        text="", font=("Avenir Next Medium", 18), fg = "black", relief="solid",
        image=self.dateart, compound=CENTER, width=1, height=1)
        self.dateartlabel.grid(row=14, column=33, columnspan=6, rowspan=2, sticky=NSEW)
        self.locationart = Image.open(r"Assets\eventviewpage\locationpicture.png")
        self.locationart = ImageTk.PhotoImage(self.locationart.resize(
            (math.ceil(240 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.locationartlabel = Label(self,
        text="", font=("Avenir Next Medium", 18), fg = "black", relief="solid",
        image=self.dateart, compound=CENTER, width=1, height=1)
        self.locationartlabel.grid(row=16, column=31, columnspan=6, rowspan=2, sticky=NSEW)

        self.leftarrowimage = Image.open(r"Assets\eventviewpage\Left Arrow.png")
        self.leftarrowimage = ImageTk.PhotoImage(self.leftarrowimage.resize(
            (math.ceil(120 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        self.leftarrowbutton = Button(self, image=self.leftarrowimage, width=1, height=1, relief="flat",
        command=lambda: self.previous_image())
        self.leftarrowbutton.grid(row=16, column=21, columnspan=3,
                                    rowspan=3, sticky= NSEW)
        self.rightarrowimage = Image.open(r"Assets\eventviewpage\Right Arrow.png")
        self.rightarrowimage = ImageTk.PhotoImage(self.rightarrowimage.resize(
            (math.ceil(120 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        self.rightarrowbutton = Button(self, image=self.rightarrowimage, width=1, height=1, relief="flat",
        command=lambda: self.next_image())
        self.rightarrowbutton.grid(row=16, column=25, columnspan=3,
                                rowspan=3, sticky=NSEW)
        self.eventsname = []

        self.after(100, self.updateevents)
        self.imageindex = 0

    def updateevents(self):
        # read all the events already created and store them in a list
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("SELECT event_name FROM eventcreation")
            self.events = self.c.fetchall()
            for index, name in list(enumerate(self.events)):
                actualname = name[0]
                self.eventsname.append((index, actualname))
        self.read_blob(self.eventsname[0][1])
        self.titleartlabel.config(text=self.eventsname[0][1])
        self.update_location(self.eventsname[0][1])
        self.update_date(self.eventsname[0][1])
    def update_location(self, event):
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("SELECT venue_name FROM eventcreation WHERE event_name = ?", (event,))
            self.location = self.c.fetchone()
            self.locationartlabel.config(text=self.location[0])
    def update_date(self, event):
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("SELECT event_startdate FROM eventcreation WHERE event_name = ?", (event,))
            self.date = self.c.fetchone()
            self.dateartlabel.config(text=self.date[0])
    def read_blob(self, eventname):
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("SELECT event_image FROM eventcreation WHERE event_name = ?", (eventname,))
            self.blobData = io.BytesIO(self.c.fetchone()[0])
            self.img = Image.open(self.blobData)
            self.img = ImageTk.PhotoImage(self.img.resize(
                (math.ceil(680 * dpi / 96), math.ceil(680 * dpi / 96)), Image.Resampling.LANCZOS))
            self.showcaseimage.configure(image=self.img)

    def previous_image(self):
        # clicking the left arrow button will show the last image at final index
        if self.imageindex > 0:
            self.imageindex -= 1
        elif self.imageindex == 0:
            self.imageindex += len(self.eventsname) - 1
        self.read_blob(self.eventsname[self.imageindex][1])
        self.titleartlabel.config(text=self.eventsname[self.imageindex][1])
        self.update_location(self.eventsname[self.imageindex][1])
        self.update_date(self.eventsname[self.imageindex][1])



    def next_image(self):
        #this function is to change the image to the next image in the list
        self.imageindex += 1
        if self.imageindex == len(self.eventsname):
            self.imageindex = 0
        self.read_blob(self.eventsname[self.imageindex][1])
        self.titleartlabel.config(text=self.eventsname[self.imageindex][1])
        self.update_location(self.eventsname[self.imageindex][1])
        self.update_date(self.eventsname[self.imageindex][1])

    


            






class EventRegistration(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=PINK)
        FONTNAME = "Avenir Next"
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=1, bg=PINK).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=1, bg=PINK).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)

        # Connect to database
        conn = sqlite3.connect('interactivesystem.db')
        # Create cursor
        c = conn.cursor()
        # Create a table
        #drop table
        # c.execute("""DROP TABLE IF EXISTS eventregistration""")
        c.execute("""CREATE TABLE IF NOT EXISTS eventregistration (
            full_name text NOT NULL,
            icpass_number text NOT NULL, 
            phone_number text,
            email text NOT NULL,
            address text,
            event_registered text NOT NULL,
            eventkey_registered TEXT REFERENCES eventcreation (eventkey_number) ON DELETE CASCADE NOT NULL
            )""")
        # Send entries to database

        def submit():
            full_nametext = fullnamefield.get()
            icpass_number = icnumberfield.get()
            phone_number = phonenumentry.get()
            email_registered = emailentry.get().strip()
            address = addressentry.get()
            event_registered = self.eventdropdown.get()
            #check if the event has already been registered by email 
            #why is this code allowing muplitple entries of the same email in 1 event
            # c.execute("SELECT email FROM eventregistration WHERE event_registered = ?", (event_registered,))
            # emailcheck = c.fetchall()
            # for email in emailcheck:
            #     if email == emailentry.get():
            #         messagebox.showerror("Error", "You have already registered for this event")
            c.execute("SELECT email, full_name FROM eventregistration WHERE event_registered = ?", (event_registered,))
            emailcheck = c.fetchall()
            for emailnum in range(len(emailcheck)):
                if email_registered == emailcheck[emailnum][0]:
                    messagebox.showerror("Error", f"You have already registered for this event using the email {emailcheck[emailnum][0]} and name {emailcheck[emailnum][1]}")
                    return
            c.execute("SELECT eventkey_number FROM eventcreation WHERE event_name = ?", (self.eventdropdown.get(),))
            eventkey_registered = c.fetchone()[0]
            information = (full_nametext, icpass_number,
                           phone_number, email_registered, address, event_registered, eventkey_registered)
            try:
                if full_nametext == "" or icpass_number == "" or phone_number == "" or email_registered == "" or address == "":
                    messagebox.showerror(
                        "Error", "Please fill in all the fields")
                else:
                    with conn:
                        c.execute(
                            "INSERT INTO eventregistration VALUES (?,?,?,?,?,?,?)", information)
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
            event.widget.master.focus_set()
            refresh()
            self.read_blob(self.eventdropdown.get())
        self.bgwallpaper = Image.open(r"Assets\EventRegistration\wallpaperflare.jpg")
        self.bgwall = ImageTk.PhotoImage(self.bgwallpaper.resize(
             (math.ceil(1680 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
        self.bgwalllabel = Label(self, image=self.bgwall, width=1, height=1, bg=LIGHTPURPLE)
        self.bgwalllabel.grid(row=0, column=0, rowspan=21, columnspan=43, sticky=N+S+E+W)
        self.bgwalllabel.grid_propagate(0)
        # Widgets
        label = Label(self, text="This is the event registration page", font=(
            'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=2, columnspan=18,
                   rowspan=1, sticky=NSEW)
        label.grid_propagate(False)
        #dropdown for events
        conn = sqlite3.connect('interactivesystem.db')
        # Create cursor
        c = conn.cursor()
        event_list = ["Select an event"]
        self.current_eventkey = ""
        #refresh the event_list everytime the combobox is selected
        def refresh():
            c.execute("SELECT event_name, eventkey_number FROM eventcreation")
            event_list.clear()
            event_list.append("Please select an event")
            for row in c.fetchall():
                event_name = row[0]
                eventkey_number = row[1] 
                information = (event_name, eventkey_number)
                event_list.append(information[0])
                self.current_eventkey = information[1]


            self.eventdropdown['values'] = event_list
        with conn:
            c.execute("""SELECT event_name, eventkey_number FROM eventcreation""")
            event_list.clear()
            event_list.append("Please select an event")
            for eventname in c.fetchall():
                event_name = eventname[0]
                eventkey = eventname[1]
                information = (event_name, eventkey)
                event_list.append(information[0])
                

        self.eventdropdown = ttk.Combobox(
            self, values=event_list, width=1, state='readonly')
        self.eventdropdown.current(0)
        self.eventdropdown.grid(row=1, column=2, columnspan=18,
                           rowspan=2, sticky=NSEW)
        self.eventdropdown.bind('<FocusIn>', defocus)
        self.eventdropdown.bind('<<ComboboxSelected>>', focusout)
        self.eventdropdown.grid_propagate(False)
        
        separator = ttk.Separator(self, orient=HORIZONTAL)
        separator.grid(row=3, column=3, columnspan=16, pady=5, sticky=EW)
        icpasslabel = Label(self, text="IC No.",
                            font=(FONTNAME, 10), bg='#FFF5E4')
        icpasslabel.grid(row=7, column=3, columnspan=2,
                         rowspan=2, sticky=NSEW)
        icpasslabel.grid_propagate(False)
        phonenumberlabel = Label(
            self, text="Phone\nNo", font=(FONTNAME, 10), bg='#FFF5E4')
        phonenumberlabel.grid(
            row=10, column=3, columnspan=2, rowspan=2, sticky=NSEW)
        emaillabel = Label(self, text="Email", font=(
            FONTNAME, 14), bg='#FFF5E4')
        emaillabel.grid(row=13, column=3, columnspan=2,
                        rowspan=2, sticky=NSEW)
        emaillabel.grid_propagate(False)
        addresslabel = Label(self, text="Address",
                             font=(FONTNAME, 10), bg='#FFF5E4')
        addresslabel.grid(row=16, column=3, columnspan=2,
                          rowspan=2, sticky=NSEW)
        addresslabel.grid_propagate(False)

        # radio_1 = ttk.Radiobutton(self, text="Male  ", variable=var, value=0)
        # radio_1.grid(row=9, column=5,rowspan=2, columnspan=2, pady=(0, 10), sticky=NS)

        # radio_1 = ttk.Radiobutton(self, text="Female", variable=var, value=1, command=lambda:print(var.get()))
        # radio_1.grid(row=9, column=7,rowspan=2, columnspan=2, pady=(0, 10), sticky=NS)

        fullnamefield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        fullnamefield.grid(row=4, column=3, columnspan=16,
                           rowspan=2, sticky=NSEW)
        fullnamefield.insert(0, "Full Name")
        #code to delete the default text when the user clicks on the entry
        def on_entry_click(event):
            if fullnamefield.get() == 'Full Name':
                fullnamefield.delete(0, "end")
                fullnamefield.insert(0, '')
                fullnamefield.config(fg='black')
        def on_focusout(event):
            if fullnamefield.get() == '':
                fullnamefield.insert(0, 'Full Name')
                fullnamefield.config(fg='grey')
        fullnamefield.bind('<FocusIn>', on_entry_click)
        fullnamefield.bind('<FocusOut>', on_focusout)
        fullnamefield.grid_propagate(False)


        icnumberfield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        icnumberfield.grid(row=7, column=5, columnspan=14,
                           rowspan=2, sticky=NSEW)
        phonenumentry = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        phonenumentry.grid(row=10, column=5, columnspan=14,
                           rowspan=2, sticky=NSEW)
        emailentry = Entry(self, width=1, bg='#FFFFFF',
                           font=(FONTNAME, 18), justify='center')
        emailentry.grid(row=13, column=5, columnspan=14,
                        rowspan=2, sticky=NSEW)
        addressentry = Entry(self, width=1, bg='#FFFFFF',
                             font=(FONTNAME, 18), justify='center')
        addressentry.grid(row=16, column=5, columnspan=14,
                          rowspan=2, sticky=NSEW)
        # Buttons
        cancelbutton = Button(self, text="Cancel", font=(FONTNAME, 14), bg='White', command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        cancelbutton.grid(row=18, column=3, columnspan=6,
                          rowspan=2, sticky=NSEW)
        confirmbutton = Button(self, text="Confirm", font=(
            FONTNAME, 14), bg='White', command=lambda: submit())
        confirmbutton.grid(row=18, column=13, columnspan=6,
                           rowspan=2, sticky=NSEW)
        self.panel = Label(self, image="",width=1,height=1, bg=ORANGE)
        self.panel.grid(row=4, column=22, columnspan=16,
                    rowspan=10, sticky=NSEW)
        self.panel.grid_propagate(False)
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
            self.panel.grid_propagate(False)

class EventCreation(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=PINK)
        FONTNAME = "Avenir Next Medium"
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=1, bg=PINK, relief=SOLID).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=1, bg=PINK, relief=SOLID).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)
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


        #Event Creation page background image)
        self.bgimageoriginal = Image.open(r"Assets\EventCreation\eventcreationbg.png")
        self.bgimage = ImageTk.PhotoImage(self.bgimageoriginal.resize(
             (math.ceil(1680 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
        self.bgimagelabel = Label(self, image=self.bgimage, width=1, height=1, bg=LIGHTPURPLE)
        self.bgimagelabel.grid(row=0, column=0, rowspan=21, columnspan=42, sticky=N+S+E+W)
        self.bgimagelabel.grid_propagate(False)

        # Widgets
        # label = Label(self, text="This is the event creation page", font=(
        #     'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
        # label.grid(row=1, column=2, columnspan=18,
        #            rowspan=2, sticky=NSEW)
        # label.grid_propagate(False)

       
        # separator = ttk.Separator(self, orient=HORIZONTAL)
        # separator.grid(row=5, column=3, columnspan=17, pady=5, sticky=EW)
        # separator.grid_propagate(False)
        # eventkeylabel = Label(self, text="Event\nNo.",
        #                     font=(FONTNAME, 14), bg='#FFF5E4', width=1,height=1)
        # eventkeylabel.grid(row=12, column=3, columnspan=2,
        #                     rowspan=2, sticky=NSEW)

        # venuenamelabel = Label(
        #     self, text="Venue\nName",
        #     width=1,height=1,
        #     font=(FONTNAME, 14), bg='#FFF5E4')
        # venuenamelabel.grid(
        #     row=15, column=3, columnspan=2, rowspan=2, sticky=NSEW)
        # venuenamelabel.grid_propagate(False)
        # hostnamelabel = Label(self, text="Host\nName", 
        # font=(FONTNAME, 14),
        # width=1,height=1,
        # bg='#FFF5E4')
        # hostnamelabel.grid(row=15, column=12, columnspan=2,
        #                 rowspan=2, sticky=NSEW)
        # hostnamelabel.grid_propagate(False)
        # organizinglabel = Label(self, text="Organized\nBy", font=(
        #     FONTNAME, 14), bg='#FFF5E4', width=1, height=1)
        # organizinglabel.grid(row=12, column=12, columnspan=2,
        #                     rowspan=2, sticky=NSEW)
        # organizinglabel.grid_propagate(False)

        self.eventnamefield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        self.eventnamefield.grid(row=5, column=5, columnspan=11,
                           rowspan=2, sticky=NSEW)
        self.eventnamefield.insert(0, "Event Name")

        self.eventdescription = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        self.eventdescription.grid(row=8, column=3, columnspan=13,
                            rowspan=2, sticky=NSEW)
        self.eventdescription.insert(0, "Event Description")
        self.eventdescription.grid_propagate(False)

        self.organizerfield = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 18), justify='center')
        self.organizerfield.grid(row=14, column=7, columnspan=6,
                                    rowspan=1, sticky=NSEW)
        self.organizerfield.insert(0, "Organizing School")
        self.organizerfield.grid_propagate(False)
        self.hostnameentry = Entry(self, width=1, bg='#FFFFFF',
                           font=(FONTNAME, 18), justify='center')
        self.hostnameentry.grid(row=17, column=7, columnspan=6,
                        rowspan=1, sticky=NSEW)

        self.venuenameentry = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        self.venuenameentry.grid(row=5, column=28, columnspan=8,
                           rowspan=2, sticky=NSEW)
        self.venuenameentry.grid_propagate(False)
        self.eventkeyfield = Entry(self, width=1, bg='#FFFFFF',
                              font=(FONTNAME, 18), justify='center')
        self.eventkeyfield.grid(row=19, column=20, columnspan=7,
                           rowspan=1, sticky=NSEW)
        self.eventkeyfield.grid_propagate(False)
        # Upload image functionality
        # self.readblobentry = Entry(self, width=1, bg='#FFFFFF',
        #                         font=(FONTNAME, 12), justify='center')
        # self.readblobentry.grid(row=16, column=38, columnspan=4,
        #                     rowspan=2, sticky=NSEW)
        # self.readblobentry.insert(0, "Enter a event key\n to find image")
        # uploadimagebutton = Button(self, text="Upload Image", width=1,height=1,
        # font=(FONTNAME, 14), bg='#FFF5E4', command=lambda:self.upload_image())
        # uploadimagebutton.grid(row=15, column=22, columnspan=8,
        #                          rowspan=2, sticky=NSEW)
        # uploadimagebutton.grid_propagate(False)
        # submitbutton = Button(self, text="Submit", width=1,height=1, font=(
        #     FONTNAME, 14), bg='#FFF5E4', command=lambda:self.submit())
        # submitbutton.grid(row=18, column=22, columnspan=8,
        #                     rowspan=2, sticky=NSEW)
        # submitbutton.grid_propagate(False)
        # deleteimagebutton = Button(self, text="Delete Image", width=1,height=1,
        # font=(FONTNAME, 14), bg='#FFF5E4', command=lambda:self.delete_image())
        # deleteimagebutton.grid(row=15, column=30, columnspan=8,
        #                             rowspan=2, sticky=NSEW)
                                    
        # readblobbutton = Button(self, text="Read Blob", font=(
        #     FONTNAME, 14), bg='#FFF5E4', command=lambda:self.read_blob(self.readblobentry.get()))
        # readblobbutton.grid(row=18, column=30, columnspan=8,
        #                             rowspan=2, sticky=NSEW)
        # readblobbutton.grid_propagate(False)
        #Store image into the eventcreation table 
        # self.c.execute("ALTER TABLE eventcreation ADD COLUMN image BLOB")
        # conn.commit()
        # c.execute("SELECT * FROM eventcreation")
        # print(c.fetchall())
        # Buttons
        # self.panel = Label(self, image="",width=1,height=1, bg=ORANGE)
        # self.panel.grid(row=1, column=22, columnspan=18,
        #             rowspan=12, sticky=NSEW)
        # self.panel.grid_propagate(False)
        self.filename = ""
        #start date
        # self.fromlabel = Label(self, text="Start Date", font=(FONTNAME, 10), bg=NICEBLUE)
        # self.fromlabel.grid(row=3, column=2, columnspan=2,  
        #                   rowspan=1, sticky=NSEW)    
        self.date_entrywidget = DateEntry(self, height=1, width=1, background=NAVYBLUE, 
        headersbackground = ORANGE,
        font=("Avenir Next Medium",16), justify='center',
        date_pattern='dd/mm/yyyy') 
        self.date_entrywidget.grid(row=10, column=20, columnspan=8,
                            rowspan=2, sticky=NSEW)

        #end date
        self.date_entrywidget2 = DateEntry(self, height=1, width=1, background=NAVYBLUE,
        headersbackground = ORANGE,
        font=("Avenir Next Medium",16), justify='center',
        date_pattern='dd/mm/yyyy')
        self.date_entrywidget2.grid(row=10, column=32, columnspan=8,
                            rowspan=2, sticky=NSEW)

        

        self.hourentry = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 18), justify='center')
        self.hourentry.grid(row=14, column=20, columnspan=2,
                            rowspan=2, sticky=NSEW)
        self.hourentry.insert(0, "HH")
        self.minentry = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 18), justify='center')
        self.minentry.grid(row=14, column=23, columnspan=2,
                            rowspan=2, sticky=NSEW)
        self.minentry.insert(0, "MM")
        #Am pm menu 
        self.ampmchoices = ["AM", "PM"]
        self.am_pmcombobox =  ttk.Combobox(self, width=1, font=(FONTNAME, 18), justify='center')
        self.am_pmcombobox['values'] = self.ampmchoices
        self.am_pmcombobox.grid(row=14, column=25, columnspan=3,
                            rowspan=2, sticky=NSEW)
        self.am_pmcombobox.current(0)
        

        self.endhourentry = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 18), justify='center')
        self.endhourentry.grid(row=14, column=32, columnspan=2,
                            rowspan=2, sticky=NSEW)
        self.endhourentry.insert(0, "HH")
        self.endminentry = Entry(self, width=1, bg='#FFFFFF',
                                font=(FONTNAME, 18), justify='center')
        self.endminentry.grid(row=14, column=35, columnspan=2,
                            rowspan=2, sticky=NSEW)
        self.endminentry.insert(0, "MM")
        #Am pm combobox
        self.endampmchoices = ["AM", "PM"]
        self.endam_pmcombobox = ttk.Combobox(self, width=1, font=(FONTNAME, 18), justify='center')
        self.endam_pmcombobox['values'] = self.endampmchoices
        self.endam_pmcombobox.grid(row=14, column=37, columnspan=3,
                            rowspan=2, sticky=NSEW)
        self.endam_pmcombobox.current(0)
        self.cancelbutton = Button(self, text="Cancel", width=1,height=1,
        font=(FONTNAME, 18), bg='White', 
        command=lambda: [
        controller.show_frame(EventView),
        controller.togglebuttonrelief(controller.eventlistbutton)])
        self.cancelbutton.grid(row=18, column=29, columnspan=5,
                          rowspan=2, sticky=NSEW)

        confirmbutton = Button(self, text="Continue\nto Insert Image", width=1,height=1,
        font=(FONTNAME, 18), bg='White', command=lambda: self.insert_blob())
        confirmbutton.grid(row=18, column=36, columnspan=5,
                           rowspan=2, sticky=NSEW)

        self.date_entrywidget.set_date(datetime.date.today())
        self.date_entrywidget2.set_date(datetime.date.today())

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
            event_starttime = self.hourentry.get() + ":" + self.minentry.get() + " " + self.am_pmcombobox.get()
            event_endtime = self.endhourentry.get() + ":" + self.endminentry.get() + " " + self.endam_pmcombobox.get()
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
            self.panel.grid_propagate(False)

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
        self.controller = controller
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=1, bg=PINK).grid(
                row=0, column=x, sticky=NSEW)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=1, bg=PINK).grid(
                row=y, column=0, sticky=NSEW)

        self.backgroundimageoriginal = Image.open(r"Assets\managementsuite\backgroundimage.png")
        self.backgroundimage = ImageTk.PhotoImage(self.backgroundimageoriginal.resize(
            (math.ceil(1680 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
        self.backgroundimagelabel = Label(self, image=self.backgroundimage, width=1, height=1, bg=LIGHTPURPLE)
        self.backgroundimagelabel.grid(row=0, column=0, rowspan=21, columnspan=43, sticky=NSEW)
        self.backgroundimagelabel.grid_propagate(False)
        self.interfaceframe = Frame(self, bg=LIGHTPURPLE, width=1,height=1)
        self.studentcntimg = Image.open(r"Assets\managementsuite\manageeventswidgets\studentscountlabel200x80.png")
        self.studentcountimg = ImageTk.PhotoImage(self.studentcntimg.resize(
            (math.ceil(200 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.cancelimageorg = Image.open(r"Assets\managementsuite\manageeventswidgets\cancelbutton.png")
        self.cancelimage= ImageTk.PhotoImage(self.cancelimageorg.resize(
            (math.ceil(160 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))          
        self.cdeleteimageorg = Image.open(r"Assets\managementsuite\manageeventswidgets\confirmbutton.png")
        self.cdeleteimage = ImageTk.PhotoImage(self.cdeleteimageorg.resize(
            (math.ceil(160 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))

        self.createinterface()
        self.createlandingwidgets()

    def createinterface(self):
        for x in range(38): # 38
            self.interfaceframe.columnconfigure(x, weight=1, uniform='x')
            Label(self.interfaceframe, width=1, bg=LIGHTPURPLE).grid(
                row=0, column=x, sticky=NSEW)
        for y in range(17): # 17
            self.interfaceframe.rowconfigure(y, weight=1, uniform='x')
            Label(self.interfaceframe, width=1, bg=LIGHTPURPLE).grid(
                row=y, column=0, sticky=NSEW)
        self.interfaceframe.grid(row=3, column=2, rowspan=17, columnspan=38, sticky=NSEW)
        self.interfaceframe.grid_propagate(False)
        self.intframebackgroundoriginal = Image.open(r"Assets\managementsuite\blankinterface.png")
        self.intframebackground = ImageTk.PhotoImage(self.intframebackgroundoriginal.resize(
            (math.ceil(1520 * dpi / 96), math.ceil(680 * dpi / 96)), Image.Resampling.LANCZOS))
        self.intframebackgroundlabel = Label(self.interfaceframe, image=self.intframebackground, width=1, height=1, bg=LIGHTPURPLE)
        self.intframebackgroundlabel.grid(row=0, column=0, rowspan=17, columnspan=38, sticky=NSEW)
        self.intframebackgroundlabel.grid_propagate(False)


    def createlandingwidgets(self):
        for widgets in self.interfaceframe.winfo_children():
            widgets.destroy()
        self.createinterface()
        self.createeventsimage = Image.open(r"Assets\managementsuite\createevents.png")
        self.createeventsimage = ImageTk.PhotoImage(self.createeventsimage.resize(
            (math.ceil(560 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        self.createeventsbutton = Button(self.interfaceframe, image=self.createeventsimage, width=1, height=1, relief=RAISED,
        command=lambda: self.controller.show_frame(EventCreation))
        self.createeventsbutton.grid(row=5, column=2, rowspan=3, columnspan=14, sticky=NSEW) 
        self.manageeventsimage = Image.open(r"Assets\managementsuite\manageevents.png")
        self.manageeventsimage = ImageTk.PhotoImage(self.manageeventsimage.resize(
            (math.ceil(560 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        self.manageeventsbutton = Button(self.interfaceframe, image=self.manageeventsimage, width=1, height=1, relief=RAISED,
        command=lambda: self.manageeventsframe())
        self.manageeventsbutton.grid(row=9, column=2, rowspan=3, columnspan=14, sticky=NSEW)
        self.viewparticipantsimage = Image.open(r"Assets\managementsuite\viewparticipants.png")
        self.viewparticipantsimage = ImageTk.PhotoImage(self.viewparticipantsimage.resize(
            (math.ceil(560 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        self.viewparticipantsbutton = Button(self.interfaceframe, image=self.viewparticipantsimage, width=1, height=1, relief=RAISED,
        command=lambda: self.view_participants())
        self.viewparticipantsbutton.grid(row=13, column=2, rowspan=3, columnspan=14, sticky=NSEW)
    def manageeventsframe(self):
        # for widgets in self.interfaceframe.winfo_children():
        #     widgets.destroy()
        self.createinterface()
        self.manageexistingeventsimage = Image.open(r"Assets\managementsuite\manageeventswidgets\manageexistingeventslabel.png")
        self.manageexistingeventsimage = ImageTk.PhotoImage(self.manageexistingeventsimage.resize(
            (math.ceil(200 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
        self.manageexistingeventslabel = Label(self.interfaceframe, image=self.manageexistingeventsimage, width=1, height=1, bg=LIGHTPURPLE)
        self.manageexistingeventslabel.grid(row=1, column=1, rowspan=3, columnspan=5, sticky=NSEW)
        self.manageexistingeventslabel.grid_propagate(False)
        self.filterlabelimage = Image.open(r"Assets\managementsuite\manageeventswidgets\filterlabel.png")
        self.filterlabelimage = ImageTk.PhotoImage(self.filterlabelimage.resize(
            (math.ceil(200 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.filterlabel = Label(self.interfaceframe, image=self.filterlabelimage, width=1, height=1, bg=LIGHTPURPLE, relief=FLAT)
        

        self.filterchoice = StringVar()
        self.filterby = ttk.Combobox(self.interfaceframe, textvariable=self.filterchoice, width=1, font=("Arial", 12), state="readonly")
        self.filterby["values"] = ("Event Name", "Organizer", "Event Key", "Venue")
        self.filterby.current(0)
        self.filterby.grid(row=7, column=1, rowspan=2, columnspan=5, sticky=NSEW)
        self.filterby.grid_propagate(False)
        self.filterlabel.grid(row=5, column=1, rowspan=2, columnspan=5, sticky=NSEW)
        self.filterentry = Entry(self.interfaceframe, width=1, font=("Atkinson Hyperlegible", 12), bg=LIGHTYELLOW, fg="black",justify=CENTER)
        self.filterentry.grid(row=9, column=1, rowspan=1, columnspan=5, sticky=NSEW)

        self.criteriasearchimage = Image.open(r"Assets\managementsuite\manageeventswidgets\criteriasearchbutton.png")
        self.criteriasearchimage = ImageTk.PhotoImage(self.criteriasearchimage.resize(
            (math.ceil(200 * dpi / 96), math.ceil(40 * dpi / 96)), Image.Resampling.LANCZOS))
        self.criteriasearchbutton = Button(self.interfaceframe, image=self.criteriasearchimage, width=1, height=1, bg=LIGHTPURPLE, relief=FLAT, command=lambda: print("hello"))
        self.criteriasearchbutton.grid(row=11, column=1, rowspan=1, columnspan=5, sticky=NSEW)
        self.criteriasearchbutton.grid_propagate(False)
        self.searchallimage = Image.open(r"Assets\managementsuite\manageeventswidgets\allsearchbutton.png")
        self.searchallimage = ImageTk.PhotoImage(self.searchallimage.resize(
            (math.ceil(200 * dpi / 96), math.ceil(40 * dpi / 96)), Image.Resampling.LANCZOS))
        self.searchallbutton = Button(self.interfaceframe, image=self.searchallimage, width=1, height=1, bg=LIGHTPURPLE, relief=FLAT, command=lambda:self.database_queries())
        self.searchallbutton.grid(row=13, column=1, rowspan=1, columnspan=5, sticky=NSEW)
        self.returnhomeimage = Image.open(r"Assets\managementsuite\manageeventswidgets\mainmenubutton.png")
        self.returnhomeimage = ImageTk.PhotoImage(self.returnhomeimage.resize(
            (math.ceil(200 * dpi / 96), math.ceil(40 * dpi / 96)), Image.Resampling.LANCZOS))
        self.returnhomebutton = Button(self.interfaceframe, image=self.returnhomeimage, width=1, height=1, bg=LIGHTPURPLE, relief=FLAT, command=lambda: self.createlandingwidgets())
        self.returnhomebutton.grid(row=15, column=1, rowspan=1, columnspan=5, sticky=NSEW)


        self.centerframe = Frame(self.interfaceframe, bg=LIGHTPURPLE, width=1, height=1)
        self.centerframe.grid(row=1, column=7, rowspan=15, columnspan=18, sticky=NSEW)
        self.centerframe.grid_propagate(False)
        for x in range(18):
            self.centerframe.columnconfigure(x, weight=1, uniform='x')
            Label(self.centerframe, width=1, bg=LIGHTPURPLE).grid(
                row=0, column=x, sticky=NSEW)
        for y in range(15):
            self.centerframe.rowconfigure(y, weight=1, uniform='y')
            Label(self.centerframe, width=1, bg=LIGHTPURPLE).grid(
                row=y, column=0, sticky=NSEW)
        self.centerframebackgroundimage = Image.open(r"Assets\managementsuite\manageeventswidgets\centerframebackground.png")
        self.centerframebackgroundimage = ImageTk.PhotoImage(self.centerframebackgroundimage.resize(
            (math.ceil(720 * dpi / 96), math.ceil(600 * dpi / 96)), Image.Resampling.LANCZOS))
        self.centerframebackgroundlabel = Label(self.centerframe, image=self.centerframebackgroundimage, width=1, height=1, bg=LIGHTPURPLE)
        self.centerframebackgroundlabel.grid(row=0, column=0, rowspan=15, columnspan=18, sticky=NSEW)
        self.rightframe = Frame(self.interfaceframe, bg=LIGHTPURPLE, width=1, height=1)
        self.rightframe.grid(row=1, column=26, rowspan=15, columnspan=11, sticky=NSEW)
        for x in range(11):
            self.rightframe.columnconfigure(x, weight=1, uniform='x')
            Label(self.rightframe, width=1, bg=LIGHTPURPLE).grid(
                row=0, column=x, sticky=NSEW)
        for y in range(15):
            self.rightframe.rowconfigure(y, weight=1, uniform='y')
            Label(self.rightframe, width=1, bg=LIGHTPURPLE).grid(
                row=y, column=0, sticky=NSEW)
        self.rightframe.grid_propagate(False)
        self.rightframebackgroundimage = Image.open(r"Assets\managementsuite\manageeventswidgets\rightframe.png")
        self.rightframebackgroundimage = ImageTk.PhotoImage(self.rightframebackgroundimage.resize(
            (math.ceil(440 * dpi / 96), math.ceil(600 * dpi / 96)), Image.Resampling.LANCZOS))
        self.rightframebackgroundlabel = Label(self.rightframe, image=self.rightframebackgroundimage, width=1, height=1, bg=LIGHTPURPLE)
        self.rightframebackgroundlabel.grid(row=0, column=0, rowspan=15, columnspan=11, sticky=NSEW)
        self.studentcountlabel = Label(self.rightframe, image=self.studentcountimg, width=1, height=1)
        self.studentcountlabel.grid()


    def generate_widgets(self):
        self.labelbackground = Image.open(r"Assets\managementsuite\manageeventswidgets\bgfortitle.png")
        self.labelbackground = ImageTk.PhotoImage(self.labelbackground.resize(
            (math.ceil(480 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.editbuttonimage = Image.open(r"Assets\managementsuite\manageeventswidgets\editicon.png")
        self.editbuttonimage = ImageTk.PhotoImage(self.editbuttonimage.resize(
            (math.ceil(80 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.deletebuttonimage = Image.open(r"Assets\managementsuite\manageeventswidgets\deleteicon.png")
        self.deletebuttonimage = ImageTk.PhotoImage(self.deletebuttonimage.resize(
            (math.ceil(80 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))

    def database_queries(self):
        self.generate_widgets()
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT COUNT(event_name) FROM eventcreation")
        self.eventcount = self.c.fetchone()
        self.eventcount = self.eventcount[0]
        self.c.execute("SELECT event_name FROM eventcreation")
        self.events = self.c.fetchall()
        self.overallframes = {}
        self.framesneeded = math.ceil(self.eventcount / 4)
        #configure a label to display the page number
        self.page = 1
        self.pagecount = Label(self.centerframe, width=1,height=1, text="Page\n" + str(self.page) + " of " + str(self.framesneeded), bg=LIGHTPURPLE, fg="black", font=("Arial", 14))
        self.pagecount.grid(row=0, column=15, rowspan=2, columnspan=3, sticky=NSEW) 
        self.backgroundforframes = Image.open(r"Assets\managementsuite\manageeventswidgets\backgroundforpages.png")
        self.backgroundforframes = ImageTk.PhotoImage(self.backgroundforframes.resize(
                (math.ceil(640 * dpi / 96), math.ceil(440 * dpi / 96)), Image.Resampling.LANCZOS))
        #configure the next and previous buttons
        button = Button(self.centerframe, text="<", height=1,width=1, command=lambda:self.previous_page())
        button.grid(row=2, column=15, rowspan=1, columnspan=1, sticky=NSEW)
        button2 = Button(self.centerframe, text=">", height=1,width=1, command=lambda:self.next_page())
        button2.grid(row=2, column=17, rowspan=1, columnspan=1, sticky=NSEW)
        #configure the frames
        for x in range(self.framesneeded):
            self.overallframes[x] = Frame(self.centerframe, bg=LIGHTPURPLE, relief=FLAT, width=1, height=1)
            self.overallframes[x].grid(row=3, column=1, rowspan=11, columnspan=16, sticky=NSEW)
            self.overallframes[x].grid_propagate(False)
            for y in range(11):
                self.overallframes[x].rowconfigure(y, weight=1, uniform='y')
                Label(self.overallframes[x], width=1, bg=NAVYBLUE).grid(
                    row=y, column=0, sticky=NSEW)
            for z in range(16):
                self.overallframes[x].columnconfigure(z, weight=1, uniform='x')
                Label(self.overallframes[x], width=1, bg=NAVYBLUE).grid(
                    row=0, column=z, sticky=NSEW)
            Label(self.overallframes[x], image=self.backgroundforframes, width=1, height=1, bg=LIGHTPURPLE).grid(
                row=0, column=0, rowspan=11, columnspan=16, sticky=NSEW)
            self.overallframes[x].grid_remove()
        #self.events = c.fetchall()
        initialrow = 0 
        rowcount = 0
        for event in self.events:
            event_name = event[0]
            if initialrow<=9:
                Label(self.overallframes[0], text=f"{event_name}", image=self.labelbackground, width=1, height=1, font=("Avenir Next Bold", 18),fg="white", bg=LIGHTPURPLE, compound=CENTER).grid(row=initialrow, column=0, rowspan=2, columnspan=12, sticky=NSEW)
                Button(self.overallframes[0], image=self.editbuttonimage, width=1, height=1, bg=LIGHTPURPLE, relief=FLAT, command=lambda event_name=event_name:self.edit_event(event_name)).grid(
                    row=initialrow, column=12, rowspan=2, columnspan=2, sticky=NSEW)
                Button(self.overallframes[0], image=self.deletebuttonimage, width=1, height=1, bg=LIGHTPURPLE, relief=FLAT, command=lambda event_name=event_name: self.confirm_delete(event_name)).grid(
                    row=initialrow, column=14, rowspan=2, columnspan=2, sticky=NSEW)
            elif initialrow<=18:
                Label(self.overallframes[1], text=f"{event_name}", image=self.labelbackground, width=1, height=1, font=("Avenir Next Bold", 18),fg="white", bg=LIGHTPURPLE, compound=CENTER).grid(row=rowcount, column=0, rowspan=2, columnspan=12, sticky=NSEW)
                Button(self.overallframes[1], image=self.editbuttonimage, width=1, height=1, bg=LIGHTPURPLE, relief=FLAT,command=lambda event_name=event_name:self.edit_event(event_name)).grid(
                    row=rowcount, column=12, rowspan=2, columnspan=2, sticky=NSEW)
                Button(self.overallframes[1], image=self.deletebuttonimage, width=1, height=1, bg=LIGHTPURPLE, relief=FLAT, command=lambda event_name=event_name: self.confirm_delete(event_name)).grid(
                    row=rowcount, column=14, rowspan=2, columnspan=2, sticky=NSEW) #Every button is configured to call the confirm_delete(this event name)
                rowcount += 3
            initialrow += 3

        self.overallframes[0].grid()
    def edit_event(self, eventname):
        self.tempframe = Frame(self.interfaceframe, bg=LIGHTPURPLE, relief=FLAT, width=1,height=1)
        self.tempframe.grid(row=1, column=7, rowspan=15, columnspan=18, sticky=NSEW)
        self.tempframe.grid_propagate(False)
        for y in range(15):
            self.tempframe.rowconfigure(y, weight=1, uniform='y')
            Label(self.tempframe, width=1, bg=NAVYBLUE).grid(
                row=y, column=0, sticky=NSEW)
        for z in range(18):
            self.tempframe.columnconfigure(z, weight=1, uniform='x')
            Label(self.tempframe, width=1, bg=NAVYBLUE).grid(
                row=0, column=z, sticky=NSEW)
        Label(self.tempframe, image=self.centerframebackgroundimage, width=1, height=1, bg=LIGHTPURPLE).grid(
            row=0, column=0, rowspan=15, columnspan=18, sticky=NSEW)
        #button to remove the frame
        Button(self.tempframe, text="X", width=1, height=1, bg=LIGHTPURPLE, relief=FLAT, command=lambda:self.tempframe.grid_remove()).grid(row=0, column=17, rowspan=1, columnspan=1, sticky=NSEW)
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM eventcreation WHERE event_name=?", (eventname,))
        # works on a temporary frame to display the event information
        event_details = self.c.fetchone()
        event_key = event_details[0]
        event_name = event_details[1]
        event_description = event_details[2]
        event_startdate = event_details[3]
        event_enddate = event_details[4]
        event_starttime = event_details[5]
        event_endtime = event_details[6]
        event_organizer = event_details[7]
        venue_name = event_details[8]
        host_name = event_details[9]
        event_image = io.BytesIO(event_details[10])
        event_image = Image.open(event_image)
        self.event_image = ImageTk.PhotoImage(event_image.resize(
            (math.ceil(200 * dpi / 96), math.ceil(200 * dpi / 96)), Image.Resampling.LANCZOS))
        event_keybutton = Button(self.tempframe, text=f"Event Key: {event_key}", anchor=CENTER, width=1, height=1, font=("Avenir Next Bold", 18),fg="white", bg=ORANGE, compound=CENTER)
        event_keybutton.grid(row=0, column=1, rowspan=1, columnspan=8, sticky=NSEW)
        event_namebutton = Button(self.tempframe, text=f"Event name: {event_name}", anchor=W, width=1, height=1, font=("Avenir Next Bold", 18),fg="white", bg=NAVYBLUE, command=lambda:self.changing_details("normal",event_key, event_name, fieldchanged="event_name"))
        event_namebutton.grid(row=1, column=1, rowspan=1, columnspan=11, sticky=NSEW)
        event_descriptionbutton = Button(self.tempframe, text=f"Description:\n{event_description}", anchor=CENTER, width=1, height=1, font=("Avenir Next Bold", 18),fg="white", bg=NAVYBLUE, command=lambda:self.changing_details("normal",event_key, event_description, fieldchanged="event_description"))
        event_descriptionbutton.grid(row=2, column=1, rowspan=3, columnspan=11, sticky=NSEW)
        event_datebutton = Button(self.tempframe, text=f"Date: {event_startdate} - {event_enddate}", anchor=W, width=1, height=1, font=("Avenir Next Bold", 18),fg="white", bg=NAVYBLUE,command=lambda:self.changing_details("date", event_key, (event_startdate, event_enddate)))
        event_datebutton.grid(row=5, column=1, rowspan=1, columnspan=11, sticky=NSEW)
        event_timebutton = Button(self.tempframe, text=f"Time: {event_starttime} - {event_endtime}", anchor=W, width=1, height=1, font=("Avenir Next Bold", 18),fg="white", bg=NAVYBLUE, command= lambda:self.changing_details("time", event_key,(event_starttime, event_endtime)))
        event_timebutton.grid(row=6, column=1, rowspan=1, columnspan=11, sticky=NSEW)
        event_organizerbutton = Button(self.tempframe, text=f"Organizer: {event_organizer}", anchor=W, width=1, height=1, font=("Avenir Next Bold", 18),fg="white", bg=NAVYBLUE, command=lambda:self.changing_details("normal", event_key,  event_organizer, fieldchanged="event_organizer"))
        event_organizerbutton.grid(row=7, column=1, rowspan=1, columnspan=11, sticky=NSEW)
        venue_namebutton = Button(self.tempframe, text=f"Venue: {venue_name}", anchor=W, width=1, height=1, font=("Avenir Next Bold", 18),fg="white", bg=NAVYBLUE, command=lambda:self.changing_details("normal", event_key, venue_name, fieldchanged="venue_name"))
        venue_namebutton.grid(row=8, column=1, rowspan=1, columnspan=11, sticky=NSEW)
        host_namebutton = Button(self.tempframe, text=f"Host: {host_name}", anchor=W, width=1, height=1, font=("Avenir Next Bold", 18),fg="white", bg=NAVYBLUE, command=lambda:self.changing_details("normal", event_key, host_name, fieldchanged="host_name"))
        host_namebutton.grid(row=9, column=1, rowspan=1, columnspan=11, sticky=NSEW)
        event_imagelabel = Label(self.tempframe, image=self.event_image, width=1, height=1, bg=LIGHTPURPLE)
        event_imagelabel.grid(row=1, column=13, rowspan=4, columnspan=4, sticky=NSEW) 
    def changing_details(self, entrytype, event_key, *args, **kwargs):
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        field_changed = kwargs.get("fieldchanged")
        #refactor this function 
        def confirm_action(entrytype, *args, **kwargs):
            if entrytype == "normal":
                with self.conn:
                    self.c.execute(f"UPDATE eventcreation SET {field_changed} = ? WHERE eventkey_number = ?", (normalentry.get(), event_key))
                    messagebox.showinfo("Success", f"{field_changed} updated successfully where event key is {event_key}")
            elif entrytype == "date":
                with self.conn:
                    self.c.execute(f"UPDATE eventcreation SET event_startdate = ?, event_enddate = ? WHERE eventkey_number = ?", (start_dateentry.get(), enddateentry.get(), event_key))
                    messagebox.showinfo("Success",  f"event_startdate changed to {start_dateentry.get()} and\nevent_enddate changed to {enddateentry.get()}.\nUpdated successfully where event key is {event_key}.")
            elif entrytype == "time":
                with self.conn:
                    self.c.execute("UPDATE eventcreation SET event_starttime = ?, event_endtime = ? WHERE eventkey_number = ?", (starttimeentry.get(), endtimeentry.get(), event_key))
                    messagebox.showinfo("Success",  f"event_starttime changed to {starttimeentry.get()} and\nevent_endtime changed to {endtimeentry.get()}.\nUpdated successfully where event key is {event_key}.")
        for widget in self.tempframe.winfo_children():
            if widget.winfo_class() == "Entry":
                widget.destroy()
        if entrytype == "normal":
            normalentry = Entry(self.tempframe, width=1, font=("Avenir Next Bold", 18),fg="black", bg=LIGHTYELLOW, justify=CENTER)
            normalentry.grid(row=11, column=3, rowspan=2, columnspan=12, sticky=NSEW)
            normalentry.delete(0, END)
            normalentry.insert(0, args[0])
            normalentry.focus_set()
            confirmbutton = Button(self.tempframe, text=f"Confirm changes for {field_changed}", anchor=CENTER, width=1, height=1, font=("Avenir Next Bold", 18),fg="black", bg=LIGHTPURPLE, command=lambda:confirm_action(entrytype, args[0]))
            confirmbutton.grid(row=13, column=3, rowspan=2, columnspan=12, sticky=NSEW)
        elif entrytype == "date":
            start_dateentry = Entry(self.tempframe, width=1, font=("Avenir Next Bold", 18),fg="black", bg=LIGHTYELLOW, justify=CENTER)
            start_dateentry.grid(row=11, column=2, rowspan=2, columnspan=6, sticky=NSEW)
            start_dateentry.delete(0, END)
            start_dateentry.insert(0, args[0][0])
            start_dateentry.focus_set()
            enddateentry = Entry(self.tempframe, width=1, font=("Avenir Next Bold", 18),fg="black", bg=LIGHTYELLOW, justify=CENTER)
            enddateentry.grid(row=11, column=10, rowspan=2, columnspan=6, sticky=NSEW)
            enddateentry.delete(0, END)
            enddateentry.insert(0, args[0][1])
            confirmbutton = Button(self.tempframe, text="Confirm changes for date", anchor=CENTER, width=1, height=1, font=("Avenir Next Bold", 18),fg="black", bg=ORANGE, command=lambda:confirm_action(entrytype))
            confirmbutton.grid(row=13, column=3, rowspan=2, columnspan=12, sticky=NSEW)
        elif entrytype == "time":
            starttimeentry = Entry(self.tempframe, width=1, font=("Avenir Next Bold", 18),fg="black", bg=LIGHTYELLOW, justify=CENTER)
            starttimeentry.grid(row=11, column=2, rowspan=2, columnspan=6, sticky=NSEW)
            starttimeentry.delete(0, END)
            starttimeentry.insert(0, args[0][0])
            starttimeentry.focus_set()
            endtimeentry = Entry(self.tempframe, width=1, font=("Avenir Next Bold", 18),fg="black", bg=LIGHTYELLOW, justify=CENTER)
            endtimeentry.grid(row=11, column=10, rowspan=2, columnspan=6, sticky=NSEW)
            endtimeentry.delete(0, END)
            endtimeentry.insert(0, args[0][1])
            confirmbutton = Button(self.tempframe, text="Confirm changes for time", anchor=CENTER, width=1, height=1, font=("Avenir Next Bold", 18),fg="black", bg=LIGHTYELLOW, command=lambda:confirm_action(entrytype))
            confirmbutton.grid(row=13, column=3, rowspan=2, columnspan=12, sticky=NSEW)
    def confirm_delete(self, event_name):
        for widget in self.rightframe.winfo_children():
            # print(widget)
            #specific widget names to destroy
            #widget to be deleted is .!frame.!viewparticipants.!frame.!frame2.!label28
            #delete all widgets where !label is greater than 28
            if widget.winfo_class() == "Button":
                widget.destroy()
 
        #Are you sure you want to delete this event?
        # Label to confirm delete
        # Button to confirm delete
        # Button to cancel delete
        #Label that counts the registrants for the event and asks if you want to delete them as well
        self.studentcountlabel.grid(row=8, column=2, rowspan=2, columnspan=5, sticky=NSEW)
        print(self.studentcountlabel.winfo_name())
        self.cancelimageorg = Image.open(r"Assets\managementsuite\manageeventswidgets\cancelbutton.png")
        self.cancelimage= ImageTk.PhotoImage(self.cancelimageorg.resize(
            (math.ceil(160 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))          
        self.cdeleteimageorg = Image.open(r"Assets\managementsuite\manageeventswidgets\confirmbutton.png")
        self.cdeleteimage = ImageTk.PhotoImage(self.cdeleteimageorg.resize(
            (math.ceil(160 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        canceldeletebutton = Button(self.rightframe, image=self.cancelimage, width=1, height=1, command=lambda:self.cancel_delete())
        canceldeletebutton.grid(row=11, column=1, rowspan=2, columnspan=4, sticky=NSEW)
        print(canceldeletebutton.winfo_class())
        confirmdeletebutton = Button(self.rightframe, width=1, height=1, image=self.cdeleteimage, command=lambda:self.delete_event(event_name))
        confirmdeletebutton.grid(row=11, column=6, rowspan=2, columnspan=4, sticky=NSEW)
        confirmdeletelabel = Button(self.rightframe, text="Are you sure you want\nto delete this event?", anchor=CENTER, width=1, height=1, font=("Avenir Next Bold", 14),fg="black", bg=LIGHTPURPLE)
        confirmdeletelabel.grid(row=1, column=1, rowspan=2, columnspan=9, sticky=NSEW)
    def cancel_delete(self):
        self.studentcountlabel.grid_remove()
        for widget in self.rightframe.winfo_children():
            if widget.winfo_class() == "Button":
                widget.destroy()
 
    def delete_event(self, event_name):
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("DELETE FROM eventcreation WHERE event_name = ?", (event_name,))
            messagebox.showinfo("Success", f"Event with event name {event_name} deleted successfully")

    def next_page(self):
        if self.page < self.framesneeded:
            self.page += 1
            self.pagecount.config(text="Page\n" + str(self.page) + " of " + str(self.framesneeded))
            self.overallframes[self.page-2].grid_remove()
            self.overallframes[self.page-1].grid()
    def previous_page(self):
        if self.page > 1:
            self.page -= 1
            self.pagecount.config(text="Page\n" + str(self.page) + " of " + str(self.framesneeded))
            self.overallframes[self.page].grid_remove()
            self.overallframes[self.page-1].grid()

    #View participants functions
    def view_participants(self):
        self.viewparticipants = Frame(self, width=1, height=1, bg=WHITE)
        self.viewparticipants.grid(row=3, column=2, rowspan=17, columnspan=38, sticky=NSEW)
        self.viewparticipants.grid_propagate(False)
        for x in range(38):
            self.viewparticipants.columnconfigure(x, weight=1, uniform="x")
            Label(self.viewparticipants, bg=WHITE).grid(row=0, column=x, sticky=NSEW)
        for y in range(17):
            self.viewparticipants.rowconfigure(y, weight=1, uniform="y")
            Label(self.viewparticipants, bg=WHITE).grid(row=y, column=0, sticky=NSEW)
        #background label
        self.searchbyeventsframe = Frame(self, width=1, height=1, bg=WHITE)
        self.searchbyeventsframe.grid(row=3, column=2, rowspan=17, columnspan=38, sticky=NSEW)
        self.searchbyeventsframe.grid_propagate(False)
        #~~~~~~~~~~~~~~ Search by events frame ~~~~~~~~~~~~~~~
        for x in range(38):
            self.searchbyeventsframe.columnconfigure(x, weight=1, uniform="x")
            Label(self.searchbyeventsframe, bg=WHITE).grid(row=0, column=x, sticky=NSEW)
        for y in range(17):
            self.searchbyeventsframe.rowconfigure(y, weight=1, uniform="y")
            Label(self.searchbyeventsframe, bg=WHITE).grid(row=y, column=0, sticky=NSEW)
        self.searchbyeventsframe.grid_remove()
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~ IMAGES ~~~~~~~~~~~~~~
        self.vpbgorg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\viewparticipantsbg.png")
        self.vpbg = ImageTk.PhotoImage(self.vpbgorg.resize(
            (math.ceil(1520 * dpi / 96), math.ceil(680 * dpi / 96)), Image.Resampling.LANCZOS))
        self.vpbglabel = Label(self.viewparticipants, image=self.vpbg,width=1,height=1,bg=WHITE)
        self.vpbglabel.grid(row=0, column=0, rowspan=17, columnspan=38, sticky=NSEW)
        self.searchregistrantsimg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\searchregistrantsbutton280x80.png")
        self.searchregistrants = ImageTk.PhotoImage(self.searchregistrantsimg.resize(
            (math.ceil(280 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.searcheventsimg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\searchbyevents280x80.png")
        self.searchevents = ImageTk.PhotoImage(self.searcheventsimg.resize(
            (math.ceil(280 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.backimg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\vpbackbutton280x80.png")
        self.back = ImageTk.PhotoImage(self.backimg.resize(
            (math.ceil(280 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.searchregistrantsbutton = Button(self.viewparticipants, image=self.searchregistrants, width=1, height=1, relief=SOLID, bd=4, highlightthickness=1, highlightbackground=LIGHTPURPLE, command=lambda:self.viewparticipants.grid())
        self.searchregistrantsbutton.grid(row=2, column=2, rowspan=2, columnspan=7, sticky=NSEW)
        self.searcheventsbutton = Button(self.viewparticipants, image=self.searchevents, width=1, height=1, command=lambda:[self.searchbyeventsframe.grid(),self.show_searchevents()])
        self.searcheventsbutton.grid(row=6, column=2, rowspan=2, columnspan=7, sticky=NSEW)
        self.backbutton = Button(self.viewparticipants, image=self.back, width=1, height=1, command=lambda:self.interfaceframe.tkraise())
        self.backbutton.grid(row=10, column=2, rowspan=2, columnspan=7, sticky=NSEW)
        self.searchframe = Frame(self.viewparticipants, width=1, height=1, bg=WHITE)
        self.searchframe.grid(row=0, column=10, rowspan=17, columnspan=11, sticky=NSEW)
        self.searchframe.grid_propagate(False)
        for x in range(11):
            self.searchframe.columnconfigure(x, weight=1, uniform="x")
            Label(self.searchframe, bg=ORANGE).grid(row=0, column=x, sticky=NSEW)
        for y in range(17):
            self.searchframe.rowconfigure(y, weight=1, uniform="y")
            Label(self.searchframe, bg=ORANGE).grid(row=y, column=0, sticky=NSEW)
        self.searchframebgorg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\searchframebg.png")
        self.searchframebg = ImageTk.PhotoImage(self.searchframebgorg.resize(
            (math.ceil(440 * dpi / 96), math.ceil(680 * dpi / 96)), Image.Resampling.LANCZOS))
        self.searchframebglabel = Label(self.searchframe, image=self.searchframebg, width=1,height=1, bg=WHITE)
        self.searchframebglabel.grid(row=0, column=0, rowspan=17, columnspan=11, sticky=NSEW)
        self.searchbuttonimg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\magnifyingbutton80x80.png")
        self.searchbutton = ImageTk.PhotoImage(self.searchbuttonimg.resize(
            (math.ceil(80 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.searchbuttonbutton = Button(self.searchframe, image=self.searchbutton, width=1, height=1, command=lambda:self.searchregistrants_function(searchentry.get()))
        self.searchbuttonbutton.grid(row=1, column=8, rowspan=2, columnspan=2, sticky=NSEW)
        searchentry = Entry(self.searchframe, width=1, bg=WHITE, fg="black", font=("Arial", 14))
        searchentry.grid(row=2, column=1, rowspan=1, columnspan=6, sticky=NSEW)
    def searchregistrants_function(self, name): #name is searchentry.get()
        #database queries
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor() 
        if name == "":
            self.c.execute("SELECT DISTINCT full_name, icpass_number, email FROM eventregistration")
        else:
            self.c.execute("SELECT DISTINCT full_name, icpass_number, email FROM eventregistration WHERE full_name LIKE ?", ("%"+name+"%",))
        self.results = self.c.fetchall()
        self.count = len(self.results)
        #in case somebody clicks a name while looking at edit page
        print(f"The return from searching up {name} are {self.results}")
        print(f"The number of students found using this name is {self.count}")
        self.searchresultsframe = Frame(self.searchframe, width=1, height=1, bg=WHITE)
        self.searchresultsframe.grid(row=6, column=1, rowspan=11, columnspan=9, sticky=NSEW)
        for x in range(9):
            self.searchresultsframe.columnconfigure(x, weight=1, uniform="x")
            Label(self.searchresultsframe, width=1, bg=WHITE).grid(row=0, column=x, sticky=NSEW)
        for y in range(11):
            self.searchresultsframe.rowconfigure(y, weight=1, uniform="x")
            Label(self.searchresultsframe, width=1, bg=WHITE).grid(row=y, column=0, sticky=NSEW)
        self.searchresultsframe.grid_propagate(False)
        self.studentprofileimg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\studentprofile360x80.png")
        self.studentprofile = ImageTk.PhotoImage(self.studentprofileimg.resize(
            (math.ceil(360 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        #display results
        # first in the database, we need to check if the person has the same name, will return 
        #searches for registrants in the eventregistration table using the name parameter
        #if the name parameter is empty, returns all registrants
        #if the name parameter is not empty, returns all registrants with the approx-same name entry in the name parameter
        #Generic student profile result picture button 
        # for loop to generate buttons for each result
        # each button will have the name of the student, and the ic/passport number
        # when the button is clicked, it will open a new window with the student's profile
        # the student's profile will have the student's name, ic/passport number, email, and the events that they have registered for
        # the student's profile will also have a button to remove the student from the event
        # the student's profile will also have a button to edit the student's profile
        # this is the code
        self.eventsregisteredforframe = Frame(self.viewparticipants, width=1, height=1, bg=WHITE)
        self.eventsregisteredforframe.grid(row=4, column=22, rowspan=11, columnspan=15, sticky=NSEW)
        for x in range(15):
            self.eventsregisteredforframe.columnconfigure(x, weight=1, uniform="x")
            Label(self.eventsregisteredforframe, bg=WHITE, width=1).grid(row=0, column=x, sticky=NSEW)
        for y in range(11):
            self.eventsregisteredforframe.rowconfigure(y, weight=1, uniform="y")
            Label(self.eventsregisteredforframe, bg=WHITE, width=1).grid(row=y, column=0, sticky=NSEW)
        self.eventsregisteredforframe.grid_propagate(False)
        # self.eventsregisteredforframebgorg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\eventsregisteredforframebg.png")
        # self.eventsregisteredforframebg = ImageTk.PhotoImage(self.eventsregisteredforframebgorg.resize(
        #     (math.ceil(680 * dpi / 96), math.ceil(680 * dpi / 96)), Image.Resampling.LANCZOS))
        # self.eventsregisteredforframebglabel = Label(self.eventsregisteredforframe, image=self.eventsregisteredforframebg, width=1,height=1, bg=WHITE)
        # self.eventsregisteredforframebglabel.grid(row=0, column=0, rowspan=17, columnspan=17, sticky=NSEW)

        for indexofdetails in range(self.count):
            self.results[indexofdetails]
            fullname = self.results[indexofdetails][0]
            icpassnumber = self.results[indexofdetails][1]
            email = self.results[indexofdetails][2]
            
            # informationtuple = (fullname, icpassnumber, email)
            Button(self.searchresultsframe, image=self.studentprofile,
                    width=1, height=1,
                    text= f"Student name = {fullname}\nIC/Pass No. = {icpassnumber}\nEmail = {email}", compound=CENTER, font=("Avenir Next", 12), fg="black", bg=WHITE,
                    command=lambda x=(fullname,icpassnumber,email) :self.generate_eventlist(x)).grid(row=indexofdetails*2, column=0, rowspan=2, columnspan=9, sticky=NSEW)
    def generate_eventlist(self, information:tuple): #searches the eventregistration list to find all instances of name, ic, email and returns the events
        #database queries
        #in case somebody clicks a name while looking at edit page
        try:
            self.frametoshowdetails.grid_remove()
        except:
            pass
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        #unpacking the tuple 
        self.fullname = information[0]
        self.icpassnumber = information[1]
        self.email = information[2]
        self.c.execute("SELECT COUNT(event_registered) FROM eventregistration WHERE full_name = ? AND icpass_number = ? AND email = ?", (self.fullname, self.icpassnumber, self.email))
        self.count = self.c.fetchone()[0]
        self.c.execute("SELECT event_registered FROM eventregistration WHERE full_name = ? AND icpass_number = ? AND email = ?", (self.fullname, self.icpassnumber, self.email))
        self.results = self.c.fetchall()
        print(f"This student with name {self.fullname} has registered for {self.results}")
        print(f"The number of events this student has registered for is {self.count}")
        #display results
        # basically presenting the events that the student has registered for
        #initializing the read student and delete student images 
        self.readstudentimg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\readstudentdetails.png")
        self.readstudent = ImageTk.PhotoImage(self.readstudentimg.resize(
            (math.ceil(80 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.deletestudentimg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\deletestudent80x80.png")
        self.deletestudent = ImageTk.PhotoImage(self.deletestudentimg.resize(
            (math.ceil(80* dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        #deleting the previous widgets in the eventsregisteredforframe
        for widget in self.eventsregisteredforframe.winfo_children():
            if widget.winfo_class() == "Button":
                widget.destroy()
        for indexofdetails in range(self.count):
            self.results[indexofdetails]
            eventregistered = self.results[indexofdetails][0]
            testbutton = Button(self.eventsregisteredforframe, state=DISABLED, width=1 , height=1, text=f"Event name = {eventregistered}", font=("Avenir Next Medium", 14), fg="black", bg=LIGHTPURPLE)
            testbutton.grid(row=indexofdetails*2, column=0, rowspan=2, columnspan=11, sticky=NSEW)
            testbutton.grid_propagate(False)
            editbutton = Button(self.eventsregisteredforframe, image=self.readstudent,
                    width=1, height=1,
                    text= f"EDIT", compound=CENTER, font=("Avenir Next Medium", 12), fg=WHITE, bg=WHITE,
                    command=lambda x=eventregistered, y=self.fullname:self.read_student_details(x,y))
            editbutton.grid(row=indexofdetails*2, column=11, rowspan=2, columnspan=2, sticky=NSEW)
            editbutton.grid_propagate(False)
            deletebutton = Button(self.eventsregisteredforframe, image=self.deletestudent,
                    width=1, height=1,
                    text= f"DELETE", compound=CENTER, font=("Avenir Next Medium", 12), fg=WHITE, bg=WHITE,
                    command=lambda x=eventregistered, y=self.fullname:self.delete_student(x,y))
            deletebutton.grid(row=indexofdetails*2, column=13, rowspan=2, columnspan=2, sticky=NSEW)
            deletebutton.grid_propagate(False)
        self.frametoshowdetails = Frame(self.eventsregisteredforframe, bg=NICEBLUE, height=1,width=1)
        self.frametoshowdetails.grid(row=0, column=0, rowspan=11, columnspan=15, sticky=NSEW)
        self.frametoshowdetails.grid_propagate(False)
        for x in range (15):
            self.frametoshowdetails.columnconfigure(x, weight=1, uniform="x")
            Label(self.frametoshowdetails, bg=NICEBLUE, width=1).grid(row=0, column=x, sticky=NSEW)
        for y in range (11):
            self.frametoshowdetails.rowconfigure(y, weight=1, uniform="y")
            Label(self.frametoshowdetails, bg=NICEBLUE, width=1).grid(row=y, column=0, sticky=NSEW)
        self.frametoshowdetails.grid_remove()
    def read_student_details(self, eventname, studentname):
        print(f"Read {studentname}'s details for {eventname}")
        self.frametoshowdetails.grid()
        self.frametoshowdetails.grid_propagate(False)
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM eventregistration WHERE full_name = ? AND event_registered = ?", (studentname, eventname))
        self.results = self.c.fetchall()
        removetheframe = Button(self.frametoshowdetails, width=1, height=1, text="X", font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, command=lambda:self.frametoshowdetails.grid_remove())
        removetheframe.grid(row=0, column=14, sticky=NSEW)
        self.fullname = self.results[0][0]
        self.icpassnumber = self.results[0][1]
        self.phonenumb = self.results[0][2]
        self.email = self.results[0][3]
        self.address = self.results[0][4]
        self.fullnameentry = Entry(self.frametoshowdetails, width=1, font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, justify=CENTER)
        self.fullnameentry.grid(row=7, column=2, rowspan=2, columnspan=11, sticky=NSEW)
        self.icpassnoentry = Entry(self.frametoshowdetails, width=1, font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, justify=CENTER)
        self.icpassnoentry.grid(row=7, column=2, rowspan=2, columnspan=11, sticky=NSEW)
        self.phonenumentry = Entry(self.frametoshowdetails, width=1, font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, justify=CENTER)
        self.phonenumentry.grid(row=7, column=2, rowspan=2, columnspan=11, sticky=NSEW)
        self.emailentry = Entry(self.frametoshowdetails, width=1, font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, justify=CENTER)
        self.emailentry.grid(row=7, column=2, rowspan=2, columnspan=11, sticky=NSEW)
        self.addressentry = Entry(self.frametoshowdetails, width=1, font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, justify=CENTER)
        self.addressentry.grid(row=7, column=2, rowspan=2, columnspan=11, sticky=NSEW)
        entrylist = [self.fullnameentry, self.icpassnoentry, self.phonenumentry, self.emailentry, self.addressentry]
        for entry in entrylist:
            entry.grid_remove()
        fullnamebutton = Button(self.frametoshowdetails, text=f"Full name: {self.fullname}", font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, command=lambda:self.entryinitializer(self.fullnameentry, self.fullname, fieldchanged="full_name",  originaltext=self.fullname, eventregistered=eventname) ).grid(row=1, column=1, columnspan=13, sticky=NSEW)
        icpassnumberbutton = Button(self.frametoshowdetails, text=f"IC/Passport number: {self.icpassnumber}", font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, command=lambda:self.entryinitializer(self.icpassnoentry, self.icpassnumber, fieldchanged="icpass_number", originaltext=self.icpassnumber, eventregistered=eventname)).grid(row=2, column=1, columnspan=13, sticky=NSEW)
        phonenumbbutton = Button(self.frametoshowdetails, text=f"Phone number: {self.phonenumb}", font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, command=lambda:self.entryinitializer(self.phonenumentry, self.phonenumb, fieldchanged="phone_number", originaltext=self.phonenumb, eventregistered=eventname)).grid(row=3, column=1, columnspan=13, sticky=NSEW)
        emailbutton = Button(self.frametoshowdetails, text=f"Email: {self.email}", font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, command=lambda:self.entryinitializer(self.emailentry, self.email, fieldchanged="email", originaltext=self.email, eventregistered=eventname)).grid(row=4, column=1, columnspan=13, sticky=NSEW)
        addressbutton = Button(self.frametoshowdetails, text=f"Address: {self.address}", font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, command=lambda:self.entryinitializer(self.addressentry, self.address, fieldchanged="address", originaltext=self.address, eventregistered=eventname)).grid(row=5, column=1, columnspan=13, sticky=NSEW)

    def entryinitializer(self, entrywanted, texttochange,  **kwargs):
        fieldchanged = kwargs.get("fieldchanged")
        originaltext = kwargs.get("originaltext")
        eventregistered = kwargs.get("eventregistered")
        #these entries all occupy the same place, only grid() when called upon.
        #remove all entries when called upon
        entrylist = [self.fullnameentry, self.icpassnoentry, self.phonenumentry, self.emailentry, self.addressentry]
        for entry in entrylist:
            if entry != entrywanted:
                entry.grid_remove()
        #grid the entry wanted
        entrywanted.grid()
        entrywanted.delete(0, END)
        entrywanted.insert(0, texttochange)
        entrywanted.focus_set()
        #confirm button
        confirmbutton = Button(self.frametoshowdetails, text="Confirm Edit", font=("Avenir Next Bold", 16), fg=WHITE, bg=NAVYBLUE, command=lambda:self.confirmchanges(entrywanted, texttochange, fieldchanged, originaltext, eventregistered)).grid(row=9, column=2, columnspan=11, sticky=NSEW)
    def confirmchanges(self, entrytogetinfo, texttochange, fieldchanged, originaltext, event_registered):
        #get the text from the entry
        textfromentry = entrytogetinfo.get()
        #update the database
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        with self.conn:
            try:
                self.c.execute(f"UPDATE eventregistration SET {fieldchanged} = ? WHERE {fieldchanged} = ? AND event_registered = ?", (textfromentry, originaltext, event_registered))
                messagebox.showinfo("Success", f"Changes have been made, where {fieldchanged} = {originaltext} has been changed to {textfromentry} under event {event_registered}")
            except Exception as e:
                messagebox.showerror("Error", f"An error has occured: {e}")

    # def edit_student_details(self, details):
    #     def update_details():
    #         self.conn = sqlite3.connect("interactivesystem.db")
    #         self.c = self.conn.cursor()
    #         with self.conn:
    #             self.c.execute("UPDATE eventregistration SET full_name = ?, ic_passport_number = ?, phone_number = ?, email = ?, address = ? WHERE full_name = ?", (self.fullname, self.icpassnumber, self.phonenumb, self.email, self.address, details))
    

        

    def delete_student(self, eventname, studentname):
        print(f"Delete {studentname}'s details for {eventname}")
        self.frametodeletestudent = Frame(self.eventsregisteredforframe, height=1, width=1,bg=PINK, relief=SOLID)
        self.frametodeletestudent.grid(row=0, column=0, rowspan=11, columnspan=15, sticky=NSEW)
        self.frametodeletestudent.grid_propagate(False)
        for x in range(15):
            self.frametodeletestudent.columnconfigure(x, weight=1)
            Label(self.frametodeletestudent, width=1, bg=PINK).grid(row=0, column=x, sticky=NSEW)
        for y in range(11):
            self.frametodeletestudent.rowconfigure(y, weight=1)
            Label(self.frametodeletestudent, width=1, bg=PINK).grid(row=y, column=0, sticky=NSEW)
        Label(self.frametodeletestudent, text=f"Are you sure you want to delete {studentname}'s details for \n{eventname}?", font=("Avenir Next", 14), fg=BLACK, bg=PINK).grid(row=1, column=1, columnspan=13, sticky=NSEW)
        Label(self.frametodeletestudent, text="This action cannot be undone.", font=("Avenir Next", 14), fg=BLACK, bg=PINK).grid(row=2, column=1, columnspan=13, sticky=NSEW)
        Label(self.frametodeletestudent, text="Please enter the word DELETE to confirm.", font=("Avenir Next", 14), fg=BLACK, bg=PINK).grid(row=3, column=1, columnspan=13, sticky=NSEW)
        self.deleteentry = Entry(self.frametodeletestudent, font=("Avenir Next", 14), fg=BLACK, bg=WHITE, justify=CENTER)
        self.deleteentry.grid(row=4, column=1, columnspan=13, sticky=NSEW)
        self.deleteentry.focus_set()
        Button(self.frametodeletestudent, text="Confirm", font=("Avenir Next", 14), fg=WHITE, bg=NAVYBLUE, command=lambda:self.delete_student_confirmed(eventname, studentname)).grid(row=5, column=1, columnspan=13, sticky=NSEW)
        Button(self.frametodeletestudent, text="Cancel", font=("Avenir Next", 14), fg=WHITE, bg=NAVYBLUE, command=lambda:self.frametodeletestudent.grid_remove()).grid(row=6, column=1, columnspan=13, sticky=NSEW)
    def delete_student_confirmed(self, eventname, studentname):
        if self.deleteentry.get() == "DELETE":
            self.conn = sqlite3.connect("interactivesystem.db")
            self.c = self.conn.cursor()
            with self.conn:
                try:
                    self.c.execute("DELETE FROM eventregistration WHERE event_registered = ? AND full_name = ?", (eventname, studentname))
                    messagebox.showinfo("Success", f"{studentname}'s details for\n{eventname} has been deleted.")
                    self.frametodeletestudent.grid_remove()
                except Exception as e:
                    messagebox.showerror("Error", f"An error has occured: {e}")
        else:
            messagebox.showerror("Error", "The word DELETE was not entered.")

    def show_searchevents(self):
        self.searchbyeventsframe.tkraise()
        
        # ~~~~~ IMAGES ~~~~~
        self.searcheventsorg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\vpsearcheventsbg.png")
        self.searcheventsbg = ImageTk.PhotoImage(self.searcheventsorg.resize(
            (math.ceil(1520 * dpi / 96), math.ceil(680 * dpi / 96)), Image.Resampling.LANCZOS))
        self.searcheventsbglabel = Label(self.searchbyeventsframe, image=self.searcheventsbg, width=1, height=1)
        self.searcheventsbglabel.grid(row=0, column=0, rowspan=17, columnspan=38, sticky=NSEW)
        self.searchregistrantsbutton = Button(self.searchbyeventsframe, image=self.searchregistrants, width=1, height=1, command=lambda:self.viewparticipants.tkraise())
        self.searchregistrantsbutton.grid(row=2, column=2, rowspan=2, columnspan=7, sticky=NSEW)
        self.searcheventsbutton = Button(self.searchbyeventsframe, image=self.searchevents, width=1, height=1,relief=SOLID, bd=4, highlightthickness=1, highlightbackground=LIGHTPURPLE, command=lambda:self.searchbyeventsframe.grid())
        self.searcheventsbutton.grid(row=6, column=2, rowspan=2, columnspan=7, sticky=NSEW)
        self.backbutton = Button(self.searchbyeventsframe, image=self.back, width=1, height=1, command=lambda:self.interfaceframe.tkraise())
        self.backbutton.grid(row=10, column=2, rowspan=2, columnspan=7, sticky=NSEW)
        self.searcheventsframe = Frame(self.searchbyeventsframe, height=1, width=1, bg=PINK)
        self.searcheventsframe.grid(row=0, column=10, rowspan=17, columnspan=11, sticky=NSEW)
        self.searcheventsframe.grid_propagate(0)
        for x in range(11):
            self.searcheventsframe.columnconfigure(x, weight=1)
            Label(self.searcheventsframe, width=1, bg=PINK).grid(row=0, column=x, sticky=NSEW)
        for y in range(17):
            self.searcheventsframe.rowconfigure(y, weight=1)
            Label(self.searcheventsframe, width=1, bg=PINK).grid(row=y, column=0, sticky=NSEW)
        self.searcheventsframebgorg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\searcheventsframebg.png")
        self.searcheventsframebg = ImageTk.PhotoImage(self.searcheventsframebgorg.resize(
            (math.ceil(440 * dpi / 96), math.ceil(680 * dpi / 96)), Image.Resampling.LANCZOS))
        self.searcheventsframebglabel = Label(self.searcheventsframe, image=self.searcheventsframebg, width=1, height=1)
        self.searcheventsframebglabel.grid(row=0, column=0, rowspan=17, columnspan=11, sticky=NSEW)
        self.searchbuttonimg1 = Image.open(r"Assets\managementsuite\viewparticipantswidgets\magnifyingbutton80x80.png")
        self.searchbutton1 = ImageTk.PhotoImage(self.searchbuttonimg.resize(
            (math.ceil(80 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.searcheventbutton = Button(self.searcheventsframe, image=self.searchbutton1, width=1, height=1, command=lambda:self.searchevents_function(eventsearchentry.get())) 
        self.searcheventbutton.grid(row=1, column=8, rowspan=2, columnspan=2, sticky=NSEW)
        self.searcheventbutton.grid_propagate(False)
        eventsearchentry =  Entry(self.searcheventsframe, width=1, font=("Avenir Next", 12), fg=BLACK, bg=WHITE)
        eventsearchentry.grid(row=2, column=1, rowspan=1, columnspan=6, sticky=NSEW)
    def searchevents_function(self, eventname): #name is eventsearchentry.get()
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        if eventname == "":
            self.c.execute("""SELECT DISTINCT event_name, eventkey_number FROM eventcreation""")
        else:
            self.c.execute("""SELECT DISTINCT event_name, eventkey_number FROM eventcreation WHERE event_name LIKE ?  """, ("%"+eventname+"%",))
        self.eresults = self.c.fetchall()
        self.ecount = len(self.eresults)
        #in case somebody clicks an event while looking at edit page
        # later
        self.searcheventsresultsframe = Frame(self.searcheventsframe, height=1, width=1, bg=PINK)
        self.searcheventsresultsframe.grid(row=6, column=1, rowspan=11, columnspan=9, sticky=NSEW)
        for x in range(9):
            self.searcheventsresultsframe.columnconfigure(x, weight=1, uniform="x")
            Label(self.searcheventsresultsframe, width=1, bg=PINK).grid(row=0, column=x, sticky=NSEW)
        for y in range(11):
            self.searcheventsresultsframe.rowconfigure(y, weight=1, uniform="x")
            Label(self.searcheventsresultsframe, width=1, bg=PINK).grid(row=y, column=0, sticky=NSEW)
        self.searcheventsresultsframe.grid_propagate(False)
        self.eventprofileimg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\eventprofile360x80.png")
        self.eventprofile = ImageTk.PhotoImage(self.eventprofileimg.resize(
            (math.ceil(360 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.studentsregisteredforframe = Frame(self.searchbyeventsframe, height=1, width=1, bg=PINK)
        self.studentsregisteredforframe.grid(row=4, column=22, rowspan=11, columnspan=15, sticky=NSEW)
        for x in range(15):
            self.studentsregisteredforframe.columnconfigure(x, weight=1)
            Label(self.studentsregisteredforframe, width=1, bg=PINK).grid(row=0, column=x, sticky=NSEW)
        for y in range(11):
            self.studentsregisteredforframe.rowconfigure(y, weight=1)
            Label(self.studentsregisteredforframe, width=1, bg=PINK).grid(row=y, column=0, sticky=NSEW)
        self.studentsregisteredforframe.grid_propagate(False)
        for indexofeventdetails in range(self.ecount):
            self.eresults[indexofeventdetails]
            nameofevent = self.eresults[indexofeventdetails][0]
            eventkey = self.eresults[indexofeventdetails][1]
            Button(self.searcheventsresultsframe, image=self.eventprofile, width=1, height=1, 
            text= f"Event name\n= {nameofevent}\n Event key = {eventkey}", compound=CENTER, font=("Avenir Next", 12),
            fg=BLACK, bg=WHITE,
            command=lambda x=(nameofevent, eventkey):self.generate_studentlist(x)).grid(row=indexofeventdetails*2, column=0, rowspan=2, columnspan=9, sticky=NSEW)
    def generate_studentlist(self, information:tuple):
        try:
            self.frametoshowdetailsevent.grid_remove()
        except:
            pass
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        #unpacking the tuple
        self.nameofevent = information[0]
        self.eventkey = information[1]
        self.c.execute("""SELECT COUNT(full_name) FROM eventregistration where eventkey_registered=?""", (self.eventkey,))
        self.countofstudentsregistered = self.c.fetchone()[0]
        self.c.execute("""SELECT full_name, icpass_number, phone_number FROM eventregistration where eventkey_registered=?""", (self.eventkey,))
        self.results = self.c.fetchall()
        print(f"This event with name {self.nameofevent} has the registrants of {self.results}")
        print(f"Total number of students registered for this event is {self.countofstudentsregistered}")
        #deleting the previous widgets in the studentsregisteredframe
        self.readstudentimg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\readstudentdetails.png")
        self.readstudent_ = ImageTk.PhotoImage(self.readstudentimg.resize(
            (math.ceil(80 * dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        self.deletestudentimg = Image.open(r"Assets\managementsuite\viewparticipantswidgets\deletestudent80x80.png")
        self.deletestudent_ = ImageTk.PhotoImage(self.deletestudentimg.resize(
            (math.ceil(80* dpi / 96), math.ceil(80 * dpi / 96)), Image.Resampling.LANCZOS))
        for widget in self.studentsregisteredforframe.winfo_children():
            if widget.winfo_class() == "Button":
                widget.destroy()
        for indexofstudentdetails in range(self.countofstudentsregistered):
            self.results[indexofstudentdetails]
            nameofstudent = self.results[indexofstudentdetails][0]
            icpass = self.results[indexofstudentdetails][1]
            phonenumber = self.results[indexofstudentdetails][2]
            testbtnevnt = Button(self.studentsregisteredforframe, state=DISABLED, width=1,height=1,text= f"Name = {nameofstudent}\nIC/Passport = {icpass}\nPhone number = {phonenumber}", font=("Avenir Next", 14), fg=BLACK, bg=PINK)
            testbtnevnt.grid(row=indexofstudentdetails*2, column=0, rowspan=2, columnspan=11, sticky=NSEW)
            testbtnevnt.grid_propagate(False)
            editbutton = Button(self.studentsregisteredforframe, image=self.readstudent_, width=1, height=1,
            text="EDIT", compound=CENTER, font=("Avenir Next Medium", 12), fg=WHITE,bg=WHITE,
            command=lambda x = self.nameofevent, y=nameofstudent: self.read_student_dtlsevnt(x, y))
            editbutton.grid(row=indexofstudentdetails*2, column=11, rowspan=2, columnspan=2, sticky=NSEW)
            editbutton.grid_propagate(False)
            deletebutton = Button(self.studentsregisteredforframe, image=self.deletestudent_, width=1, height=1,
            text="DELETE", compound=CENTER, font=("Avenir Next Medium", 12), fg=WHITE,bg=WHITE,
            command=lambda x = self.nameofevent, y=nameofstudent: self.delete_studentevent(x, y))
            deletebutton.grid(row=indexofstudentdetails*2, column=13, rowspan=2, columnspan=2, sticky=NSEW)
            deletebutton.grid_propagate(False)
        self.frametoshowdetailsevent = Frame(self.studentsregisteredforframe, height=1, width=1, bg=PINK)
        self.frametoshowdetailsevent.grid(row=0,column=0,rowspan=11,columnspan=15,sticky=NSEW)
        self.frametoshowdetailsevent.grid_propagate(False)
        for x in range(15):
            self.frametoshowdetailsevent.columnconfigure(x, weight=1)
            Label(self.frametoshowdetailsevent, width=1, bg=PINK).grid(row=0, column=x, sticky=NSEW)
        for y in range(11):
            self.frametoshowdetailsevent.rowconfigure(y, weight=1)
            Label(self.frametoshowdetailsevent, width=1, bg=PINK).grid(row=y, column=0, sticky=NSEW)
        self.frametoshowdetailsevent.grid_propagate(False)
        self.frametoshowdetailsevent.grid_remove()
    def read_student_dtlsevnt(self, nameofevent, nameofstudent):
        print(f"Name of event is {nameofevent} and name of student is {nameofstudent}")
        self.frametoshowdetailsevent.grid()
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        self.c.execute("""SELECT * FROM eventregistration where full_name=? AND event_registered =? """, (nameofstudent, nameofevent))
        self.results = self.c.fetchall()
        removeeventframe = Button(self.frametoshowdetailsevent, width=1, height=1, text="X", font=("Avenir Next Bold", 16),
        fg=BLACK, bg=PINK, command=lambda:self.frametoshowdetailsevent.grid_remove())
        removeeventframe.grid(row=0, column=14, sticky=NSEW)
        self.fullname = self.results[0][0]
        self.icpassnumber = self.results[0][1]
        self.phonenumber = self.results[0][2]
        self.email = self.results[0][3]
        self.address = self.results[0][4]
        self.eventfullnameentry = Entry(self.frametoshowdetailsevent, width=1, font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, justify=CENTER)
        self.eventfullnameentry.grid(row=7, column=2, rowspan=2, columnspan=11, sticky=NSEW)
        self.eventicpassnoentry = Entry(self.frametoshowdetailsevent, width=1, font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, justify=CENTER)
        self.eventicpassnoentry.grid(row=7, column=2, rowspan=2, columnspan=11, sticky=NSEW)
        self.eventphonenumberentry = Entry(self.frametoshowdetailsevent, width=1, font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, justify=CENTER)
        self.eventphonenumberentry.grid(row=7, column=2, rowspan=2, columnspan=11, sticky=NSEW)
        self.eventemailentry = Entry(self.frametoshowdetailsevent, width=1, font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, justify=CENTER)
        self.eventemailentry.grid(row=7, column=2, rowspan=2, columnspan=11, sticky=NSEW)
        self.eventaddressentry = Entry(self.frametoshowdetailsevent, width=1, font=("Avenir Next Bold", 16), fg=BLACK, bg=WHITE, justify=CENTER)
        self.eventaddressentry.grid(row=7, column=2, rowspan=2, columnspan=11, sticky=NSEW)
        entrylist = [self.eventfullnameentry, self.eventicpassnoentry, self.eventphonenumberentry, self.eventemailentry, self.eventaddressentry]
        for entry in entrylist:
            entry.grid_remove()
        fullnamebutton = Button(self.frametoshowdetailsevent, text=f"Full name: {self.fullname}", font=("Avenir Next Bold", 16), fg=BLACK, bg=PINK, command=lambda:self.evententryinitializer(self.eventfullnameentry,self.fullname,fieldchanged="full_name", originaltext=self.fullname, eventregistered=nameofevent)).grid(row=1, column=1, columnspan=13, sticky=NSEW)
        icpassnobutton = Button(self.frametoshowdetailsevent, text=f"IC/Passport number: {self.icpassnumber}", font=("Avenir Next Bold", 16), fg=BLACK, bg=PINK, command=lambda:self.evententryinitializer(self.eventicpassnoentry,self.icpassnumber,fieldchanged="icpass_number", originaltext=self.icpassnumber,eventregistered=nameofevent)).grid(row=2, column=1, columnspan=13, sticky=NSEW)
        phonenumberbutton = Button(self.frametoshowdetailsevent, text=f"Phone number: {self.phonenumber}", font=("Avenir Next Bold", 16), fg=BLACK, bg=PINK, command=lambda:self.evententryinitializer(self.eventphonenumberentry,self.phonenumber,fieldchanged="phone_number", originaltext=self.phonenumber,eventregistered=nameofevent)).grid(row=3, column=1, columnspan=13, sticky=NSEW)
        emailbutton = Button(self.frametoshowdetailsevent, text=f"Email: {self.email}", font=("Avenir Next Bold", 16), fg=BLACK, bg=PINK, command=lambda:self.evententryinitializer(self.eventemailentry,self.email,fieldchanged="email", originaltext=self.email,eventregistered=nameofevent)).grid(row=4, column=1, columnspan=13, sticky=NSEW)
        addressbutton = Button(self.frametoshowdetailsevent, text=f"Address: {self.address}", font=("Avenir Next Bold", 16), fg=BLACK, bg=PINK, command=lambda:self.evententryinitializer(self.eventaddressentry,self.address,fieldchanged="address", originaltext=self.address,eventregistered=nameofevent)).grid(row=5, column=1, columnspan=13, sticky=NSEW)
    def evententryinitializer(self, entrywanted, texttochange, **kwargs):
        fieldchanged = kwargs.get("fieldchanged")
        originaltext = kwargs.get("originaltext")
        eventregistered = kwargs.get("eventregistered")
        entrylist = [self.eventfullnameentry, self.eventicpassnoentry, self.eventphonenumberentry, self.eventemailentry, self.eventaddressentry]
        for entry in entrylist:
            if entry != entrywanted:
                entry.grid_remove()
        entrywanted.grid()
        entrywanted.delete(0, END)
        entrywanted.insert(0, texttochange)
        entrywanted.focus_set()
        confirmbuttonevent = Button(self.frametoshowdetailsevent, text="Confirm Edit", font=("Avenir Next Bold", 16), fg=BLACK, bg=PINK, command=lambda:self.eventconfirmchanges(entrywanted, texttochange, fieldchanged, originaltext, eventregistered)).grid(row=9, column=2, columnspan=11, sticky=NSEW)
    def eventconfirmchanges(self, eventtogetinfo, texttochange, fieldchanged, originaltext, event_registered):
        textfromentry = eventtogetinfo.get()
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        with self.conn:
            try:
                self.c.execute(f"""UPDATE eventregistratioon SET {fieldchanged} = ? WHERE {fieldchanged} = ? AND event_registered = ?""", (textfromentry, originaltext, event_registered))
                messagebox.showinfo("Success", f"Changes have been made where {fieldchanged} = {originaltext}  has been changed to {textfromentry} under event {event_registered}")
            except Exception as e:
                messagebox.showerror("Error", f"An error has occured: {e}")

    def delete_studentevent(self, eventname, studentname):
        print(f"Delete {studentname}'s details from {eventname}")
        self.frametodeletestudentsevent = Frame(self.studentsregisteredforframe, height=1, width=1, bg=WHITE,relief=SOLID)
        self.frametodeletestudentsevent.grid(row=0, column=0,rowspan=11,columnspan=15, sticky=NSEW)
        self.frametodeletestudentsevent.grid_propagate(False)
        for x in range(15):
            self.frametodeletestudentsevent.columnconfigure(x, weight=1)
            Label(self.frametodeletestudentsevent, width=1, bg=WHITE).grid(row=0, column=x, sticky=NSEW)
        for y in range(11):
            self.frametodeletestudentsevent.rowconfigure(y, weight=1)
            Label(self.frametodeletestudentsevent, height=1, bg=WHITE).grid(row=y, column=0, sticky=NSEW)
        Label(self.frametodeletestudentsevent, text=f"Are you sure you\nwant to delete {studentname}'s details\n from {eventname}?", font=("Avenir Next", 14), fg=BLACK, bg=WHITE).grid(row=1, column=1, columnspan=13, sticky=NSEW)
        Label(self.frametodeletestudentsevent, text="This action cannot be undone", font=("Avenir Next", 14), fg=BLACK, bg=WHITE).grid(row=2, column=1, columnspan=13, sticky=NSEW)
        Label(self.frametodeletestudentsevent, text="Please type the word DELETE to confirm", font=("Avenir Next", 14), fg=BLACK, bg=WHITE).grid(row=3, column=1, columnspan=13, sticky=NSEW)
        self.deleteentryevent = Entry(self.frametodeletestudentsevent, font=("Avenir Next", 14), fg=BLACK, bg=WHITE)
        self.deleteentryevent.grid(row=4, column=1, columnspan=13, sticky=NSEW)
        self.deleteentryevent.focus_set()
        confirmdeleteevent = Button(self.frametodeletestudentsevent, text="Confirm Delete", font=("Avenir Next", 14), fg=BLACK, bg=PINK, command=lambda:self.delete_studenteventconfirm(eventname, studentname)).grid(row=5, column=1, columnspan=13, sticky=NSEW)
        cancelbuttonevent = Button(self.frametodeletestudentsevent, text="Cancel", font=("Avenir Next", 14), fg=BLACK, bg=PINK, command=lambda:self.frametodeletestudentsevent.grid_remove()).grid(row=6, column=1, columnspan=13, sticky=NSEW)
    def delete_studenteventconfirm(self, eventname, studentname):
        if self.deleteentryevent.get() == "DELETE":
            self.conn = sqlite3.connect("interactivesystem.db")
            self.c = self.conn.cursor()
            with self.conn:
                try:
                    self.c.execute("""DELETE FROM eventregistratioon WHERE event_registered = ? AND name = ?""", (eventname, studentname))
                    messagebox.showinfo("Success", f"{studentname}'s details have been deleted from {eventname}")
                    self.frametodeletestudentsevent.grid_remove()
                    self.frametoshowdetailsevent.grid_remove()
                    self.show_studentsevent(eventname)
                except Exception as e:
                    messagebox.showerror("Error", f"An error has occured: {e}")
        else:
            messagebox.showerror("Error", "The word DELETE was not entered correctly")



    
    def viewregistrant(self, name):
        #searches for the registrant in the eventregistration table using the name parameter
        #returns a tuple containing the registrant's name, email, and event name
        self.conn = sqlite3.connect("interactivesystem.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT eventkey_registered FROM eventregistration WHERE full_name=?", (name,))
        self.registrant = self.c.fetchall()
        print(self.registrant)
        self.conn.commit()
        self.conn.close()
        


            





        
        


class FeedbackForm(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=PINK)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=1, bg=PINK, relief="flat").grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=1, bg=PINK, relief="flat").grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)

        # Widgets
        label = Label(self, text="This is a feedback form to help us improve our app.\nPlease answer the questions below to the best of your ability.\nThank you for your time!", font=(
            'Segoe Ui Semibold', 14), width=1, height=1, fg='#000000', bg='#FFF5E4')
        label.grid(row=1, column=10, columnspan=22,
                   rowspan=2, sticky=NSEW)
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
                               columnspan=2, sticky=NSEW)
            self.firstrow.grid_propagate(False)
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
                                rowspan=1, columnspan=2, sticky=NSEW)
            self.secondrow.grid_propagate(False)
            count2 += 4

        # Creating Likelihood Scale
        for text, rating in scaleoflikelihood:
            self.thirdrow = Radiobutton(self, text=text, variable=question3answer, value=rating, bg=ORANGE, font=("Helvetica", 18),
                                        justify=CENTER, width=1, height=1)
            self.thirdrow.grid(row=9, column=count3, rowspan=1,
                               columnspan=2, sticky=NSEW)
            self.thirdrow.grid_propagate(False)
            count3 += 4  # have to set column=count2,because different type of answers
            # in options means different count needs to be used, basically, count is for satisfaction questions,
            # count2 is for likelihood questions, count3 for yes no questions
            # notice gap value is still 4

        # Creating Easiness Scale(because using easiness question)
        for text, rating in scaleofeasiness:
            self.fourthrow = Radiobutton(self, text=text, variable=question4answer, value=rating, bg=ORANGE, font=("Helvetica", 18),
                                         justify=CENTER, width=1, height=1)
            self.fourthrow.grid(row=11, column=count4,
                                rowspan=1, columnspan=2, sticky=NSEW)
            self.fourthrow.grid_propagate(False)
            count4 += 4

        # Creating Yes No
        for text in yesnooptions:
            self.fifthrow = Radiobutton(self, text=text, variable=yesnoquestionanswer, value=text, bg=ORANGE, font=("Helvetica", 18),
                                        justify=CENTER, width=1, height=1)
            self.fifthrow.grid(row=13, column=count5,
                               rowspan=2, columnspan=3, sticky=NSEW)
            self.fifthrow.grid_propagate(False)
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
                             columnspan=6, sticky=NSEW)
        self.getanswers.grid_propagate(False)

        self.getanswers = Button(self, text="Confirm", command=lambda: [
                                 ShowChoice(), dosomedatabasemagic()], bg=ORANGE, font=("Helvetica", 18), width=1, height=1)
        self.getanswers.grid(row=18, column=26, rowspan=2,
                             columnspan=6, sticky=NSEW)
        self.getanswers.grid_propagate(False)

        # Picture
        self.decorateimage = Image.open(r"assets\decoration.jpg")
        self.decoratingimage = ImageTk.PhotoImage(self.decorateimage.resize(
            (math.ceil(200 * dpi / 96), math.ceil(800 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.decoratingimage,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=1, column=3, columnspan=5,
                        rowspan=18, sticky=NSEW)

        self.decorate2image = Image.open(r"assets\decoration.jpg")
        self.decorating2image = ImageTk.PhotoImage(self.decorate2image.resize(
            (math.ceil(200 * dpi / 96), math.ceil(800 * dpi / 96)), Image.Resampling.LANCZOS))
        imagelabel = Label(self, image=self.decorating2image,
                           anchor=CENTER, width=1, height=1)
        imagelabel.grid(row=1, column=34, columnspan=5,
                        rowspan=18, sticky=NSEW)


class CalendarPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=PINK)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        for x in range(42):
            self.columnconfigure(x, weight=1, uniform='x')
            Label(self, width=1, bg=NICEPURPLE).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(21):
            self.rowconfigure(y, weight=1, uniform='x')
            Label(self, width=1, bg=NICEPURPLE).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)
        def hidetheentireframe():
            self.grid_remove()
        xbuttonlabel = Button(self, text="X", font=("Avenir Next Medium", 18), height=1,width=1,
        bg=DARKBLUE, fg="white",
        command= lambda:hidetheentireframe())
        xbuttonlabel.grid(row=0, column=40, rowspan=2, columnspan=2, sticky=NSEW)
        # Widgets
        label = Label(self, text="This is the Calendar", font=(
            'Segoe Ui Semibold', 14), width=1, height=1, fg='#000000', bg='#FFF5E4', justify="left")
        label.grid(row=0, column=2, columnspan=6,
                   rowspan=2, sticky=NSEW)
        self.cal = tkCalendar(self, width=1, height=1,
            background = DARKBLUE, foreground = 'white', 
            bordercolor = ORANGE, 
            headersbackground = NAVYBLUE, headersforeground = 'white', 
            selectbackground = NICEBLUE, selectforeground = 'black',
            showothermonthdays = False,
            selectmode="day",
            font=("Avenir Next Medium", 18),
            date_pattern="dd-mm-yyyy")
        self.cal.grid(row=2, column=2, columnspan=21, rowspan=17, sticky=NSEW)
        self.cal.bind("<<CalendarSelected>>", self.generate_buttons)

        #Go back to current date button
        self.gobackbutton = Button(self, text="Change view to current date", width=1, height=1,
        bg=ORANGE, font=("Atkinson Hyperlegible", 18), command=lambda: [self.go_to_today()])
        self.gobackbutton.grid(row=19, column=3, rowspan=2,
                             columnspan=8, sticky=NSEW)
        self.gobackbutton.grid_propagate(False)
        self.refreshbutton = Button(self, text="Refresh",
        bg=ORANGE, font=("Atkinson Hyperlegible", 18), width=1, height=1,
        command=lambda: [self.add_events()])
        self.refreshbutton.grid(row=19, column=14, rowspan=2,
                                columnspan=6, sticky=NSEW)
        self.refreshbutton.grid_propagate(False)
        self.buttonframe=Frame(self, bg = ORANGE, relief=RAISED, width=1, height=1,)
        self.buttonframe.grid(row=4, column=24, rowspan=15, columnspan=17, sticky=NSEW)
        self.buttonframe.grid_propagate(False)
        self.detailslabel = Label(self, text="Click on an event to view the details.", width=1, height=1,
        font = ("Avenir Next Medium", 18), background=LIGHTYELLOW)
        self.detailslabel.grid(row=2, column=24, rowspan=2, columnspan=17, sticky=NSEW)
        self.add_events()
    def generate_buttons(self, event):
        detailslabel = self.detailslabel 
        for widgets in self.buttonframe.winfo_children():
            widgets.destroy()
        for x in range(15):
            self.buttonframe.columnconfigure(x, weight=1, uniform='x')
            Label(self.buttonframe, width=1, bg=ORANGE).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(15):
            self.buttonframe.rowconfigure(y, weight=1, uniform='x')
            Label(self.buttonframe, width=1, bg=ORANGE).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)
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
            font = ("Avenir Next Medium", 18)).grid(row=0+startingrowno, column=0, rowspan=2, columnspan=11, sticky=NSEW)
            Button(self.buttonframe, text="View details", width=1, height=1,
            bg = PINK, fg = "black", relief="groove",
            font = ("Avenir Next Medium", 18),
            # lambda command fix thanks to https://stackoverflow.com/questions/17677649/tkinter-assign-button-command-in-a-for-loop-with-lambda
            command=lambda name=name:self.createdetails(name)).grid(row=0+startingrowno, column=11, rowspan=2, columnspan=4, sticky=NSEW)
            startingrowno += 2

    def createdetails(self, name):
        #A frame to display the details of the event
        self.subframe = Frame(self.buttonframe, bg = NICEBLUE, relief=RAISED, height=1, width=1)
        self.subframe.grid(row=0, column=0, rowspan=15, columnspan=15, sticky=NSEW)
        for x in range(15):
            self.subframe.columnconfigure(x, weight=1, uniform='x')
            Label(self.subframe, width=1, bg=LIGHTYELLOW).grid(
                row=0, column=x, rowspan=1, columnspan=1, sticky=NSEW)
        for y in range(15):
            self.subframe.rowconfigure(y, weight=1, uniform='x')
            Label(self.subframe, width=1, bg=LIGHTYELLOW).grid(
                row=y, column=0, rowspan=1, columnspan=1, sticky=NSEW)
        self.subframe.grid_propagate(False)
        self.conn = sqlite3.connect('interactivesystem.db')
        self.c = self.conn.cursor()
        self.c.execute("""SELECT 
        event_name, event_startdate, event_enddate, event_starttime, event_endtime, event_organizer, venue_name, host_name FROM eventcreation WHERE event_name = ?""", (name,))
        self.eventdetails = self.c.fetchall()
        for row in self.eventdetails:
            Label(self.subframe, text="Event details", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=0, column=0, rowspan=2, columnspan=15, sticky=NSEW)
            Label(self.subframe, text=f"Event name: {row[0]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=2, column=0, rowspan=2, columnspan=15, sticky=NSEW)
            Label(self.subframe, text=f"Event Date: From {row[1]} to {row[2]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=4, column=0, rowspan=2, columnspan=15, sticky=NSEW)
            Label(self.subframe, text=f"Event time: {row[3]} - {row[4]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=6, column=0, rowspan=2, columnspan=15, sticky=NSEW)
            Label(self.subframe, text=f"Event organizer: {row[5]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=8, column=0, rowspan=2, columnspan=15, sticky=NSEW)
            Label(self.subframe, text=f"Host name: {row[7]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=10, column=0, rowspan=2, columnspan=15, sticky=NSEW)
            Label(self.subframe, text=f"Venue: {row[6]}", width=1,height=1,
            bg = LAVENDER, fg = "black", font = ("Avenir Next Medium", 18)).grid(
                row=12, column=0, rowspan=2, columnspan=15, sticky=NSEW)
            Button(self.subframe, text="Back", width=1, height=1,
            bg = PINK, fg = "black", relief="groove",
            font = ("Avenir Next Medium", 18),
            command=lambda: self.subframe.grid_remove()).grid(row=14, column=0, rowspan=2, columnspan=15, sticky=NSEW)

    
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