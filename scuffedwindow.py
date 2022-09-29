from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()

window.title('window')

window.geometry('1920x1080')

new_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
new_label.pack()

new_label["text"] = "New Text"
new_label.config(text="New Text")

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    new_label.config(text=new_text)
    

button = Button(text="Click Me", command=button_clicked) 
button.pack()

#Entry
input = Entry(width=100)
input.pack()
window.mainloop()