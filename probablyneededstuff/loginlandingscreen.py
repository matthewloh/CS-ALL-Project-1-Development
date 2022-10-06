from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image, ImageOps
import math
import sqlite3
from databasestuff import UsersRegistration

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # 
PINK = "#FFE3E1"
LIGHTYELLOW = "#FFF5E4"

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Database Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
db = UsersRegistration()

stuff = (
    
)




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Widgets ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# TODO: Add the ability to add account to database (sign up), and then check if it is in the database
# TODO: Add a function to check if the username is already taken
# TODO: Add the ability to check if account is in database
# ~~~~~~~~~~~~~~~~~~~~~~~ Functions For Login Landing Screen ~~~~~~~~~~~~~~~~~~~~~~~ #
EMAILMESSAGE = "Please insert your registered email."
PASSWORDMESSAGE = "Please insert your registered password."


def clearpasswordentry():
    if PasswordEntry.get() == PASSWORDMESSAGE:
        PasswordEntry.delete(0, END)
    PasswordEntry.configure(show="*")


def repopulatepassword():
    PasswordEntry.configure(show="")
    if len(PasswordEntry.get()) == 0:
        PasswordEntry.insert(0, PASSWORDMESSAGE)
    else:
        PasswordEntry.configure(show="*")


def clearemailentry():
    if EmailEntry.get() == EMAILMESSAGE:
        EmailEntry.delete(0, END)


def repopulateemail():
    if len(EmailEntry.get()) == 0:
        EmailEntry.insert(0, EMAILMESSAGE)


def signupbuttonpressed(): # Basically, we need to get the entries, query the registration database with username and password, if username and password in database, return successfullogin, else return failedlogin
    emailtext = EmailEntry.get()
    passwordtext = PasswordEntry.get()
    try:
        if emailtext == EMAILMESSAGE or passwordtext == PASSWORDMESSAGE:
            messagebox.showerror(
                "Login Failure", "You have not entered one of either your email or password.")
            
        else:
            pass  # execute the function to add the account to the database
    except:
        messagebox.showerror("Login Failed", "Please try again")


def signinbuttonpressed():
    text = EmailEntry.get()
    text2 = PasswordEntry.get()
    print(text)
    print(text2)
    try:
        if text == "admin" and text2 == "admin":
            messagebox.showinfo("Login Successful", "Welcome back!")
    except:
        messagebox.showerror("Login Failed", "Please try again")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Deleting Widgets on Login~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def hideallsigninwidgets():
    LoginLabel.grid_forget()
    EmailEntry.grid_forget()
    PasswordEntry.grid_forget()
    SignInButton.grid_forget()
    SignUpButton.grid_forget()
    ForgotPassword.grid_forget()
    PlaceholderRadioButton.grid_forget()

    passwordsignupentry = Entry(window, width = 1, bg = '#FFFFFF', font = ('Arial', 16), justify = 'center')
    passwordsignupentry.grid(row = 11, column = 21, columnspan = 6, rowspan = 1, sticky = N+S+E+W)
    passwordsignupentry.insert(0, "Please enter your password")
    SignUpEmailEntry = Entry(window, width = 1, bg = '#FFFFFF', font = ('Arial', 16), justify = 'center')
    SignUpEmailEntry.grid(row = 9, column = 21, columnspan = 6, rowspan = 1, sticky = N+S+E+W)
    SignUpEmailEntry.insert(0, "Please enter your student email")
    Entry1 = Entry(window, width = 1, bg = '#FFFFFF', font = ('Arial', 16), justify = 'center')
    Entry1.grid(row = 7, column = 21, columnspan = 2, rowspan = 1, sticky = N+S+E+W)
    Entry1.insert(0, "First Name")
    Entry2 = Entry(window, width = 1, bg = '#FFFFFF', font = ('Arial', 16), justify = 'center')
    Entry2.grid(row = 7, column = 25, columnspan = 2, rowspan = 1, sticky = N+S+E+W)
    Entry2.insert(0, "Last Name")
    signupregister = Button(window, text="SIGN UP", font=(
    'Arial', 16), width=1, height=1, fg='#000000', command=print('hello'), bg='#FFF5E4')
    signupregister.grid(row=13, column=21, columnspan=6, rowspan=1, sticky=N+S+E+W)
    gotosigninbutton = Button(window, text="Click here for sign in page", font=(
        'Arial', 14), width=1, height=1, fg='#000000', command=print("hello"), bg='#00FFFF')
    gotosigninbutton.grid(row=15, column=26, columnspan=2,
                        rowspan=1, sticky=N+S+E+W)
# def showallsigninwidgets():
#     passwordsignupentry = Entry(window, width = 1, bg = '#FFFFFF', font = ('Arial', 16), justify = 'center')
#     passwordsignupentry.grid(row = 11, column = 21, columnspan = 6, rowspan = 1, sticky = N+S+E+W)
#     passwordsignupentry.insert(0, "Please enter your password")
#     SignUpEmailEntry = Entry(window, width = 1, bg = '#FFFFFF', font = ('Arial', 16), justify = 'center')
#     SignUpEmailEntry.grid(row = 9, column = 21, columnspan = 6, rowspan = 1, sticky = N+S+E+W)
#     SignUpEmailEntry.insert(0, "Please enter your student email")
#     Entry1 = Entry(window, width = 1, bg = '#FFFFFF', font = ('Arial', 16), justify = 'center')
#     Entry1.grid(row = 7, column = 21, columnspan = 2, rowspan = 1, sticky = N+S+E+W)
#     Entry1.insert(0, "First Name")
#     Entry2 = Entry(window, width = 1, bg = '#FFFFFF', font = ('Arial', 16), justify = 'center')
#     Entry2.grid(row = 7, column = 25, columnspan = 2, rowspan = 1, sticky = N+S+E+W)
#     Entry2.insert(0, "Last Name")
#     signupregister = Button(window, text="SIGN UP", font=(
#     'Arial', 16), width=1, height=1, fg='#000000', command=print('hello'), bg='#FFF5E4')
#     signupregister.grid(row=13, column=21, columnspan=6, rowspan=1, sticky=N+S+E+W)
#     gotosigninbutton = Button(window, text="Click here for sign in page", font=(
#         'Arial', 14), width=1, height=1, fg='#000000', command=showall, bg='#00FFFF')
#     gotosigninbutton.grid(row=15, column=26, columnspan=2,
#                         rowspan=1, sticky=N+S+E+W)
#     passwordsignupentry.grid_forget()
#     SignUpEmailEntry.grid_forget()
#     Entry1.grid_forget()
#     Entry2.grid_forget()
#     signupregister.grid_forget()
#     gotosigninbutton.grid_forget()

#     LoginLabel.grid()
#     EmailEntry.grid()
#     PasswordEntry.grid()
#     SignInButton.grid()
#     SignUpButton.grid()
#     ForgotPassword.grid()
#     PlaceholderRadioButton.grid()
    
    



    


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Labels Specific for Login ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
LoginLabel = Label(window, text="Sign in to your account", font=(
    'Arial', 18), width=1, height=1, fg='#000000', bg='#FFF5E4')
LoginLabel.grid(row=6, column=21, columnspan=6, rowspan=1, sticky=N+S+E+W)

NewIntiLabel = Label(window, text="New to INTI Interactive System?", font=(
    'Arial', 8), width=1, height=1, fg='#000000', bg='#00FFFF')
NewIntiLabel.grid(row=14, column=21, columnspan=4, rowspan=1, sticky=N+S+E+W)

ForgotPassword = Label(window, text="Forgot password?", font=(
    'Arial', 14), width=1, height=1, fg='#000000', bg='#00FFFF')
ForgotPassword.grid(row=13, column=21, columnspan=3, rowspan=1, sticky=N+S+E+W)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Entries Specific for Login ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# TODO: Add the ability to hide and show password
# TODO: Default entry text should be greyed out
# TODO: On click of the entry, the text should disappear, cursor should be in the entry and the text should reappear if no text is present #Done

EmailEntry = Entry(window, width=1, bg='#FFFFFF', font=('Arial', 14),
                   justify='center', highlightthickness=0, bd=0)

EmailEntry.grid(row=8, column=21, columnspan=6, rowspan=1, sticky=N+S+E+W)

EmailEntry.insert(0, EMAILMESSAGE)

EmailEntry.bind("<FocusIn>", lambda a: clearemailentry())

EmailEntry.bind("<FocusOut>", lambda a: repopulateemail())


PasswordEntry = Entry(window, width=1, bg='#FFFFFF', font=(
    'Arial', 14), justify='center', highlightthickness=0, bd=0)

PasswordEntry.bind("<FocusIn>", lambda a: clearpasswordentry())

PasswordEntry.bind("<FocusOut>", lambda a: repopulatepassword())

PasswordEntry.insert(0, PASSWORDMESSAGE)
PasswordEntry.grid(row=10, column=21, columnspan=6, rowspan=1, sticky=N+S+E+W)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTONS for Login~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SignUpButton = Button(window, text="Sign Up", font=('Arial', 16), width=1, height=1,
                      fg='#000000', command=hideallsigninwidgets, bg=LIGHTYELLOW)
SignUpButton.grid(row=14, column=25, columnspan=2, rowspan=1, sticky=N+S+E+W)
SignInButton = Button(window, text="SIGN IN", font=('Arial', 16), width=1, height=1,
                      fg='#000000', command=signinbuttonpressed, bg=LIGHTYELLOW)
SignInButton.grid(row=12, column=25, columnspan=2, rowspan=1, sticky=N+S+E+W)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Checkbutton~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PlaceholderRadioButton = Checkbutton(window, text="Remember me", font=(
    'Arial', 16), width=1, height=1, fg='#000000', bg=LIGHTYELLOW)
PlaceholderRadioButton.grid(
    row=12, column=21, columnspan=3, rowspan=1, sticky=N+S+E+W),
# # Inti Picture Processing Using PIL
# INTI_BannerOriginal = Image.open(
#     r'C:/Users/matth/Desktop/yeah/Home-Banner-INTI.png')  # Will need to change the path to the image
# INTI_BannerImage = ImageOps.exif_transpose(INTI_BannerOriginal)
# INTI_BannerImage = ImageTk.PhotoImage(INTI_BannerImage.resize(
#     (math.ceil(480 * dpi / 96), math.ceil(180 * dpi / 96)), Image.Resampling.LANCZOS))
# # Inti Logo
# INTI_Banner = Label(window, image=INTI_BannerImage, width=1, height=1, bg='#FFE3E1')
# INTI_Banner.grid(row=2, column=20, columnspan=8, rowspan=3, sticky=N+S+E+W)
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
# haveanaccountlabel = Label(window, text = "Already have an account?", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#00FFFF')
# haveanaccountlabel.grid(row = 15, column = 20, columnspan = 5, rowspan = 1, sticky = N+S+E+W)
# SignUpLabel = Label(window, text = "Please enter your details as shown.", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#FFF5E4')
# SignUpLabel.grid(row = 5, column = 20, columnspan = 8, rowspan = 1, sticky = N+S+E+W)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Entries for Signup~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Buttons for Signup~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()
