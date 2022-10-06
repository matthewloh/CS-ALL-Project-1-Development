from tkinter import *
from PIL import ImageTk, Image, ImageOps
import math
from loginlandingscreenoop import Window
PINK = "#FFE3E1"
LIGHTYELLOW = "#FFF5E4"

class SignupWindow(Window):
    def __init__(
        self, title = "Sign Up Screen", width=1920, height=1080):
        super().__init__(title, width, height)
    
    def initializewidgets(self):
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

    def initializepictures(self):
        inti_banner_canvas = Canvas(self.root, width=1240, height=401, highlightthickness=0, bd=0)
        inti_banner_img = PhotoImage(file="Home-Banner-INTI.png")
        inti_banner_canvas.create_image(1240, 401, image=inti_banner_img)
        inti_banner_canvas.grid(row=2, column=20, columnspan=8, rowspan=3, sticky=N+S+E+W)


    
        
PINK = "#FFE3E1"
LIGHTYELLOW = "#FFF5E4"

def main():
    window = SignupWindow()
    window.initializewidgets()
    window.initializepictures()
    window.start()



if __name__ == "__main__":
    main()
