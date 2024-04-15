

import tkinter as tk
from tkinter import *

win = tk.Tk()

win.title("IBM")

lbl = Label(win, text="Welcome to TKinter", fg = 'red', font=("Harlow Solid Italic", 26))

lbl.place(x = 25, y = 50)

txtfld = Entry(win, font=("Arial", 24))

txtfld.place(x = 50, y = 130)

btn = Button(win, text="Exit", font=("Arial", 28), command=quit)

btn.place(x = 100, y = 200)

win.geometry("600x500+10+20")

win.mainloop()
