from tkinter import *
import sqlite3


        
class SignInPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.instruction = Label(self, text = "Please enter your information below.")
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        self.first_name_label = Label(self, text = "First Name: ")
        self.first_name_label.grid(row = 1, column = 0, sticky = W)
        
        self.first_name_entry = Entry(self)
        self.first_name_entry.grid(row = 1, column = 1, sticky = W)
        
        self.last_name_label = Label(self, text = "Last Name: ")
        self.last_name_label.grid(row = 2, column = 0, sticky = W)
        
        self.last_name_entry = Entry(self)
        self.last_name_entry.grid(row = 2, column = 1, sticky = W)
        
        self.email_label = Label(self, text = "Email: ")
        self.email_label.grid(row = 3, column = 0, sticky = W)
        
        self.email_entry = Entry(self)
        self.email_entry.grid(row = 3, column = 1, sticky = W)
        
        self.submit_button = Button(self, text = "Submit", command = self.write_to_database)
        self.submit_button.grid(row = 4, column = 0, sticky = W)
        
        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row = 5, column = 0, columnspan = 2, sticky = W)
        
    def write_to_database(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (self.first_name_entry.get(), self.last_name_entry.get(), self.email_entry.get()))
        conn.commit()
        self.text.delete(0.0, END)
        self.text.insert(0.0, "You have been signed in!")

window = Tk()
window.title("Sign In")
app = SignInPage(window)
window.mainloop()