

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

win = tk.Tk()

win.title("IBM")

lbl = Label(win, text="Welcome to TKinter", fg = 'red', font=("Harlow Solid Italic", 26))

lbl.place(x = 25, y = 50)

txtfld = Entry(win, font=("Arial", 24))

txtfld.place(x = 50, y = 130)

btn = Button(win, text="Exit", font=("Arial", 28), command=quit)

btn.place(x = 100, y = 200)

img = ImageTk.PhotoImage(Image.open("C:\Training\PycharmProjects\IBMBatch01\Day11\Macaw.jpg"))

panel = Label(win, image=img)
panel.place(x = 100, y = 280)

win.geometry("800x800+10+20")

win.mainloop()
