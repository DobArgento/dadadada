import tkinter as tk

root = tk.Tk()

whatever_you_do = "Whatever you do will be insignificant, " \
"but it is very important that you do it.\n(Mahatma Gandhi)"

msg = tk.Message(root, text=whatever_you_do, bg='lightgreen', font="Times 24 italic")

msg.grid()


root.mainloop()