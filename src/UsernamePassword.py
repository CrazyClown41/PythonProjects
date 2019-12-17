import tkinter as tk
from tkinter import Entry, Label
from datetime import datetime

def writeToFile():
    dateTime = datetime.time(datetime.now())
    f = open("info.txt","w+")
    f.write(e1.get())
    f.write(e2.get())
    f.close()

window = tk.Tk()
window.title ("Hello World")
Label(window, text='Username:').grid(row=  0) 
Label(window, text='Password:').grid(row = 1) 
e1 = Entry(window) 
e2 = Entry(window) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
button = tk.Button(window, text = 'Submit', width = 25, command = writeToFile()) 
button.grid(row = 3, column = 1)
button = tk.Button(window, text = 'Close', width = 25, command = window.destroy)
button.grid(row = 4, column = 1)

window.mainloop()