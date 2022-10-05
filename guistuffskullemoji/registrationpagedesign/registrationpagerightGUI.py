#GUI file generated by GUI Pie, developed by Jabberwock
#https://apps.microsoft.com/store/detail/gui-pie/9P5TH15LZSL7


import os
import sys
import subprocess
import math
from tkinter import *
from tkinter import ttk
import tkinter.font

dpiError = False
try:
  from ctypes import windll
  windll.shcore.SetProcessDpiAwareness(1)
except:
  print('ERROR. Could not set DPI awareness.')
  dpiError = True
if __name__ == "__main__":
  registrationpagerightGUI = Tk()
else:
  registrationpagerightGUI = Tk()
registrationpagerightGUI.title('registrationpagerightGUI')
if dpiError:
  dpi = 96
else:
  dpi = registrationpagerightGUI.winfo_fpixels('1i')
registrationpagerightGUI.geometry(f'{math.ceil(780 * dpi / 96)}x{math.ceil(897 * dpi / 96)}')
registrationpagerightGUI.grid_propagate(False)
for x in range(20):
  Grid.columnconfigure(registrationpagerightGUI, x, weight=1, uniform='row')
  Label(registrationpagerightGUI, width = 1, bg = '#00FFFF').grid(row = 0, column = x, sticky = N+S+E+W)
for y in range(23):
  Grid.rowconfigure(registrationpagerightGUI, y, weight=1, uniform='row')
  Label(registrationpagerightGUI, width = 1, bg = '#00FFFF').grid(row = y, column = 0, sticky = N+S+E+W)
registrationpagerightGUI.configure(background='#00FFFF')
registrationpagerightGUI.resizable(False, False)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WIDGETS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

registrationpagerightGUI.enterdetailslabel = Label(registrationpagerightGUI, text = "Welcome to the login page of\nINTI Interactive System!", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#FFF5E4')
registrationpagerightGUI.enterdetailslabel.grid(row = 1, column = 2, columnspan = 16, rowspan = 2, sticky = N+S+E+W)
registrationpagerightGUI.Label1 = Label(registrationpagerightGUI, text = "Label1", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#FF0000')
registrationpagerightGUI.Label1.grid(row = 15, column = 9, columnspan = 2, rowspan = 1, sticky = N+S+E+W)
registrationpagerightGUI.emailfield = Entry(registrationpagerightGUI, width = 1, bg = '#FFFFFF', font = ('Arial', 18), justify = 'center')
registrationpagerightGUI.emailfield.grid(row = 5, column = 2, columnspan = 16, rowspan = 2, sticky = N+S+E+W)
registrationpagerightGUI.emailfield.insert(0, "Please enter your student email.")
registrationpagerightGUI.passwordfield = Entry(registrationpagerightGUI, width = 1, bg = '#FFFFFF', font = ('Arial', 18), justify = 'center')
registrationpagerightGUI.passwordfield.grid(row = 8, column = 2, columnspan = 16, rowspan = 2, sticky = N+S+E+W)
registrationpagerightGUI.passwordfield.insert(0, "Please enter your password.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def rungotosignin(argument):
  if not(__name__ == '__main__'):
    from main import gotosignin
    try:
      gotosignin(argument)
    except TypeError:
      gotosignin()
def runsignupbuttonclicked(argument):
  if not(__name__ == '__main__'):
    from main import signupbuttonclicked
    try:
      signupbuttonclicked(argument)
    except TypeError:
      signupbuttonclicked()
registrationpagerightGUI.havepassword = Button(registrationpagerightGUI, text = "Don't have an account? Click here to sign up.", font = ('Arial', 12), width = 1, height = 1, fg = '#000000', command = lambda: rungotosignin("havepassword"), bg = '#FF0000')
registrationpagerightGUI.havepassword.grid(row = 21, column = 4, columnspan = 11, rowspan = 1, sticky = N+S+E+W)
registrationpagerightGUI.signupbutton = Button(registrationpagerightGUI, text = "SIGN IN", font = ('Arial', 18), width = 1, height = 1, fg = '#000000', command = lambda: runsignupbuttonclicked("signupbutton"), bg = '#FF0000')
registrationpagerightGUI.signupbutton.grid(row = 12, column = 6, columnspan = 8, rowspan = 2, sticky = N+S+E+W)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~HELPER FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def initModules():
  raise Exception('This main file is outdated. Script main.py must be updated to reflect the changes in GUI Pie v3.')
def init():
  from main import gotosignin
  from main import signupbuttonclicked
registrationpagerightGUI.initModules = initModules
def hide():
  registrationpagerightGUI.withdraw()
def show():
  registrationpagerightGUI.deiconify()
def hideAllWidgets():
    registrationpagerightGUI.enterdetailslabel.grid_remove()
    registrationpagerightGUI.Label1.grid_remove()
    registrationpagerightGUI.emailfield.grid_remove()
    registrationpagerightGUI.passwordfield.grid_remove()
    registrationpagerightGUI.havepassword.grid_remove()
    registrationpagerightGUI.signupbutton.grid_remove()
registrationpagerightGUI.hideAllWidgets = hideAllWidgets
def showAllWidgets():
    registrationpagerightGUI.enterdetailslabel.grid()
    registrationpagerightGUI.Label1.grid()
    registrationpagerightGUI.emailfield.grid()
    registrationpagerightGUI.passwordfield.grid()
    registrationpagerightGUI.havepassword.grid()
    registrationpagerightGUI.signupbutton.grid()
registrationpagerightGUI.showAllWidgets = showAllWidgets
def run():
  global dimensions
  dimensions = [0,0]
  if __name__ != "__main__":
    init()
  resizeEvent(None)
  registrationpagerightGUI.mainloop()
registrationpagerightGUI.run = run
registrationpagerightGUI.hide = hide
registrationpagerightGUI.show = show

dimensions = [registrationpagerightGUI.winfo_width(), registrationpagerightGUI.winfo_height()]
def resize():
  global registrationpagerightGUI, dimensions
  if registrationpagerightGUI.winfo_width() != dimensions[0] or registrationpagerightGUI.winfo_height() != dimensions[1]:
    registrationpagerightGUI.enterdetailslabel.config(wraplength = math.ceil(registrationpagerightGUI.winfo_width() * 16 / 20) + 2)
    registrationpagerightGUI.Label1.config(wraplength = math.ceil(registrationpagerightGUI.winfo_width() * 2 / 20) + 2)
    registrationpagerightGUI.havepassword.config(wraplength = math.ceil(registrationpagerightGUI.winfo_width() * 11 / 20) + 2)
    registrationpagerightGUI.signupbutton.config(wraplength = math.ceil(registrationpagerightGUI.winfo_width() * 8 / 20) + 2)
    dimensions = [registrationpagerightGUI.winfo_width(), registrationpagerightGUI.winfo_height()]

eventID = None
registrationpagerightGUI.resizeDelay = 100
def resizeEvent(event):
  global eventID
  if eventID:
    registrationpagerightGUI.after_cancel(eventID)
  eventID = registrationpagerightGUI.after(registrationpagerightGUI.resizeDelay, resize)
registrationpagerightGUI.bind('<Configure>', resizeEvent)
if __name__ == "__main__":
  registrationpagerightGUI.run()
