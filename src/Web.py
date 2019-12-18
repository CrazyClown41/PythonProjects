import tkinter as tk
import webbrowser as web

def openWeb():
    web.open("https://www.github.com/CrazyClown41")

window = tk.Tk()
window.title ("Redirect to Github")
button = tk.Button(window, text = "Open Github", width = 25, command = openWeb()) 
button.grid(row = 1, column = 1)
button = tk.Button(window, text = "Close", width = 25, command = window.destroy)
button.grid(row = 2, column = 1)
    
        
window.mainloop()