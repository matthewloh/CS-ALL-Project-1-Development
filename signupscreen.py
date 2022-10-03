from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image, ImageOps
import math
import sqlite3

from mysqlx import IntegrityError

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
PINK = "#FFE3E1"
LIGHTYELLOW = "#FFF5E4"
ORANGE = "#FFAA22"
MAGENTA = "#FF00FF"
LIGHTGREEN = "#00FFC7"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Window Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
dpi = 96
window = Tk()

window.title('INTI Interactive System')
window.grid_propagate(False)
window.geometry('1920x1080')
for x in range(32):
    Grid.columnconfigure(window, x, weight=1, uniform='row')
    Label(width=1, bg='#FFE3E1').grid(row=0, column=x, sticky=N+S+E+W)
for y in range(18):
    Grid.rowconfigure(window, y, weight=1, uniform='row')
    Label(width=1, bg='#FFE3E1').grid(row=y, column=0, sticky=N+S+E+W)
window.configure(background='#FFE3E1')
window.resizable(True, True)
# signupframe = Frame(window, bg=LIGHTGREEN, bd=2, relief="groove")
# signupframe.grid(row=4, column=19, rowspan=12, columnspan=10, sticky=N+S+E+W)
# signupframe.grid_propagate(False)
# Grid.columnconfigure(signupframe, 0, weight=1, uniform='row')
# Grid.rowconfigure(signupframe, 0, weight=1, uniform='row')


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Database Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Database Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
conn = sqlite3.connect('registration.db')

c = conn.cursor()
#Creating a Table 
c.execute("""CREATE TABLE IF NOT EXISTS users(
            first_name text NOT NULL,
            last_name text NOT NULL,
            email text NOT NULL PRIMARY KEY,
            password text NOT NULL
            )""")
# c.execute("DROP TABLE users")

def signupbuttonpressed():
    emailtext = SignUpEmailEntry.get()
    passwordtext = passwordsignupentry.get()
    firstnametext = Entry1.get()
    lastnametext = Entry2.get()
    information = (firstnametext, lastnametext, emailtext, passwordtext)
    try:
        if emailtext == "Please enter your student email" or passwordtext == "Please enter your password" or firstnametext == "First Name" or lastnametext == "Last Name":
            messagebox.showerror(
                "Sign Up Failure", "You have not entered one or more of the fields correctly")
        else:
            with conn:
                c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", information)
                messagebox.showinfo("Sign Up Successful", "Welcome to the club!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Login Failed", "Email already exists")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Labels Specific for SignUp ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
haveanaccountlabel = Label(window, text="Already have an account?", font=(
    'Arial', 16), width=1, height=1, fg='#000000', bg='#00FFFF')
haveanaccountlabel.grid(row=15, column=20, columnspan=5,
                        rowspan=1, sticky=N+S+E+W)
SignUpLabel = Label(window, text="Please enter your details as shown.", font=(
    'Arial', 16), width=1, height=1, fg='#000000', bg='#FFF5E4')
SignUpLabel.grid(row=5, column=20, columnspan=8, rowspan=1, sticky=N+S+E+W)
SignUpEmailEntry = Entry(window, width=1, bg='#FFFFFF',
                         font=('Arial', 16), justify='center')
SignUpEmailEntry.insert(0, "Please enter your student email")
SignUpEmailEntry.grid(row=9, column=21, columnspan=6,
                      rowspan=1, sticky=N+S+E+W)
# SignUpEmailEntry.bind("<FocusIn>", lambda args: SignUpEmailEntry.delete('0', 'end'))
# SignUpEmailEntry.bind("<FocusOut>", lambda args: SignUpEmailEntry.insert(0, "Please enter your student email") if len(SignUpEmailEntry.get()) == 0 else None)
passwordsignupentry = Entry(
    window, width=1, bg='#FFFFFF', font=('Arial', 16), justify='center')
passwordsignupentry.grid(
    row=11, column=21, columnspan=6, rowspan=1, sticky=N+S+E+W)
passwordsignupentry.insert(0, "Please enter your password")
# passwordsignupentry.bind("<FocusIn>", lambda args: passwordsignupentry.delete('0', 'end'))
# passwordsignupentry.bind("<FocusOut>", lambda args: passwordsignupentry.insert(0, "Please enter your password") if len(passwordsignupentry.get()) == 0 else None)
Entry1 = Entry(window, width=1, bg='#FFFFFF',
               font=('Arial', 16), justify='center')
Entry1.grid(row=7, column=21, columnspan=2, rowspan=1, sticky=N+S+E+W)
Entry1.insert(0, "First Name")
# Entry1.bind("<FocusIn>", lambda args: Entry1.delete('0', 'end'))
# Entry1.bind("<FocusOut>", lambda args: Entry1.insert(0, "First Name"))
Entry2 = Entry(window, width=1, bg='#FFFFFF',
               font=('Arial', 16), justify='center')
# Entry2.bind("<FocusIn>", lambda args: Entry2.delete('0', 'end'))
# Entry2.bind("<FocusOut>", lambda args: Entry2.insert(0, "Last Name"))
Entry2.grid(row=7, column=25, columnspan=2, rowspan=1, sticky=N+S+E+W)
Entry2.insert(0, "Last Name")



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Buttons for Signup~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
signupregister = Button(window, text="SIGN UP", font=(
    'Arial', 16), width=1, height=1, fg='#000000', command=signupbuttonpressed, bg='#FFF5E4')
signupregister.grid(row=13, column=21, columnspan=6, rowspan=1, sticky=N+S+E+W)
gotosigninbutton = Button(window, text="Click here for sign in page", font=(
    'Arial', 14), width=1, height=1, fg='#000000', command=print("hello"), bg='#00FFFF')
gotosigninbutton.grid(row=15, column=26, columnspan=2,
                      rowspan=1, sticky=N+S+E+W)

# Inti Picture Processing Using PIL
INTI_BannerOriginal = Image.open(
    r'C:/Users/matth/Desktop/yeah/Home-Banner-INTI.png')  # Will need to change the path to the image
INTI_BannerImage = ImageOps.exif_transpose(INTI_BannerOriginal)
INTI_BannerImage = ImageTk.PhotoImage(INTI_BannerImage.resize(
    (math.ceil(480 * dpi / 96), math.ceil(180 * dpi / 96)), Image.Resampling.LANCZOS))
# Inti Logo
INTI_Banner = Label(window, image=INTI_BannerImage,
                    width=1, height=1, bg='#FFE3E1')
INTI_Banner.grid(row=2, column=20, columnspan=8, rowspan=3, sticky=N+S+E+W)
INTI_BannerOriginal = Image.open(
    r'C:/Users/matth/Desktop/yeah/Home-Banner-INTI.png')
INTI_BannerImage = ImageOps.exif_transpose(INTI_BannerOriginal)
INTI_BannerImage = ImageTk.PhotoImage(INTI_BannerImage.resize(
    (math.ceil(359 * dpi / 96), math.ceil(120 * dpi / 96)), Image.Resampling.LANCZOS))
INTI_Banner = Label(image=INTI_BannerImage, width=1, height=1, bg='#FFE3E1')
INTI_Banner.grid(row=2, column=20, columnspan=8, rowspan=2, sticky=N+S+E+W)

LandingPageArtOriginal = Image.open(
    r'D:/Syncthingstuff/Abstruct/Colored ocean in another world.jpg')  # Will need to change the path to the image
LandingPageArtImage = ImageOps.exif_transpose(LandingPageArtOriginal)
LandingPageArtImage = ImageTk.PhotoImage(LandingPageArtImage.resize(
    (math.ceil(840 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
LandingPageArt = Label(window, image=LandingPageArtImage,
                       width=1, height=1, bg='#FFE3E1')
LandingPageArt.grid(row=2, column=2, columnspan=14, rowspan=14, sticky=N+S+E+W)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Labels for Signup~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Entries for Signup~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



window.mainloop()
