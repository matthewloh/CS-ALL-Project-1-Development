"""
Create a Tkinter App that lets you register for events
"""


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Register:
    def __init__(self, master):
        self.master = master
        self.master.title("Register for Events")
        self.master.resizable(False, False)
        self.master.configure(background = '#e1d8b9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file = r'D:\Syncthingstuff\degreestuff\CS Project\images.png')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = "Register for Events", style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("Use this app to register for events. "
                          "You can register for as many events as you want.")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Event:').grid(row = 1, column = 0, padx = 5, sticky = 'sw')

        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))

        self.entry_name.grid(row = 0, column = 0, padx = 5)
        self.entry_email.grid(row = 0, column = 1, padx = 5)

        self.combobox_event = ttk.Combobox(self.frame_content, width = 22, state = 'readonly', font = ('Arial', 10))
        self.combobox_event['values'] = ('Conference', 'Seminar', 'Meeting')
        self.combobox_event.current(0)
        self.combobox_event.grid(row = 1, column = 0, padx = 5)

        ttk.Button(self.frame_content, text = 'Register', command = self.register).grid(row = 1, column = 1, padx = 5, pady = 5)

        self.frame_footer = ttk.Frame(master)
        self.frame_footer.pack()

        ttk.Label(self.frame_footer, text = 'Copyright © 2019').grid(row = 0, column = 0, pady = 5)

        self.db = 'event_registration.db'

    def register(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        event = self.combobox_event.get()

        if name == '' or email == '' or event == '':
            messagebox.showerror(title = 'Error', message = 'Please fill out the fields!')
        else:
            conn = sqlite3.connect(self.db)
            with conn:
                cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS tbl_event( \
                            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                            col_name TEXT, \
                            col_email TEXT, \
                            col_event TEXT \
                            );')
            cursor.execute('INSERT INTO tbl_event (col_name, col_email, col_event) VALUES (?, ?, ?)', \
                           (name, email, event))
            conn.commit()
            self.entry_name.delete(0, 'end')
            self.entry_email.delete(0, 'end')
            self.combobox_event.current(0)
            messagebox.showinfo(title = 'Success', message = 'You have successfully registered for the event!')
            conn.close()

def main():
    root = Tk()
    register = Register(root)
    root.mainloop()

if __name__ == "__main__":
     main()