import tkinter as tk

root = tk.Tk()

#logo = tk.PhotoImage(file="img/python_logo.gif")
logo = tk.PhotoImage(file="img/python_logo.png")

#label = tk.Label(root, image=logo)

label = tk.Label(root,
    compound=tk.CENTER, # text and image together
    image=logo,
    text="[Python logo]"
)

label.image = logo # keep a reference! (from effbot.org)

label.grid()


root.mainloop() # run the tkinter event loop