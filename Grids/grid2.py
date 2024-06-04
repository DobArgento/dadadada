import tkinter as tk

root = tk.Tk()

for i in range (3):
    #Expanding window configuration
    #Every row column has to be configured separately.
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)

for i in range(3):
    for j in range (3):
        frame = tk.Frame(
          master=root,
            relief=tk.RAISED,
              borderwidth=1 
        )
        frame.grid(row=i, column=j, padx=5, pady=5) #external padding in pixels
        label = tk.Label(frame, text="Row {}\nColumn {}".format(i, j))
        label.grid(padx=5, pady=5)#internal padding pixels

root.mainloop()