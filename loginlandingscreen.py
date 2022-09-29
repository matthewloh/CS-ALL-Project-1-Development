from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image, ImageOps
import math
import sqlite3

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFE3E1"
LIGHTYELLOW = "#FFF5E4"

# ----------------------Window Setup----------------------
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
window.resizable(False, False)

# ~~~~~~~~~~~~~~~~~~~~~~~Database Functions~~~~~~~~~~~~~~~~~~~~~~~
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE users(
            username text,
            password text
            )""")

def insert_user(username, password):
    with conn:
        c.execute("INSERT INTO users VALUES (:username, :password)", {'username': username, 'password': password})


#TODO: Add the ability to add account to database (sign up), and then check if it is in the database
#TODO: Add a function to check if the username is already taken
#TODO: Add the ability to check if account is in database
# ~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~


def signupbuttonpressed():
    print("auugh")

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

        
    


# ----------------------Widgets----------------------
# Inti Picture Processing Using PIL
INTI_BannerOriginal = Image.open(
    r'C:/Users/User/Desktop/BCSCU - Year 1 - Semester 1/CS Project/yeah/Home-Banner-INTI.png')  # Will need to change the path to the image C:/Users/User/Desktop/BCSCU - Year 1 - Semester 1/CS Project/yeah/Home-Banner-INTI.png
INTI_BannerImage = ImageOps.exif_transpose(INTI_BannerOriginal)
INTI_BannerImage = ImageTk.PhotoImage(INTI_BannerImage.resize(
    (math.ceil(480 * dpi / 96), math.ceil(180 * dpi / 96)), Image.Resampling.LANCZOS))
# Inti Logo
INTI_Banner = Label(image=INTI_BannerImage, width=1, height=1, bg='#FFE3E1')
INTI_Banner.grid(row=2, column=20, columnspan=8, rowspan=3, sticky=N+S+E+W)

LandingPageArtOriginal = Image.open(
    r'C:/Users/User/Desktop/BCSCU - Year 1 - Semester 1/CS Project/Abstruct/Colored ocean in another world.jpg') #Will need to change the path to the image #On Laptop: C:/Users/User/Desktop/BCSCU - Year 1 - Semester 1/CS Project/Abstruct/Colored ocean in another world.jpg
LandingPageArtImage = ImageOps.exif_transpose(LandingPageArtOriginal)
LandingPageArtImage = ImageTk.PhotoImage(LandingPageArtImage.resize(
    (math.ceil(840 * dpi / 96), math.ceil(840 * dpi / 96)), Image.Resampling.LANCZOS))
LandingPageArt = Label(image=LandingPageArtImage,
                       width=1, height=1, bg='#FFE3E1')
LandingPageArt.grid(row=2, column=2, columnspan=14, rowspan=14, sticky=N+S+E+W)

# ----------------------Labels----------------------
LoginLabel = Label(text="Sign in to your account", font=(
    'Arial', 18), width=1, height=1, fg='#000000', bg='#FFF5E4')
LoginLabel.grid(row=6, column=21, columnspan=6, rowspan=1, sticky=N+S+E+W)

NewIntiLabel = Label(text="New to INTI Interactive System?", font=(
    'Arial', 8), width=1, height=1, fg='#000000', bg='#00FFFF')
NewIntiLabel.grid(row=14, column=21, columnspan=4, rowspan=1, sticky=N+S+E+W)

ForgotPassword = Label(text="Forgot password?", font=(
    'Arial', 14), width=1, height=1, fg='#000000', bg='#00FFFF')
ForgotPassword.grid(row=13, column=21, columnspan=3, rowspan=1, sticky=N+S+E+W)
# ----------------------Checkbutton----------------------
PlaceholderRadioButton = Checkbutton(text="Remember me", font=(
    'Arial', 16), width=1, height=1, fg='#000000', bg=LIGHTYELLOW)
PlaceholderRadioButton.grid(
    row=12, column=21, columnspan=3, rowspan=1, sticky=N+S+E+W)

# ----------------------Entries----------------------
#TODO: Add the ability to hide password
#TODO: Default entry text should be greyed out
#TODO: On click of the entry, the text should disappear, cursor should be in the entry and the text should reappear if no text is present

EmailEntry = Entry(width=1, bg='#FFFFFF', font=('Arial', 14),
                   justify='center', highlightthickness=0, bd=0)
EmailEntry.grid(row=8, column=21, columnspan=6, rowspan=1, sticky=N+S+E+W)
EmailEntry.insert(0, "Please insert your student email.")
PasswordEntry = Entry(width=1, bg='#FFFFFF', font=(
    'Arial', 14), justify='center', highlightthickness=0, bd=0)
PasswordEntry.grid(row=10, column=21, columnspan=6, rowspan=1, sticky=N+S+E+W)
PasswordEntry.insert(0, "Please insert your password.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SignUpButton = Button(window, text="Sign Up", font=('Arial', 16), width=1, height=1,
                      fg='#000000', command=signupbuttonpressed, bg=LIGHTYELLOW)
SignUpButton.grid(row=14, column=25, columnspan=2, rowspan=1, sticky=N+S+E+W)
SignInButton = Button(window, text="SIGN IN", font=('Arial', 16), width=1, height=1,
                      fg='#000000', command=signinbuttonpressed, bg=LIGHTYELLOW)
SignInButton.grid(row=12, column=25, columnspan=2, rowspan=1, sticky=N+S+E+W)

window.mainloop()
