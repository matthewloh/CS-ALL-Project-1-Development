
import os
import sys
import subprocess
import math
from tkinter import *
from tkinter import ttk
import tkinter.font
try:
  from PIL import ImageTk, Image, ImageOps
except:
  print('Installing PIL.')
  subprocess.check_call(['pip', 'install', 'pillow'])
  print('Done.')
  from PIL import ImageTk, Image, ImageOps
dpiError = False
try:
  from ctypes import windll
  windll.shcore.SetProcessDpiAwareness(1)
except:
  print('ERROR. Could not set DPI awareness.')
  dpiError = True
if __name__ == "__main__":
  landingpageGUI = Tk()
else:
  landingpageGUI = Tk()
landingpageGUI.title('landingpageGUI')
if dpiError:
  dpi = 96
else:
  dpi = landingpageGUI.winfo_fpixels('1i')
landingpageGUI.geometry(f'{math.ceil(1920 * dpi / 96)}x{math.ceil(1080 * dpi / 96)}')
landingpageGUI.grid_propagate(False)
for x in range(32):
  Grid.columnconfigure(landingpageGUI, x, weight=1, uniform='row')
  Label(landingpageGUI, width = 1, bg = '#FFE3E1').grid(row = 0, column = x, sticky = N+S+E+W)
for y in range(18):
  Grid.rowconfigure(landingpageGUI, y, weight=1, uniform='row')
  Label(landingpageGUI, width = 1, bg = '#FFE3E1').grid(row = y, column = 0, sticky = N+S+E+W)
landingpageGUI.configure(background='#FFE3E1')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WIDGETS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

landingpageGUI.Image1Original = Image.open(r'C:/Users/matth/Desktop/yeah/Home-Banner-INTI.png')
landingpageGUI.Image1Image = ImageOps.exif_transpose(landingpageGUI.Image1Original)
landingpageGUI.Image1Image = ImageTk.PhotoImage(landingpageGUI.Image1Image.resize((math.ceil(480 * dpi / 96), math.ceil(180 * dpi / 96)), Image.Resampling.LANCZOS))
landingpageGUI.Image1 = Label(landingpageGUI, image = landingpageGUI.Image1Image, width = 1, height = 1, bg = '#FFE3E1')
landingpageGUI.Image1.grid(row = 2, column = 20, columnspan = 8, rowspan = 3, sticky = N+S+E+W)
landingpageGUI.Image2Original = Image.open(r'D:/Syncthingstuff/Abstruct/Colored ocean in another world.jpg')
landingpageGUI.Image2Image = ImageOps.exif_transpose(landingpageGUI.Image2Original)
landingpageGUI.Image2Image = ImageTk.PhotoImage(landingpageGUI.Image2Image.resize((math.ceil(840 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
landingpageGUI.Image2 = Label(landingpageGUI, image = landingpageGUI.Image2Image, width = 1, height = 1, bg = '#FFE3E1')
landingpageGUI.Image2.grid(row = 2, column = 2, columnspan = 14, rowspan = 14, sticky = N+S+E+W)
landingpageGUI.LoginLabel = Label(landingpageGUI, text = "Sign in to your account", font = ('Arial', 18), width = 1, height = 1, fg = '#000000', bg = '#FFF5E4')
landingpageGUI.LoginLabel.grid(row = 6, column = 21, columnspan = 6, rowspan = 1, sticky = N+S+E+W)
landingpageGUI.NewIntiLabel = Label(landingpageGUI, text = "New to INTI Interactive System?", font = ('Arial', 14), width = 1, height = 1, fg = '#000000', bg = '#00FFFF')
landingpageGUI.NewIntiLabel.grid(row = 14, column = 21, columnspan = 4, rowspan = 1, sticky = N+S+E+W)
landingpageGUI.PlaceholderRadioButton = Label(landingpageGUI, text = "Placeholder | Remember me.?", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#00FFFF')
landingpageGUI.PlaceholderRadioButton.grid(row = 12, column = 22, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
landingpageGUI.EmailEntry = Entry(landingpageGUI, width = 1, bg = '#FFFFFF', font = ('Arial', 14), justify = 'center', highlightthickness = 0, bd=0)
landingpageGUI.EmailEntry.grid(row = 8, column = 21, columnspan = 6, rowspan = 1, sticky = N+S+E+W)
landingpageGUI.EmailEntry.insert(0, "Please insert your student email.")
landingpageGUI.PasswordEntry = Entry(landingpageGUI, width = 1, bg = '#FFFFFF', font = ('Arial', 14), justify = 'center', highlightthickness = 0, bd=0)
landingpageGUI.PasswordEntry.grid(row = 10, column = 21, columnspan = 6, rowspan = 1, sticky = N+S+E+W)
landingpageGUI.PasswordEntry.insert(0, "Please insert your password.")


dimensions = [landingpageGUI.winfo_width(), landingpageGUI.winfo_height()]
def resize():
  global landingpageGUI, dimensions
  if landingpageGUI.winfo_width() != dimensions[0] or landingpageGUI.winfo_height() != dimensions[1]:
    landingpageGUI.LoginLabel.config(wraplength = math.ceil(landingpageGUI.winfo_width() * 6 / 32) + 2)
    landingpageGUI.NewIntiLabel.config(wraplength = math.ceil(landingpageGUI.winfo_width() * 4 / 32) + 2)
    landingpageGUI.PlaceholderRadioButton.config(wraplength = math.ceil(landingpageGUI.winfo_width() * 3 / 32) + 2)
    landingpageGUI.Image1Original = Image.open(r'C:/Users/matth/Desktop/yeah/Home-Banner-INTI.png')
    landingpageGUI.Image1Image = ImageOps.exif_transpose(landingpageGUI.Image1Original)
    landingpageGUI.Image1Image = ImageTk.PhotoImage(landingpageGUI.Image1Image.resize((math.ceil(landingpageGUI.winfo_width() * 8 / 32), math.ceil(landingpageGUI.winfo_height() * 3 / 18)), Image.Resampling.LANCZOS))
    landingpageGUI.Image1.config(image = landingpageGUI.Image1Image)
    landingpageGUI.Image2Original = Image.open(r'D:/Syncthingstuff/Abstruct/Colored ocean in another world.jpg')
    landingpageGUI.Image2Image = ImageOps.exif_transpose(landingpageGUI.Image2Original)
    if (landingpageGUI.winfo_height() / 18 * 14) * 2340 / 2340 < landingpageGUI.winfo_width() * 14 / 32:
      landingpageGUI.Image2Image = ImageTk.PhotoImage(landingpageGUI.Image2Image.resize((math.ceil(landingpageGUI.winfo_height() * 14 / 18 * 2340 / 2340), math.ceil(landingpageGUI.winfo_height() * 14 / 18)), Image.Resampling.LANCZOS))
    else:
      landingpageGUI.Image2Image = ImageTk.PhotoImage(landingpageGUI.Image2Image.resize((math.ceil(landingpageGUI.winfo_width() * 14 / 32), math.ceil(landingpageGUI.winfo_width() * 14 / 32 * 2340 / 2340)), Image.Resampling.LANCZOS))
    landingpageGUI.Image2.config(image = landingpageGUI.Image2Image)
    dimensions = [landingpageGUI.winfo_width(), landingpageGUI.winfo_height()]

eventID = None
landingpageGUI.resizeDelay = 100
def resizeEvent(event):
  global eventID
  if eventID:
    landingpageGUI.after_cancel(eventID)
  eventID = landingpageGUI.after(landingpageGUI.resizeDelay, resize)
landingpageGUI.bind('<Configure>', resizeEvent)

landingpageGUI.mainloop()

