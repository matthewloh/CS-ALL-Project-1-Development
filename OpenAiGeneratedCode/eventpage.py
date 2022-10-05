"""
Create a Tkinter App that lets you register for events and has another page to view events
"""
import tkinter as tk
LARGE_FONT = "Verdana 35 bold"

class EventRegistration(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, RegisterPage, ViewPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Register",
                           command=lambda: controller.show_frame(RegisterPage))
        button.pack()

        button2 = tk.Button(self, text="View Events",
                            command=lambda: controller.show_frame(ViewPage))
        button2.pack()


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Register for an Event", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="View Events",
                            command=lambda: controller.show_frame(ViewPage))
        button2.pack()

        # Create a list of events
        events = ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5"]

        # Create a variable to store the selected event
        selected_event = tk.StringVar()
        selected_event.set(events[0])

        # Create a dropdown menu
        dropdown = tk.OptionMenu(self, selected_event, *events)
        dropdown.pack()

        # Create a text box to enter the name
        name_label = tk.Label(self, text="Enter your name: ")
        name_label.pack()
        name_entry = tk.Entry(self)
        name_entry.pack()

        # Create a text box to enter the email
        email_label = tk.Label(self, text="Enter your email: ")
        email_label.pack()
        email_entry = tk.Entry(self)
        email_entry.pack()

        # Create a button to submit the registration
        submit_button = tk.Button(self, text="Submit", command=lambda: self.submit_registration(selected_event.get(),
                                                                                                name_entry.get(),
                                                                                                email_entry.get()))
        submit_button.pack()

    def submit_registration(self, event, name, email):
        print("You have registered for {}".format(event))
        print("Your name is {}".format(name))
        print("Your email is {}".format(email))


class ViewPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="View Events", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame(RegisterPage))
        button2.pack()


app = EventRegistration()
app.mainloop()