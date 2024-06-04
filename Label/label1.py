import tkinter as tk # Py3

root = tk.Tk() # root widget
# widgets are added here

label = tk.Label(root, text="A label with a very long text")
#label = tk.Label(root, text="Hello", bg="red")

label.grid() # using a geometry manager


root.mainloop()