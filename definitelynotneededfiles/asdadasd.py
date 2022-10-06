import tkinter as tk 
import sqlite3
from tkinter import messagebox
from tkinter import SOLID, N, messagebox, W, LEFT, RIDGE, BOTH, RIGHT, TOP, filedialog, END, ttk
f = ('Arial', 14)
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (
                RegistrationPage,
                ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(RegistrationPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class RegistrationPage(tk.Frame):

    def __init__(self, parent, controller):
        con = sqlite3.connect('ebook_db.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS record(
                            user_id integer primary key autoincrement,
                            name text, 
                            email text, 
                            contact number, 
                            gender text, 
                            country text,
                            password text
                        )
                    ''')
        con.commit()

        tk.Frame.__init__(self, parent, bg='#BFCACA')
        var = tk.StringVar()
        var.set('male')

        countries = []
        variable = tk.StringVar()
        world = open('countries.txt', 'r')
        for country in world:
            country = country.rstrip('\n')
            countries.append(country)
        variable.set(countries[106])

        # widgets
        registration_lbl = tk.Label(self, text="Registration Page", bg='#BFCACA')
        registration_lbl.config(font=("Verdana", 20, 'bold'))

        registration_desc = tk.Label(self, text="Create A New Account", bg='#BFCACA')
        registration_desc.config(font=("Verdana", 18, 'italic'))

        mainFrame = tk.Frame(self, bd=0, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)

        tk.Label(mainFrame, text="Enter Name", bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Enter Email", bg='#CCCCCC', font=f).grid(row=1, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Contact Number", bg='#CCCCCC', font=f).grid(row=2, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Select Gender", bg='#CCCCCC', font=f).grid(row=3, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Select Country", bg='#CCCCCC', font=f).grid(row=4, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Enter Password", bg='#CCCCCC', font=f).grid(row=5, column=0, sticky=W, pady=10)
        tk.Label(mainFrame, text="Re-Enter Password", bg='#CCCCCC', font=f).grid(row=6, column=0, sticky=W, pady=10)

        gender_frame = tk.LabelFrame(mainFrame, bg='#CCCCCC', padx=10, pady=10, )
        register_name = tk.Entry(mainFrame, font=f)
        register_email = tk.Entry(mainFrame, font=f)
        register_mobile = tk.Entry(mainFrame, font=f)

        male_rb = tk.Radiobutton(gender_frame, text='Male', bg='#CCCCCC', variable=var, value='male',
                                 font=('Times', 10))
        female_rb = tk.Radiobutton(gender_frame, text='Female', bg='#CCCCCC', variable=var, value='female',
                                   font=('Times', 10))

        register_country = tk.OptionMenu(mainFrame, variable, *countries)
        register_country.config(width=15, font=('Times', 12))

        register_pwd = tk.Entry(mainFrame, font=f, show='*')
        pwd_again = tk.Entry(mainFrame, font=f, show='*')

        register_btn = tk.Button(mainFrame, width=15, text='Join Now!', bg='green', font=f, relief=SOLID,
                                 cursor='hand2',
                                 command=lambda: insert_record())



        register_name.grid(row=0, column=1, pady=10, padx=20)
        register_email.grid(row=1, column=1, pady=10, padx=20)
        register_mobile.grid(row=2, column=1, pady=10, padx=20)
        register_country.grid(row=4, column=1, pady=10, padx=20)
        register_pwd.grid(row=5, column=1, pady=10, padx=20)
        pwd_again.grid(row=6, column=1, pady=10, padx=20)
        register_btn.grid(row=7, column=0, pady=10, padx=20)
 

        registration_lbl.place(x=310, y=30)
        registration_desc.place(x=310, y=65)
        mainFrame.place(x=215, y=110)

        gender_frame.grid(row=3, column=1, pady=10, padx=20)
        male_rb.pack(expand=True, side=LEFT)
        female_rb.pack(expand=True, side=LEFT)

        def insert_record():
            check_counter = 0
            warn = ""
            if register_name.get() == "":
                warn = "Name can't be empty"
            else:
                check_counter += 1

            if register_email.get() == "":
                warn = "Email can't be empty"
            else:
                check_counter += 1

            if register_mobile.get() == "":
                warn = "Contact can't be empty"
            else:
                check_counter += 1

            if var.get() == "":
                warn = "Select Gender"
            else:
                check_counter += 1

            if variable.get() == "":
                warn = "Select Country"
            else:
                check_counter += 1

            if register_pwd.get() == "":
                warn = "Password can't be empty"
            else:
                check_counter += 1

            if pwd_again.get() == "":
                warn = "Re-enter password can't be empty"
            else:
                check_counter += 1

            if register_pwd.get() != pwd_again.get():
                warn = "Passwords didn't match!"
            else:
                check_counter += 1

            if check_counter == 8:
                try:
                    con = sqlite3.connect('ebook_db.db')
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO record (name, email, contact, gender, country, password) VALUES (:name, :email, "
                        ":contact, :gender, :country, :password)", {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': var.get(),
                            'country': variable.get(),
                            'password': register_pwd.get()

                        })
                    con.commit()
                    messagebox.showinfo('Confirmation', 'Registration Successful!')
                    register_name.delete(0, 'end')
                    register_email.delete(0, 'end')
                    register_mobile.delete(0, 'end')
                    register_pwd.delete(0, 'end')
                    pwd_again.delete(0, 'end')


                except Exception as ep:
                    messagebox.showerror('', ep)
            else:
                messagebox.showerror('Error', warn)

app = App()
app.geometry('1600x900')
app.title('Ebook Reader')
app.mainloop()