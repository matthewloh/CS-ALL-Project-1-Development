from tkinter import *

class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for F in (
                RegistrationPage, #SignInPage, HomePage, SearchPage, EventViewPage, EventManagePage, MorePage 
                ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(RegistrationPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class RegistrationPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#FFE3E1')
      



        LoginLabel = Label(self, text="Sign ingcount", font=(
            'Arial', 18),  fg='#000000', bg='#FFF5E4')
        LoginLabel.pack(padx=10, pady=10)
        
        

        NewIntiLabel = Label(self, text="New to INTI Interactive System?", font=(
            'Arial', 8),  fg='#000000', bg='#00FFFF')
        NewIntiLabel.pack()

        ForgotPassword = Label(self, text="Forgot password?", font=(
            'Arial', 14),  fg='#000000', bg='#00FFFF')
        ForgotPassword.pack()





window = Window()
window.geometry('1600x900')
window.title("what the fuck")
window.resizable(0,0)
window.mainloop()