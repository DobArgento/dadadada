import tkinter as tk

root = tk.Tk()

for i in range(3):
    for j in range (3):
        frame = tk.Frame(
          master=root,
            relief=tk.RAISED,
              borderwidth=1 
        )
        frame.grid(row=i, column=j)
        label = tk.Label(frame, text="Row {}\nColumn {}".format(i, j))
        label.grid()

root.mainloop()
        
    